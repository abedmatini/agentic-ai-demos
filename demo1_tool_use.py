"""
Demo 1: Single Agent with Tool Use
Smart Conference Assistant - Shows tool calling and decision making

This demo showcases:
- Single agent with multiple tools
- Visual tool execution tracking
- Real-time decision making display
- Function calling pattern
"""

import streamlit as st
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI
from datetime import datetime
import time

load_dotenv()

st.set_page_config(
    page_title="Demo 1: Tool Use Pattern",
    page_icon="🛠️",
    layout="wide"
)

# Tool definitions (mock implementations for demo)
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather forecast for a specific city and date",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. Cape Town"
                    },
                    "date": {
                        "type": "string",
                        "description": "The date in YYYY-MM-DD format"
                    }
                },
                "required": ["city", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_venue_info",
            "description": "Get information about a conference venue including address, capacity, and facilities",
            "parameters": {
                "type": "object",
                "properties": {
                    "venue_name": {
                        "type": "string",
                        "description": "The name of the venue or conference"
                    }
                },
                "required": ["venue_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_travel_time",
            "description": "Calculate travel time between two locations",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_location": {
                        "type": "string",
                        "description": "Starting location"
                    },
                    "to_location": {
                        "type": "string",
                        "description": "Destination location"
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["driving", "walking", "public_transport"],
                        "description": "Mode of transportation"
                    }
                },
                "required": ["from_location", "to_location"]
            }
        }
    }
]

# Mock tool implementations
def get_weather(city, date):
    """Mock weather API - returns realistic data"""
    time.sleep(0.5)  # Simulate API call
    weather_data = {
        "Cape Town": {
            "temperature": "22°C",
            "condition": "Partly Cloudy",
            "humidity": "65%",
            "wind": "15 km/h",
            "precipitation": "10%",
            "recommendation": "Perfect weather for outdoor activities!"
        }
    }
    return weather_data.get(city, {
        "temperature": "20°C",
        "condition": "Clear",
        "humidity": "60%",
        "wind": "10 km/h",
        "precipitation": "5%"
    })

def get_venue_info(venue_name):
    """Mock venue API - returns conference details"""
    time.sleep(0.5)  # Simulate API call
    return {
        "name": ".NET Conf 2025 Cape Town",
        "address": "Cape Town Convention Centre, 1 Lower Long St, Cape Town",
        "capacity": "500 attendees",
        "facilities": ["WiFi", "Parking", "Catering", "AV Equipment"],
        "start_time": "09:00 AM",
        "end_time": "05:00 PM",
        "sessions": 12,
        "tracks": ["AI/ML", ".NET Core", "Azure", "DevOps"]
    }

def calculate_travel_time(from_location, to_location, mode="driving"):
    """Mock travel time calculator"""
    time.sleep(0.5)  # Simulate API call
    times = {
        "driving": "25 minutes",
        "walking": "1 hour 15 minutes",
        "public_transport": "35 minutes"
    }
    return {
        "from": from_location,
        "to": to_location,
        "mode": mode,
        "duration": times.get(mode, "30 minutes"),
        "distance": "12 km",
        "traffic": "Light traffic expected"
    }

def execute_tool(tool_name, arguments):
    """Execute the appropriate tool based on name"""
    if tool_name == "get_weather":
        return get_weather(**arguments)
    elif tool_name == "get_venue_info":
        return get_venue_info(**arguments)
    elif tool_name == "calculate_travel_time":
        return calculate_travel_time(**arguments)
    return {"error": "Unknown tool"}

def get_azure_client():
    """Initialize Azure OpenAI client"""
    api_key = os.getenv("AZURE_AI_API_KEY")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    
    if not endpoint or not api_key:
        return None
    
    if 'cognitiveservices' in endpoint:
        return OpenAI(base_url=endpoint, api_key=api_key)
    else:
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
        return AzureOpenAI(api_key=api_key, api_version=api_version, azure_endpoint=endpoint)

def run_agent_with_tools(client, user_message):
    """Run agent with tool calling capability"""
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    messages = [
        {
            "role": "system",
            "content": """You are a helpful conference assistant. You help attendees prepare for conferences.
            When asked about conference preparation, use the available tools to gather information about:
            - Weather conditions
            - Venue details
            - Travel times
            Then provide comprehensive, personalized advice based on the tool results."""
        },
        {"role": "user", "content": user_message}
    ]
    
    tool_calls_made = []
    iterations = 0
    max_iterations = 5
    
    while iterations < max_iterations:
        iterations += 1
        
        # Call the model
        response = client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )
        
        assistant_message = response.choices[0].message
        
        # Check if the model wants to call tools
        if assistant_message.tool_calls:
            # Add assistant message to conversation
            messages.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in assistant_message.tool_calls
                ]
            })
            
            # Execute each tool call
            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Track tool call for display
                tool_calls_made.append({
                    "name": function_name,
                    "arguments": function_args,
                    "status": "executing"
                })
                
                # Execute the tool
                function_response = execute_tool(function_name, function_args)
                
                # Update status
                tool_calls_made[-1]["status"] = "completed"
                tool_calls_made[-1]["result"] = function_response
                
                # Add tool response to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": json.dumps(function_response)
                })
        else:
            # No more tool calls, return final response
            return {
                "response": assistant_message.content,
                "tool_calls": tool_calls_made
            }
    
    return {
        "response": "Maximum iterations reached",
        "tool_calls": tool_calls_made
    }

# Sidebar
with st.sidebar:
    st.title("🛠️ Demo 1: Tool Use")
    st.markdown("---")
    
    st.markdown("### 📋 What This Shows")
    st.info("""
    **Agentic Pattern: Tool Use**
    
    - Agent decides which tools to call
    - Executes tools autonomously
    - Synthesizes results into answer
    - Shows decision-making process
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔧 Available Tools")
    for tool in TOOLS:
        func = tool["function"]
        with st.expander(f"📌 {func['name']}"):
            st.write(f"**Description:** {func['description']}")
            st.write(f"**Parameters:** {', '.join(func['parameters']['properties'].keys())}")
    
    st.markdown("---")
    
    # Configuration status
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_API_KEY")
    
    if endpoint and api_key:
        st.success("✅ Azure AI configured")
    else:
        st.warning("⚠️ Configure .env file")

# Main content
st.title("🛠️ Demo 1: Single Agent with Tool Use")
st.markdown("### Smart Conference Assistant")

st.markdown("""
This demo shows how an AI agent can **autonomously decide** which tools to use and **execute them** 
to answer your questions. Watch the tool execution in real-time!
""")

st.markdown("---")

# Example prompts
st.markdown("### 💡 Try These Examples:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌤️ Weather Check", use_container_width=True):
        st.session_state.prompt = "What's the weather like in Cape Town on November 22, 2025?"

with col2:
    if st.button("📍 Venue Info", use_container_width=True):
        st.session_state.prompt = "Tell me about the .NET Conf venue in Cape Town"

with col3:
    if st.button("🎯 Full Preparation", use_container_width=True):
        st.session_state.prompt = "I'm attending .NET Conf in Cape Town on November 22. Help me prepare!"

st.markdown("---")

# User input
user_input = st.text_area(
    "Ask the Conference Assistant:",
    value=st.session_state.get('prompt', ''),
    height=100,
    placeholder="e.g., I'm attending .NET Conf in Cape Town on November 22. What should I prepare?"
)

if st.button("🚀 Run Agent", type="primary", use_container_width=True):
    if user_input:
        client = get_azure_client()
        
        if client:
            with st.spinner("🤖 Agent is thinking and calling tools..."):
                result = run_agent_with_tools(client, user_input)
            
            # Display tool calls
            if result["tool_calls"]:
                st.markdown("### 🔄 Tool Execution Log")
                
                for idx, tool_call in enumerate(result["tool_calls"], 1):
                    with st.expander(f"🔧 Tool Call {idx}: `{tool_call['name']}`", expanded=True):
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            st.markdown("**Arguments:**")
                            st.json(tool_call["arguments"])
                            
                            if tool_call["status"] == "completed":
                                st.success("✅ Completed")
                            else:
                                st.info("⏳ Executing...")
                        
                        with col2:
                            if tool_call["status"] == "completed":
                                st.markdown("**Result:**")
                                st.json(tool_call["result"])
            
            # Display final response
            st.markdown("---")
            st.markdown("### 🎯 Agent's Final Response")
            st.success(result["response"])
            
        else:
            st.error("⚠️ Please configure Azure AI credentials in .env file")
    else:
        st.warning("Please enter a question first")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p><b>Demo 1:</b> Tool Use Pattern | Built for .NET Conf 2025 Presentation</p>
</div>
""", unsafe_allow_html=True)

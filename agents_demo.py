"""
Advanced Multi-Agent Demo with Azure AI Foundry
This demonstrates more complex agent interactions and workflows
"""

import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI
import json

load_dotenv()

st.set_page_config(
    page_title="Advanced Agent Workflows",
    page_icon="🔮",
    layout="wide"
)

# Advanced agent configurations with specialized roles
ADVANCED_AGENTS = {
    "Analyst": {
        "name": "Data Analyst Agent",
        "system_prompt": """You are a data analyst AI. You excel at:
        - Analyzing data patterns and trends
        - Creating insights from information
        - Providing statistical perspectives
        - Suggesting data-driven decisions
        Always structure your responses with clear findings and recommendations.""",
        "icon": "📊",
        "color": "#FF6B6B"
    },
    "Strategist": {
        "name": "Strategic Planning Agent",
        "system_prompt": """You are a strategic planning AI. You specialize in:
        - Long-term planning and goal setting
        - Risk assessment and mitigation
        - Resource allocation strategies
        - Competitive analysis
        Provide structured strategic recommendations with pros and cons.""",
        "icon": "🎯",
        "color": "#4ECDC4"
    },
    "Innovator": {
        "name": "Innovation Agent",
        "system_prompt": """You are an innovation-focused AI. Your strengths include:
        - Creative problem-solving
        - Identifying emerging trends
        - Proposing novel solutions
        - Thinking outside the box
        Offer innovative ideas with practical implementation paths.""",
        "icon": "💡",
        "color": "#95E1D3"
    },
    "Critic": {
        "name": "Critical Reviewer Agent",
        "system_prompt": """You are a critical analysis AI. You focus on:
        - Identifying potential flaws and weaknesses
        - Challenging assumptions
        - Providing constructive criticism
        - Ensuring quality and rigor
        Give balanced critiques with specific improvement suggestions.""",
        "icon": "🔍",
        "color": "#F38181"
    }
}

def get_azure_client():
    """Initialize Azure OpenAI client"""
    api_key = os.getenv("AZURE_AI_API_KEY")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    
    if not endpoint or not api_key:
        return None
    
    # Check if using Cognitive Services endpoint
    if 'cognitiveservices' in endpoint:
        return OpenAI(
            base_url=endpoint,
            api_key=api_key
        )
    else:
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
        return AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=endpoint
        )

def get_agent_response(client, agent_key, conversation_history):
    """Get response from Azure OpenAI agent with conversation history"""
    agent = ADVANCED_AGENTS[agent_key]
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    try:
        messages = [{"role": "system", "content": agent["system_prompt"]}]
        messages.extend(conversation_history)
        
        response = client.chat.completions.create(
            model=deployment_name,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def multi_agent_workflow(client, user_query):
    """Run a multi-agent workflow where agents build on each other's responses"""
    workflow_results = {}
    
    # Agent workflow order
    workflow_order = ["Analyst", "Strategist", "Innovator", "Critic"]
    
    conversation_history = [{"role": "user", "content": user_query}]
    
    for agent_key in workflow_order:
        with st.spinner(f"Consulting {ADVANCED_AGENTS[agent_key]['name']}..."):
            response = get_agent_response(client, agent_key, conversation_history)
            workflow_results[agent_key] = response
            
            # Add this agent's response to the conversation history
            conversation_history.append({"role": "assistant", "content": f"[{agent_key}]: {response}"})
    
    return workflow_results

# Sidebar
with st.sidebar:
    st.title("🔮 Advanced Agents")
    st.markdown("---")
    
    # Mode selector
    mode = st.radio(
        "Select Mode:",
        ["Single Agent", "Multi-Agent Workflow", "Agent Comparison"]
    )
    
    st.markdown("---")
    
    # Configuration status
    st.markdown("### ⚙️ Configuration")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_API_KEY")
    
    if endpoint and api_key:
        st.success("✅ Azure AI configured")
    else:
        st.warning("⚠️ Configure .env file")
    
    st.markdown("---")
    
    # Agent descriptions
    st.markdown("### 🤖 Available Agents")
    for key, agent in ADVANCED_AGENTS.items():
        with st.expander(f"{agent['icon']} {agent['name']}"):
            st.write(agent['system_prompt'])

# Main content
st.title("🔮 Advanced Azure AI Agent Workflows")

# Mode-specific UI
if mode == "Single Agent":
    st.markdown("### Single Agent Mode")
    st.info("Chat with one specialized agent at a time.")
    
    selected_agent = st.selectbox(
        "Choose an agent:",
        list(ADVANCED_AGENTS.keys()),
        format_func=lambda x: f"{ADVANCED_AGENTS[x]['icon']} {ADVANCED_AGENTS[x]['name']}"
    )
    
    if 'single_agent_history' not in st.session_state:
        st.session_state.single_agent_history = []
    
    # Display chat history
    for msg in st.session_state.single_agent_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask your question..."):
        st.session_state.single_agent_history.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        client = get_azure_client()
        if client:
            conversation = [{"role": "user", "content": prompt}]
            response = get_agent_response(client, selected_agent, conversation)
            
            with st.chat_message("assistant"):
                st.markdown(response)
            
            st.session_state.single_agent_history.append({"role": "assistant", "content": response})

elif mode == "Multi-Agent Workflow":
    st.markdown("### Multi-Agent Workflow")
    st.info("Submit a query and watch multiple agents collaborate sequentially, building on each other's insights.")
    
    query = st.text_area("Enter your query:", height=100, placeholder="e.g., How can we improve customer retention for our SaaS product?")
    
    if st.button("🚀 Run Workflow", type="primary"):
        if query:
            client = get_azure_client()
            if client:
                st.markdown("---")
                results = multi_agent_workflow(client, query)
                
                for agent_key, response in results.items():
                    agent = ADVANCED_AGENTS[agent_key]
                    with st.expander(f"{agent['icon']} {agent['name']}", expanded=True):
                        st.markdown(response)
                
                # Summary
                st.markdown("---")
                st.success("✅ Workflow completed! Review each agent's perspective above.")
            else:
                st.error("Please configure Azure AI credentials.")
        else:
            st.warning("Please enter a query first.")

elif mode == "Agent Comparison":
    st.markdown("### Agent Comparison Mode")
    st.info("Compare responses from multiple agents side-by-side.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        agent1 = st.selectbox(
            "Agent 1:",
            list(ADVANCED_AGENTS.keys()),
            format_func=lambda x: f"{ADVANCED_AGENTS[x]['icon']} {ADVANCED_AGENTS[x]['name']}"
        )
    
    with col2:
        agent2 = st.selectbox(
            "Agent 2:",
            [k for k in ADVANCED_AGENTS.keys() if k != agent1],
            format_func=lambda x: f"{ADVANCED_AGENTS[x]['icon']} {ADVANCED_AGENTS[x]['name']}"
        )
    
    query = st.text_area("Enter your question:", height=100)
    
    if st.button("🔄 Compare Responses", type="primary"):
        if query:
            client = get_azure_client()
            if client:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### {ADVANCED_AGENTS[agent1]['icon']} {ADVANCED_AGENTS[agent1]['name']}")
                    with st.spinner("Thinking..."):
                        response1 = get_agent_response(client, agent1, [{"role": "user", "content": query}])
                        st.markdown(response1)
                
                with col2:
                    st.markdown(f"### {ADVANCED_AGENTS[agent2]['icon']} {ADVANCED_AGENTS[agent2]['name']}")
                    with st.spinner("Thinking..."):
                        response2 = get_agent_response(client, agent2, [{"role": "user", "content": query}])
                        st.markdown(response2)
            else:
                st.error("Please configure Azure AI credentials.")
        else:
            st.warning("Please enter a question first.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Advanced Multi-Agent System | Built with Streamlit and Azure AI Foundry</p>
</div>
""", unsafe_allow_html=True)

import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Azure AI Foundry Multi-Agent Demo",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = {}
if 'current_agent' not in st.session_state:
    st.session_state.current_agent = "Agent 1"

# Agent configurations
AGENTS = {
    "Agent 1": {
        "name": "Research Assistant",
        "system_prompt": "You are a helpful research assistant. You provide detailed, well-researched answers with citations and explanations.",
        "icon": "📚",
        "color": "#FF6B6B"
    },
    "Agent 2": {
        "name": "Code Helper",
        "system_prompt": "You are an expert programming assistant. You help with code review, debugging, and writing clean, efficient code.",
        "icon": "💻",
        "color": "#4ECDC4"
    },
    "Agent 3": {
        "name": "Creative Writer",
        "system_prompt": "You are a creative writing assistant. You help with storytelling, content creation, and creative ideation.",
        "icon": "✍️",
        "color": "#95E1D3"
    }
}

def get_azure_client():
    """Initialize Azure OpenAI client"""
    api_key = os.getenv("AZURE_AI_API_KEY")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    
    if not endpoint or not api_key:
        return None
    
    # Check if using Cognitive Services endpoint (contains 'cognitiveservices')
    if 'cognitiveservices' in endpoint:
        # Use OpenAI client with base_url for Cognitive Services endpoints
        from openai import OpenAI
        return OpenAI(
            base_url=endpoint,
            api_key=api_key
        )
    else:
        # Use AzureOpenAI client for standard Azure OpenAI endpoints
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
        return AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=endpoint
        )

def get_agent_response(client, agent_key, user_message):
    """Get response from Azure OpenAI agent"""
    agent = AGENTS[agent_key]
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": agent["system_prompt"]},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("🤖 Azure AI Agents")
    st.markdown("---")
    
    # Agent selector
    selected_agent = st.radio(
        "Select an Agent:",
        list(AGENTS.keys()),
        format_func=lambda x: f"{AGENTS[x]['icon']} {AGENTS[x]['name']}",
        key="agent_selector"
    )
    
    st.markdown("---")
    
    # Agent info
    agent_info = AGENTS[selected_agent]
    st.markdown(f"### {agent_info['icon']} {agent_info['name']}")
    st.info(agent_info['system_prompt'])
    
    st.markdown("---")
    
    # Configuration status
    st.markdown("### ⚙️ Configuration")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_API_KEY")
    
    if endpoint and api_key:
        st.success("✅ Azure AI configured")
    else:
        st.warning("⚠️ Configure .env file")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = {}
        st.rerun()

# Main content
st.title("🤖 Azure AI Foundry Multi-Agent Demo")
st.markdown(f"Currently chatting with: **{AGENTS[selected_agent]['icon']} {AGENTS[selected_agent]['name']}**")

# Initialize message history for current agent
if selected_agent not in st.session_state.messages:
    st.session_state.messages[selected_agent] = []

# Display chat messages
for message in st.session_state.messages[selected_agent]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages[selected_agent].append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get Azure AI client
    client = get_azure_client()
    
    # Display assistant response
    with st.chat_message("assistant"):
        if client:
            with st.spinner("Thinking..."):
                response = get_agent_response(client, selected_agent, prompt)
                st.markdown(response)
                st.session_state.messages[selected_agent].append({"role": "assistant", "content": response})
        else:
            error_msg = "⚠️ Please configure your Azure AI credentials in the .env file."
            st.error(error_msg)
            st.session_state.messages[selected_agent].append({"role": "assistant", "content": error_msg})

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Built with Streamlit and Azure AI Foundry | Practice Demo</p>
</div>
""", unsafe_allow_html=True)

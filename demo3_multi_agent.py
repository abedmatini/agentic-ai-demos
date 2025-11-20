"""
Demo 3: Multi-Agent Coordination
Product Launch Team - Shows agent orchestration and collaboration

This demo showcases:
- Multiple specialized agents working together
- Visual orchestration and handoffs
- Sequential and parallel agent execution
- Result synthesis from multiple perspectives
"""

import streamlit as st
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI
import time
from datetime import datetime

load_dotenv()

st.set_page_config(
    page_title="Demo 3: Multi-Agent Coordination",
    page_icon="🤝",
    layout="wide"
)

# Agent definitions with specialized roles
AGENTS = {
    "researcher": {
        "name": "Market Researcher",
        "icon": "📊",
        "color": "#FF6B6B",
        "role": "market_analysis",
        "system_prompt": """You are a Market Research Analyst specializing in tech products.
        
Your responsibilities:
- Analyze market trends and opportunities
- Identify target audiences and competitors
- Provide data-driven insights
- Assess market readiness

Keep your analysis concise (3-4 key points) and actionable."""
    },
    "strategist": {
        "name": "Launch Strategist",
        "icon": "🎯",
        "color": "#4ECDC4",
        "role": "strategy_planning",
        "system_prompt": """You are a Product Launch Strategist with expertise in go-to-market planning.

Your responsibilities:
- Develop launch strategies based on research
- Define positioning and messaging
- Create timeline and milestones
- Identify key success metrics

Keep your strategy focused (3-4 main initiatives) and realistic."""
    },
    "writer": {
        "name": "Content Creator",
        "icon": "✍️",
        "color": "#95E1D3",
        "role": "content_creation",
        "system_prompt": """You are a Creative Content Writer specializing in tech marketing.

Your responsibilities:
- Create compelling marketing copy
- Write engaging product descriptions
- Craft social media content
- Ensure brand voice consistency

Keep your content punchy and memorable (2-3 key messages)."""
    },
    "reviewer": {
        "name": "Quality Reviewer",
        "icon": "🔍",
        "color": "#F38181",
        "role": "quality_assurance",
        "system_prompt": """You are a Quality Assurance Reviewer for marketing campaigns.

Your responsibilities:
- Review all previous agent outputs
- Identify gaps or inconsistencies
- Provide constructive feedback
- Suggest improvements

Keep your review balanced (2-3 strengths, 2-3 improvements)."""
    }
}

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

def call_agent(client, agent_key, context, previous_outputs=None):
    """Call a specific agent with context"""
    agent = AGENTS[agent_key]
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    # Build the prompt with context from previous agents
    messages = [{"role": "system", "content": agent["system_prompt"]}]
    
    # Add previous agent outputs as context
    if previous_outputs:
        context_summary = "\n\n".join([
            f"**{AGENTS[k]['name']}:**\n{v}" 
            for k, v in previous_outputs.items()
        ])
        messages.append({
            "role": "user",
            "content": f"""Based on the following context from other team members:

{context_summary}

Now, as the {agent['name']}, provide your contribution for: {context}"""
        })
    else:
        messages.append({
            "role": "user",
            "content": f"As the {agent['name']}, analyze this: {context}"
        })
    
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def run_sequential_workflow(client, user_input, workflow_type="sequential"):
    """Run agents in sequence, each building on previous outputs"""
    
    if workflow_type == "sequential":
        # Sequential: Each agent sees all previous outputs
        agent_order = ["researcher", "strategist", "writer", "reviewer"]
        workflow_results = {}
        
        for agent_key in agent_order:
            agent = AGENTS[agent_key]
            
            # Show progress
            yield {
                "type": "agent_start",
                "agent": agent_key,
                "agent_name": agent["name"],
                "icon": agent["icon"],
                "status": "thinking"
            }
            
            # Simulate thinking time for demo effect
            time.sleep(0.5)
            
            # Call the agent
            result = call_agent(client, agent_key, user_input, workflow_results)
            workflow_results[agent_key] = result
            
            # Return result
            yield {
                "type": "agent_complete",
                "agent": agent_key,
                "agent_name": agent["name"],
                "icon": agent["icon"],
                "result": result,
                "status": "completed"
            }
    
    elif workflow_type == "parallel_then_review":
        # Parallel: Researcher, Strategist, Writer work independently, then Reviewer
        parallel_agents = ["researcher", "strategist", "writer"]
        workflow_results = {}
        
        # Phase 1: Parallel execution (simulated)
        for agent_key in parallel_agents:
            agent = AGENTS[agent_key]
            
            yield {
                "type": "agent_start",
                "agent": agent_key,
                "agent_name": agent["name"],
                "icon": agent["icon"],
                "status": "thinking"
            }
        
        time.sleep(0.5)
        
        # Execute all parallel agents
        for agent_key in parallel_agents:
            agent = AGENTS[agent_key]
            result = call_agent(client, agent_key, user_input, None)
            workflow_results[agent_key] = result
            
            yield {
                "type": "agent_complete",
                "agent": agent_key,
                "agent_name": agent["name"],
                "icon": agent["icon"],
                "result": result,
                "status": "completed"
            }
        
        # Phase 2: Reviewer synthesizes
        yield {
            "type": "agent_start",
            "agent": "reviewer",
            "agent_name": AGENTS["reviewer"]["name"],
            "icon": AGENTS["reviewer"]["icon"],
            "status": "thinking"
        }
        
        time.sleep(0.5)
        
        result = call_agent(client, "reviewer", user_input, workflow_results)
        workflow_results["reviewer"] = result
        
        yield {
            "type": "agent_complete",
            "agent": "reviewer",
            "agent_name": AGENTS["reviewer"]["name"],
            "icon": AGENTS["reviewer"]["icon"],
            "result": result,
            "status": "completed"
        }
    
    # Final summary
    yield {
        "type": "workflow_complete",
        "results": workflow_results
    }

# Sidebar
with st.sidebar:
    st.title("🤝 Demo 3: Multi-Agent")
    st.markdown("---")
    
    st.markdown("### 📋 What This Shows")
    st.info("""
    **Agentic Pattern: Coordination**
    
    - Multiple specialized agents
    - Sequential collaboration
    - Context sharing between agents
    - Orchestrated workflows
    """)
    
    st.markdown("---")
    
    st.markdown("### 🤖 Agent Team")
    for agent_key, agent in AGENTS.items():
        with st.expander(f"{agent['icon']} {agent['name']}"):
            st.markdown(f"**Role:** {agent['role']}")
            st.markdown(f"**Specialization:** {agent['system_prompt'][:100]}...")
    
    st.markdown("---")
    
    # Workflow selector
    st.markdown("### 🔄 Workflow Type")
    workflow_type = st.radio(
        "Choose workflow:",
        ["sequential", "parallel_then_review"],
        format_func=lambda x: "Sequential (Chain)" if x == "sequential" else "Parallel + Review"
    )
    
    st.markdown("---")
    
    # Configuration status
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_API_KEY")
    
    if endpoint and api_key:
        st.success("✅ Azure AI configured")
    else:
        st.warning("⚠️ Configure .env file")

# Main content
st.title("🤝 Demo 3: Multi-Agent Coordination")
st.markdown("### Product Launch Team Simulation")

st.markdown("""
Watch how multiple specialized AI agents collaborate to plan a product launch. 
Each agent brings unique expertise and builds on others' work.
""")

st.markdown("---")

# Example scenarios
st.markdown("### 💡 Try These Scenarios:")
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 AI-Powered Dev Tool", use_container_width=True):
        st.session_state.scenario = "We're launching an AI-powered developer productivity tool that helps write better code using machine learning. Target audience: professional developers."

with col2:
    if st.button("📱 Mobile App Launch", use_container_width=True):
        st.session_state.scenario = "We're launching a mobile app for remote team collaboration with real-time video and AI meeting summaries. Target audience: distributed teams."

st.markdown("---")

# User input
user_input = st.text_area(
    "Describe your product launch:",
    value=st.session_state.get('scenario', ''),
    height=100,
    placeholder="e.g., We're launching an AI coding assistant for .NET developers..."
)

if st.button("🚀 Run Multi-Agent Workflow", type="primary", use_container_width=True):
    if user_input:
        client = get_azure_client()
        
        if client:
            st.markdown("---")
            st.markdown("### 🔄 Agent Workflow Execution")
            
            # Create containers for each agent
            agent_containers = {}
            for agent_key in AGENTS.keys():
                agent_containers[agent_key] = st.empty()
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Run workflow
            total_agents = len(AGENTS)
            completed_agents = 0
            
            results = {}
            
            for event in run_sequential_workflow(client, user_input, workflow_type):
                if event["type"] == "agent_start":
                    agent_key = event["agent"]
                    status_text.info(f"🤔 {event['icon']} {event['agent_name']} is thinking...")
                    
                    with agent_containers[agent_key].container():
                        st.markdown(f"### {event['icon']} {event['agent_name']}")
                        st.info("⏳ Processing...")
                
                elif event["type"] == "agent_complete":
                    agent_key = event["agent"]
                    completed_agents += 1
                    progress_bar.progress(completed_agents / total_agents)
                    
                    results[agent_key] = event["result"]
                    
                    with agent_containers[agent_key].container():
                        st.markdown(f"### {event['icon']} {event['agent_name']}")
                        
                        with st.expander("📄 View Output", expanded=True):
                            st.markdown(event["result"])
                        
                        st.success("✅ Completed")
                
                elif event["type"] == "workflow_complete":
                    status_text.success("🎉 All agents completed!")
                    progress_bar.progress(1.0)
            
            # Final summary
            st.markdown("---")
            st.markdown("### 📊 Workflow Summary")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Agents Involved", len(AGENTS))
            with col2:
                st.metric("Workflow Type", "Sequential" if workflow_type == "sequential" else "Parallel")
            with col3:
                st.metric("Status", "✅ Complete")
            
            # Download results
            st.markdown("---")
            results_json = json.dumps(results, indent=2)
            st.download_button(
                label="📥 Download Results (JSON)",
                data=results_json,
                file_name=f"product_launch_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
            
        else:
            st.error("⚠️ Please configure Azure AI credentials in .env file")
    else:
        st.warning("Please describe your product launch first")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p><b>Demo 3:</b> Multi-Agent Coordination Pattern | Built for .NET Conf 2025 Presentation</p>
</div>
""", unsafe_allow_html=True)

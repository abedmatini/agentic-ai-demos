"""
Demo 4: Planning Pattern
Task Planner Agent - Shows task decomposition and systematic execution

This demo showcases:
- Breaking complex tasks into manageable steps
- Creating execution plans dynamically
- Visual step-by-step progress tracking
- Reflection and adaptation during execution
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
    page_title="Demo 4: Planning Pattern",
    page_icon="📋",
    layout="wide"
)

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

def create_plan(client, task):
    """Create a step-by-step plan for the given task"""
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    system_prompt = """You are an expert task planner. Your job is to break down complex tasks into clear, actionable steps.

For each task, create a plan with:
1. A brief analysis of the task
2. 4-6 specific, actionable steps
3. Expected outcome for each step

Format your response as JSON:
{
    "analysis": "Brief analysis of the task",
    "steps": [
        {
            "step_number": 1,
            "title": "Step title",
            "description": "What to do",
            "expected_outcome": "What should result"
        }
    ],
    "success_criteria": "How to know if the task is complete"
}

Be specific and practical. Each step should be clear enough to execute."""

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Create a detailed execution plan for this task: {task}"}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        plan_json = response.choices[0].message.content
        return json.loads(plan_json)
    except Exception as e:
        return {
            "error": str(e),
            "analysis": "Failed to create plan",
            "steps": [],
            "success_criteria": "N/A"
        }

def execute_step(client, step, task_context, previous_results):
    """Execute a single step of the plan"""
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    system_prompt = """You are an expert executor. You receive a step from a plan and execute it thoughtfully.

For each step:
1. Consider the context and previous results
2. Execute the step thoroughly
3. Provide concrete, actionable output
4. Note any challenges or insights

Keep your response focused and practical (2-3 paragraphs max)."""

    context_summary = ""
    if previous_results:
        context_summary = "\n\nPrevious steps completed:\n" + "\n".join([
            f"Step {r['step_number']}: {r['result'][:100]}..." 
            for r in previous_results
        ])

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"""Task Context: {task_context}
                
Current Step:
- Title: {step['title']}
- Description: {step['description']}
- Expected Outcome: {step['expected_outcome']}
{context_summary}

Execute this step and provide the results."""}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error executing step: {str(e)}"

def reflect_on_execution(client, task, plan, results):
    """Reflect on the execution and provide insights"""
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    system_prompt = """You are a reflective analyst. Review the task execution and provide insights.

Analyze:
1. What went well
2. What could be improved
3. Key learnings
4. Next steps or recommendations

Be concise (3-4 key points total)."""

    results_summary = "\n".join([
        f"Step {r['step_number']} ({r['title']}): {r['result'][:150]}..."
        for r in results
    ])

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"""Original Task: {task}

Execution Results:
{results_summary}

Provide your reflection and insights."""}
            ],
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in reflection: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("📋 Demo 4: Planning")
    st.markdown("---")
    
    st.markdown("### 📋 What This Shows")
    st.info("""
    **Agentic Pattern: Planning**
    
    - Task decomposition
    - Step-by-step execution
    - Progress tracking
    - Reflection and learning
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔄 Planning Process")
    st.markdown("""
    1. **Analyze** - Understand the task
    2. **Plan** - Break into steps
    3. **Execute** - Complete each step
    4. **Reflect** - Learn and improve
    """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Key Benefits")
    st.markdown("""
    - Handles complex tasks
    - Transparent progress
    - Systematic approach
    - Learns from execution
    """)
    
    st.markdown("---")
    
    # Configuration status
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_API_KEY")
    
    if endpoint and api_key:
        st.success("✅ Azure AI configured")
    else:
        st.warning("⚠️ Configure .env file")

# Main content
st.title("📋 Demo 4: Planning Pattern")
st.markdown("### AI Task Planner & Executor")

st.markdown("""
Watch how an AI agent breaks down complex tasks into manageable steps, 
executes them systematically, and reflects on the results.
""")

st.markdown("---")

# Example tasks
st.markdown("### 💡 Try These Complex Tasks:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Launch Campaign", use_container_width=True):
        st.session_state.task = "Plan and execute a social media campaign for launching a new AI-powered mobile app targeting young professionals"

with col2:
    if st.button("📊 Market Research", use_container_width=True):
        st.session_state.task = "Conduct comprehensive market research for entering the AI education space with online courses"

with col3:
    if st.button("🏗️ Build MVP", use_container_width=True):
        st.session_state.task = "Plan the development of an MVP for a SaaS platform that helps small businesses manage customer relationships"

st.markdown("---")

# User input
user_task = st.text_area(
    "Describe your complex task:",
    value=st.session_state.get('task', ''),
    height=100,
    placeholder="e.g., Organize a tech conference with 500 attendees, including venue, speakers, and marketing..."
)

# Execution mode
col1, col2 = st.columns([3, 1])
with col1:
    execute_mode = st.radio(
        "Execution mode:",
        ["Plan Only", "Plan + Execute", "Plan + Execute + Reflect"],
        horizontal=True,
        index=2
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button("🚀 Start Planning", type="primary", use_container_width=True)

if run_button and user_task:
    client = get_azure_client()
    
    if client:
        st.markdown("---")
        
        # Phase 1: Planning
        st.markdown("## 📝 Phase 1: Planning")
        with st.spinner("🤔 Analyzing task and creating plan..."):
            plan = create_plan(client, user_task)
            time.sleep(0.5)  # Demo effect
        
        if "error" not in plan:
            # Show analysis
            st.markdown("### 🔍 Task Analysis")
            st.info(plan.get("analysis", "No analysis available"))
            
            # Show plan
            st.markdown("### 📋 Execution Plan")
            
            steps_data = []
            for step in plan.get("steps", []):
                steps_data.append({
                    "Step": f"#{step['step_number']}",
                    "Title": step['title'],
                    "Description": step['description'][:60] + "..." if len(step['description']) > 60 else step['description']
                })
            
            if steps_data:
                st.table(steps_data)
            
            # Show success criteria
            with st.expander("🎯 Success Criteria", expanded=False):
                st.write(plan.get("success_criteria", "N/A"))
            
            # Phase 2: Execution
            if execute_mode in ["Plan + Execute", "Plan + Execute + Reflect"]:
                st.markdown("---")
                st.markdown("## ⚙️ Phase 2: Execution")
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                execution_results = []
                total_steps = len(plan.get("steps", []))
                
                for idx, step in enumerate(plan.get("steps", [])):
                    step_number = step['step_number']
                    
                    # Update progress
                    progress = (idx) / total_steps
                    progress_bar.progress(progress)
                    status_text.info(f"⚙️ Executing Step {step_number}: {step['title']}...")
                    
                    # Create step container
                    with st.expander(f"📍 Step {step_number}: {step['title']}", expanded=True):
                        st.markdown(f"**Description:** {step['description']}")
                        st.markdown(f"**Expected Outcome:** {step['expected_outcome']}")
                        
                        with st.spinner("Processing..."):
                            result = execute_step(client, step, user_task, execution_results)
                            time.sleep(0.5)  # Demo effect
                        
                        st.markdown("**Result:**")
                        st.success(result)
                        
                        execution_results.append({
                            "step_number": step_number,
                            "title": step['title'],
                            "result": result
                        })
                
                # Complete progress
                progress_bar.progress(1.0)
                status_text.success("✅ All steps completed!")
                
                # Phase 3: Reflection
                if execute_mode == "Plan + Execute + Reflect":
                    st.markdown("---")
                    st.markdown("## 🔍 Phase 3: Reflection")
                    
                    with st.spinner("🤔 Reflecting on execution..."):
                        reflection = reflect_on_execution(client, user_task, plan, execution_results)
                        time.sleep(0.5)  # Demo effect
                    
                    st.markdown("### 💡 Insights & Learnings")
                    st.info(reflection)
            
            # Summary
            st.markdown("---")
            st.markdown("## 📊 Summary")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Steps", len(plan.get("steps", [])))
            with col2:
                completed = len(execution_results) if execute_mode != "Plan Only" else 0
                st.metric("Completed", completed)
            with col3:
                st.metric("Mode", execute_mode.split(" + ")[0])
            with col4:
                st.metric("Status", "✅ Complete")
            
            # Download option
            if execute_mode != "Plan Only":
                st.markdown("---")
                export_data = {
                    "task": user_task,
                    "plan": plan,
                    "execution_results": execution_results if execute_mode != "Plan Only" else [],
                    "reflection": reflection if execute_mode == "Plan + Execute + Reflect" else None,
                    "timestamp": datetime.now().isoformat()
                }
                
                st.download_button(
                    label="📥 Download Complete Report (JSON)",
                    data=json.dumps(export_data, indent=2),
                    file_name=f"task_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        else:
            st.error(f"Failed to create plan: {plan.get('error', 'Unknown error')}")
    
    else:
        st.error("⚠️ Please configure Azure AI credentials in .env file")

elif run_button:
    st.warning("Please describe a task first")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p><b>Demo 4:</b> Planning Pattern | Built for .NET Conf 2025 Presentation</p>
</div>
""", unsafe_allow_html=True)

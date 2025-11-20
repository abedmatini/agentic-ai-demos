# Demo 4: Planning Pattern 📋

## Overview

This demo showcases the **Planning Pattern** - where an AI agent breaks down complex tasks into manageable steps, executes them systematically, and reflects on the results. This is how agents handle tasks that are too complex for a single response.

## What It Demonstrates

### Key Concepts
- ✅ **Task Decomposition** - Breaking complex tasks into steps
- ✅ **Systematic Execution** - Following a plan step-by-step
- ✅ **Progress Tracking** - Visual execution monitoring
- ✅ **Reflection** - Learning from execution results

### Agentic Pattern: Planning
The agent acts as a project manager that:
1. Analyzes the complex task
2. Creates a detailed execution plan
3. Executes each step systematically
4. Reflects on results and learns

## Running the Demo

### Quick Start
```bash
streamlit run demo4_planning.py
```

The app will open at: `http://localhost:8501`

### Prerequisites
- Virtual environment activated
- `.env` file configured with Azure OpenAI credentials
- Dependencies installed (`requirements.txt`)

## The Planning Process

### Phase 1: Planning 📝
**What happens:**
- Agent analyzes the task
- Identifies key components
- Creates 4-6 actionable steps
- Defines success criteria

**Output:**
- Task analysis
- Step-by-step plan
- Expected outcomes per step

### Phase 2: Execution ⚙️
**What happens:**
- Execute each step in order
- Use context from previous steps
- Track progress visually
- Capture results

**Output:**
- Detailed results per step
- Progress tracking
- Execution log

### Phase 3: Reflection 🔍
**What happens:**
- Review all execution results
- Identify what went well
- Note improvements
- Provide learnings

**Output:**
- Insights and learnings
- Recommendations
- Next steps

## Demo Flow (5-7 minutes)

### 1. Introduction (1 minute)
**Say:**
> "Complex tasks can't be solved in a single step. The planning pattern shows how AI agents 
> can think like project managers - breaking down big problems into manageable pieces."

**Show:**
- The three phases in the sidebar
- The execution mode options

### 2. Choose a Task (30 seconds)
**Click:** "Launch Campaign" button

**Say:**
> "Let's plan a social media campaign. This involves multiple steps - research, strategy, 
> content creation, scheduling, and more. Watch how the agent breaks this down."

### 3. Run Plan + Execute + Reflect (4 minutes)
**Select:** "Plan + Execute + Reflect"  
**Click:** "Start Planning"

**As it runs, narrate:**

**During Planning Phase:**
> "First, the agent analyzes the task and creates a structured plan. Notice how it breaks 
> the campaign into specific, actionable steps."

**Show the plan table:**
> "Each step has a clear description and expected outcome. This is like a project roadmap."

**During Execution Phase:**
> "Now watch as the agent executes each step. It uses context from previous steps to inform 
> its decisions - just like a human would."

**As each step completes:**
> "Step 1 complete - the agent has done market research. Now it's using that research to 
> inform Step 2's strategy..."

**During Reflection Phase:**
> "Finally, the agent reflects on the entire execution. It identifies what worked well and 
> what could be improved. This is how agents learn and improve."

### 4. Show the Results (1 minute)
**Expand step details:**
> "Look at the depth of each step's output. The agent didn't just list ideas - it created 
> actionable content for each phase of the campaign."

**Show the reflection:**
> "The reflection provides meta-insights about the execution process itself."

### 5. Explain the Pattern (1 minute)
**Say:**
> "This is the planning pattern. It's essential for:
> - Complex multi-step tasks
> - Projects that need structure
> - Tasks where order matters
> - Situations requiring reflection and learning
> 
> In production, you'd combine this with tool use - each step might call external APIs 
> or databases to gather information or take action."

## Execution Modes

### Plan Only
- Creates the plan
- Shows task breakdown
- No execution
- **Use for:** Quick planning, brainstorming

### Plan + Execute
- Creates plan
- Executes all steps
- Tracks progress
- **Use for:** Full task completion

### Plan + Execute + Reflect
- Creates plan
- Executes all steps
- Reflects on results
- **Use for:** Learning and improvement

## Example Tasks

### Task 1: Launch Campaign (Recommended for Demo)
```
Plan and execute a social media campaign for launching a new AI-powered 
mobile app targeting young professionals
```

**Why it's good:**
- Clear multi-step process
- Relevant to tech audience
- Shows strategic thinking

### Task 2: Market Research
```
Conduct comprehensive market research for entering the AI education 
space with online courses
```

### Task 3: Build MVP
```
Plan the development of an MVP for a SaaS platform that helps small 
businesses manage customer relationships
```

### Custom Task Template
```
[Action verb] a [project type] that [objective] for [target audience], 
including [key components]
```

## Technical Implementation

### Planning Agent
```python
system_prompt = """You are an expert task planner. 
Break down complex tasks into clear, actionable steps."""

# Returns structured JSON plan
{
    "analysis": "Task analysis",
    "steps": [...],
    "success_criteria": "How to measure success"
}
```

### Execution Agent
```python
# Each step receives:
- Current step details
- Task context
- Previous step results

# Returns:
- Execution results
- Concrete outputs
```

### Reflection Agent
```python
# Analyzes:
- What went well
- What could improve
- Key learnings
- Next steps
```

## Talking Points for Presentation

### Why Planning Matters
**Traditional:** AI gives one-shot response  
**Planning:** AI breaks down and solves systematically

### Real-World Applications

**Project Management:**
- Event planning (venue, catering, marketing, logistics)
- Product launches (research, strategy, execution, review)
- Software development (design, implement, test, deploy)

**Research & Analysis:**
- Market research (data collection, analysis, insights, report)
- Competitive analysis (identify competitors, analyze, compare, recommend)
- Due diligence (gather info, verify, assess risk, conclude)

**Content Production:**
- Book writing (outline, research, draft, edit, publish)
- Course creation (curriculum, content, videos, assessments)
- Marketing campaigns (strategy, content, distribution, measure)

**Business Operations:**
- Hiring process (job description, sourcing, interviews, offer)
- Onboarding (documentation, training, setup, check-ins)
- Process improvement (analyze, design, implement, measure)

### Key Advantages

1. **Handles Complexity** - Breaks down overwhelming tasks
2. **Systematic** - Ensures nothing is missed
3. **Transparent** - See exactly what's happening
4. **Adaptive** - Can adjust based on results
5. **Learnable** - Reflection improves future plans

### Design Considerations

**When to use planning:**
- Multi-step tasks with dependencies
- Complex projects needing structure
- Tasks where order matters
- Need for progress tracking

**When NOT to use:**
- Simple, single-step tasks
- Real-time responses needed
- Tasks without clear structure
- When speed is critical

## Combining Patterns

### Planning + Tool Use
```
Plan: "Step 1: Research competitors"
Execute: Call search_web() tool
Result: Use data in next step
```

### Planning + Multi-Agent
```
Plan: Create 5-step launch plan
Execute: Assign each step to specialized agent
Result: Coordinated multi-agent execution
```

### All Three Together
```
Planning Agent creates plan
→ Each step assigned to specialized agent
  → Each agent uses tools to execute
    → Results feed into next step
```

## Customization Ideas

### Add Dynamic Re-planning
```python
def replan_if_needed(step_result, remaining_steps):
    """Adjust plan based on execution results"""
    if step_result.indicates_change_needed():
        return create_new_plan(remaining_steps)
```

### Add Human-in-the-Loop
```python
def get_approval(step):
    """Request human approval before execution"""
    if step.is_critical():
        return request_user_approval(step)
```

### Add Parallel Execution
```python
def execute_parallel_steps(independent_steps):
    """Execute steps that don't depend on each other"""
    return asyncio.gather(*[execute(s) for s in independent_steps])
```

### Add Cost Estimation
```python
def estimate_cost(plan):
    """Estimate API costs before execution"""
    return sum(step.estimated_tokens * token_cost for step in plan)
```

## Troubleshooting

### Plans Too Generic
- Make task description more specific
- Add constraints or requirements
- Request more detailed steps

### Execution Steps Too Long
- Adjust system prompt for conciseness
- Set max token limits
- Request bullet-point format

### Steps Not Building on Each Other
- Ensure previous results are passed
- Make dependencies explicit in plan
- Review context sharing logic

### Reflection Not Insightful
- Provide more execution detail
- Ask specific reflection questions
- Include metrics in execution results

## Comparison with Other Demos

| Aspect | Demo 1 (Tool) | Demo 3 (Multi-Agent) | Demo 4 (Planning) |
|--------|---------------|----------------------|-------------------|
| **Focus** | Actions | Collaboration | Structure |
| **Complexity** | Single task | Multiple perspectives | Multi-step process |
| **Coordination** | Tool selection | Agent handoffs | Step sequence |
| **Best For** | External actions | Complex reasoning | Project execution |

## Production Considerations

### Add Checkpointing
```python
# Save progress after each step
save_checkpoint(step_number, results)

# Resume from failure
resume_from_checkpoint(last_successful_step)
```

### Add Monitoring
```python
# Track execution metrics
monitor_step_duration(step)
monitor_token_usage(step)
monitor_success_rate(step)
```

### Add Error Handling
```python
# Retry failed steps
if step_fails():
    retry_with_backoff(step, max_retries=3)

# Skip non-critical steps
if step_fails() and not step.is_critical():
    log_and_continue()
```

## Files

- `demo4_planning.py` - Main demo application
- `DEMO4_README.md` - This file
- `.env` - Configuration (Azure credentials)

## Presentation Tips

### Do's ✅
- Use "Launch Campaign" example (most visual)
- Select "Plan + Execute + Reflect" mode
- Narrate during execution
- Show the step details
- Emphasize the systematic approach

### Don'ts ❌
- Don't use "Plan Only" mode (less impressive)
- Don't skip the reflection phase
- Don't rush through step execution
- Don't forget to show the progress bar

### Time Management
- **5 min version:** One task, explain pattern
- **7 min version:** One task, deep dive on phases
- **10 min version:** Two tasks, compare approaches

## Key Takeaway

> "The planning pattern is how AI agents handle complexity. Instead of trying to solve 
> everything at once, they think like project managers - breaking down, executing 
> systematically, and learning from results. This is essential for production AI systems."

## Transition to Wrap-up

**After Demo 4:**
> "We've now seen three fundamental agentic patterns:
> - **Tool Use** - Agents that take action
> - **Multi-Agent** - Agents that collaborate
> - **Planning** - Agents that handle complexity
> 
> In production, you combine these patterns to build sophisticated AI systems that can 
> handle real-world challenges. The key is choosing the right pattern for your problem."

---

**Demo 4 Complete!** Ready to showcase systematic task execution! 🎉

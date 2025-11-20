# Demo 1: Single Agent with Tool Use 🛠️

## Overview

This demo showcases the **Tool Use** agentic pattern - where an AI agent autonomously decides which tools to call, executes them, and synthesizes the results into a comprehensive answer.

## What It Demonstrates

### Key Concepts
- ✅ **Autonomous Decision Making** - Agent chooses which tools to use
- ✅ **Function Calling** - Real-time tool execution
- ✅ **Result Synthesis** - Combining multiple data sources
- ✅ **Visual Tracking** - See what the agent is doing

### Agentic Pattern: Tool Use
The agent acts as an orchestrator that:
1. Analyzes the user's request
2. Determines which tools are needed
3. Calls tools in the right order
4. Synthesizes results into a coherent answer

## Running the Demo

### Quick Start
```bash
streamlit run demo1_tool_use.py
```

The app will open at: `http://localhost:8501`

### Prerequisites
- Virtual environment activated
- `.env` file configured with Azure OpenAI credentials
- Dependencies installed (`requirements.txt`)

## Demo Flow (3-5 minutes)

### 1. Introduction (30 seconds)
**Say:**
> "Let me show you how an AI agent can use tools autonomously. This isn't just a chatbot - 
> it's an agent that can decide what information it needs and go get it."

### 2. Show the Interface (30 seconds)
**Point out:**
- The 3 available tools in the sidebar
- Each tool has a specific purpose
- The agent will decide which ones to use

### 3. Run Example 1: Simple Tool Use (1 minute)
**Click:** "Weather Check" button

**Say:**
> "Watch what happens. The agent recognizes it needs weather data, 
> calls the weather tool, and gives us a formatted response."

**Show:**
- Tool execution log appearing
- Arguments passed to the tool
- Result returned
- Final synthesized answer

### 4. Run Example 2: Multiple Tools (2 minutes)
**Click:** "Full Preparation" button

**Say:**
> "Now let's ask something more complex. The agent needs to coordinate multiple tools 
> to give a complete answer."

**Show:**
- Multiple tool calls appearing in sequence
- Weather tool → Venue tool → Travel tool
- Each tool's arguments and results
- How the agent combines all information

**Key Point:**
> "Notice the agent decided on its own to call all three tools. We didn't tell it to - 
> it understood what information was needed to answer the question completely."

### 5. Explain the Pattern (1 minute)
**Say:**
> "This is the Tool Use pattern. The agent:
> 1. Analyzes what you need
> 2. Selects appropriate tools
> 3. Executes them autonomously
> 4. Synthesizes the results
> 
> This is fundamental to building agents that can interact with real-world systems."

## Available Tools

### 1. `get_weather(city, date)`
**Purpose:** Get weather forecast for conference planning

**Example Use:**
- "What's the weather in Cape Town on Nov 22?"
- "Should I bring an umbrella to the conference?"

### 2. `get_venue_info(venue_name)`
**Purpose:** Get conference venue details

**Example Use:**
- "Tell me about the venue"
- "What facilities are available?"

### 3. `calculate_travel_time(from, to, mode)`
**Purpose:** Calculate travel times

**Example Use:**
- "How long to get from the airport?"
- "What's the best way to reach the venue?"

## Example Prompts for Live Demo

### Simple (1 tool)
```
"What's the weather like in Cape Town on November 22, 2025?"
```

### Medium (2 tools)
```
"Tell me about the .NET Conf venue and what the weather will be like"
```

### Complex (3 tools)
```
"I'm attending .NET Conf in Cape Town on November 22. Help me prepare!"
```

### Custom
```
"I'm staying at the Waterfront. How should I plan my day for the conference?"
```

## Technical Implementation

### Tool Definition (OpenAI Function Calling)
```python
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get weather forecast...",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "date": {"type": "string"}
            }
        }
    }
}
```

### Agent Loop
1. Send message + tool definitions to model
2. Model responds with tool calls
3. Execute tools and get results
4. Send results back to model
5. Model synthesizes final answer

### Visual Tracking
- Real-time display of tool execution
- Arguments and results shown in expandable sections
- Status indicators (executing → completed)

## Talking Points for Presentation

### Why This Matters
- **Traditional:** Hardcoded if/else logic
- **Agentic:** AI decides dynamically what to do

### Real-World Applications
- Customer support agents calling CRM/ticketing systems
- Research agents querying databases and APIs
- DevOps agents interacting with cloud services
- Sales agents accessing product catalogs and inventory

### Key Advantages
1. **Flexibility** - Add new tools without changing code
2. **Intelligence** - Agent learns when to use each tool
3. **Scalability** - Works with dozens of tools
4. **Maintainability** - Tools are modular and testable

## Customization Ideas

### Add More Tools
```python
def search_documentation(query):
    """Search .NET documentation"""
    pass

def book_meeting_room(time, duration):
    """Book a meeting room at venue"""
    pass

def send_calendar_invite(attendees, time):
    """Send calendar invites"""
    pass
```

### Make Tools Real
Replace mock implementations with actual APIs:
- OpenWeatherMap API
- Google Maps API
- Calendar APIs (Google/Outlook)
- Venue management systems

### Add Error Handling
Show how agents handle tool failures gracefully

## Troubleshooting

### Tools Not Being Called
- Check that `tools` parameter is passed to API
- Verify tool definitions are valid JSON schema
- Ensure model supports function calling (GPT-4, GPT-3.5-turbo)

### Infinite Loop
- Set `max_iterations` limit (currently 5)
- Check that tools return proper responses
- Verify tool results are being added to conversation

### No Response
- Check Azure OpenAI credentials
- Verify deployment name is correct
- Check console for error messages

## Next Steps

After Demo 1, transition to:
- **Demo 2:** RAG pattern (context-aware reasoning)
- **Demo 3:** Multi-agent coordination (agents working together)
- **Demo 4:** Planning pattern (breaking down complex tasks)

## Files

- `demo1_tool_use.py` - Main demo application
- `DEMO1_README.md` - This file
- `.env` - Configuration (Azure credentials)

## Presentation Tips

### Do's ✅
- Run the "Full Preparation" example - it's most impressive
- Pause to show the tool execution log
- Explain that the agent chose the tools, not you
- Mention real-world applications

### Don'ts ❌
- Don't skip the tool execution visualization
- Don't rush through the multi-tool example
- Don't forget to mention this is just the beginning
- Don't get stuck in technical details

### Time Management
- **3 min version:** Show one complex example, explain pattern
- **5 min version:** Show 2 examples, explain + Q&A
- **7 min version:** Show 3 examples, deep dive on one

## Key Takeaway

> "This is how we move from chatbots to agents. The AI doesn't just respond - 
> it takes action, gathers information, and solves problems autonomously."

---

**Demo 1 Complete!** Ready for your .NET Conf presentation! 🎉

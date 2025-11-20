# 🤖 Agentic AI Patterns - .NET Conf 2025 Demo Collection

> **From Idea to Agent: Rapid AI Prototyping with GitHub Copilot and Azure AI Foundry**

A comprehensive collection of 4 production-ready demos showcasing fundamental agentic design patterns, built for the .NET Conf 2025 presentation in Cape Town.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)

---

## 📖 The Story

This project was created to demonstrate how developers can rapidly prototype intelligent AI agents using modern tools and patterns. Built with **GitHub Copilot** assistance and powered by **Azure AI Foundry**, these demos showcase the four fundamental patterns that enable AI systems to move beyond simple chatbots to true agentic behavior.

### 🎯 The Vision

**Traditional AI:** Responds to questions  
**Agentic AI:** Plans, acts, collaborates, and learns

This repository demonstrates how to build agents that:
- 🛠️ **Take action** in the real world (Tool Use)
- 📚 **Ground responses** in your data (RAG)
- 🤝 **Collaborate** like human teams (Multi-Agent)
- 📋 **Handle complexity** systematically (Planning)

---

## 🎬 The Four Demos

### Demo 1: Tool Use Pattern 🛠️
**Time:** 3-5 minutes  
**Pattern:** Single agent with autonomous tool calling

An AI conference assistant that autonomously decides which tools to use:
- 🌤️ Weather forecasting
- 📍 Venue information
- 🚗 Travel time calculation

**Key Learning:** Agents can interact with external systems and make autonomous decisions about which tools to call.

**Run it:**
```bash
streamlit run demo1_tool_use.py
```

---

### Demo 2: RAG Pattern 📚
**Time:** 4-6 minutes  
**Pattern:** Retrieval-Augmented Generation

A knowledge base Q&A system that grounds responses in your documents:
- 📄 5 built-in knowledge documents
- 🔍 Document retrieval visualization
- ✅ Source attribution
- 📊 Comparison: With RAG vs Without RAG

**Key Learning:** Ground AI in YOUR data to prevent hallucinations and ensure factual accuracy.

**Run it:**
```bash
streamlit run demo2_rag.py
```

---

### Demo 3: Multi-Agent Coordination 🤝
**Time:** 5-7 minutes  
**Pattern:** Multiple specialized agents collaborating

A product launch team with 4 specialized agents:
- 📊 Market Researcher
- 🎯 Launch Strategist
- ✍️ Content Creator
- 🔍 Quality Reviewer

**Key Learning:** Specialized agents working together produce results no single agent could achieve alone.

**Run it:**
```bash
streamlit run demo3_multi_agent.py
```

---

### Demo 4: Planning Pattern 📋
**Time:** 5-7 minutes  
**Pattern:** Task decomposition and systematic execution

A task planner that breaks down complex projects:
- 📝 Analyzes and creates execution plans
- ⚙️ Executes steps systematically
- 🔍 Reflects on results and learns
- 📊 Visual progress tracking

**Key Learning:** Handle complexity through systematic planning, execution, and reflection.

**Run it:**
```bash
streamlit run demo4_planning.py
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Azure AI Foundry account** ([Get started](https://ai.azure.com/))
- **API credentials** (endpoint + key)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd prototype
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Azure Credentials

Create a `.env` file in the project root:

```env
# Azure OpenAI Configuration
AZURE_AI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/openai/v1/
AZURE_AI_API_KEY=your_api_key_here
AZURE_AI_MODEL_NAME=gpt-4o

# Optional: Only needed for standard Azure OpenAI endpoints
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

**Where to get credentials:**
1. Go to [Azure AI Foundry](https://ai.azure.com/)
2. Create/select your project
3. Deploy a model (e.g., GPT-4)
4. Copy endpoint and API key
5. Paste into `.env` file

See [AZURE_SETUP.md](AZURE_SETUP.md) for detailed instructions.

### 5. Run Any Demo

```bash
# Demo 1: Tool Use
streamlit run demo1_tool_use.py

# Demo 2: RAG
streamlit run demo2_rag.py

# Demo 3: Multi-Agent
streamlit run demo3_multi_agent.py

# Demo 4: Planning
streamlit run demo4_planning.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
prototype/
│
├── 🎬 Demos (4 complete applications)
│   ├── demo1_tool_use.py          # Tool Use pattern
│   ├── demo2_rag.py               # RAG pattern
│   ├── demo3_multi_agent.py       # Multi-Agent pattern
│   └── demo4_planning.py          # Planning pattern
│
├── 📚 Documentation
│   ├── README.md                  # This file
│   ├── DEMO1_README.md            # Tool Use guide
│   ├── DEMO2_README.md            # RAG guide
│   ├── DEMO3_README.md            # Multi-Agent guide
│   ├── DEMO4_README.md            # Planning guide
│   ├── DEMO_COMPARISON.md         # Pattern comparison
│   ├── DEMO_LAUNCHER.md           # Quick reference
│   ├── PRESENTATION_GUIDE.md      # Presentation playbook
│   └── ALL_DEMOS_SUMMARY.md       # Complete overview
│
├── ⚙️ Configuration
│   ├── .env                       # Your credentials (create this)
│   ├── .env.example               # Template
│   ├── requirements.txt           # Python dependencies
│   └── .gitignore                 # Git exclusions
│
├── 🔧 Setup Guides
│   ├── QUICKSTART.md              # Quick start guide
│   ├── AZURE_SETUP.md             # Azure credentials setup
│   ├── ENV_SETUP.md               # Environment configuration
│   ├── COGNITIVE_SERVICES_SETUP.md # Cognitive Services guide
│   └── TROUBLESHOOTING_404.md     # Common issues
│
├── 📦 Original Practice Files
│   ├── app.py                     # Basic multi-agent chat
│   └── agents_demo.py             # Original advanced demo
│
└── 🗂️ Environment
    └── venv/                      # Virtual environment (create this)
```

---

## 🎓 Learning Path

### For Beginners

1. **Start with Demo 1 (Tool Use)**
   - Understand basic agent-tool interaction
   - See autonomous decision making
   - Learn function calling pattern

2. **Move to Demo 2 (RAG)**
   - Learn document retrieval
   - Understand context injection
   - See grounding in action

3. **Explore Demo 3 (Multi-Agent)**
   - See agent collaboration
   - Understand specialization
   - Learn orchestration patterns

4. **Master Demo 4 (Planning)**
   - Handle complex tasks
   - Systematic execution
   - Reflection and learning

### For Intermediate Developers

1. **Understand the patterns** - Read comparison guide
2. **Modify the demos** - Add your own agents/tools
3. **Combine patterns** - RAG + Tools, Multi-Agent + Planning
4. **Build your own** - Apply to your use case

### For Advanced Developers

1. **Production-ize** - Add error handling, monitoring
2. **Scale up** - Vector databases, async execution
3. **Optimize** - Caching, cost reduction
4. **Deploy** - Azure App Service, containers

---

## 🔑 Key Concepts

### What Are Agentic Patterns?

**Agentic AI** goes beyond simple question-answering. Agents can:
- **Plan** multi-step tasks
- **Use tools** to interact with the world
- **Retrieve information** from knowledge bases
- **Collaborate** with other agents
- **Reflect** on their actions and improve

### The Four Fundamental Patterns

| Pattern | What It Does | When to Use |
|---------|--------------|-------------|
| **Tool Use** | Calls external functions/APIs | Need external actions |
| **RAG** | Retrieves relevant documents | Need grounded answers |
| **Multi-Agent** | Coordinates specialized agents | Need multiple perspectives |
| **Planning** | Breaks down complex tasks | Need systematic execution |

### Combining Patterns

In production, you combine these patterns:

```
Complex Application
├── Planning Agent (breaks down task)
│   ├── Research Agent (uses RAG)
│   │   └── Calls search_documents()
│   ├── Analysis Agent (uses Tools)
│   │   └── Calls analyze_data()
│   └── Execution Agent (uses Tools)
│       └── Calls execute_action()
```

---

## 💡 Use Cases

### Enterprise Applications

**Customer Support:**
- RAG for knowledge base
- Tools for order lookup
- Multi-Agent for complex issues

**HR Systems:**
- RAG for policies
- Tools for employee data
- Planning for onboarding

**Sales & Marketing:**
- Multi-Agent for campaigns
- RAG for product info
- Planning for launches

### Development Tools

**Code Assistant:**
- Tools for running tests
- RAG for documentation
- Planning for refactoring

**DevOps:**
- Tools for deployments
- Multi-Agent for reviews
- Planning for migrations

---

## 🛠️ Customization Guide

### Adding Your Own Documents (Demo 2)

```python
# In demo2_rag.py, add to KNOWLEDGE_BASE:
KNOWLEDGE_BASE["my_doc"] = {
    "title": "My Company Guide",
    "content": """
    Your document content here...
    """
}
```

### Adding Your Own Tools (Demo 1)

```python
# In demo1_tool_use.py, add to TOOLS:
{
    "type": "function",
    "function": {
        "name": "my_tool",
        "description": "What it does",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string"}
            }
        }
    }
}

# Implement the function:
def my_tool(param1):
    # Your logic here
    return result
```

### Adding Your Own Agents (Demo 3)

```python
# In demo3_multi_agent.py, add to AGENTS:
"my_agent": {
    "name": "My Agent",
    "icon": "🎨",
    "color": "#FF6B6B",
    "role": "my_role",
    "system_prompt": "You are a..."
}
```

---

## 📊 Technical Stack

### Core Technologies

- **Python 3.8+** - Programming language
- **Streamlit** - Web framework for demos
- **Azure OpenAI** - LLM provider
- **OpenAI SDK** - API client

### Key Libraries

```
streamlit>=1.29.0      # Web UI framework
openai>=1.30.0         # Azure OpenAI client
python-dotenv>=1.0.0   # Environment variables
```

### Architecture

```
User Interface (Streamlit)
        ↓
Application Logic (Python)
        ↓
OpenAI SDK
        ↓
Azure AI Foundry
        ↓
GPT-4 / GPT-3.5
```

---

## 🎤 Presentation Mode

This project was built for a conference presentation. Here's how to use it:

### Quick Demo Selector

**15-minute slot:** Demo 1 + Demo 2  
**20-minute slot:** Demo 1 + Demo 2 + Demo 3  
**25-minute slot:** All 4 demos  
**10-minute slot:** Demo 2 only

### Pre-Presentation Checklist

- [ ] Virtual environment activated
- [ ] `.env` file configured
- [ ] All demos tested once
- [ ] Browser zoom set to 125%
- [ ] Backup screenshots ready

See [PRESENTATION_GUIDE.md](PRESENTATION_GUIDE.md) for complete scripts and talking points.

---

## 🐛 Troubleshooting

### Common Issues

**"Please configure Azure AI credentials"**
- Check `.env` file exists
- Verify endpoint format
- Confirm API key is valid

**"404 Resource not found"**
- Check deployment name matches model
- Verify endpoint URL is correct
- See [TROUBLESHOOTING_404.md](TROUBLESHOOTING_404.md)

**Import errors**
```bash
pip install -r requirements.txt --force-reinstall
```

**Port already in use**
```bash
streamlit run demo1_tool_use.py --server.port 8502
```

### Getting Help

1. Check individual demo READMEs
2. Review setup guides
3. See troubleshooting docs
4. Check Azure AI Foundry status

---

## 🎯 What You'll Learn

### Agentic Design Patterns
- How agents use tools autonomously
- How to ground AI in your data
- How agents collaborate effectively
- How to handle complex multi-step tasks

### Practical Skills
- Building with Streamlit
- Integrating Azure AI Foundry
- Prompt engineering for agents
- Orchestrating multi-agent systems

### Best Practices
- Error handling for AI applications
- Cost optimization strategies
- Monitoring and evaluation
- Production deployment patterns

---

## 🚀 Next Steps

### After Running the Demos

1. **Experiment** - Modify prompts, add features
2. **Combine** - Mix patterns for your use case
3. **Build** - Create your own agent application
4. **Deploy** - Take to production

### Suggested Projects

**Beginner:**
- Personal assistant with 3 tools
- FAQ bot with RAG
- Simple multi-agent workflow

**Intermediate:**
- Customer support system
- Document analysis pipeline
- Research assistant

**Advanced:**
- Full enterprise application
- Multi-agent orchestration platform
- Custom agent framework

---

## 📚 Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

### Learning Materials
- [Agentic Design Patterns](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/)
- [LangChain Documentation](https://python.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Community
- [Streamlit Community](https://discuss.streamlit.io/)
- [Azure AI Community](https://techcommunity.microsoft.com/t5/ai-azure-ai-services/ct-p/Azure-AI-Services)

---

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork and experiment
- Add your own demos
- Improve documentation
- Share your learnings

---

## 📄 License

This project is for educational purposes. Built for .NET Conf 2025 presentation.

---

## 🙏 Acknowledgments

- **GitHub Copilot** - AI pair programming assistant
- **Azure AI Foundry** - LLM infrastructure
- **Streamlit** - Rapid prototyping framework
- **.NET Conf 2025** - Presentation opportunity

---

## 📞 Contact

**Presenter:** Abed Matini  
**Event:** .NET Conf 2025 - Cape Town  
**Date:** November 22, 2025  
**Session:** "From Idea to Agent: Rapid AI Prototyping"

---

## ⭐ Key Takeaways

1. **Agentic AI** is the future of software development
2. **Four patterns** cover most use cases
3. **Rapid prototyping** is possible with modern tools
4. **Production deployment** requires additional considerations
5. **Start simple**, scale up as needed

---

**Built with ❤️ using GitHub Copilot and Azure AI Foundry**

🎤 **Ready to build your own agents? Start with Demo 1!** 🚀

```bash
streamlit run demo1_tool_use.py
```

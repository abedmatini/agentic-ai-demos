# 🚀 Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Activate Virtual Environment

```bash
# Windows
.\venv\Scripts\activate

# You should see (venv) in your terminal prompt
```

## Step 2: Configure Azure AI

1. Copy `.env.example` to `.env`
2. Fill in your Azure AI credentials:

```env
AZURE_AI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_AI_API_KEY=your_api_key_here
AZURE_AI_MODEL_NAME=gpt-4
```

**Don't have Azure AI credentials yet?**
- Visit [Azure AI Foundry](https://ai.azure.com/)
- Create a free account
- Deploy a model (GPT-4 recommended)
- Copy your endpoint and API key

## Step 3: Run the App

**Option A: Basic Multi-Agent Chat**
```bash
streamlit run app.py
```

**Option B: Advanced Agent Workflows**
```bash
streamlit run agents_demo.py
```

## Step 4: Start Chatting!

1. Your browser will open automatically to `http://localhost:8501`
2. Select an agent from the sidebar
3. Type your message and press Enter
4. Watch the AI respond!

## 🎯 Try These Examples

### Research Assistant
```
"Explain quantum computing in simple terms"
```

### Code Helper
```
"Help me debug this Python function that's not working"
```

### Creative Writer
```
"Write a short story about a robot learning to paint"
```

### Multi-Agent Workflow
```
"How can we improve customer retention for our SaaS product?"
```

## 🛑 Troubleshooting

**App won't start?**
```bash
# Make sure virtual environment is activated
.\venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

**"Configure .env file" warning?**
- Check that `.env` file exists (not `.env.example`)
- Verify credentials are correct
- Ensure no extra spaces in the values

**Port already in use?**
```bash
streamlit run app.py --server.port 8502
```

## 📚 Next Steps

1. ✅ Try all different agents
2. ✅ Experiment with the Multi-Agent Workflow
3. ✅ Compare agent responses side-by-side
4. ✅ Customize agents with your own prompts
5. ✅ Build your own agent!

## 💡 Tips

- Each agent maintains separate chat history
- Use "Clear Chat History" to start fresh
- Try the same question with different agents
- Experiment with different prompts and questions

Happy coding! 🎉

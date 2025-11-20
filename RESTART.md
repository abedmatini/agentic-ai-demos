# 🔄 Quick Restart Guide

## After Making Changes

Whenever you update `.env` or install new packages, restart Streamlit:

### Windows (PowerShell)

1. **Stop the app:**
   - Press `Ctrl + C` in the terminal running Streamlit

2. **Restart the app:**
   ```bash
   streamlit run app.py
   ```

### Alternative: Force Kill and Restart

If Ctrl+C doesn't work:

```bash
# Stop all Streamlit processes
taskkill /F /IM streamlit.exe

# Restart
streamlit run app.py
```

## ✅ Checklist Before Running

- [ ] `.env` file exists (not `.env.example`)
- [ ] All values in `.env` are filled in (no placeholders)
- [ ] Virtual environment is activated `(venv)`
- [ ] Dependencies are installed: `pip install -r requirements.txt`

## 🎯 Your Current Setup

Based on your configuration, your `.env` should have:

```env
AZURE_AI_ENDPOINT=https://abedmatini-streamlit-resource.cognitiveservices.azure.com/openai/v1/
AZURE_AI_API_KEY=<your-actual-api-key>
AZURE_AI_MODEL_NAME=gpt-4o
```

## 🚀 Ready to Test!

```bash
streamlit run app.py
```

Then open: http://localhost:8501

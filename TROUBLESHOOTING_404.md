# Troubleshooting 404 Error

## Error: (404) Resource not found

This error means Azure can't find your model deployment. Here's how to fix it:

## 🔍 Root Causes & Solutions

### 1. Model Not Deployed ⚠️ MOST COMMON

**Problem:** You haven't deployed a model in Azure AI Studio yet.

**Solution:**
1. Go to [Azure AI Studio](https://ai.azure.com/)
2. Select your project
3. Click **"Deployments"** in the left sidebar
4. Click **"+ Deploy model"** or **"+ Create"**
5. Choose a model (e.g., `gpt-4`, `gpt-35-turbo`)
6. Give it a deployment name (e.g., `gpt-4-deployment`)
7. Click **"Deploy"**
8. **IMPORTANT:** Copy the deployment name exactly!

### 2. Wrong Model/Deployment Name

**Problem:** The `AZURE_AI_MODEL_NAME` in your `.env` doesn't match your deployment name.

**How to Check:**
1. Go to Azure AI Studio → Deployments
2. Look at the **"Deployment name"** column
3. Copy it EXACTLY (case-sensitive!)

**Update `.env`:**
```env
AZURE_AI_MODEL_NAME=your-exact-deployment-name
```

**Common mistakes:**
- ❌ `AZURE_AI_MODEL_NAME=gpt-4` (model name)
- ✅ `AZURE_AI_MODEL_NAME=gpt-4-deployment` (deployment name)

### 3. Wrong Endpoint Format

**Problem:** Endpoint URL is incorrect or incomplete.

**Correct format:**
```
https://your-resource-name.openai.azure.com/
```

**Check:**
- ✅ Starts with `https://`
- ✅ Contains `.openai.azure.com/`
- ✅ Ends with `/`
- ❌ No extra paths after `.azure.com/`

**Where to find it:**
1. Azure Portal → Your Azure OpenAI resource
2. **"Keys and Endpoint"** section
3. Copy the **"Endpoint"** value

### 4. Using Azure AI Foundry Endpoint Instead

**Problem:** You're using an Azure AI Foundry endpoint instead of Azure OpenAI.

**Wrong:**
```
https://something.api.azureml.ms/
https://something.cognitiveservices.azure.com/
```

**Correct:**
```
https://your-name.openai.azure.com/
```

## 🛠️ Step-by-Step Fix

### Step 1: Verify Your Deployment

```bash
# In Azure AI Studio, check:
1. Go to https://ai.azure.com/
2. Select your project
3. Click "Deployments"
4. Confirm you see at least one deployment
5. Note the exact "Deployment name"
```

### Step 2: Update .env File

```env
# Use your Azure OpenAI endpoint (from Azure Portal)
AZURE_AI_ENDPOINT=https://YOUR-RESOURCE-NAME.openai.azure.com/

# Use your API key (from Azure Portal → Keys and Endpoint)
AZURE_AI_API_KEY=your_api_key_here

# Use your DEPLOYMENT NAME (from Azure AI Studio → Deployments)
AZURE_AI_MODEL_NAME=your-deployment-name
```

### Step 3: Restart Streamlit

```bash
# Stop the app (Ctrl+C)
# Restart it
streamlit run app.py
```

### Step 4: Check Debug Info

1. Look at the sidebar in the app
2. Expand **"🔍 View Configuration Details"**
3. Verify all values are correct
4. Send a test message
5. If error occurs, read the detailed error message

## 📋 Quick Checklist

- [ ] Azure OpenAI resource created in Azure Portal
- [ ] Model deployed in Azure AI Studio
- [ ] Deployment name copied exactly
- [ ] Endpoint format: `https://xxx.openai.azure.com/`
- [ ] API key copied from Azure Portal
- [ ] `.env` file exists (not `.env.example`)
- [ ] No extra spaces in `.env` values
- [ ] Streamlit app restarted after changing `.env`

## 🎯 Example Working Configuration

**Azure Portal:**
- Resource name: `my-openai-resource`
- Endpoint: `https://my-openai-resource.openai.azure.com/`
- API Key: `abc123...xyz789`

**Azure AI Studio:**
- Deployment name: `gpt-4-deployment`

**Your `.env` file:**
```env
AZURE_AI_ENDPOINT=https://my-openai-resource.openai.azure.com/
AZURE_AI_API_KEY=abc123...xyz789
AZURE_AI_MODEL_NAME=gpt-4-deployment
```

## 🆘 Still Not Working?

1. **Check the debug info in the app** - It shows your exact configuration
2. **Try a simple deployment name** - Use something like `gpt4` or `test-deployment`
3. **Verify API key is valid** - Copy it again from Azure Portal
4. **Check Azure subscription** - Ensure it's active and has credits
5. **Try a different model** - Deploy `gpt-35-turbo` instead of `gpt-4`

## 💡 Pro Tips

- Deployment names are case-sensitive
- The endpoint must end with `/`
- Don't include the model name in the endpoint
- The API key should be 32+ characters long
- Restart Streamlit after any `.env` changes

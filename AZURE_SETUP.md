# Azure OpenAI Setup Guide

## Getting Your Azure OpenAI Credentials

### Step 1: Access Azure Portal
1. Go to [Azure Portal](https://portal.azure.com/)
2. Sign in with your Microsoft account

### Step 2: Create/Access Azure OpenAI Resource
1. Search for "Azure OpenAI" in the search bar
2. Either:
   - Click on your existing Azure OpenAI resource, OR
   - Create a new one: Click "+ Create" → Fill in details → Create

### Step 3: Get Your Endpoint
1. In your Azure OpenAI resource, go to **"Keys and Endpoint"** (left sidebar)
2. Copy the **Endpoint** - it looks like:
   ```
   https://your-resource-name.openai.azure.com/
   ```
3. This is your `AZURE_AI_ENDPOINT`

### Step 4: Get Your API Key
1. On the same "Keys and Endpoint" page
2. Copy **KEY 1** or **KEY 2** (either works)
3. This is your `AZURE_AI_API_KEY`

### Step 5: Deploy a Model (if not already done)
1. Go to **"Model deployments"** in your Azure OpenAI resource
2. Click **"Manage Deployments"** → Opens Azure AI Studio
3. Click **"+ Create new deployment"**
4. Select a model (e.g., `gpt-4`, `gpt-35-turbo`)
5. Give it a deployment name (e.g., `gpt-4`)
6. Click **"Create"**

### Step 6: Update Your .env File

Create/edit `.env` file in your project:

```env
AZURE_AI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_AI_API_KEY=your_actual_api_key_here
AZURE_AI_MODEL_NAME=gpt-4
```

**Important Notes:**
- ✅ Use **Azure OpenAI endpoint** (format: `https://xxx.openai.azure.com/`)
- ❌ NOT Azure AI Foundry endpoint
- The endpoint should end with a `/`
- Keep your API key secret - never commit it to Git

## Troubleshooting

### "Authentication failed"
- Check your API key is correct
- Ensure no extra spaces in `.env` file
- Verify the key hasn't expired

### "Model not found"
- Make sure you've deployed a model in Azure AI Studio
- Check the model name matches your deployment name
- Common names: `gpt-4`, `gpt-35-turbo`, `gpt-4-turbo`

### "Endpoint not found"
- Verify endpoint format: `https://xxx.openai.azure.com/`
- Must end with `/`
- No extra paths after `.azure.com/`

## Testing Your Setup

Run the app:
```bash
streamlit run app.py
```

If configured correctly, you should see:
- ✅ "Azure AI configured" in the sidebar
- No errors when sending a message

## Free Tier / Pricing

- Azure OpenAI requires an Azure subscription
- Free trial available with $200 credit
- Pay-as-you-go pricing after trial
- Check [Azure OpenAI Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)

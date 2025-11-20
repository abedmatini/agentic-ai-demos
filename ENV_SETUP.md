# .env File Setup - Quick Reference

## ✅ Correct Configuration

Your `.env` file should look like this:

```env
AZURE_AI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_AI_API_KEY=abc123def456...
AZURE_AI_MODEL_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

## 🔍 Where to Find Each Value

### 1. AZURE_AI_ENDPOINT
**Location:** Azure Portal → Your Azure OpenAI Resource → "Keys and Endpoint"

**Format:** `https://your-resource-name.openai.azure.com/`

**Example:** `https://my-openai-east.openai.azure.com/`

✅ Must end with `/`
✅ Must contain `.openai.azure.com/`

### 2. AZURE_AI_API_KEY
**Location:** Azure Portal → Your Azure OpenAI Resource → "Keys and Endpoint"

**Copy:** Either KEY 1 or KEY 2 (both work)

**Length:** Usually 32+ characters

### 3. AZURE_AI_MODEL_NAME ⚠️ IMPORTANT
**Location:** Azure AI Studio (ai.azure.com) → Your Project → "Deployments"

**This is your DEPLOYMENT NAME, not the model name!**

**Example:**
- ❌ Wrong: `gpt-4` (this is the model name)
- ✅ Correct: `gpt-4-deployment` (this is what you named it when deploying)

**How to find it:**
1. Go to https://ai.azure.com/
2. Select your project
3. Click "Deployments" in sidebar
4. Look at the "Deployment name" column
5. Copy it EXACTLY (case-sensitive!)

### 4. AZURE_OPENAI_API_VERSION
**Default:** `2024-02-15-preview`

**Usually you don't need to change this.**

## 📝 Example Real Configuration

```env
# Real example (with fake credentials)
AZURE_AI_ENDPOINT=https://contoso-openai.openai.azure.com/
AZURE_AI_API_KEY=1234567890abcdef1234567890abcdef
AZURE_AI_MODEL_NAME=gpt-4-turbo-deployment
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

## ⚠️ Common Mistakes

### Mistake 1: Using Model Name Instead of Deployment Name
```env
# ❌ Wrong
AZURE_AI_MODEL_NAME=gpt-4

# ✅ Correct
AZURE_AI_MODEL_NAME=my-gpt4-deployment
```

### Mistake 2: Wrong Endpoint Format
```env
# ❌ Wrong - Missing trailing slash
AZURE_AI_ENDPOINT=https://my-resource.openai.azure.com

# ❌ Wrong - Azure AI Foundry endpoint
AZURE_AI_ENDPOINT=https://something.api.azureml.ms/

# ✅ Correct
AZURE_AI_ENDPOINT=https://my-resource.openai.azure.com/
```

### Mistake 3: Extra Spaces
```env
# ❌ Wrong - Space before value
AZURE_AI_API_KEY= abc123...

# ✅ Correct - No spaces
AZURE_AI_API_KEY=abc123...
```

## 🧪 Test Your Configuration

After setting up your `.env` file:

1. **Restart Streamlit:**
   ```bash
   streamlit run app.py
   ```

2. **Check the sidebar** - Expand "🔍 View Configuration Details"

3. **Look for:**
   - ✓ Endpoint format looks correct
   - ✓ API Key is set
   - ✓ Deployment name is shown

4. **Send a test message** - Try: "Hello, how are you?"

## 🆘 Still Getting 404 Error?

The most common cause is **deployment name mismatch**.

**Double-check:**
1. Go to Azure AI Studio → Deployments
2. Find your deployment
3. Copy the EXACT name (case-sensitive!)
4. Update `AZURE_AI_MODEL_NAME` in `.env`
5. Restart Streamlit

## 💡 Pro Tip

Create a simple deployment name like:
- `gpt4`
- `gpt35`
- `test-deployment`

This makes it easier to remember and less prone to typos!

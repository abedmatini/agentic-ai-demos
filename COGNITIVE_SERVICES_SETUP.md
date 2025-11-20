# Cognitive Services Endpoint Setup

## 🎯 Your Configuration

Based on your example, your `.env` file should look like this:

```env
AZURE_AI_ENDPOINT=https://abedmatini-streamlit-resource.cognitiveservices.azure.com/openai/v1/
AZURE_AI_API_KEY=your_actual_api_key
AZURE_AI_MODEL_NAME=gpt-4o
```

## 📝 Key Differences

### Cognitive Services Endpoint vs Azure OpenAI Endpoint

**Cognitive Services (Your Case):**
```
https://your-name.cognitiveservices.azure.com/openai/v1/
```
- Contains `cognitiveservices`
- Includes `/openai/v1/` path
- No API version needed

**Azure OpenAI (Alternative):**
```
https://your-name.openai.azure.com/
```
- Contains `openai.azure.com`
- No path after domain
- Requires API version

## ✅ Your Setup Steps

1. **Create/Edit `.env` file:**
   ```env
   AZURE_AI_ENDPOINT=https://abedmatini-streamlit-resource.cognitiveservices.azure.com/openai/v1/
   AZURE_AI_API_KEY=<paste-your-actual-api-key>
   AZURE_AI_MODEL_NAME=gpt-4o
   ```

2. **Replace `<paste-your-actual-api-key>`** with your real API key

3. **Save the file**

4. **Run Streamlit:**
   ```bash
   streamlit run app.py
   ```

## 🔍 How It Works

The app now automatically detects your endpoint type:

- If endpoint contains `cognitiveservices` → Uses `OpenAI` client with `base_url`
- If endpoint contains `openai.azure.com` → Uses `AzureOpenAI` client

## 🎉 You're All Set!

Your configuration should work now. The app will:
1. Detect your Cognitive Services endpoint
2. Use the correct OpenAI client
3. Connect to your `gpt-4o` deployment

Try sending a message like "Hello, how are you?" to test!

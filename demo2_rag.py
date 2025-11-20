"""
Demo 2: RAG Pattern (Retrieval-Augmented Generation)
Knowledge Base Q&A - Shows context-aware responses using your own data

This demo showcases:
- Document retrieval from knowledge base
- Context injection into prompts
- Grounded, factual responses
- Source attribution and transparency
"""

import streamlit as st
import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAI
import re
from typing import List, Dict

load_dotenv()

st.set_page_config(
    page_title="Demo 2: RAG Pattern",
    page_icon="📚",
    layout="wide"
)

# Sample knowledge base - In production, this would be a vector database
KNOWLEDGE_BASE = {
    "dotnet_conf_2025": {
        "title": ".NET Conf 2025 - Cape Town Event Guide",
        "content": """
.NET Conf 2025 Community Edition South Africa
Date: November 22, 2025
Location: Cape Town Convention Centre, 1 Lower Long St, Cape Town, South Africa

Event Schedule:
- 08:00 - 09:00: Registration and Breakfast
- 09:00 - 09:30: Opening Keynote
- 09:30 - 17:00: Technical Sessions (3 parallel tracks)
- 17:00 - 18:00: Networking Reception

Tracks:
1. AI/ML Track - Focus on Azure AI, ML.NET, and AI integration
2. .NET Core Track - Latest features in .NET 8 and .NET 9
3. Cloud & DevOps Track - Azure services, containers, and CI/CD

Featured Speakers:
- Abed Matini: "From Idea to Agent: Rapid AI Prototyping"
- Sarah Chen: "Building Scalable Microservices with .NET"
- Marcus Johnson: "Azure AI Services Deep Dive"

Registration: Free for community members
Capacity: 500 attendees
WiFi: Available throughout venue
Parking: On-site parking available ($10/day)

Contact: info@dotnetconf.co.za
Website: https://dotnetconf.co.za
        """
    },
    "azure_ai_foundry": {
        "title": "Azure AI Foundry Overview",
        "content": """
Azure AI Foundry (formerly Azure AI Studio)
A comprehensive platform for building, deploying, and managing AI applications.

Key Features:
- Model Catalog: Access to GPT-4, GPT-3.5, Llama, Mistral, and more
- Prompt Flow: Visual designer for AI workflows
- Evaluation Tools: Test and measure AI application quality
- Deployment: One-click deployment to Azure
- Monitoring: Track usage, costs, and performance

Agentic Capabilities:
- Tool/Function Calling: Enable agents to use external tools
- Multi-turn Conversations: Maintain context across interactions
- RAG Support: Built-in vector search and document indexing
- Agent Templates: Pre-built patterns for common scenarios

Pricing:
- Pay-as-you-go based on token usage
- GPT-4: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens
- GPT-3.5: ~$0.0015 per 1K input tokens, ~$0.002 per 1K output tokens
- Vector search: Included in Azure AI Search pricing

Getting Started:
1. Create Azure AI Foundry resource in Azure Portal
2. Deploy a model (e.g., GPT-4)
3. Get API key and endpoint
4. Start building with SDK or API

Documentation: https://learn.microsoft.com/azure/ai-studio/
        """
    },
    "agentic_patterns": {
        "title": "Agentic Design Patterns Guide",
        "content": """
Agentic Design Patterns for AI Applications

1. Tool Use Pattern
Description: Agent autonomously selects and executes tools/functions
Use Cases: API integration, data retrieval, action execution
Example: Customer service bot accessing order database
Key Benefit: Agents can interact with external systems

2. Retrieval-Augmented Generation (RAG)
Description: Agent retrieves relevant context before responding
Use Cases: Document Q&A, knowledge bases, technical support
Example: HR bot answering policy questions from employee handbook
Key Benefit: Grounded responses based on your data

3. Multi-Agent Coordination
Description: Multiple specialized agents collaborate on tasks
Use Cases: Complex workflows, diverse expertise needed
Example: Product launch team with research, strategy, content agents
Key Benefit: Specialization and parallel processing

4. Planning Pattern
Description: Agent breaks down complex tasks into steps
Use Cases: Project management, multi-step workflows
Example: Event planning agent creating detailed execution plan
Key Benefit: Handles complexity systematically

5. Reflection Pattern
Description: Agent reviews and critiques its own outputs
Use Cases: Quality assurance, iterative improvement
Example: Code review agent checking generated code
Key Benefit: Self-improvement and error detection

Combining Patterns:
- RAG + Tool Use: Retrieve docs, then call APIs based on content
- Multi-Agent + Planning: Each agent creates plans for their domain
- Planning + Reflection: Execute plan, reflect, adjust next steps

Best Practices:
- Start simple with one pattern
- Add complexity as needed
- Monitor costs and performance
- Test thoroughly with evaluation sets
- Implement error handling and retries
        """
    },
    "github_copilot": {
        "title": "GitHub Copilot for AI Development",
        "content": """
GitHub Copilot: Your AI Pair Programmer

What is Copilot?
An AI-powered code completion tool that suggests entire lines or blocks of code as you type.
Powered by OpenAI Codex, trained on billions of lines of public code.

Key Features:
- Code Suggestions: Real-time completions as you type
- Chat Interface: Ask questions and get code explanations
- Code Generation: Generate functions from comments
- Test Generation: Create unit tests automatically
- Documentation: Generate docstrings and comments

For AI Development:
- Prompt Engineering: Helps write effective system prompts
- API Integration: Suggests correct API usage patterns
- Error Handling: Recommends try-catch patterns
- Best Practices: Follows common patterns and conventions

Productivity Gains:
- 55% faster task completion (GitHub study)
- 74% of developers feel more focused
- Reduces context switching and documentation lookup

Tips for AI Projects:
1. Write clear comments describing what you want
2. Use descriptive variable and function names
3. Show examples in comments for complex patterns
4. Review suggestions - Copilot isn't always right
5. Use Copilot Chat for explanations and debugging

Pricing:
- Individual: $10/month or $100/year
- Business: $19/user/month
- Enterprise: Custom pricing

Getting Started:
1. Install GitHub Copilot extension in VS Code
2. Sign in with GitHub account
3. Start typing and accept suggestions with Tab
4. Use Ctrl+Enter to see more suggestions

Documentation: https://docs.github.com/copilot
        """
    },
    "python_streamlit": {
        "title": "Building AI Apps with Python and Streamlit",
        "content": """
Streamlit: Rapid Prototyping for AI Applications

What is Streamlit?
An open-source Python framework for building data and AI web applications.
Turn Python scripts into interactive web apps in minutes.

Key Features:
- Pure Python: No HTML, CSS, or JavaScript needed
- Reactive: Auto-updates when code or data changes
- Component Library: Charts, tables, forms, media
- Session State: Maintain state across interactions
- Caching: Speed up expensive computations

For AI Applications:
- Chat Interfaces: Built-in chat message components
- File Upload: Easy document upload for RAG
- Progress Tracking: Show agent execution progress
- Visualization: Display agent workflows and results
- Deployment: Deploy to Streamlit Cloud for free

Common Patterns:
1. Chat Interface: st.chat_message() and st.chat_input()
2. Sidebar Controls: st.sidebar for configuration
3. Expanders: st.expander() for collapsible content
4. Progress: st.progress() and st.spinner()
5. State Management: st.session_state for persistence

Example AI App Structure:
```python
import streamlit as st
from openai import OpenAI

st.title("My AI App")

# Sidebar configuration
with st.sidebar:
    api_key = st.text_input("API Key", type="password")

# Main chat interface
if prompt := st.chat_input("Ask me anything"):
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.write(response)
```

Deployment Options:
- Streamlit Cloud: Free hosting for public apps
- Docker: Containerize and deploy anywhere
- Azure App Service: Enterprise deployment
- AWS/GCP: Cloud platform deployment

Best Practices:
- Use st.cache_data for expensive operations
- Keep UI responsive with st.spinner()
- Organize code with functions and modules
- Handle errors gracefully with try-except
- Test locally before deploying

Resources:
- Documentation: https://docs.streamlit.io
- Gallery: https://streamlit.io/gallery
- Community: https://discuss.streamlit.io

Installation:
pip install streamlit
streamlit run app.py
        """
    }
}

def simple_search(query: str, top_k: int = 2) -> List[Dict]:
    """
    Simple keyword-based search (in production, use vector embeddings)
    Returns documents ranked by keyword matches
    """
    query_lower = query.lower()
    query_words = set(re.findall(r'\w+', query_lower))
    
    results = []
    for doc_id, doc in KNOWLEDGE_BASE.items():
        content_lower = (doc['title'] + " " + doc['content']).lower()
        content_words = set(re.findall(r'\w+', content_lower))
        
        # Simple scoring: count matching words
        matches = len(query_words.intersection(content_words))
        
        if matches > 0:
            results.append({
                'doc_id': doc_id,
                'title': doc['title'],
                'content': doc['content'],
                'score': matches
            })
    
    # Sort by score and return top_k
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:top_k]

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

def answer_with_rag(client, question: str, retrieved_docs: List[Dict]) -> str:
    """Generate answer using retrieved context"""
    deployment_name = os.getenv("AZURE_AI_MODEL_NAME", "gpt-4")
    
    # Build context from retrieved documents
    context = "\n\n---\n\n".join([
        f"Document: {doc['title']}\n{doc['content']}"
        for doc in retrieved_docs
    ])
    
    system_prompt = """You are a helpful assistant that answers questions based on the provided context.

Rules:
1. Only use information from the provided context
2. If the context doesn't contain the answer, say so clearly
3. Cite which document you're using when answering
4. Be concise but complete
5. If asked about something not in the context, acknowledge the limitation"""

    user_prompt = f"""Context from knowledge base:

{context}

---

Question: {question}

Please answer based on the context above."""

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3  # Lower temperature for more factual responses
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("📚 Demo 2: RAG")
    st.markdown("---")
    
    st.markdown("### 📋 What This Shows")
    st.info("""
    **Agentic Pattern: RAG**
    
    - Document retrieval
    - Context injection
    - Grounded responses
    - Source attribution
    """)
    
    st.markdown("---")
    
    st.markdown("### 📖 Knowledge Base")
    st.write(f"**{len(KNOWLEDGE_BASE)} documents loaded:**")
    for doc_id, doc in KNOWLEDGE_BASE.items():
        with st.expander(f"📄 {doc['title'][:30]}..."):
            st.caption(f"ID: {doc_id}")
            st.caption(f"Length: {len(doc['content'])} chars")
    
    st.markdown("---")
    
    st.markdown("### 🔍 How RAG Works")
    st.markdown("""
    1. **Retrieve** relevant docs
    2. **Inject** as context
    3. **Generate** grounded answer
    4. **Cite** sources used
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
st.title("📚 Demo 2: RAG Pattern")
st.markdown("### Knowledge Base Q&A System")

st.markdown("""
Ask questions about .NET Conf, Azure AI Foundry, agentic patterns, or development tools. 
The agent will retrieve relevant documents and provide **grounded, factual answers**.
""")

st.markdown("---")

# Example questions
st.markdown("### 💡 Try These Questions:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📅 Event Details", use_container_width=True):
        st.session_state.question = "What are the key details about .NET Conf 2025 in Cape Town?"

with col2:
    if st.button("🤖 Agentic Patterns", use_container_width=True):
        st.session_state.question = "What are the main agentic design patterns and when should I use each?"

with col3:
    if st.button("💰 Azure Pricing", use_container_width=True):
        st.session_state.question = "How much does Azure AI Foundry cost and what's included?"

st.markdown("---")

# User input
user_question = st.text_area(
    "Ask a question:",
    value=st.session_state.get('question', ''),
    height=100,
    placeholder="e.g., What tools does GitHub Copilot offer for AI development?"
)

# Advanced options
with st.expander("⚙️ Advanced Options"):
    num_docs = st.slider("Number of documents to retrieve:", 1, 5, 2)
    show_context = st.checkbox("Show retrieved context", value=True)

if st.button("🔍 Ask Question", type="primary", use_container_width=True):
    if user_question:
        client = get_azure_client()
        
        if client:
            st.markdown("---")
            
            # Step 1: Retrieval
            st.markdown("## 🔍 Step 1: Document Retrieval")
            with st.spinner("Searching knowledge base..."):
                retrieved_docs = simple_search(user_question, top_k=num_docs)
            
            if retrieved_docs:
                st.success(f"✅ Found {len(retrieved_docs)} relevant document(s)")
                
                # Show retrieved documents
                for idx, doc in enumerate(retrieved_docs, 1):
                    with st.expander(f"📄 Document {idx}: {doc['title']}", expanded=show_context):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.markdown(f"**Relevance Score:** {doc['score']} matching keywords")
                        with col2:
                            st.caption(f"ID: {doc['doc_id']}")
                        
                        if show_context:
                            st.markdown("**Content:**")
                            st.text(doc['content'][:500] + "..." if len(doc['content']) > 500 else doc['content'])
                
                # Step 2: Generation
                st.markdown("---")
                st.markdown("## 💬 Step 2: Answer Generation")
                
                with st.spinner("Generating answer from context..."):
                    answer = answer_with_rag(client, user_question, retrieved_docs)
                
                # Show answer
                st.markdown("### 🎯 Answer")
                st.success(answer)
                
                # Show sources
                st.markdown("---")
                st.markdown("### 📚 Sources Used")
                for doc in retrieved_docs:
                    st.caption(f"• {doc['title']}")
                
                # Comparison: With vs Without RAG
                st.markdown("---")
                with st.expander("🔬 Compare: With RAG vs Without RAG"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**✅ With RAG (Above)**")
                        st.info("""
                        - Uses your specific documents
                        - Factually grounded
                        - Cites sources
                        - Up-to-date with your data
                        """)
                    
                    with col2:
                        st.markdown("**❌ Without RAG**")
                        st.warning("""
                        - Uses only training data
                        - May hallucinate
                        - No source attribution
                        - Knowledge cutoff date
                        """)
            else:
                st.warning("No relevant documents found. Try rephrasing your question.")
        
        else:
            st.error("⚠️ Please configure Azure AI credentials in .env file")
    else:
        st.warning("Please enter a question first")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p><b>Demo 2:</b> RAG Pattern | Built for .NET Conf 2025 Presentation</p>
    <p><i>In production, use vector embeddings (Azure AI Search, Pinecone, etc.) for better retrieval</i></p>
</div>
""", unsafe_allow_html=True)

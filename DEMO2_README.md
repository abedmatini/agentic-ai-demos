# Demo 2: RAG Pattern 📚

## Overview

This demo showcases the **RAG (Retrieval-Augmented Generation) Pattern** - where an AI agent retrieves relevant information from your own documents before answering questions. This grounds responses in your data, preventing hallucinations and ensuring factual accuracy.

## What It Demonstrates

### Key Concepts
- ✅ **Document Retrieval** - Finding relevant information from knowledge base
- ✅ **Context Injection** - Adding retrieved docs to the prompt
- ✅ **Grounded Responses** - Answers based on your data, not just training
- ✅ **Source Attribution** - Showing which documents were used

### Agentic Pattern: RAG
The agent acts as a research assistant that:
1. Searches your knowledge base for relevant documents
2. Retrieves the most relevant content
3. Uses that content as context when answering
4. Cites sources for transparency

## Running the Demo

### Quick Start
```bash
streamlit run demo2_rag.py
```

The app will open at: `http://localhost:8501`

### Prerequisites
- Virtual environment activated
- `.env` file configured with Azure OpenAI credentials
- Dependencies installed (`requirements.txt`)

## The Knowledge Base

### 5 Built-in Documents

1. **📅 .NET Conf 2025 - Cape Town Event Guide**
   - Event details, schedule, speakers
   - Location and logistics
   - Registration information

2. **🤖 Azure AI Foundry Overview**
   - Platform features and capabilities
   - Pricing and deployment options
   - Getting started guide

3. **🎯 Agentic Design Patterns Guide**
   - All major patterns explained
   - Use cases and examples
   - Best practices for combining patterns

4. **💻 GitHub Copilot for AI Development**
   - Features and capabilities
   - Productivity tips
   - Integration with AI projects

5. **🐍 Building AI Apps with Python and Streamlit**
   - Framework overview
   - Common patterns for AI apps
   - Deployment options

## Demo Flow (4-6 minutes)

### 1. Introduction (1 minute)
**Say:**
> "One of the biggest challenges with AI is hallucination - making up facts. RAG solves this 
> by grounding the AI in your actual documents. Let me show you how this works."

**Show:**
- The knowledge base in the sidebar (5 documents)
- Explain these are your company docs, policies, or data

### 2. Show the Two-Step Process (30 seconds)
**Say:**
> "RAG has two steps: First, retrieve relevant documents. Second, use them as context 
> when generating the answer. Watch how this works."

### 3. Run Example Question (3 minutes)
**Click:** "Event Details" button

**As it runs, narrate:**

**During Retrieval:**
> "First, the system searches the knowledge base. It found the .NET Conf document because 
> it matches the question keywords."

**Show the retrieved document:**
> "Here's what it retrieved - the actual content from our knowledge base. This becomes 
> the context for the AI."

**During Generation:**
> "Now the AI generates an answer, but it can ONLY use information from this document. 
> It can't make things up."

**Show the answer:**
> "Notice how specific this is - dates, location, schedule. All from our document. 
> And it cites the source at the bottom."

### 4. Compare With vs Without RAG (1 minute)
**Expand:** "Compare: With RAG vs Without RAG"

**Say:**
> "Without RAG, the AI would use its training data - which might be outdated or wrong. 
> With RAG, it uses YOUR data. This is critical for enterprise applications where 
> accuracy matters."

### 5. Try Another Example (Optional, 1-2 minutes)
**Click:** "Agentic Patterns" button

**Say:**
> "Let's try something more complex. Watch how it retrieves the patterns guide and 
> provides a comprehensive answer based on that specific document."

### 6. Explain the Pattern (1 minute)
**Say:**
> "This is RAG - Retrieval-Augmented Generation. It's essential for:
> - Customer support (company policies, product docs)
> - HR systems (employee handbooks, procedures)
> - Technical documentation (API docs, guides)
> - Legal/Compliance (regulations, contracts)
> 
> Anywhere you need factual, grounded answers from your own data."

## How RAG Works

### Step 1: Retrieval 🔍
```
User Question → Search Algorithm → Ranked Documents
```

**In this demo:**
- Simple keyword matching
- Scores based on word overlap
- Returns top 2 most relevant docs

**In production:**
- Vector embeddings (semantic search)
- Azure AI Search, Pinecone, Weaviate
- Much more accurate retrieval

### Step 2: Context Injection 📝
```
Retrieved Docs → Format as Context → Add to Prompt
```

**System Prompt:**
```
You are a helpful assistant that answers questions 
based on the provided context.

Rules:
1. Only use information from the provided context
2. If context doesn't contain answer, say so
3. Cite which document you're using
```

**User Prompt:**
```
Context: [Retrieved documents here]

Question: [User's question]

Answer based on context above.
```

### Step 3: Generation 💬
```
Prompt with Context → LLM → Grounded Answer
```

**Key settings:**
- Lower temperature (0.3) for factual responses
- Explicit instructions to cite sources
- Clear rules about staying grounded

## Example Questions

### Question 1: Event Details (Recommended)
```
What are the key details about .NET Conf 2025 in Cape Town?
```

**Why it's good:**
- Clear, specific answer in knowledge base
- Shows exact retrieval
- Demonstrates source citation

### Question 2: Agentic Patterns
```
What are the main agentic design patterns and when should I use each?
```

**Why it's good:**
- More complex, multi-part answer
- Shows comprehensive retrieval
- Demonstrates synthesis from document

### Question 3: Pricing
```
How much does Azure AI Foundry cost and what's included?
```

**Why it's good:**
- Specific factual information
- Shows grounding prevents hallucination
- Clear source attribution

### Question 4: Comparison
```
What's the difference between GitHub Copilot and Azure AI Foundry?
```

**Why it's good:**
- Requires multiple documents
- Shows multi-document retrieval
- Demonstrates synthesis

### Custom Question Template
```
[Specific question] about [topic in knowledge base]?
```

## Technical Implementation

### Simple Search (Demo)
```python
def simple_search(query, top_k=2):
    # Keyword matching
    query_words = set(query.lower().split())
    
    for doc in knowledge_base:
        # Count matching words
        matches = count_matches(query_words, doc)
        scores.append((doc, matches))
    
    # Return top K
    return sorted(scores)[:top_k]
```

### Production Search (Recommended)
```python
# Using Azure AI Search
from azure.search.documents import SearchClient

def vector_search(query, top_k=2):
    # Generate embedding for query
    query_embedding = get_embedding(query)
    
    # Vector similarity search
    results = search_client.search(
        search_text=query,
        vector=query_embedding,
        top=top_k
    )
    
    return results
```

### RAG Pipeline
```python
def answer_with_rag(question):
    # 1. Retrieve
    docs = retrieve_documents(question)
    
    # 2. Format context
    context = format_context(docs)
    
    # 3. Generate
    answer = llm.generate(
        system_prompt=rag_system_prompt,
        user_prompt=f"Context: {context}\n\nQuestion: {question}"
    )
    
    # 4. Return with sources
    return {
        "answer": answer,
        "sources": [doc.title for doc in docs]
    }
```

## Talking Points for Presentation

### Why RAG Matters
**Traditional AI:** Limited to training data (knowledge cutoff)  
**RAG:** Uses your current, specific data

### The Hallucination Problem
**Say:**
> "AI models are trained on internet data up to a certain date. They don't know about:
> - Your company's products or policies
> - Recent events or changes
> - Proprietary information
> - Specific details about your domain
> 
> RAG solves this by grounding responses in YOUR documents."

### Real-World Applications

**Customer Support:**
- Knowledge base: Product manuals, FAQs, troubleshooting guides
- Use case: Answer customer questions accurately
- Benefit: Consistent, factual support

**HR & Employee Services:**
- Knowledge base: Employee handbook, policies, benefits
- Use case: Answer employee questions 24/7
- Benefit: Reduce HR workload, instant answers

**Technical Documentation:**
- Knowledge base: API docs, code examples, architecture
- Use case: Help developers find information
- Benefit: Faster development, fewer errors

**Legal & Compliance:**
- Knowledge base: Regulations, contracts, procedures
- Use case: Answer compliance questions
- Benefit: Reduce risk, ensure accuracy

**Sales & Marketing:**
- Knowledge base: Product catalogs, pricing, case studies
- Use case: Help sales team find information
- Benefit: Faster quotes, better pitches

### Key Advantages

1. **Accuracy** - Grounded in your data, not hallucinated
2. **Currency** - Always up-to-date with your latest docs
3. **Transparency** - Shows sources used
4. **Control** - You control what data is used
5. **Privacy** - Your data stays in your system

### Design Considerations

**When to use RAG:**
- Need factual, grounded answers
- Have domain-specific knowledge
- Accuracy is critical
- Need source attribution

**When NOT to use:**
- Creative tasks (writing, brainstorming)
- General knowledge questions
- Real-time data needs (use tools instead)
- Very small knowledge bases

## Upgrading to Production

### 1. Use Vector Embeddings
```python
# Instead of keyword matching
from openai import OpenAI

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding
```

### 2. Use Vector Database
```python
# Azure AI Search, Pinecone, Weaviate, etc.
from azure.search.documents import SearchClient

search_client = SearchClient(
    endpoint=search_endpoint,
    index_name="my-knowledge-base",
    credential=credential
)
```

### 3. Add Chunking
```python
# Split large documents into chunks
def chunk_document(doc, chunk_size=500):
    chunks = []
    for i in range(0, len(doc), chunk_size):
        chunks.append(doc[i:i+chunk_size])
    return chunks
```

### 4. Add Reranking
```python
# Rerank retrieved docs for better relevance
def rerank(query, docs):
    scores = []
    for doc in docs:
        score = calculate_relevance(query, doc)
        scores.append((doc, score))
    return sorted(scores, reverse=True)
```

### 5. Add Hybrid Search
```python
# Combine keyword and vector search
results = search_client.search(
    search_text=query,          # Keyword search
    vector=query_embedding,      # Vector search
    top=10
)
```

## Customization Ideas

### Add Your Own Documents
```python
KNOWLEDGE_BASE["my_document"] = {
    "title": "My Company Product Guide",
    "content": """
    Your document content here...
    """
}
```

### Add File Upload
```python
uploaded_file = st.file_uploader("Upload document")
if uploaded_file:
    content = uploaded_file.read().decode()
    add_to_knowledge_base(content)
```

### Add Document Management
```python
# CRUD operations for knowledge base
def add_document(title, content):
    pass

def update_document(doc_id, content):
    pass

def delete_document(doc_id):
    pass
```

### Add Conversation Memory
```python
# Remember previous questions in session
if 'history' not in st.session_state:
    st.session_state.history = []

# Use history as additional context
context = format_context(docs, st.session_state.history)
```

## Troubleshooting

### No Documents Retrieved
- Check if question keywords match document content
- Try rephrasing question
- Lower the relevance threshold
- Add more documents to knowledge base

### Irrelevant Documents Retrieved
- Improve search algorithm (use embeddings)
- Add document metadata for filtering
- Increase chunk granularity
- Use reranking

### Answer Not Using Context
- Check system prompt instructions
- Lower temperature (more factual)
- Make context more prominent in prompt
- Verify context is being passed correctly

### Answer Too Long/Short
- Adjust max_tokens parameter
- Add length instructions to prompt
- Use different model (GPT-4 vs GPT-3.5)

## Comparison with Other Demos

| Aspect | Demo 1 (Tool) | Demo 2 (RAG) | Demo 3 (Multi-Agent) | Demo 4 (Planning) |
|--------|---------------|--------------|----------------------|-------------------|
| **Data Source** | External APIs | Your documents | Multiple agents | Task breakdown |
| **Grounding** | Real-time data | Historical docs | Agent expertise | Step structure |
| **Use Case** | Actions | Knowledge Q&A | Complex reasoning | Project execution |
| **Accuracy** | API-dependent | Document-based | Consensus-based | Process-based |

## Combining RAG with Other Patterns

### RAG + Tool Use
```
Question → Retrieve docs → Extract API params → Call API → Answer
```

**Example:** "What's the weather for the .NET Conf venue?"
- Retrieve: .NET Conf doc (get location)
- Tool: Call weather API for Cape Town
- Answer: Combine doc info + weather data

### RAG + Multi-Agent
```
Question → Each agent retrieves relevant docs → Collaborate → Answer
```

**Example:** Product launch with document-backed agents
- Research agent: Uses market research docs
- Strategy agent: Uses strategy playbooks
- Content agent: Uses brand guidelines

### RAG + Planning
```
Complex task → Retrieve relevant docs → Create plan → Execute with context
```

**Example:** Event planning with company procedures
- Retrieve: Event planning procedures
- Plan: Create steps based on procedures
- Execute: Follow documented process

## Files

- `demo2_rag.py` - Main demo application
- `DEMO2_README.md` - This file
- `.env` - Configuration (Azure credentials)

## Presentation Tips

### Do's ✅
- Use "Event Details" example first (clearest)
- Show the retrieved documents
- Emphasize "grounded in YOUR data"
- Expand the comparison section
- Mention production vector databases

### Don'ts ❌
- Don't skip showing the retrieval step
- Don't forget to show sources
- Don't get too technical on embeddings
- Don't rush through the comparison

### Time Management
- **4 min version:** One example, explain pattern
- **6 min version:** Two examples, show comparison
- **8 min version:** Three examples, discuss production

## Key Takeaway

> "RAG is how you make AI work with YOUR data. Instead of relying on what the model 
> was trained on, you ground it in your documents, policies, and knowledge. This is 
> essential for enterprise AI where accuracy and trust matter."

## Transition to Next Demo

**If doing Demo 3 next:**
> "We've seen how agents use tools and retrieve documents. Now let's see what happens 
> when multiple specialized agents work together..."

**If doing Demo 4 next:**
> "RAG gives agents access to knowledge. But what about complex, multi-step tasks? 
> That's where planning comes in..."

---

**Demo 2 Complete!** Ready to showcase knowledge-grounded AI! 🎉

# Multi-Agent System: Web Search and Financial Analysis Agents

This repository implements a **Multi-Agent System** leveraging the **Phidata framework** and **Groq model** with OpenAi in backend to provide versatile functionalities, including financial data analysis and web information retrieval. Each agent serves specific roles and can work collaboratively to enhance user experience.

---

## **Agents Overview**
### 1. **Web Search Agent**
- **Role**: Searches the web for information.  
- **Tool**: DuckDuckGo for retrieving search results.  
- **Features**: Always includes sources for the retrieved information.  

### 2. **Financial AI Agent**
- **Role**: Provides detailed financial insights.  
- **Tool**: YFinanceTools for stock prices, analyst recommendations, stock fundamentals, and company news.  
- **Features**: Data displayed in tables for readability.  

### 3. **Multi-Agent System**
- **Role**: Combines individual agents into a collaborative system to handle complex tasks.  
- **Instructions**: Includes sources and utilizes tables for structured output.

---

## **Features**
- **Web Search**: Retrieve up-to-date web information with sources.  
- **Stock Analysis**: Access stock prices, fundamentals, and analyst recommendations.  
- **Company News**: Fetch the latest news articles for specified companies.  
- **Collaborative Processing**: Multi-agent functionality allows agents to share insights and process tasks collectively.  

---

## **Tech Stack**
1. **Phidata Framework**: Simplifies agent creation and integration.  
2. **Groq Model**: Employs `llama-3.2-11b-vision-preview` for advanced AI capabilities.  
3. **YFinanceTools**: Retrieves financial data for analysis.  
4. **DuckDuckGo Tool**: Facilitates web search with source inclusion.  
5. **Environment Management**: Uses `.env` files for secure API key handling.

---

#### **Note**:
Please add your OpenAi Api Key in .env file with Groq and Phidata Api Key.
----


### Command to Run the Agent
Execute the script:
```bash
python financial_multi_agent_Phi_groq.py
```

---

## **How It Works**
1. **Environment Initialization**: Loads the API key for secure access to the Groq model.
2. **Agent Creation**:
   - `Web Search Agent`: Utilizes DuckDuckGo for web information.
   - `Financial Agent`: Leverages YFinanceTools for financial data retrieval.
   - `Multi-Agent`: Combines both agents for collaborative tasks.
3. **Task Execution**: Agents process queries and present results, ensuring clarity and source inclusion.

---

## **Example Queries**
1. **Financial Agent**:  
   Query: *"Provide details of stock AAPL"*  
   Response: Stock prices, analyst recommendations, and fundamentals displayed in a table.

2. **Multi-Agent System**:  
   Query: *"Summarize analyst recommendations and share the latest news from AAPL"*  
   Response: Collaborative output combining financial data and web news, with sources included.

---


## **Contributing**
Contributions to improve the system or extend its functionalities are welcome. Submit issues or pull requests via GitHub.

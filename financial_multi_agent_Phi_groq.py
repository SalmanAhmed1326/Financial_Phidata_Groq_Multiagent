import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Load environment variables
def initialize_environment():
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    return groq_api_key

# Create a Web Search Agent
# Create a Web Search Agent
def create_web_search_agent(api_key):
    return Agent(
        name="Web Search Agent",
        role="Search the web for information",
        model=Groq(id="llama-3.2-11b-vision-preview", api_key=api_key),  # Ensure Groq model is used
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=True,
        markdown=True,
    )

# Create a Financial Agent
def create_financial_agent(api_key):
    return Agent(
        name="Finance AI Agent",
        model=Groq(id="llama-3.2-11b-vision-preview", api_key=api_key),  # Ensure Groq model is used
        tools=[YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )],
        instructions=["Use tables to display the data"],
        show_tool_calls=True,
        markdown=True,
    )

# Create a Multi-Agent System
def create_multi_agent(agents):
    return Agent(
        team=agents,
        instructions=[
            "Always include sources",
            "Use tables to display the data",
        ],
        show_tool_calls=True,
        markdown=True,
    )

# Main function
def main():
    try:
        # Initialize environment variables and get the API key
        groq_api_key = initialize_environment()

        # Create individual agents
        web_search_agent = create_web_search_agent(groq_api_key)
        financial_agent = create_financial_agent(groq_api_key)

        # Combine into a multi-agent system
        multi_agent = create_multi_agent([web_search_agent, financial_agent])

        # Perform tasks using the multi-agent system
        print("=== Financial Agent Response ===")
        financial_agent.print_response(
            "Provide details of stock AAPL",
            stream=True,
        )

        print("\n=== Multi-Agent Response ===")
        multi_agent.print_response(
            "Summarize analyst recommendation and share the latest news from AAPL",
            stream=True,
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

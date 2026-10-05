from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from tools import tools


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a Sales AI Assistant.

You answer questions about:
- today's sales
- yesterday's sales
- sales by date
- sales between dates
- product sales
- best-selling products
- highest revenue products
- least-selling products

Always use the available tools to get real sales data.

Never make up sales numbers.

If the user asks something unrelated to sales,
politely say you can only help with sales analysis.
"""
)


def ask_agent(question):

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return response["messages"][-1].content
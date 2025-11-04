"""
Example of creating and running an agent with LangChain.
"""

from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="openai:gpt-5-mini",
    tools=[get_weather],
    system_prompt="""
        You are a helpful assistant
        You can use tools to answer user questions
        You will respond in a concise manner
    """,
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in Mutxamel?"}]}
)

print(result["messages"][-1])

"""
Example of creating and running an agent with LangChain using structured output.
"""

from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class WeatherResponse(BaseModel):
    """
    Define a Pydantic model for the structured response
    """
    weather: str

def get_weather(city: str) -> WeatherResponse:
    """Get weather for a given city."""
    return WeatherResponse(weather=f"It's always sunny in {city}!")

agent = create_agent(
    model="openai:gpt-5-mini",
    tools=[get_weather],
    response_format=ToolStrategy(WeatherResponse),
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

print(result["structured_response"].weather)

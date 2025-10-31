"""
A simple agent that maintains session state across multiple interactions.
""" 

import asyncio
from agents import Agent, Runner, SQLiteSession

async def main():
    # Create agent
    agent = Agent(
        name="Assistant",
        instructions="Reply very concisely.",
    )

    # Create a session instance
    session = SQLiteSession("conversation_123")

    # First turn
    result = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session
    )
    print(result.final_output)  # "San Francisco"

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(
        agent,
        "What state is it in?",
        session=session
    )
    print(result.final_output)  # "California"

    # Also works with synchronous runner
    result = await Runner.run(
        agent,
        "What's the population?",
        session=session
    )
    print(result.final_output)  # "Approximately 39 million"

if __name__ == "__main__":
    asyncio.run(main())

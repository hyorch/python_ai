from agents import Agent, Runner

agent = Agent(name="MyAgent", model="gpt-4",instructions="You are a helpful assistant.")

result = Runner.run_sync(agent, "Summarize the plot of 'Romeo and Juliet' in two sentences.")

print(result.final_output)

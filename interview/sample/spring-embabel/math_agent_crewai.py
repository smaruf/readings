# pip install crewai openai
# export OPENAI_API_KEY=your_key_here

from crewai import Agent, Task, Crew
from langchain.tools import tool
from langchain.chat_models import ChatOpenAI

# Step 1: Define a Tool
@tool
def add_numbers_tool(input: str) -> str:
    try:
        parts = [int(x.strip()) for x in input.split("and")]
        return f"The result is {sum(parts)}"
    except Exception as e:
        return f"Error: {e}"

# Step 2: Create an Agent with the Tool
math_agent = Agent(
    role='Math Solver',
    goal='Accurately add two numbers provided in a natural sentence',
    backstory='A highly accurate math assistant using Python tools.',
    tools=[add_numbers_tool],
    verbose=True,
    allow_delegation=False
)

# Step 3: Define the Task for the Agent
task = Task(
    description="Please add 4 and 6 and return the result.",
    expected_output="The result is 10.",
    agent=math_agent
)

# Step 4: Create the Crew and run it
crew = Crew(
    agents=[math_agent],
    tasks=[task],
    verbose=True
)

# Run the Crew
result = crew.kickoff()
print("\n✅ Final Result:", result)

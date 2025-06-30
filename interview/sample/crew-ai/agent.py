from crewai import Agent
from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Create a memory for the agent
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define a tool for addition
@tool
def add_numbers_tool(input: str) -> str:
    try:
        parts = [int(x.strip()) for x in input.split("and")]
        return f"The result is {sum(parts)}"
    except Exception as e:
        return f"Error: {e}"

# Define the CrewAI agent
math_agent = Agent(
    role="Math Solver",
    goal="Solve addition problems and remember previous interactions",
    backstory="A smart assistant who solves addition problems and recalls previous answers.",
    tools=[add_numbers_tool],
    memory=memory,
    verbose=True,
    allow_delegation=False
)

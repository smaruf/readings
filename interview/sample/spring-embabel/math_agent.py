# pip install langchain openai
# export OPENAI_API_KEY=your_key_here

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI

# Define a tool for math addition
def add_numbers(input: str) -> str:
    try:
        parts = [int(x.strip()) for x in input.split("and")]
        return str(sum(parts))
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="AddTwoNumbers",
        func=add_numbers,
        description="Adds two integers. Input format: '4 and 6'."
    )
]

# Use OpenAI GPT-3.5 agent with tools
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Try the agent
response = agent.run("Please add 4 and 6")
print("Result:", response)

from fastapi import FastAPI, Body
from agent import math_agent
from crewai import Task, Crew

app = FastAPI(title="CrewAI Math Agent")

@app.post("/add")
async def solve_math(prompt: str = Body(..., embed=True)):
    task = Task(
        description=prompt,
        expected_output="The result of the math operation.",
        agent=math_agent
    )

    crew = Crew(agents=[math_agent], tasks=[task], verbose=True)
    result = crew.kickoff()
    return {"result": result}

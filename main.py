import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM  


from tools.calculator_tools import AddTool, MultiplyTool


load_dotenv()


llm = LLM(
    model="gemini/gemini-2.5-pro", 
    api_key=os.environ.get("GEMINI_API_KEY")
)


math_specialist = Agent(
    role="Math Specialist",
    goal="Accurately solve mathematical expressions by breaking them down and using the correct tools.",
    backstory=(
        "You are an expert in mathematics. You are given a complex math problem "
        "and a set of tools. Your job is to break the problem down into simple steps "
        "and use your specialized tools to solve each step in order."
    ),
    tools=[AddTool(), MultiplyTool()],
    llm=llm,
    verbose=True 
)

task_1_add = Task(
    description="Calculate the sum of 10 and 5.",
    expected_output="A single numerical result of the addition.",
    agent=math_specialist
)

task_2_multiply = Task(
    description="Multiply the result of the first calculation by 2.",
    expected_output="The final numerical result of the multiplication.",
    agent=math_specialist,
    context=[task_1_add] 
)


crew = Crew(
    agents=[math_specialist],
    tasks=[task_1_add, task_2_multiply],
    process=Process.sequential,
    verbose=True
)

print("Starting the Math Crew...")
result = crew.kickoff()

print("\n--- Mission Complete! ---")
print("The final answer is:")
print(result)
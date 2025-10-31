import os
from crewai.tools import BaseTool  
from typing import Type, Optional
from pydantic import BaseModel, Field


class AddToolInput(BaseModel):
    a: float = Field(description="The first number to add")
    b: float = Field(description="The second number to add")

class AddTool(BaseTool):
    name: str = "add"
    description: str = "A specialized tool for adding two numbers."
    args_schema: Type[BaseModel] = AddToolInput

    def _run(self, a: float, b: float) -> str:
        """The code that executes when the agent uses this tool."""
        result = a + b
        
        return str(result)


class MultiplyToolInput(BaseModel):
    a: float = Field(description="The first number to multiply")
    b: float = Field(description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "A specialized tool for multiplying two numbers."
    args_schema: Type[BaseModel] = MultiplyToolInput

    def _run(self, a: float, b: float) -> str:
        """The code that executes when the agent uses this tool."""
        result = a * b
        
        return str(result)
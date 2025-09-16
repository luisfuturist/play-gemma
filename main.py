from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# --- 1. Define your structured Task model ---
class Task(BaseModel):
    title: str = Field(description="The title of the task")
    description: Optional[str] = Field(description="Detailed description of the task", default=None)
    priority: Optional[str] = Field(
        description="Priority level of the task", 
        default="medium",
        pattern="^(low|medium|high)$"
    )
    due_date: Optional[str] = Field(description="Due date in ISO format (YYYY-MM-DD)", default=None)

class TaskList(BaseModel):
    tasks: List[Task] = Field(description="List of extracted tasks")

# --- 2. Initialize LangChain components ---
# Initialize Ollama with JSON format for structured output
llm = ChatOllama(
    model="gemma3:1b",
    keep_alive=-1,
    format="json",
    temperature=0.5
)

# Create prompt template
prompt_template = PromptTemplate.from_template(
    """Extract tasks from the following conversation and return them as a JSON object with a "tasks" array.

Text to analyze:
{text}

For each task mentioned, extract:
- title: A clear, concise title for the task
- description: More details about what needs to be done (if available)
- priority: "low", "medium", or "high" based on context clues
- due_date: Date mentioned in YYYY-MM-DD format (if mentioned)

Return the result as a JSON object with this exact structure:
{{
  "tasks": [
    {{
      "title": "task title",
      "description": "task description",
      "priority": "medium",
      "due_date": "2024-01-15"
    }}
  ]
}}
"""
)

# --- 3. Set up structured output chain ---
structured_llm = llm.with_structured_output(TaskList)
chain = prompt_template | structured_llm

# --- 4. Task extraction function ---
def extract_tasks(text: str) -> List[Task]:
    try:
        # Use the chain to get structured output
        response = chain.invoke({"text": text})
        return response.tasks
    except Exception as e:
        print("Error extracting tasks:", e)
        return []

# --- 3. Example usage ---
def main():
    text = """
    Luis: Hey, have you had a chance to look at the report draft?

    Alex: Not yet, I’ve been swamped. Is it urgent?

    Luis: Yeah, I really need to finish writing it by Friday. It’s the top priority this week.

    Alex: Got it. Do you want me to help with anything?

    Luis: Maybe later. First, I need to call Alice about the project updates—nothing too urgent, but it should get done soon.

    Alex: Okay, I can remind you about that. Anything else on your plate?

    Luis: Hmm… probably need to buy groceries at some point, but that’s not pressing.

    Alex: Alright, so Friday for the report, call Alice soon, and groceries whenever. Makes sense.

    Luis: Exactly. Thanks for keeping me on track!
    """
    
    print("Extracting tasks from text...")
    tasks = extract_tasks(text)
    
    if tasks:
        print(f"\nFound {len(tasks)} tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"\nTask {i}:")
            print(f"  Title: {task.title}")
            print(f"  Description: {task.description}")
            print(f"  Priority: {task.priority}")
            print(f"  Due Date: {task.due_date}")
    else:
        print("No tasks could be extracted.")

if __name__ == "__main__":
    main()

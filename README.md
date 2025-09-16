# Play Gemma: Task Extraction Playground

A Python playground for experimenting with local LLMs (using Ollama) and LangChain to extract structured tasks from conversational text.

## Overview

This project demonstrates how to use LangChain with Ollama to extract structured task information from natural language conversations. It uses Pydantic models to ensure type-safe, structured output from the LLM.

## Features

- **Structured Task Extraction**: Extracts tasks with title, description, priority, and due date
- **Local LLM Integration**: Uses Ollama with Gemma3:1b model for local processing
- **Type Safety**: Pydantic models ensure structured, validated output
- **LangChain Integration**: Leverages LangChain's structured output capabilities

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Gemma3:1b model pulled in Ollama

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/luisfuturist/play-gemma.git
   cd play-gemma
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make sure Ollama is running and you have the Gemma3:1b model:
   ```bash
   ollama pull gemma3:1b
   ```

## Usage

Run the main script to see task extraction in action:

```bash
python main.py
```

The script will analyze a sample conversation and extract structured tasks with the following information:
- **Title**: Clear, concise task title
- **Description**: Detailed description of what needs to be done
- **Priority**: "low", "medium", or "high" based on context
- **Due Date**: Date in YYYY-MM-DD format (if mentioned)

## Example Output

```
Extracting tasks from text...

Found 3 tasks:

Task 1:
  Title: Finish writing report draft
  Description: Complete the report draft that needs to be finished
  Priority: high
  Due Date: 2024-01-19

Task 2:
  Title: Call Alice about project updates
  Description: Contact Alice to discuss project updates
  Priority: medium
  Due Date: None

Task 3:
  Title: Buy groceries
  Description: Purchase groceries at some point
  Priority: low
  Due Date: None
```

## Project Structure

```
play-gemma/
├── main.py              # Main application with task extraction logic
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Key Components

### Task Models
- `Task`: Individual task with title, description, priority, and due date
- `TaskList`: Container for multiple tasks

### LangChain Integration
- Uses `ChatOllama` for local LLM interaction
- Implements structured output with Pydantic models
- Prompt template for consistent task extraction

### Configuration
- Model: `gemma3:1b` (configurable in `main.py`)
- Temperature: 0.5 for balanced creativity/consistency
- JSON format enforced for structured output

## Customization

You can easily modify the project to:
- Use different Ollama models
- Adjust the prompt template for different extraction patterns
- Add new fields to the Task model
- Process different types of text input

## Dependencies

Key dependencies include:
- `langchain`: Framework for LLM applications
- `langchain-ollama`: Ollama integration for LangChain
- `pydantic`: Data validation and settings management
- `ollama`: Python client for Ollama

See `requirements.txt` for the complete list of dependencies.

## Notes

- This is a playground project for experimentation
- Requires Ollama to be running locally
- Designed for educational and experimental purposes

## License

This is a playground project for learning and experimentation.

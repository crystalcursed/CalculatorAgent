# Agentic AI Calculator

A multi-agent AI system built with Python, CrewAI, and Google's Gemini for orchestrating and executing mathematical calculations. This project demonstrates a "master-worker" (orchestrator-specialist) agentic architecture where a manager agent delegates tasks to specialized tools.

---

## Tech Stack

* **Python 3.10+**
* **CrewAI**: For creating and orchestrating the agents and tasks.
* **LangChain**: Used as the foundational library for creating the agent tools (`BaseTool`).
* **Google Gemini**: The Large Language Model (LLM) that serves as the "brain" for the agents' reasoning and planning.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Prerequisites

* Python (3.10 or higher)
* Git
* A Google Gemini API Key (available from Google AI Studio)

### 2. Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/crystalcursed/CalculatorAgent.git](https://github.com/crystalcursed/CalculatorAgent.git)
    cd CalculatorAgent
    ```

2.  **Create and activate a virtual environment:**
    *(This is crucial for isolating project dependencies)*
    ```sh
    # Create the virtual environment
    python -m venv .venv
    
    # Activate on Windows
    .\.venv\Scripts\activate
    
    # Activate on macOS/Linux
    # source .venv/bin/activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Create your environment file:**
    Create a file named `.env` in the root of the project folder. Your API key will be kept here, safe from being pushed to GitHub (as it's included in `.gitignore`).

    **`.env`**
    ```
    GEMINI_API_KEY="YOUR_GOOGLE_AI_STUDIO_API_KEY_GOES_HERE"
    ```

---

## How to Run

With your virtual environment active and your `.env` file in place, simply run the `main.py` script:

```sh
python main.py

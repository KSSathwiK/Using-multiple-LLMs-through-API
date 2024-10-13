## Streamlit Frontend with Multiple LLM Integration via Ollama, FAST API

## Project Overview

This project provides a **Streamlit-based front-end UI** integrated with two **open-source LLMs** hosted through **Ollama**. The goal is to leverage the diverse capabilities of each model by providing APIs that dynamically switch between LLMs based on user interactions. This approach allows users to access multiple models, enabling better responses and results for various tasks.

## Features

- **Streamlit UI**: A responsive front-end UI built with Streamlit for querying the LLMs.
- **FASTAPI Backend**: A robust API built with FASTAPI to handle interactions between the UI and the LLMs.
- **Ollama LLM Integration**: Two open-source LLMs from Ollama are used to process user queries and provide responses.
- **Langchain**: Used for handling chains of components and facilitating interactions with the LLMs.

## Pull models into Ollama through command prompt, After downloading
```bash
ollama run <model name>
```
## Running the App

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Activate on Windows
   venv\Scripts\activate
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run app.py 
    ```bash
   python app.py
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
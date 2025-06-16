# Impersona-Ai

Impersona AI ChatBot is a GenAI-powered chatbot that can switch between different personas and assist users with tailored, context-aware responses. It features a Streamlit frontend and a FastAPI backend, leveraging Groq LLMs via LangChain.

## Overview

The Impersona-AI Chatbot is a Python-Streamlit web-based application that leverages AI to answer user queries in natural language.

The SQL AI Agent is built using the following technologies and modules:
- **Python** - Used as the primary programming language for the application.

- **Streamlit** - Used to create the web-based user interface and handle front-end interactions.

- **LangChain** - Used for building language models and generating responses as per the user input.

- **GROQ's APIs** - Used for advanced language model capabilities and integration with various open-sourced LLMs provided by Groq Cloud.

## Features

- **Multiple Personas:** Choose from various chatbot personas (storyteller, tech-guru, health-expert, and more).
- **LLM Selection:** Select from a list of supported Groq LLMs.
- **Modern UI:** Interactive chat interface built with Streamlit.
- **Backend API:** FastAPI backend for LLM orchestration and persona management.
- **Centralized Logging:** For debugging and monitoring the application.


## Getting Started

## Installation

### Prerequisites

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/) installed
- [FastAPI](https://fastapi.tiangolo.com/) installed

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:m-asif-ansari/Impersona-Ai.git
   cd streamlit-app
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash 
    pip install -r requirements.txt
    ```

4. Start the application:
    ```bash
    python start-app.py

    # You can also start the backend and frontend manually for the application from the below commands
    1- fastapi run backend/api/main.py
    2- streamlit run streamlit_app.py

    ```

### Usage

1. Generate your GROQ API KEY:
    - Create an account on [Groq](https://groq.com).
    - Generate your free Groq API Key.
    - Create a .env file as per the sample .env.example file.
    - Paste your Groq API key in env file. 

2. Open the Application:
    - Start the ChatBot Application
    - Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

2. Select the Chatbot Persona:
    - Use the dropdown in the sidebar to select the persona for the Chatbot.

3. Select an LLM:
    - Use the dropdown in the sidebar to select a language model.

4. Start a Conversation:
    - Enter your query in the chat input box and press Enter.
    - The agent will interpret your query and provide a response.


## Directory Structure

```
ChatBot/
├── streamlit-app/                   # Main application folder (Streamlit frontend + backend logic)
│   │
│   ├── start_app.py                 # Entry point to run both backend & frontend
│   ├── streamlit_app.py             # Main UI logic for the chatbot using Streamlit
│   ├── assets/                      # assets folder for the frontend
│   │   └── static/                  # Subfolder for storing static files
│   │        └── applogo.png          # Logo for the application
│   │
│   └── backend/                     # All backend logic and services
│       ├── api/                     # API layer
│       │   └── main.py              # FastAPI app
│       ├── llm/                     # LLM (Large Language Model) related utilities
│       │   ├── get_llm_response.py  # Logic to get responses from the selected LLM
│       │   └── init_llm.py          # Initializes LLM models from using Groq API
│       ├── llm_list/                # Handles listing of multiple LLMs from GROQ
│       │   └── get_llm_list.py      # Function to return active LLMs
│       └── logger/                  # Logging setup
│           └── init_logger.py       # Initializes logging configuration
│
├── .env.example                     # Sample environment file for setting environment variables
├── .gitignore                       # Specifies files/folders to ignore in version control
├── LICENSE                          # License file for open-source usage terms
├── README.md                        # Project overview, setup instructions, and usage guide
├── mini_requirements.txt            # Lightweight version of dependencies
└── requirements.txt                 # Full list of Python dependencies
```


## Credits

### Author:
- Mohd Asif Ansari 
- Github - [m-asif-ansari](https://github.com/m-asif-ansari)
- Gmail - [asif16907@gmail.com](mailto:asif16907@gmail.com)

### License:
- This project is licensed under the MIT License. See the [LICENSE](https://github.com/m-asif-ansari/Impersona-Ai/blob/main/LICENSE) file for details.
- Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have suggestions for improvements.
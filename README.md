# Eren Chatbot

A Gradio-based chatbot that simulates Eren Yeager (Season 4/Paths) using the Groq API. This project provides an immersive conversational experience with the Attack Titan himself.

## Features

- **Immersive Persona**: Interacts as Eren Yeager, maintaining character with a focus on freedom, fighting ("Tatakae"), and a weary but resolute tone.
- **Gradio Interface**: A clean and simple web interface for chatting.
- **Groq API Powered**: Utilizes the Llama 3.3 70B model via Groq for fast and high-quality responses.
- **Contextual Awareness**: Loads a character summary from `summary.txt` to ground the persona.

## Prerequisites

- Python 3.12 or higher
- A [Groq API Key](https://console.groq.com/keys)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd eren-chatbot
    ```

2.  **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**

    This project uses `pyproject.toml`. You can install dependencies using `pip`:

    ```bash
    pip install -e .
    ```

    Or if you are using `uv`:

    ```bash
    uv sync
    ```

4.  **Configure Environment Variables:**

    Create a `.env` file in the root directory and add your Groq API key:

    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Access the chatbot:**

    Open the URL provided in the terminal (usually `http://127.0.0.1:7860`) in your web browser.

3.  **Chat:**

    Start a conversation. Try asking "Why do you fight?" or "What is freedom?".

## Project Structure

-   `main.py`: The main application script containing the `ErenChatbot` class and Gradio interface setup.
-   `summary.txt`: A text file containing the character profile and behavioral guidelines for Eren.
-   `pyproject.toml`: Project configuration and dependencies.
-   `.env`: (Not committed) Stores sensitive environment variables like the API key.

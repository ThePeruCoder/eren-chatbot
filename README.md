# ⚔️ Eren Yeager (Paths) Chatbot

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/build-passing-brightgreen)

**A high-fidelity, roleplay-focused AI interface embodying Eren Yeager from Attack on Titan (Season 4).**

## 📖 What the project does

This project provides a local, web-based chat interface that simulates a conversation with Eren Yeager in the "Paths" dimension. It utilizes **Groq's Llama 3** inference engine for ultra-fast responses and **Gradio** for a clean, distraction-free user interface.

Unlike generic chatbots, this application is strictly governed by a dynamic system prompt (`summary.txt`) to maintain deep character immersion, refusing to break the "fourth wall" or act as a helpful assistant.

## 🚀 Why the project is useful

For developers and fans alike, this project demonstrates:
* **Persona Injection:** How to enforce strict character guidelines using a decoupled text file rather than hard-coded strings.
* **Resilient Architecture:** Implements a "Safe Mode" that prevents application crashes even if API keys or configuration files are missing.
* **Concurrency Management:** Uses a queuing system to allow multiple simultaneous users on a single API key without triggering rate limits.
* **Cost-Effective AI:** Leverages the Groq API for high-performance inference with minimal latency.

## ⚡ How to get started

### Prerequisites
* Python 3.9 or higher
* A Groq API Key (available for free at [console.groq.com](https://console.groq.com))

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YourUsername/eren-chatbot.git](https://github.com/YourUsername/eren-chatbot.git)
    cd eren-chatbot
    ```

2.  **Set up the environment**
    It is recommended to use a virtual environment:
    ```bash
    # Using uv (Recommended)
    uv venv
    source .venv/bin/activate

    # OR Using standard pip
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install gradio groq python-dotenv
    ```

4.  **Configuration**
    Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```
    Open it and add your API Key:
    ```env
    GROQ_API_KEY=gsk_your_actual_api_key_here
    ```

### Usage

Run the application:
```bash
python main.py
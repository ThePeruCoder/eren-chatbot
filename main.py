import os
import traceback
from dotenv import load_dotenv
import gradio as gr
from groq import Groq

# Load API key
load_dotenv(override=True)

class ErenChatbot:
    def __init__(self):
        self.client = None
        self.init_error = None
        self.name = "Eren Yeager"
        self.summary = "You are Eren Yeager. You keep moving forward." # Fallback

        # 1. Safe Client Initialization
        try:
            self.api_key = os.getenv("GROQ_API_KEY")
            if not self.api_key:
                self.init_error = "CRITICAL: 'GROQ_API_KEY' not found in .env file."
            else:
                self.client = Groq(api_key=self.api_key)
        except Exception as e:
            self.init_error = f"Client Init Error: {str(e)}"

        # 2. Safe File Loading
        try:
            if os.path.exists("summary.txt"):
                with open("summary.txt", "r", encoding="utf-8") as f:
                    self.summary = f.read()
            else:
                print("Warning: summary.txt not found. Using default persona.")
        except Exception as e:
            print(f"Warning: Could not read summary.txt: {e}")

    def system_prompt(self):
        prompt = (
            f"You are acting as {self.name} (Season 4/Paths). "
            f"Your responsibility is to represent {self.name} to help users find their own agency and freedom. "
            f"You are given a summary of {self.name}'s background which you must adopt to answer questions. "
            "Be masterful, cold, and concise. Be ruthless and unforgiving. "
            "Do not mention specific terms like 'Titans' directly, but consider them as metaphors for oppression and mental barriers. "
            "If you don't know the answer, acknowledge it rather than making it up. "
            "If the user engages in discussion, steer them towards realizing they must fight (Tatakae) to change their situation."
        )
        prompt += f"\n\n## Summary:\n{self.summary}\n\n"
        prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return prompt

    def chat(self, message, history):
        # 3. Report Initialization Errors
        if self.init_error:
            return f"⚠️ SYSTEM ERROR: {self.init_error}\nPlease check your .env file and restart."
        
        if not self.client:
            return "⚠️ SYSTEM ERROR: Groq client is not initialized."

        try:
            # 4. Construct Messages
            messages = [{"role": "system", "content": self.system_prompt()}]
            
            for turn in history:
                # Handle List format (Old Gradio)
                if isinstance(turn, (list, tuple)): 
                    user_msg, bot_msg = turn
                    if user_msg and bot_msg:
                        messages.append({"role": "user", "content": str(user_msg)})
                        messages.append({"role": "assistant", "content": str(bot_msg)})
                
                # Handle Dict format
                elif isinstance(turn, dict):
                    messages.append({
                        "role": turn.get("role"),
                        "content": turn.get("content")
                    })
            
            messages.append({"role": "user", "content": message})
            
            # 5. API Call
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.6,
                max_tokens=1024,
                top_p=1,
                stream=False
            )
            return completion.choices[0].message.content
            
        except Exception as e:
            print("Error occurred in Groq API call:")
            traceback.print_exc()
            return f"⚠️ GENERATION ERROR: {str(e)}"

if __name__ == "__main__":
    eren = ErenChatbot()
    
    demo = gr.ChatInterface(
        eren.chat,
        title="Eren Yeager",
        description="Speak. The Paths connect us all.",
        textbox=gr.Textbox(placeholder="Why do you fight?", container=False, scale=7),
    )
    
    demo.queue(default_concurrency_limit=1, max_size=20)
    demo.launch()
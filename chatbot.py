import json
import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

# Internal Fallback Intent Database
DEFAULT_INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greetings", "ssup"],
        "response": "Hello! How can I assist you with DecodeLabs today?"
    },
    "identity": {
        "keywords": ["who are you", "your name", "what are you", "bot"],
        "response": "I am a deterministic, rule-based AI assistant built for control flow logic."
    },
    "courses": {
        "keywords": ["course", "courses", "program", "learn", "track", "offer"],
        "response": "We offer tracks in AI/ML, Web Development, Java, and Data Analytics."
    },
    "contact": {
        "keywords": ["contact", "email", "website", "reach", "phone", "location"],
        "response": "Reach out via decodelabs.tech@gmail.com, call +91 89330 06408, or visit decodelabs.tech."
    }
}

def load_intents(file_path="intents.json"):
    """Loads intent database from JSON file with fallback support."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)
    
    if os.path.exists(full_path):
        try:
            with open(full_path, "r") as file:
                data = json.load(file)
                if data:
                    return data
        except Exception:
            pass
    return DEFAULT_INTENTS

INTENTS = load_intents()

def log_conversation(user_input: str, bot_response: str, log_file="chat_log.txt"):
    """Logs conversation history with timestamps to a local text file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, log_file)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] User: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n\n")

def check_regex_patterns(clean_input: str) -> str | None:
    """Extracts entities like Order IDs, Phone Numbers, or Emails using Regex."""
    # Pattern 1: Order ID (e.g., ORD12345 or #12345)
    order_match = re.search(r'\b(ord\d{5}|#\d{5})\b', clean_input)
    if order_match:
        return f"Detected Order ID '{order_match.group(0).upper()}'. Tracking status: Processing."
    
    # Pattern 2: Phone number extraction
    phone_match = re.search(r'\+?\d{10,12}', clean_input)
    if phone_match:
        return f"Captured phone number: {phone_match.group(0)}. An agent will contact you shortly."
        
    return None

def get_bot_response(user_input: str) -> tuple[str, bool]:
    # 1. Sanitization & Normalization
    clean_input = user_input.lower().strip()
    
    # 2. Kill/Exit Commands
    if any(exit_cmd in clean_input for exit_cmd in ["exit", "quit", "bye", "stop"]):
        return "Goodbye! Keep up the great coding work.", True
    
    # 3. Regex Pattern Extraction
    regex_response = check_regex_patterns(clean_input)
    if regex_response:
        return regex_response, False

    # 4. Intent Keyword Matching Logic
    for intent, data in INTENTS.items():
        for keyword in data["keywords"]:
            if keyword in clean_input:
                return data["response"], False
                
    # 5. Default Fallback Response
    return "I do not understand that command yet. Try asking about courses, contact info, or who I am.", False

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DecodeLabs AI Assistant - Production")
        self.root.geometry("480x580")
        self.root.configure(bg="#1e1e1e")
        
        # Chat Display Window
        self.chat_history = scrolledtext.ScrolledText(
            root, state='disabled', wrap=tk.WORD, 
            bg="#252526", fg="#d4d4d4", font=("Consolas", 10),
            insertbackground="white"
        )
        self.chat_history.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)
        
        # User Input Box
        self.entry_box = tk.Entry(
            root, font=("Segoe UI", 11), bg="#3c3c3c", fg="#ffffff", insertbackground="white"
        )
        self.entry_box.pack(padx=12, pady=(0, 12), fill=tk.X)
        self.entry_box.bind("<Return>", self.send_message)
        
        self.display_message("Bot", "=== DecodeLabs AI Assistant Active ===")

    def display_message(self, sender, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)

    def send_message(self, event=None):
        user_text = self.entry_box.get().strip()
        if not user_text:
            return
            
        self.entry_box.delete(0, tk.END)
        self.display_message("You", user_text)
        
        reply, should_exit = get_bot_response(user_text)
        self.display_message("Bot", reply)
        
        # Log to file
        log_conversation(user_text, reply)
        
        if should_exit:
            self.root.after(1200, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
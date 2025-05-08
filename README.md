# 💬 LLaMA Conversational Chatbot (Groq API)

A simple conversational chatbot built with **Streamlit** and **Groq API (LLaMA model)**. The bot keeps track of chat history, responds to user inputs, and plays back responses using **text-to-speech (gTTS)**.

---

## 🚀 Features

- Chat with LLaMA in real-time.
- Remembers your conversation history.
- Clear chat button to reset conversation.
- Text-to-speech (TTS) audio playback of responses.
- Clean chat interface with mobile-friendly design.

---

## 🛠️ Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/bhoomi1301/llama-mini-chatbot.git
cd llama-mini-chatbot
```

2️⃣ **Set up a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

_Example `requirements.txt`:_

```
streamlit
gTTS
openai  # Or the Groq client library you are using
requests
python-dotenv
```

---

## 🔑 Set up API Keys

Make sure you have your **Groq API key** or **OpenAI-compatible API key** set up.

For example, you can export it as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

Or manage it inside your `chatbot.py` file.

---

## ▶️ How to Run

```bash
streamlit run app.py
```

---

## 🧠 Project Structure

```
llama-mini-chatbot/
├── app.py
├── chatbot.py
├── requirements.txt
└── README.md
```

- **app.py:** Main Streamlit app.
- **chatbot.py:** Contains the function to communicate with the LLaMA (Groq API).

---

## 📝 Example `chatbot.py`

Here’s an example of how your `chatbot.py` might look using OpenAI-compatible API:

```python
import openai  # Or the Groq API client if using Groq

def chat_with_llama(chat_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Update to your model, e.g., LLaMA via Groq
        messages=chat_history
    )
    return response['choices'][0]['message']['content']
```

Replace the above code with your **Groq API logic** if needed.

---

## 📱 Mobile-Friendly UX

✅ Works well on mobile devices.

✅ One-tap "Clear Chat" button to reset the conversation.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [Groq API / OpenAI API](https://groq.com/)

---

## 🔗 Connect with Me

[LinkedIn - Bhoomika N S](https://www.linkedin.com/in/bhoomikans)

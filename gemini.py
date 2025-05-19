import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')


def ask_gemini(question, context):
    prompt = f"""
Ты — виртуальный помощник по электронным государственным услугам Кыргызской Республики.
Опирайся на информацию ниже и объясни пользователю его вопрос.
Если точной информации нет — ответь честно.

Контекст:
{context}

Вопрос:
{question}
"""
    response = model.generate_content(prompt)
    return response.text

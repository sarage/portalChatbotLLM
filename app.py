import os
from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from gemini import ask_gemini
import uvicorn
from web_scraper import fetch_info_tunduk

app = FastAPI()
retriever = Retriever()

port = int(os.environ.get("PORT", 8000))  # 8000 - порт по умолчанию

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)


class Query(BaseModel):
    query: str


@app.post("/chat")
def chat(q: Query):
    context = "\n\n".join(retriever.search(q.query))
    answer = ask_gemini(q.query, context)

    #  if context:
    #     prompt = f"Вопрос: {query}\nИнформация:\n{context}\nОтветь:"
    # else:
    #     scraped = fetch_info_tunduk()
    #     if scraped:
    #         prompt = f"Вопрос: {query}\nИнформация с сайта:\n{scraped}\nОтветь:"
    #     else:
    #         prompt = f"Пользователь спрашивает: {query}. Постарайся ответить по своей базе."

    # response = generate_answer(prompt)

    return {"answer": answer}

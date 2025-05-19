from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from gemini import ask_gemini
from web_scraper import fetch_info_tunduk

app = FastAPI()
retriever = Retriever()


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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.data_loader import load_employees
from app.simple_chatbot import simple_match, format_response, filter_employees

app = FastAPI()

employees = load_employees()

class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    try:
        response = filter_employees(request.query, employees)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

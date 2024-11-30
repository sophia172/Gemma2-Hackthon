import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from news_summary_extractor import ArticleExtractor

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class URLData(BaseModel):
    url: str

@app.post("/api/data")
async def process_everything(request_data: URLData):
    print("8.d")
    news_url = request_data.url
    article_extractor = ArticleExtractor()
    article_summary =await article_extractor(news_url)
    return JSONResponse(content={"message": "Data received successfully",  "summary": article_summary}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

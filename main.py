import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from news_summary_extractor import ArticleExtractor
from speak import speak
from fastapi.responses import StreamingResponse
from logger import logging
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
    try:
        news_url = request_data.url
        article_extractor = ArticleExtractor()
        article_summary =await article_extractor(news_url)
        audio_bytes= await speak(article_summary)
        logging.info(f"audio byte created with {audio_bytes}")
        return StreamingResponse(audio_bytes, media_type="audio/wav")
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from news_summary_extractor import ArticleExtractor
from speak import speak
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
    print("this endpoint hit, data: ", request_data.model_dump_json())
    news_url = request_data.url
    article_extractor = ArticleExtractor(news_url)
    article_summary = article_extractor.summarize_with_gemma()
    await speak(article_summary)
    return JSONResponse(content={"message": "Data received successfully"}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

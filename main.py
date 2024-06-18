from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from web_scraper import scrape_website, scrape_youtube

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/scrape_website")
async def scrape_website_endpoint(request: URLRequest):
    try:
        data = scrape_website(request.url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/scrape_youtube")
async def scrape_youtube_endpoint(request: URLRequest):
    try:
        data = scrape_youtube(request.url)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

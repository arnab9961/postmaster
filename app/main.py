from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from app.config import APP_NAME, APP_DESCRIPTION, APP_VERSION
from app.api import router as api_router
import os

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Include API routes
app.include_router(api_router)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    """
    Serve the chat interface
    """
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
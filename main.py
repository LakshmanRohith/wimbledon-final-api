from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware  # ✅ Add this
from data import wimbledon_finals

app = FastAPI()

# ✅ Add this block for CORS (allows frontend to access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/wimbledon")
def get_wimbledon_final(year: int):
    if year not in wimbledon_finals:
        return {"error": "Data not available for this year"}
    return {"year": year, **wimbledon_finals[year]}

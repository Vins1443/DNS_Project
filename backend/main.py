import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Allow CORS from any origin (you can restrict to http://localhost:3000 if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:3000"] for security
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/file", response_class=PlainTextResponse)
def read_txt():
    # Get the parent directory of the backend folder
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(parent_dir, "output.txt")

    # Ensure file exists before opening
    if not os.path.exists(file_path):
        return "Error: output.txt not found."

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

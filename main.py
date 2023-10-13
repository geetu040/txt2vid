from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from generator import generate_video

app = FastAPI()

@app.get("/")
async def index():
    return "Hi"

@app.get("/get_video")
async def get_video(prompt):
	video_path = generate_video(prompt)
	return FileResponse(video_path, media_type="video/mp4")
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from generator import generate_video
from video_convertor import convert_video_format

app = FastAPI()

@app.get("/")
async def index():
	print("someone just went to the home page")
	return "Hi"

@app.get("/get_video")
async def get_video(prompt, video_format="mp3"):
	video_path = generate_video(prompt)
	if video_format in ["webm", "mov"]:
		video_path = convert_video_format(video_path, video_format)
	else:
		video_format = "mp3"
	return FileResponse(video_path, media_type=f"video/{video_format}")
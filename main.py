from fastapi import FastAPI
from fastapi.responses import FileResponse
import mimetypes
from pathlib import Path
# from generator import generate_video
from video_convertor import convert_video_format
import logging

logging.basicConfig(filename='app_logs.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = FastAPI()

@app.get("/")
async def index():
	print("someone just went to the home page")
	logging.info('Hit at Index')
	return "The App is running"

@app.get("/get_video")
async def get_video(prompt, video_format="mp3", video_length=1):
	logging.info(f'prompt: {prompt}\tvideo_format: {video_format}\tvideo_length:{video_length}')

	# making sure video_length is between 1 and 10 seconds
	video_length = int(video_length)
	video_length = min(video_length, 15)
	video_length = max(video_length, 1)

	video_path = "test\\thunder-file_e46c3db6.mp4"
	# video_path = generate_video(prompt, video_length)
	if video_format in ["webm", "mov"]:
		video_path = convert_video_format(video_path, video_format)

	media_type, _ = mimetypes.guess_type(video_path)

	print("Media Type:", media_type)
	logging.info(f'video_path: {video_path}\tmedia_type: {media_type}')

	return FileResponse(video_path, media_type=media_type)
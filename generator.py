from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
import torch

pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", variant="fp16")

# GPU EFFICIENT
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

# MAIN
def generate_video(prompt):
	# prompt = "Spiderman is surfing"

	print("Generating the video .....")
	video_frames = pipe(prompt, num_inference_steps=25).frames
	
	print("Saving the video ..... ", end="")
	video_path = export_to_video(video_frames)
	print(f"saved: {video_path}")

	return video_path
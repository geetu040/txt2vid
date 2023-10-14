import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

# LOAD PIPE
pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")

# GPU EFFICIENT
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
# pipe.enable_vae_slicing()

# MAIN
def generate_video(prompt, video_length):

	# calculating frames: 1 second = 8 frames
	num_frames = video_length * 8

	# generating frames
	video_frames = pipe(prompt, num_inference_steps=25, num_frames=num_frames).frames

	# coverting to video
	video_path = export_to_video(video_frames)
	print(f"saved: {video_path}")

	return video_path
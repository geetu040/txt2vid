import os
from moviepy.editor import VideoFileClip

def convert_video_format(input_video_path, output_format):
	output_format = "." + output_format

	# Load the video
	video_clip = VideoFileClip(input_video_path)

	# Extract the original file path and name without extension
	video_path, video_name = os.path.split(input_video_path)
	video_name_without_ext, _ = os.path.splitext(video_name)

	# Define the output video file path with the new extension
	output_video_path = os.path.join(video_path, video_name_without_ext + output_format)

	video_codec = 'libvpx' if output_format == '.webm' else 'libx264'

	# Convert the video to the specified format
	video_clip.write_videofile(output_video_path, codec=video_codec)

	print(f"Video converted and saved as {output_video_path}")

	return output_video_path

if __name__ == "__main__":
	convert_video_format("test\\thunder-file_e46c3db6.mp4", "webm")
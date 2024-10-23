import os
from moviepy.editor import ImageSequenceClip, ImageClip

# Define the path to the folder containing the images
image_folder = os.sys.argv [1]

# List all image files in the folder
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]

# Define a common size (width, height) to resize all images
target_size = (1280, 720)  # Replace with your desired size

# Resize images and create ImageClip objects
image_clips = [ImageClip(img).resize(target_size) for img in image_files]

# Create a video clip from the resized images
clip = ImageSequenceClip([img.get_frame(0) for img in image_clips], fps=.5)

# Define the output video file path
output_video = f'{image_folder}.mp4'

# Write the video file
clip.write_videofile(output_video, codec='libx264')

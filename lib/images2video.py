import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip

# Specify the path to the folder containing the images
image_folder = os.sys.argv[1]

# Specify the output video file name
output_video = f'{image_folder}.mp4'

# Specify the path to the audio file
audio_file = os.sys.argv[2]

# Get the list of images
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
images.sort()  # Sort the images by name

# Read the first image to get the dimensions
frame = cv2.imread(os.path.join(image_folder, images[0]))

# Get the height and width of the images
height, width, layers = frame.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For .mp4 output
video = cv2.VideoWriter(output_video, fourcc, 1, (width, height))

# Number of seconds each image will appear on screen
seconds_per_image = 5

# Convert seconds_per_image to frame count (assuming 1 fps)
frames_per_image = seconds_per_image * 1

# Iterate over the images and write them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    for _ in range(frames_per_image):
        video.write(frame)

# Release the video writer object
video.release()

# Add audio to the video using MoviePy
video_clip = VideoFileClip(output_video)
audio_clip = AudioFileClip(audio_file)
final_clip = video_clip.set_audio(audio_clip)

# Save the final video
final_clip.write_videofile('final_slideshow_with_audio.mp4', codec='libx264')

print('Slideshow video with audio saved as final_slideshow_with_audio.mp4')

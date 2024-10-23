from moviepy.editor import VideoFileClip, AudioFileClip
import sys 

# Define the paths to the video and audio files
video_path = sys.argv [1]
audio_path = sys.argv [2]

# Load the video clip
video_clip = VideoFileClip(video_path)

# Load the audio clip
audio_clip = AudioFileClip(audio_path)
audio_clip = audio_clip.subclip(0,video_clip.duration)

# Set the audio of the video clip to the loaded audio
video_with_audio = video_clip.set_audio(audio_clip)

# Define the output video file path with audio
output_video_with_audio = f'{video_path}.with_audio.mp4'

# Write the final video file
video_with_audio.write_videofile(output_video_with_audio, codec='libx264')

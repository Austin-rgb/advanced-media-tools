from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

clips = sys.argv[0:]

# Load your video files
videos = [VideoFileClip(clip) for clip in clips]

# Append videos
final_video = concatenate_videoclips(videos)

# Save the final video
final_video.write_videofile("final_video.mp4", codec="libx264")

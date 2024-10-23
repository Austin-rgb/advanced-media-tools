import ffmpeg

def mp42mp3(file,output):
    # Extract the audio from the video
    #ffmpeg.input(file).output(f'{file}.mp3').run()
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(file)
    video.audio.write_audiofile(output)
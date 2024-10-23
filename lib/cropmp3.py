from pydub import AudioSegment

def crop_mp3(input_file, start_time, end_time, output_file=None):
    if not output_file:
        output_file = f"{input_file}-crop-{start_time}-{end_time}.mp3"
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)
    
    # Convert start and end times from seconds to milliseconds
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    
    # Crop the audio segment
    cropped_audio = audio[start_ms:end_ms]
    
    # Export the cropped audio
    cropped_audio.export(output_file, format="mp3")


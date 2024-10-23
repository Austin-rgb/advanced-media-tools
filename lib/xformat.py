from pydub import AudioSegment
def change_format(file, output,target_format):
    audio = AudioSegment.from_file(file)
    audio.export(f'{output}',target_format)
from pydub import AudioSegment
import os

def convert_m4a_to_wav(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.m4a'):
            m4a_path = os.path.join(folder_path, file_name)
            wav_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + '.wav')
            
            # Convert m4a to wav
            audio = AudioSegment.from_file(m4a_path, format='m4a')
            audio.export(wav_path, format='wav')
            print(f"Converted {file_name} to WAV.")

convert_m4a_to_wav('recordings')

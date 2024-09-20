from pydub import AudioSegment
from pydub.playback import play

# Reading and playing an audio file
def read_audio(audio_path):
    try:
        audio = AudioSegment.from_file(audio_path)
        play(audio)  # Plays the audio
        print(f"Audio loaded successfully from {audio_path}")
    except FileNotFoundError:
        print(f"Audio file {audio_path} not found.")
    except Exception as e:
        print(f"Error loading audio: {e}")

# Example usage
audio_path = "guitar_test.mp3"  # Provide the path to the audio file
read_audio(audio_path)

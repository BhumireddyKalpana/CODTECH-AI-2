import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        print("Processing audio...")
        audio_data = recognizer.record(source)
        try:
            # Using Google's free web API
            text = recognizer.recognize_google(audio_data)
            return f"Transcription: {text}"
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "API unavailable."

# Note: Replace 'sample.wav' with your audio file path
# print(transcribe_audio("sample.wav"))
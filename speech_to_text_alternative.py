<<<<<<< HEAD
import sounddevice as sd
import wavio
import speech_recognition as sr

# Record audio with sounddevice
def record_audio(filename, duration=5, fs=44100):
    print("Recording... Speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Recording complete.")

# Convert speech to text
def speech_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

# Main function
if __name__ == "__main__":
    filename = "output.wav"
    record_audio(filename)
=======
import sounddevice as sd
import wavio
import speech_recognition as sr

# Record audio with sounddevice
def record_audio(filename, duration=5, fs=44100):
    print("Recording... Speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Recording complete.")

# Convert speech to text
def speech_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

# Main function
if __name__ == "__main__":
    filename = "output.wav"
    record_audio(filename)
>>>>>>> df62b7ee844413c23b7f2c9f7c7ace6d31c53773
    speech_to_text(filename)
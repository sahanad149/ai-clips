import moviepy.editor as mp
import speech_recognition as sr
import tensorflow as tf
from transformers import pipeline

# Function to extract audio from video
def extract_audio(video_file, audio_file):
    clip = mp.VideoFileClip(video_file)
    clip.audio.write_audiofile(audio_file)

# Function to convert audio to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text

# Function to summarize the transcript
def summarize_text(text):
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    video_file = "sample_video.mp4"
    audio_file = "sample_audio.wav"
    
    # Extract audio from video
    extract_audio(video_file, audio_file)
    
    # Convert audio to text
    transcript = audio_to_text(audio_file)
    print("Transcript:", transcript)
    
    # Summarize the transcript
    summary = summarize_text(transcript)
    print("Summary:", summary)
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from transcript_processing import extract_audio, audio_to_text, summarize_text
from video_processing import add_text_to_video

app = FastAPI()

@app.post("/process-video/")
async def process_video(file: UploadFile = File(...)):
    # Save the uploaded video file
    video_path = f"temp_{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())
    
    # Extract audio and generate summary
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)
    transcript = audio_to_text(audio_path)
    summary = summarize_text(transcript)
    
    # Process video with text overlay
    output_video = f"output_{file.filename}"
    add_text_to_video(video_path, output_video, summary, start_time=5, duration=10)
    
    # Cleanup temporary files
    os.remove(video_path)
    os.remove(audio_path)
    
    return FileResponse(output_video, media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
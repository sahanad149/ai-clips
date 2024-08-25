import cv2
import numpy as np

# Function to add text overlay to video
def add_text_to_video(video_file, output_file, text, start_time, duration, position=(50, 50)):
    cap = cv2.VideoCapture(video_file)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        current_time = frame_count / fps
        if start_time <= current_time <= start_time + duration:
            cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        out.write(frame)
        frame_count += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = "sample_video.mp4"
    output_file = "output_video.mp4"
    text = "Sample Summary"
    start_time = 5  # start time in seconds
    duration = 10  # duration in seconds

    add_text_to_video(video_file, output_file, text, start_time, duration)
    print("Video processing complete.")
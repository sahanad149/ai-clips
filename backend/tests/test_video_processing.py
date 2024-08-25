import unittest
import cv2
from video_processing import add_text_to_video

class TestVideoProcessing(unittest.TestCase):

    def test_add_text_to_video(self):
        video_file = "sample_video.mp4"
        output_file = "test_output_video.mp4"
        text = "Test Summary"
        start_time = 1
        duration = 2

        add_text_to_video(video_file, output_file, text, start_time, duration)
        
        cap = cv2.VideoCapture(output_file)
        self.assertTrue(cap.isOpened())
        cap.release()

if __name__ == "__main__":
    unittest.main()
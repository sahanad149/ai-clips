import unittest
from transcript_processing import summarize_text

class TestTranscriptProcessing(unittest.TestCase):

    def test_summarize_text(self):
        text = "This is a long text that needs to be summarized. The summary should be concise and to the point."
        summary = summarize_text(text)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

if __name__ == "__main__":
    unittest.main()
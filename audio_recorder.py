"""
Audio recording module using sounddevice library.
Records audio from the default microphone for a specified duration.
"""

import sounddevice as sd
import soundfile as sf
import numpy as np
from datetime import datetime
import os


class AudioRecorder:
    """Handles audio recording from the microphone."""
    
    def __init__(self, sample_rate=16000):
        """
        Initialize the audio recorder.
        
        Args:
            sample_rate (int): Sample rate for audio recording (default: 16000 Hz for YAMNet)
        """
        self.sample_rate = sample_rate
        
    def record(self, duration=10, output_dir="output"):
        """
        Record audio from the microphone.
        
        Args:
            duration (int): Duration of recording in seconds
            output_dir (str): Directory to save the recorded audio
            
        Returns:
            tuple: (audio_data, sample_rate, file_path)
        """
        print(f"[MIC] Recording audio for {duration} seconds...")
        print("Speak now or make sounds near the microphone!")
        
        # Record audio
        audio_data = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()  # Wait until recording is finished
        
        print("[OK] Recording complete!")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(output_dir, f"recording_{timestamp}.wav")
        
        # Save to file
        sf.write(file_path, audio_data, self.sample_rate)
        print(f"[SAVE] Audio saved to: {file_path}")
        
        return audio_data, self.sample_rate, file_path


def main():
    """Test the audio recorder."""
    recorder = AudioRecorder()
    audio_data, sample_rate, file_path = recorder.record(duration=5)
    print(f"Audio shape: {audio_data.shape}")
    print(f"Sample rate: {sample_rate} Hz")


if __name__ == "__main__":
    main()

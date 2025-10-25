"""
Audio classification module using YAMNet model from TensorFlow Hub.
Classifies audio and converts the results into text descriptions.
"""

import warnings
import os

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF info/warning messages
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
from pathlib import Path

# Suppress TensorFlow deprecation warnings
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class AudioClassifier:
    """Handles audio classification using YAMNet."""
    
    def __init__(self):
        """Initialize the YAMNet model and load class names."""
        print("[LOAD] Loading YAMNet model from TensorFlow Hub...")
        self.model = hub.load('https://tfhub.dev/google/yamnet/1')
        
        # Load class names
        self.class_names = self._load_class_names()
        print("[OK] YAMNet model loaded successfully!")
        
    def _load_class_names(self):
        """
        Load YAMNet class names from the model.
        
        Returns:
            list: List of class names
        """
        class_map_path = self.model.class_map_path().numpy()
        class_names = []
        
        with tf.io.gfile.GFile(class_map_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                class_names.append(row['display_name'])
                
        return class_names
    
    def classify(self, audio_data, sample_rate=16000, top_k=5, threshold=0.1):
        """
        Classify audio and return top predictions for all detected sounds.
        
        Args:
            audio_data (np.ndarray): Audio waveform data
            sample_rate (int): Sample rate of the audio
            top_k (int): Number of top predictions to return
            threshold (float): Minimum confidence threshold for detection (0.0-1.0)
            
        Returns:
            dict: Classification results with all detected sounds
        """
        print("[CLASSIFY] Analyzing audio...")
        
        # Ensure audio is 1D
        if len(audio_data.shape) > 1:
            audio_data = np.squeeze(audio_data)
        
        # YAMNet expects float32 audio in [-1.0, 1.0]
        audio_data = audio_data.astype(np.float32)
        
        # Run inference - YAMNet returns predictions for each 0.96s frame
        scores, embeddings, spectrogram = self.model(audio_data)
        
        # Get the mean prediction across all frames
        mean_scores = np.mean(scores.numpy(), axis=0)
        
        # Get top K predictions
        top_indices = np.argsort(mean_scores)[-top_k:][::-1]
        top_classes = [self.class_names[i] for i in top_indices]
        top_scores = [mean_scores[i] for i in top_indices]
        
        # Find ALL sounds above threshold across the entire recording
        all_detected_sounds = []
        for i, score in enumerate(mean_scores):
            if score >= threshold:
                all_detected_sounds.append({
                    'class': self.class_names[i],
                    'score': float(score)
                })
        
        # Sort by score descending
        all_detected_sounds.sort(key=lambda x: x['score'], reverse=True)
        
        # Analyze per-frame detections to find sounds throughout the recording
        frame_detections = []
        num_frames = scores.shape[0]
        for frame_idx in range(num_frames):
            frame_scores = scores[frame_idx].numpy()
            max_idx = np.argmax(frame_scores)
            max_score = frame_scores[max_idx]
            
            if max_score >= threshold:
                timestamp = frame_idx * 0.96  # YAMNet frame is ~0.96 seconds
                frame_detections.append({
                    'timestamp': round(timestamp, 2),
                    'class': self.class_names[max_idx],
                    'score': float(max_score)
                })
        
        # Create results dictionary
        results = {
            'top_predictions': [
                {'class': cls, 'score': float(score)}
                for cls, score in zip(top_classes, top_scores)
            ],
            'primary_class': top_classes[0],  # Add primary class
            'confidence': float(top_scores[0]),
            'all_detected_sounds': all_detected_sounds[:15],  # Top 15 detected sounds
            'timeline': frame_detections,  # Timeline of sounds throughout recording
            'num_frames_analyzed': num_frames,
            'total_sounds_detected': len(all_detected_sounds)
        }
        
        print(f"[OK] Primary sound: {results['primary_class']} (confidence: {results['confidence']:.2%})")
        print(f"[OK] Total sounds detected: {results['total_sounds_detected']}")
        
        return results
    
    def generate_timeline_text(self, classification_results):
        """
        Generate raw timeline text of all detected sounds with timestamps.
        This will be sent directly to LM Studio without narrative description.
        
        Args:
            classification_results (dict): Results from classify()
            
        Returns:
            str: Raw timeline of sounds with timestamps and confidence scores
        """
        timeline = classification_results.get('timeline', [])
        total_sounds = classification_results.get('total_sounds_detected', 0)
        
        if not timeline:
            return "No sounds detected in the audio timeline."
        
        # Create raw timeline format
        timeline_text = f"Sound Timeline - {len(timeline)} detections across {classification_results.get('num_frames_analyzed', 0)} frames:\n\n"
        
        # List each detection with timestamp
        for detection in timeline:
            confidence_pct = detection['score'] * 100
            timeline_text += f"{detection['timestamp']}s - {detection['class']} ({confidence_pct:.1f}%)\n"
        
        # Add summary statistics
        unique_sounds = list(set([t['class'] for t in timeline]))
        timeline_text += f"\nTotal unique sounds: {len(unique_sounds)}"
        timeline_text += f"\nAll detected sound types: {total_sounds}"
        
        print(f"[TIMELINE] Generated timeline with {len(timeline)} detections")
        print(f"[INFO] Unique sounds in timeline: {len(unique_sounds)}")
        print("[INFO] First 10 detections:")
        for detection in timeline[:10]:
            print(f"  {detection['timestamp']}s: {detection['class']} ({detection['score']:.2%})")
        if len(timeline) > 10:
            print(f"  ... and {len(timeline) - 10} more detections")
        
        return timeline_text


def main():
    """Test the audio classifier."""
    import soundfile as sf
    
    # Load a sample audio file (you can replace this with your recorded audio)
    print("Testing AudioClassifier...")
    print("Please provide a path to a .wav file or record audio first.")
    
    classifier = AudioClassifier()
    
    # Example with dummy audio (replace with actual file)
    # audio_data, sample_rate = sf.read('path/to/audio.wav')
    # results = classifier.classify(audio_data, sample_rate)
    # description = classifier.generate_description(results)
    # print(f"\nFinal description: {description}")


if __name__ == "__main__":
    main()

"""
Main AI Pipeline - Audio to Image Generation
Records audio, classifies it, enhances the description, and generates an image.
"""

import os
import sys
from datetime import datetime
import json

from audio_recorder import AudioRecorder
from audio_classifier import AudioClassifier
from prompt_enhancer import PromptEnhancer
from image_generator import ImageGenerator


class AudioToImagePipeline:
    """Orchestrates the complete AI pipeline from audio to image."""
    
    def __init__(self, config=None):
        """
        Initialize the pipeline with all components.
        
        Args:
            config (dict): Configuration dictionary
        """
        # Default configuration
        self.config = {
            'audio_duration': 10,
            'sample_rate': 16000,
            'audio_output_dir': 'Sound file',
            'image_output_dir': 'GeneratedImage',
            'lm_studio_url': 'http://localhost:1234/v1/chat/completions',
            'image_style': 'photorealistic',
            'image_width': 512,
            'image_height': 512,
            'num_inference_steps': 30,
        }
        
        # Update with user config
        if config:
            self.config.update(config)
        
        # Initialize components
        print("=" * 60)
        print("INITIALIZING AI PIPELINE")
        print("=" * 60)
        
        self.recorder = AudioRecorder(sample_rate=self.config['sample_rate'])
        self.classifier = AudioClassifier()
        self.enhancer = PromptEnhancer(api_url=self.config['lm_studio_url'])
        self.image_gen = ImageGenerator()
        
        print("\n[OK] All components initialized successfully!\n")
        
    def run(self):
        """
        Execute the complete pipeline.
        
        Returns:
            dict: Results including paths to audio and image files
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'config': self.config
        }
        
        try:
            # Step 1: Record Audio
            print("=" * 60)
            print("STEP 1: RECORDING AUDIO")
            print("=" * 60)
            audio_data, sample_rate, audio_path = self.recorder.record(
                duration=self.config['audio_duration'],
                output_dir=self.config['audio_output_dir']
            )
            results['audio_path'] = audio_path
            print()
            
            # Step 2: Classify Audio
            print("=" * 60)
            print("STEP 2: CLASSIFYING AUDIO")
            print("=" * 60)
            classification = self.classifier.classify(audio_data, sample_rate, threshold=0.2)  # Lower = more sounds detected
            sound_timeline = self.classifier.generate_timeline_text(classification)
            results['classification'] = classification
            results['sound_timeline'] = sound_timeline
            print()
            
            # Step 3: Enhance Prompt with LM Studio
            print("=" * 60)
            print("STEP 3: ENHANCING PROMPT WITH LM STUDIO")
            print("=" * 60)
            # Send sound timeline directly to LM Studio
            enhanced_prompt = self.enhancer.enhance(
                sound_timeline,
                style=self.config['image_style']
            )
            results['enhanced_prompt'] = enhanced_prompt
            print()
            
            # Step 4: Generate Image with Stable Diffusion
            print("=" * 60)
            print("STEP 4: GENERATING IMAGE")
            print("=" * 60)
            image_path = self.image_gen.generate(
                prompt=enhanced_prompt,
                output_dir=self.config['image_output_dir'],
                width=self.config['image_width'],
                height=self.config['image_height'],
                num_inference_steps=self.config['num_inference_steps']
            )
            results['image_path'] = image_path
            print()
            
            # Save pipeline results
            self._save_results(results)
            
            # Display summary
            print("=" * 60)
            print("PIPELINE COMPLETE!")
            print("=" * 60)
            print(f"[OK] Audio recorded: {audio_path}")
            print(f"[OK] Classification: {classification['primary_class']} ({classification['confidence']:.2%})")
            print(f"[OK] Sound timeline: {len(classification.get('timeline', []))} detections")
            print(f"[OK] Enhanced prompt: {enhanced_prompt}")
            print(f"[OK] Image generated: {image_path}")
            print("=" * 60)
            
            return results
            
        except KeyboardInterrupt:
            print("\n\n[WARN] Pipeline interrupted by user.")
            sys.exit(0)
            
        except Exception as e:
            print(f"\n[ERROR] Error in pipeline: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    
    def _save_results(self, results):
        """Save pipeline results to a JSON file."""
        results_dir = self.config['image_output_dir']
        os.makedirs(results_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_path = os.path.join(results_dir, f"results_{timestamp}.json")
        
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"[SAVE] Results saved to: {results_path}")


def main():
    """Main entry point for the pipeline."""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║       AI AUDIO-TO-IMAGE GENERATION PIPELINE               ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    # Optional: Custom configuration
    config = {
        'audio_duration': 10,  # seconds
        'image_style': 'photorealistic',  # or 'artistic', 'abstract', etc.
        'image_width': 512,
        'image_height': 512,
        'num_inference_steps': 30,  # Higher = better quality but slower
    }
    
    # Create and run pipeline
    pipeline = AudioToImagePipeline(config=config)
    results = pipeline.run()
    
    print("\n[DONE] All done!")
    print(f"Audio files saved in: Sound file\\")
    print(f"Images saved in: GeneratedImage\\")
    print()


if __name__ == "__main__":
    main()

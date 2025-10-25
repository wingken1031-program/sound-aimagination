"""
Image generation module using Stable Diffusion.
Generates images based on text prompts.
"""

import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image
import os
from datetime import datetime


class ImageGenerator:
    """Handles image generation using Stable Diffusion."""
    
    def __init__(self, model_id="Lykon/dreamshaper-8-lcm", device=None):
        """
        Initialize the Stable Diffusion pipeline.
        
        Args:
            model_id (str): HuggingFace model ID for Stable Diffusion
            device (str): Device to run on ('cuda', 'cpu', or None for auto-detect)
        """
        print("[LOAD] Loading Stable Diffusion model...")
        print("(This may take a few minutes on first run)")
        
        # Auto-detect device if not specified
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"Using device: {self.device}")
        
        # Load the pipeline
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            safety_checker=None,  # Disable safety checker for faster generation
            requires_safety_checker=False
        )
        
        # Use a faster scheduler
        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
            self.pipe.scheduler.config
        )
        
        # Move to device
        self.pipe = self.pipe.to(self.device)
        
        # Enable memory optimizations if using CUDA
        if self.device == "cuda":
            try:
                self.pipe.enable_attention_slicing()
                print("[OK] Memory optimization enabled")
            except:
                pass
        
        print("[OK] Stable Diffusion model loaded successfully!")
        
    def generate(self, prompt, output_dir="output", num_inference_steps=100, 
                 guidance_scale=9, width=512, height=512, seed=None):
        """
        Generate an image from a text prompt.
        
        Args:
            prompt (str): Text prompt for image generation
            output_dir (str): Directory to save the generated image
            num_inference_steps (int): Number of denoising steps (more = better quality but slower)
            guidance_scale (float): How closely to follow the prompt (7-9 is typical)
            width (int): Image width in pixels
            height (int): Image height in pixels
            seed (int): Random seed for reproducibility (None for random)
            
        Returns:
            str: Path to the generated image
        """
        print(f"[GEN] Generating image from prompt...")
        print(f"Prompt: {prompt}")
        
        # Set random seed if provided
        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)
        
        # Generate the image
        with torch.no_grad():
            result = self.pipe(
                prompt=prompt,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                width=width,
                height=height,
                generator=generator
            )
        
        image = result.images[0]
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(output_dir, f"generated_{timestamp}.png")
        
        # Save the image
        image.save(file_path)
        
        print(f"[OK] Image generated and saved to: {file_path}")
        
        return file_path
    
    def generate_batch(self, prompts, **kwargs):
        """
        Generate multiple images from a list of prompts.
        
        Args:
            prompts (list): List of text prompts
            **kwargs: Additional arguments to pass to generate()
            
        Returns:
            list: Paths to generated images
        """
        image_paths = []
        for i, prompt in enumerate(prompts, 1):
            print(f"\n[{i}/{len(prompts)}]")
            path = self.generate(prompt, **kwargs)
            image_paths.append(path)
        
        return image_paths

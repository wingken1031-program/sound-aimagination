"""
LM Studio integration module.
Sends text descriptions to LM Studio for prompt enhancement.
"""

import requests
import json


class PromptEnhancer:
    """Handles communication with LM Studio to enhance prompts."""
    
    def __init__(self, api_url="http://localhost:1234/v1/chat/completions"):
        """
        Initialize the prompt enhancer.
        
        Args:
            api_url (str): LM Studio API endpoint URL
        """
        self.api_url = api_url
        
    def enhance(self, sound_timeline, style="photorealistic", all_sounds=None):
        """
        Enhance a sound timeline into a detailed visual prompt.
        Receives raw timeline of all detected sounds with timestamps.
        
        Args:
            sound_timeline (str): Raw timeline of detected sounds with timestamps and confidence
            style (str): Visual style preference (photorealistic, artistic, etc.)
            all_sounds (list): List of all detected sounds with scores (optional, for backward compatibility)
            
        Returns:
            str: Enhanced visual prompt for image generation
        """
        print(f"[LLM] Sending sound timeline to LM Studio for creative prompt...")
        
        # Construct the prompt for LM Studio
        system_message = """You are a creative visual storyteller and image prompt expert. 
Your task is to analyze a TIMELINE of detected sounds from an audio recording and create a SHORT, CREATIVE, VIVID visual prompt for image generation.

IMPORTANT RULES:
- Maximum 25 words
- Review the sound timeline showing what sounds occurred at what times
- Create an interesting scene that captures the audio journey
- Consider the progression and combination of sounds
- Use vivid, descriptive language
- Include mood, atmosphere, or artistic style
- Be creative and imaginative
- Output ONLY the prompt, no explanation"""
        
        user_message = f"""Sound Timeline from Audio Recording:

{sound_timeline}

Style preference: {style}

Analyze the sound timeline above and create a creative, concise visual prompt (max 25 words) that captures the scene."""

        # Prepare the API request
        payload = {
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 200,
            "stream": False
        }
        
        try:
            # Send request to LM Studio
            response = requests.post(
                self.api_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=30
            )
            
            response.raise_for_status()
            
            # Extract the enhanced prompt
            result = response.json()
            enhanced_prompt = result['choices'][0]['message']['content'].strip()
            
            print(f"[OK] Enhanced prompt received!")
            print(f"[LLM] Enhanced prompt: {enhanced_prompt}")
            
            return enhanced_prompt
            
        except requests.exceptions.ConnectionError:
            print("[ERROR] Could not connect to LM Studio.")
            print("Make sure LM Studio is running with the local server enabled.")
            print("Returning original timeline as fallback.")
            return sound_timeline
            
        except requests.exceptions.Timeout:
            print("[ERROR] Request to LM Studio timed out.")
            print("Returning original timeline as fallback.")
            return sound_timeline
            
        except Exception as e:
            print(f"[ERROR] Communicating with LM Studio: {str(e)}")
            print("Returning original timeline as fallback.")
            return sound_timeline
    
    def test_connection(self):
        """
        Test the connection to LM Studio.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            # Simple test request
            payload = {
                "messages": [
                    {"role": "user", "content": "Hello"}
                ],
                "max_tokens": 10
            }
            
            response = requests.post(
                self.api_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=5
            )
            
            response.raise_for_status()
            print("[OK] LM Studio connection successful!")
            return True
            
        except Exception as e:
            print(f"[ERROR] LM Studio connection failed: {str(e)}")
            return False


def main():
    """Test the prompt enhancer."""
    enhancer = PromptEnhancer()
    
    # Test connection
    print("Testing LM Studio connection...")
    enhancer.test_connection()
    
    # Test enhancement
    print("\nTesting prompt enhancement...")
    sample_description = "The audio contains sounds of a dog barking"
    enhanced = enhancer.enhance(sample_description)
    print(f"\nOriginal: {sample_description}")
    print(f"Enhanced: {enhanced}")


if __name__ == "__main__":
    main()

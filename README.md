#  Sound AImagination #



**Transform sounds into stunning AI-generated images!**This project implements an AI pipeline that:

1. Records 10 seconds of audio from your microphone

Sound AImagination is an innovative audio-to-image generation pipeline that records sounds, analyzes them with AI, creates creative prompts, and generates unique images. Experience the magic of turning your voice, music, or any sound into beautiful visual art.2. Uses YAMNet (via TensorFlow Hub) to classify and describe the audio

3. Sends the description to LM Studio to generate an enhanced visual prompt

![Python](https://img.shields.io/badge/Python-3.13-blue)4. Uses Stable Diffusion to generate an image from the enhanced prompt

![License](https://img.shields.io/badge/License-MIT-green)

![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)## Requirements



---### Software

- Python 3.8 or higher

## ✨ Features- LM Studio running locally (default: http://localhost:1234)

- CUDA-capable GPU (optional but recommended for Stable Diffusion)

- 🎤 **Audio Recording**: Record 10 seconds of any sound

- 🔊 **Sound Analysis**: AI-powered audio classification using Google's YAMNet Python Libraries

- ⏱️ **Timeline Detection**: Tracks what sounds occurred at what timesInstall dependencies with:

- 🤖 **Creative Prompt Generation**: Uses LM Studio to create artistic image prompts

- 🎨 **Image Generation**: Produces unique images with Stable Diffusionpip install -r requirements.txt

- 📱 **Modern GUI**: Beautiful step-by-step interface with phone app design

- 📊 **Real-time Progress**: Visual feedback throughout the entire process


If you find this project fun&creative, please consider giving it a star! ⭐

## Quickstart (Windows PowerShell)

1. Create a virtual environment (optional but recommended):
```
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```
pip install -r requirements.txt
```
3. Install and Open LM studio - Load any language model & Click **Start Server** (default port: 1234)
   
4. Run the app:
```
gui_app_steps.py
```




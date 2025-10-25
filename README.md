# 🎵 Sound AImagination# AI Audio-to-Image Pipeline



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

- 🔊 **Sound Analysis**: AI-powered audio classification using Google's YAMNet (521 sound classes)### Python Libraries

- ⏱️ **Timeline Detection**: Tracks what sounds occurred at what timesInstall dependencies with:

- 🤖 **Creative Prompt Generation**: Uses LM Studio to create artistic image prompts```bash

- 🎨 **Image Generation**: Produces unique images with Stable Diffusionpip install -r requirements.txt

- 📱 **Modern GUI**: Beautiful step-by-step interface with phone app design```

- 📊 **Real-time Progress**: Visual feedback throughout the entire process

## Setup

---

1. **Install dependencies:**

## 🎯 How It Works   ```bash

   pip install -r requirements.txt

```   ```

Record Audio (10s) → Analyze Sounds → Generate Timeline → Create Prompt → Generate Image

```2. **Start LM Studio:**

   - Download and install LM Studio from https://lmstudio.ai/

1. **Record**: Capture 10 seconds of audio (speech, music, ambient sounds, etc.)   - Load a model (e.g., Llama 3, Mistral, etc.)

2. **Analyze**: YAMNet AI detects all sounds with timestamps and confidence scores   - Start the local server (default port: 1234)

3. **Timeline**: Creates a detailed timeline showing when each sound occurred

4. **Enhance**: LM Studio analyzes the timeline and creates a creative visual prompt3. **Run the pipeline:**

5. **Generate**: Stable Diffusion produces a unique image from the prompt   ```bash

   python main.py

---   ```



## 📋 Prerequisites## Project Structure



- **Windows 10/11**```

- **Python 3.13** (or 3.9+).

- **LM Studio** running locally with server enabled├── main.py                 # Main pipeline orchestrator

  - Download: [https://lmstudio.ai/](https://lmstudio.ai/)├── audio_recorder.py       # Audio recording module

  - Load any model (e.g., Llama, Mistral, Phi)├── audio_classifier.py     # YAMNet audio classification

  - Enable local server on port 1234├── prompt_enhancer.py      # LM Studio integration

- **16GB+ RAM** recommended├── image_generator.py      # Stable Diffusion integration

- **GPU** (NVIDIA recommended for faster image generation)├── requirements.txt        # Python dependencies

└── output/                 # Generated audio and images

---```



## 🚀 Installation## Configuration



### 1. Clone the RepositoryEdit the configuration in `main.py` to customize:

- Audio recording duration (default: 10 seconds)

```bash- LM Studio API endpoint

git clone https://github.com/yourusername/sound-aimagination.git- Stable Diffusion model

cd sound-aimagination- Output directories

```

## Usage

### 2. Run Setup Script

Simply run:

```bash```bash

setup.batpython main.py

``````



This will:The pipeline will:

- Create a virtual environment1. Record audio for 10 seconds

- Install all dependencies (PyTorch, TensorFlow, Diffusers, Kivy, etc.)2. Classify the audio

- Set up the project structure3. Generate an enhanced prompt

4. Create an image

### 3. Start LM Studio5. Save everything to the `output/` directory



1. Open **LM Studio**## Troubleshooting

2. Load any language model

3. Go to **Local Server** tab- **Microphone not working:** Check your default input device in system settings

4. Click **Start Server** (default port: 1234)- **LM Studio connection failed:** Ensure LM Studio is running with the server enabled

- **Out of memory error:** Reduce the Stable Diffusion image size or use CPU mode

---

## 🎮 Usage

### GUI Application (Recommended)

Simply double-click:
```
run_gui_steps.bat
```

Or run manually:
```bash
.venv\Scripts\python.exe gui_app_steps.py
```

### Command Line

```bash
.venv\Scripts\python.exe main.py
```

---

## 🖼️ GUI Walkthrough

### Step 1: Welcome Screen
- Press **START RECORDING** to begin
- Prepare to make sounds for 10 seconds

### Step 2: Processing
- Real-time progress bar
- Shows current AI operation
- Visual feedback with icons

### Step 3: Results
- Displays all detected sounds with confidence levels
- Shows timeline of when sounds occurred
- Reveals the creative prompt generated by LM Studio

### Step 4: Complete
- View your generated image
- Option to create another

---

## 🧠 AI Models Used

### 1. YAMNet (Audio Classification)
- **Source**: Google Research / TensorFlow Hub
- **Purpose**: Analyzes audio and detects 521 different sound classes
- **Frame Rate**: ~0.96 seconds per frame
- **Output**: Timeline of sounds with timestamps and confidence scores

### 2. LM Studio (Creative Prompts)
- **Purpose**: Analyzes sound timeline and creates artistic image prompts
- **Input**: Raw timeline with timestamps and confidence percentages
- **Output**: Creative, concise visual description (max 25 words)
- **Runs**: Locally on your machine

### 3. Stable Diffusion (Image Generation)
- **Source**: Hugging Face Diffusers
- **Model**: stabilityai/stable-diffusion-2-1-base
- **Purpose**: Generates unique images from text prompts
- **Resolution**: 512x512 (configurable)

---

## 📁 Project Structure

```
sound-aimagination/
├── gui_app_steps.py        # Main GUI application
├── main.py                 # Command-line pipeline
├── audio_recorder.py       # Audio recording module
├── audio_classifier.py     # YAMNet sound analysis
├── prompt_enhancer.py      # LM Studio integration
├── image_generator.py      # Stable Diffusion wrapper
├── requirements.txt        # Python dependencies
├── setup.bat              # Setup script
├── run_gui_steps.bat      # GUI launcher
├── Sound file/            # Recorded audio files (auto-created)
└── GeneratedImage/        # Generated images (auto-created)
```

---

## ⚙️ Configuration

Edit the configuration in `gui_app_steps.py` or `main.py`:

```python
config = {
    'audio_duration': 10,              # Recording duration (seconds)
    'sample_rate': 16000,              # Audio sample rate
    'image_style': 'photorealistic',   # Image style preference
    'image_width': 512,                # Output image width
    'image_height': 512,               # Output image height
    'num_inference_steps': 30,         # SD steps (higher = better quality)
    'lm_studio_url': 'http://localhost:1234/v1/chat/completions'
}
```

---

## 🔧 Troubleshooting

### LM Studio Connection Failed
- Ensure LM Studio is running
- Check that local server is enabled (port 1234)
- Verify a model is loaded

### Audio Recording Issues
- Check microphone permissions
- Verify default audio input device is set correctly
- Try adjusting volume levels

### Image Generation Slow
- GPU recommended for faster generation
- Reduce `num_inference_steps` (e.g., 20)
- Lower image resolution (e.g., 256x256)

### Out of Memory
- Close other applications
- Reduce batch size or resolution
- Consider using CPU-only mode (slower)

---

## 📊 Example Timeline Output

```
Sound Timeline - 11 detections across 11 frames:

0.0s - Music (98.2%)
0.96s - Music (96.5%)
1.92s - Piano (85.6%)
2.88s - Piano (89.1%)
3.84s - Speech (72.3%)
4.8s - Speech (75.8%)
5.76s - Crowd (63.4%)
6.72s - Applause (56.7%)
7.68s - Laughter (48.9%)
8.64s - Music (84.5%)
9.6s - Orchestra (67.8%)

Total unique sounds: 7
```

**LM Studio Prompt**:
> "Photorealistic: A grand concert hall erupts with emotion – piano melodies, soaring orchestra, captivated speech, and joyous applause."

---

## 🎨 Example Use Cases

- **Music Visualization**: Record your favorite song and see AI's interpretation
- **Voice Art**: Speak words or poetry and generate visual representations
- **Ambient Soundscapes**: Capture nature sounds for unique landscape images
- **Sound Effects**: Create images from everyday sounds (rain, traffic, laughter)
- **Creative Experiments**: Mix different sounds for unexpected results

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Google Research** - YAMNet audio classification model
- **Stability AI** - Stable Diffusion image generation
- **Hugging Face** - Diffusers library and model hosting
- **LM Studio** - Local LLM inference platform
- **Kivy** - Cross-platform GUI framework

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Made with ❤️ and AI**

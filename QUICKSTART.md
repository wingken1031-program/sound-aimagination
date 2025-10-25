# ⚡ Quick Start Guide

Get Sound AImagination running in 3 easy steps!

## 🎯 Prerequisites Checklist

Before you start, make sure you have:
- [ ] Windows 10 or 11
- [ ] Python 3.9 or higher installed
- [ ] LM Studio downloaded from https://lmstudio.ai/
- [ ] 16GB+ RAM (8GB minimum)
- [ ] Working microphone

## 📦 Installation (5 minutes)

### Step 1: Clone or Download
```bash
git clone https://github.com/yourusername/sound-aimagination.git
cd sound-aimagination
```
Or download ZIP and extract it.

### Step 2: Run Setup
Double-click `setup.bat` or run:
```bash
setup.bat
```

This installs all required AI models and dependencies.  
☕ **Takes 5-10 minutes** depending on your internet speed.

### Step 3: Start LM Studio
1. Open **LM Studio**
2. Download any model (recommended: Llama 3 or Mistral)
3. Go to **"Local Server"** tab
4. Click **"Start Server"**
5. Leave it running (port 1234)

## 🎮 Usage (1 minute)

### Launch the App
Double-click `run_gui_steps.bat`

### Use the App
1. **Step 1**: Click "START RECORDING"
2. **Step 2**: Make sounds for 10 seconds (speak, play music, sing, etc.)
3. **Step 3**: Watch AI analyze your sounds
4. **Step 4**: See your unique generated image!

That's it! 🎉

## 🎯 What to Try First

### Easy Tests
1. **Speech**: Say "Hello, this is a test of Sound AImagination"
2. **Music**: Play your favorite song from phone/computer
3. **Nature**: Birds chirping, rain sounds, wind
4. **Mixed**: Talk while music plays in background

### Creative Ideas
- Beatbox or make drum sounds
- Read a poem dramatically
- Play an instrument
- Mix different sound sources
- Try ambient cafe/street sounds

## 🔧 Troubleshooting

### "Can't connect to LM Studio"
✅ Make sure LM Studio local server is running on port 1234

### "Audio recording failed"
✅ Check microphone permissions in Windows Settings
✅ Test microphone in Windows Sound settings

### "Out of memory"
✅ Close other applications
✅ Try lower resolution in config (256x256)

### "Takes too long"
✅ Normal! First run downloads models (~4GB)
✅ Image generation takes 1-3 minutes (30 steps)
✅ Reduce steps to 20 for faster results

## 📊 Expected Times

- **First Run**: 5-10 min (downloading models)
- **Recording**: 10 seconds
- **Sound Analysis**: 5-10 seconds
- **Prompt Generation**: 2-5 seconds
- **Image Generation**: 1-3 minutes
- **Total**: ~2-4 minutes per image

## 🎨 Tips for Best Results

1. **Clear Audio**: Speak clearly or play music loudly
2. **Variety**: Mix different sounds for interesting results
3. **Experiment**: Try unexpected sound combinations
4. **Be Patient**: Image generation takes time but is worth it!
5. **Have Fun**: There are no wrong sounds, just explore!

## 📁 Where Files Are Saved

- **Recorded Audio**: `Sound file/audio_YYYYMMDD_HHMMSS.wav`
- **Generated Images**: `GeneratedImage/image_YYYYMMDD_HHMMSS.png`
- **Results JSON**: `GeneratedImage/results_YYYYMMDD_HHMMSS.json`

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. See troubleshooting section above
3. Open an issue on GitHub
4. Check existing issues for solutions

## 🎉 You're Ready!

Now go create some amazing sound-generated art! 🎵✨

---

**Next**: After trying it, share your results and star the repo! ⭐

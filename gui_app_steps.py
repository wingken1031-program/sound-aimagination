"""
Kivy GUI Application for Audio-to-Image AI Pipeline
Modern Step-by-Step Phone App Design
"""

import os
import threading
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image as KivyImage
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle

from audio_recorder import AudioRecorder
from audio_classifier import AudioClassifier
from prompt_enhancer import PromptEnhancer
from image_generator import ImageGenerator


# Step 1: Welcome/Record Screen
class WelcomeScreen(Screen):
    """Welcome screen with record button."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Background
        with layout.canvas.before:
            Color(0.95, 0.95, 0.98, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        
        # Main content container
        content = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=30,
            size_hint=(0.9, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text='[b]Sound AImagination[/b]',
            markup=True,
            font_size='36sp',
            size_hint_y=None,
            height=80,
            color=(0.2, 0.3, 0.5, 1)
        )
        content.add_widget(title)
        
        # Step indicator
        step_label = Label(
            text='Step 1 of 4',
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1)
        )
        content.add_widget(step_label)
        

        
        # Description
        desc = Label(
            text='Record 10 seconds of audio\nSpeak, play music, or make any sound',
            font_size='18sp',
            size_hint_y=None,
            height=80,
            color=(0.3, 0.3, 0.3, 1),
            halign='center'
        )
        content.add_widget(desc)
        
        # Spacer
        content.add_widget(Widget(size_hint_y=0.3))
        
        # Record button
        self.record_btn = Button(
            text='START RECORDING',
            size_hint_y=None,
            height=70,
            font_size='20sp',
            bold=True,
            background_color=(0.2, 0.6, 1, 1),
            background_normal=''
        )
        self.record_btn.bind(on_press=self.start_recording)
        content.add_widget(self.record_btn)
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def start_recording(self, instance):
        """Start recording and move to next screen."""
        self.record_btn.disabled = True
        self.record_btn.text = 'RECORDING...'
        self.record_btn.background_color = (0.9, 0.3, 0.3, 1)
        
        # Start pipeline in background
        app = App.get_running_app()
        app.root.start_pipeline()


# Step 2: Processing Screen
class ProcessingScreen(Screen):
    """Screen showing processing progress."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Background
        with layout.canvas.before:
            Color(0.95, 0.95, 0.98, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        
        # Main content
        content = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20,
            size_hint=(0.9, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Step indicator
        self.step_label = Label(
            text='Step 2 of 4',
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1)
        )
        content.add_widget(self.step_label)
        
        # Processing icon
        self.icon = Label(
            text='[size=100sp]🔊[/size]',
            markup=True,
            size_hint_y=None,
            height=150
        )

        
        # Status text
        self.status = Label(
            text='Recording audio...',
            font_size='22sp',
            size_hint_y=None,
            height=60,
            color=(0.2, 0.3, 0.5, 1),
            bold=True
        )
        content.add_widget(self.status)
        
        # Progress bar with card background
        progress_card = BoxLayout(
            orientation='vertical',
            padding=20,
            size_hint_y=None,
            height=100
        )
        with progress_card.canvas.before:
            Color(1, 1, 1, 1)
            self.progress_bg = RoundedRectangle(
                pos=progress_card.pos,
                size=progress_card.size,
                radius=[15]
            )
        progress_card.bind(pos=self._update_progress_bg, size=self._update_progress_bg)
        
        self.progress = ProgressBar(
            max=100,
            value=0,
            size_hint_y=None,
            height=30
        )
        progress_card.add_widget(self.progress)
        
        self.progress_text = Label(
            text='0%',
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1)
        )
        progress_card.add_widget(self.progress_text)
        
        content.add_widget(progress_card)
        
        # Details text
        self.details = Label(
            text='Please wait...',
            font_size='14sp',
            size_hint_y=None,
            height=40,
            color=(0.6, 0.6, 0.6, 1)
        )
        content.add_widget(self.details)
        
        content.add_widget(Widget())  # Spacer
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def _update_progress_bg(self, instance, value):
        self.progress_bg.pos = instance.pos
        self.progress_bg.size = instance.size
    
    def update_progress(self, value, status, details='', icon='[size=100sp]🔊[/size]', step='2'):
        """Update processing screen."""
        self.progress.value = value
        self.progress_text.text = f'{int(value)}%'
        self.status.text = status
        self.details.text = details
        self.icon.text = icon
        self.step_label.text = f'Step {step} of 4'


# Step 3: Results Screen (Sounds Detected)
class ResultsScreen(Screen):
    """Screen showing detected sounds and prompt."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Background
        with layout.canvas.before:
            Color(0.95, 0.95, 0.98, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        
        # Scrollable content
        scroll = ScrollView()
        content = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))
        
        # Step indicator
        step_label = Label(
            text='Step 3 of 4',
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.5, 0.5, 0.5, 1)
        )
        content.add_widget(step_label)
        
        # Title
        title = Label(
            text='[b]Sounds Detected[/b]',
            markup=True,
            font_size='28sp',
            size_hint_y=None,
            height=60,
            color=(0.2, 0.3, 0.5, 1)
        )
        content.add_widget(title)
        
        # Sounds card
        sounds_card = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10,
            size_hint_y=None,
            height=300
        )
        with sounds_card.canvas.before:
            Color(1, 1, 1, 1)
            self.sounds_bg = RoundedRectangle(
                pos=sounds_card.pos,
                size=sounds_card.size,
                radius=[15]
            )
        sounds_card.bind(pos=self._update_sounds_bg, size=self._update_sounds_bg)
        
        sounds_scroll = ScrollView()
        self.sounds_text = Label(
            text='Analyzing...',
            size_hint_y=None,
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1),
            markup=True,
            halign='left',
            valign='top',
            padding=(10, 10)
        )
        self.sounds_text.bind(
            texture_size=lambda *x: setattr(self.sounds_text, 'height', self.sounds_text.texture_size[1] + 20)
        )
        self.sounds_text.bind(
            width=lambda *x: setattr(self.sounds_text, 'text_size', (self.sounds_text.width - 20, None))
        )
        sounds_scroll.add_widget(self.sounds_text)
        sounds_card.add_widget(sounds_scroll)
        
        content.add_widget(sounds_card)
        
        # Enhanced Prompt card
        prompt_card = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10,
            size_hint_y=None,
            height=250
        )
        with prompt_card.canvas.before:
            Color(0.9, 0.95, 1, 1)
            self.prompt_bg = RoundedRectangle(
                pos=prompt_card.pos,
                size=prompt_card.size,
                radius=[15]
            )
        prompt_card.bind(pos=self._update_prompt_bg, size=self._update_prompt_bg)
        
        prompt_title = Label(
            text='[b]Image Prompt:[/b]',
            markup=True,
            font_size='18sp',
            size_hint_y=None,
            height=30,
            color=(0.2, 0.3, 0.5, 1),
            halign='left'
        )
        prompt_title.bind(width=lambda *x: setattr(prompt_title, 'text_size', (prompt_title.width - 40, None)))
        prompt_card.add_widget(prompt_title)
        
        prompt_scroll = ScrollView()
        self.prompt_text = Label(
            text='Generating...',
            size_hint_y=None,
            font_size='14sp',
            color=(0.3, 0.3, 0.3, 1),
            markup=True,
            halign='left',
            valign='top',
            padding=(10, 10)
        )
        self.prompt_text.bind(
            texture_size=lambda *x: setattr(self.prompt_text, 'height', self.prompt_text.texture_size[1] + 20)
        )
        self.prompt_text.bind(
            width=lambda *x: setattr(self.prompt_text, 'text_size', (self.prompt_text.width - 20, None))
        )
        prompt_scroll.add_widget(self.prompt_text)
        prompt_card.add_widget(prompt_scroll)
        
        content.add_widget(prompt_card)
        
        # Next button
        self.next_btn = Button(
            text='GENERATING IMAGE...',
            size_hint_y=None,
            height=60,
            font_size='18sp',
            bold=True,
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal='',
            disabled=True
        )
        content.add_widget(self.next_btn)
        
        content.add_widget(Widget(size_hint_y=None, height=40))  # Bottom padding
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def _update_sounds_bg(self, instance, value):
        self.sounds_bg.pos = instance.pos
        self.sounds_bg.size = instance.size
    
    def _update_prompt_bg(self, instance, value):
        self.prompt_bg.pos = instance.pos
        self.prompt_bg.size = instance.size
    
    def update_sounds(self, text):
        """Update detected sounds."""
        self.sounds_text.text = text
    
    def update_prompt(self, text):
        """Update enhanced prompt."""
        self.prompt_text.text = text


# Step 4: Final Image Screen
class ImageScreen(Screen):
    """Screen showing the generated image."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        # Background
        with layout.canvas.before:
            Color(0.95, 0.95, 0.98, 1)
            self.bg = Rectangle(size=Window.size, pos=(0, 0))
        
        # Scrollable content
        scroll = ScrollView()
        content = BoxLayout(
            orientation='vertical',
            padding=40,
            spacing=20,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))
        
        # Step indicator
        step_label = Label(
            text='Step 4 of 4 - Complete!',
            font_size='16sp',
            size_hint_y=None,
            height=30,
            color=(0.2, 0.7, 0.4, 1)
        )
        content.add_widget(step_label)
        
        # Success icon
        success_icon = Label(
            text='[size=80sp]✓[/size]',
            markup=True,
            size_hint_y=None,
            height=100,
            color=(0.2, 0.7, 0.4, 1)
        )

        
        # Title
        title = Label(
            text='[b]Here is your Image[/b]',
            markup=True,
            font_size='28sp',
            size_hint_y=None,
            height=60,
            color=(0.2, 0.3, 0.5, 1)
        )
        content.add_widget(title)
        
        # Image card
        image_card = FloatLayout(size_hint_y=None, height=500)
        with image_card.canvas.before:
            Color(1, 1, 1, 1)
            self.image_bg = RoundedRectangle(
                pos=image_card.pos,
                size=image_card.size,
                radius=[15]
            )
        image_card.bind(pos=self._update_image_bg, size=self._update_image_bg)
        
        self.image_widget = KivyImage(
            source='',
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(0.95, 0.95),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        image_card.add_widget(self.image_widget)
        
        content.add_widget(image_card)
        
        # Save status
        self.save_label = Label(
            text='✓ Saved to GeneratedImage/',
            font_size='14sp',
            size_hint_y=None,
            height=40,
            color=(0.2, 0.7, 0.4, 1)
        )
        content.add_widget(self.save_label)
        
        # Restart button
        restart_btn = Button(
            text='CREATE ANOTHER',
            size_hint_y=None,
            height=60,
            font_size='18sp',
            bold=True,
            background_color=(0.2, 0.6, 1, 1),
            background_normal=''
        )
        restart_btn.bind(on_press=self.restart)
        content.add_widget(restart_btn)
        
        content.add_widget(Widget(size_hint_y=None, height=40))  # Bottom padding
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def _update_image_bg(self, instance, value):
        self.image_bg.pos = instance.pos
        self.image_bg.size = instance.size
    
    def update_image(self, image_path):
        """Update the displayed image."""
        self.image_widget.source = image_path
        self.image_widget.reload()
    
    def restart(self, instance):
        """Go back to welcome screen."""
        app = App.get_running_app()
        app.root.reset()


# Main Manager
class AudioToImageManager(ScreenManager):
    """Manages the step-by-step flow."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(direction='left', duration=0.3)
        
        # Configuration
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
        
        # Pipeline components (lazy loading)
        self.recorder = None
        self.classifier = None
        self.enhancer = None
        self.image_gen = None
        
        # Add screens
        self.add_widget(WelcomeScreen(name='welcome'))
        self.add_widget(ProcessingScreen(name='processing'))
        self.add_widget(ResultsScreen(name='results'))
        self.add_widget(ImageScreen(name='image'))
        
        self.current = 'welcome'
    
    def initialize_components(self):
        """Initialize AI components (lazy loading)."""
        if self.recorder is None:
            self.recorder = AudioRecorder(sample_rate=self.config['sample_rate'])
            self.classifier = AudioClassifier()
            self.enhancer = PromptEnhancer(api_url=self.config['lm_studio_url'])
            self.image_gen = ImageGenerator()
    
    def start_pipeline(self):
        """Start the AI pipeline in background thread."""
        self.current = 'processing'
        thread = threading.Thread(target=self.run_pipeline)
        thread.daemon = True
        thread.start()
    
    def run_pipeline(self):
        """Execute the complete AI pipeline."""
        try:
            # Initialize components
            Clock.schedule_once(lambda dt: self.update_processing(
                5, 'Initializing AI models...', 'Loading YAMNet and Stable Diffusion', 
                '[size=100sp]⚙️[/size]', '1'
            ), 0)
            
            self.initialize_components()
            import time
            time.sleep(1)
            
            # Step 1: Record Audio
            Clock.schedule_once(lambda dt: self.update_processing(
                10, 'Recording audio...', 'Speak now! (10 seconds)', 
                '[size=100sp]🎤[/size]', '1'
            ), 0)
            
            audio_data, sample_rate, audio_path = self.recorder.record(
                duration=self.config['audio_duration'],
                output_dir=self.config['audio_output_dir']
            )
            
            Clock.schedule_once(lambda dt: self.update_processing(
                25, 'Recording complete!', 'Analyzing audio...', 
                '[size=100sp]✓[/size]', '1'
            ), 0)
            time.sleep(0.5)
            
            # Step 2: Classify Audio
            Clock.schedule_once(lambda dt: self.update_processing(
                30, 'Analyzing audio...', 'Detecting sounds with YAMNet', 
                '[size=100sp]🔊[/size]', '2'
            ), 0)
            
            classification = self.classifier.classify(audio_data, sample_rate, threshold=0.2)
            
            # Format detected sounds
            detected_sounds = classification.get('all_detected_sounds', [])
            timeline = classification.get('timeline', [])
            total_sounds = classification.get('total_sounds_detected', 0)
            
            sounds_text = f"[b][size=20sp]Total: {total_sounds} sounds[/size][/b]\n\n"
            
            if detected_sounds:
                sounds_text += "[b]Top Detected Sounds:[/b]\n\n"
                for i, sound in enumerate(detected_sounds[:10], 1):
                    sounds_text += f"{i}. {sound['class']} - {sound['score']:.1%}\n"
                
                if timeline:
                    sounds_text += "\n[b]Timeline:[/b]\n\n"
                    for entry in timeline[:8]:
                        sounds_text += f"[{entry['timestamp']:.1f}s] {entry['class']}\n"
            else:
                sounds_text += "No sounds detected above threshold."
            
            Clock.schedule_once(lambda dt: self.update_processing(
                50, 'Sounds detected!', f'Found {total_sounds} different sounds', 
                '[size=100sp]✓[/size]', '2'
            ), 0)
            
            Clock.schedule_once(lambda dt: self.get_screen('results').update_sounds(sounds_text), 0)
            time.sleep(0.5)
            
            # Step 3: Enhance Prompt
            Clock.schedule_once(lambda dt: self.update_processing(
                55, 'Enhancing prompt...', 'Using LM Studio for creative prompt', 
                '[size=100sp]💭[/size]', '3'
            ), 0)
            
            sound_timeline = self.classifier.generate_timeline_text(classification)
            # Send sound timeline directly to LM Studio
            enhanced_prompt = self.enhancer.enhance(
                sound_timeline,
                style=self.config['image_style']
            )
            
            Clock.schedule_once(lambda dt: self.get_screen('results').update_prompt(enhanced_prompt), 0)
            
            Clock.schedule_once(lambda dt: self.update_processing(
                65, 'Prompt ready!', 'Moving to results...', 
                '[size=100sp]✓[/size]', '3'
            ), 0)
            time.sleep(1)
            
            # Show results screen
            Clock.schedule_once(lambda dt: setattr(self, 'current', 'results'), 0)
            time.sleep(2)
            
            # Step 4: Generate Image
            Clock.schedule_once(lambda dt: self.update_processing(
                70, 'Generating image...', 'Using Stable Diffusion (this takes time)', 
                '[size=100sp]🎨[/size]', '4'
            ), 0)
            
            # Switch back to processing for image generation
            Clock.schedule_once(lambda dt: setattr(self, 'current', 'processing'), 0)
            
            image_path = self.image_gen.generate(
                prompt=enhanced_prompt,
                output_dir=self.config['image_output_dir'],
                width=self.config['image_width'],
                height=self.config['image_height'],
                num_inference_steps=self.config['num_inference_steps']
            )
            
            Clock.schedule_once(lambda dt: self.update_processing(
                100, 'Complete!', 'Your image is ready!', 
                '[size=100sp]✓[/size]', '4'
            ), 0)
            time.sleep(0.5)
            
            # Show final image
            if image_path and os.path.exists(image_path):
                Clock.schedule_once(lambda dt: self.get_screen('image').update_image(image_path), 0)
                Clock.schedule_once(lambda dt: setattr(self, 'current', 'image'), 0)
            
        except Exception as e:
            error_msg = f'Error: {str(e)}'
            Clock.schedule_once(lambda dt: self.update_processing(
                0, 'Error occurred', error_msg, 
                '[size=100sp]❌[/size]', '0'
            ), 0)
            import traceback
            traceback.print_exc()
    
    def update_processing(self, value, status, details, icon, step):
        """Update the processing screen."""
        screen = self.get_screen('processing')
        screen.update_progress(value, status, details, icon, step)
    
    def reset(self):
        """Reset to welcome screen for another run."""
        self.transition.direction = 'right'
        self.current = 'welcome'
        self.transition.direction = 'left'
        
        # Reset welcome screen button
        welcome = self.get_screen('welcome')
        welcome.record_btn.disabled = False
        welcome.record_btn.text = 'START RECORDING'
        welcome.record_btn.background_color = (0.2, 0.6, 1, 1)


class AudioToImageApp(App):
    """Kivy Application for Audio-to-Image Pipeline."""
    
    def build(self):
        """Build the application."""
        Window.size = (400, 700)  # Phone-like aspect ratio
        Window.clearcolor = (0.95, 0.95, 0.98, 1)
        self.title = 'Sound AImagination'
        self.icon = 'icon.png'
        return AudioToImageManager()
    


def main():
    """Main entry point for the GUI application."""
    AudioToImageApp().run()


if __name__ == "__main__":
    main()

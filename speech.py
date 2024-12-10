from gtts import gTTS
import pygame
import io

def speech(input, language):
    tts = gTTS(text=input, lang=language)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    #   Initialize pygame mixer and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()

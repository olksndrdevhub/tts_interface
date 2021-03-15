from gtts import gTTS



class TextToSpeechUARecognizer():
    
    def __init__(self, text) -> None:
        self.text = text



    def recognize_text_ua(self):

        recognized_text = gTTS(text=self.text, slow=True, lang='uk')
        print('Text recognized!')
        return recognized_text


    def save_recognized_text(self, recognized_text, filename):
        recognized_text.save(filename)
        print(f'Saved to {filename}')



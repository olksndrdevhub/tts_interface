from gtts import gTTS, lang


class TextToSpeechUARecognizer():

    def recognize_text(self, text, lang):

        recognized_text = gTTS(text=text, slow=True, lang=lang)
        print('Text recognized!')
        return recognized_text


    def save_recognized_text(self, recognized_text, filename):
        recognized_text.save(filename)
        print(f'Saved to {filename}')

    def get_languages_to_display(self):
        languages_list = lang.tts_langs()
        languages_to_displ = []
        for language in languages_list:
            language = (str(language).upper(), str(languages_list.get(language)))
            languages_to_displ.append(language)
        return languages_to_displ

    def get_languages(self):
        languages_list = lang.tts_langs()
        languages = []
        for language in languages_list:
            languages.append(language)
        return languages

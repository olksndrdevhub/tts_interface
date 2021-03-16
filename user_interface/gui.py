from gtts import langs
from tts_backend.text_to_speech import TextToSpeechUARecognizer

import PySimpleGUI as sg

import platform

oper_sys = platform.system()
print(oper_sys)

TEXT = ''
FILENAME = ''
LANG = ''

FONT_1 = 'Ubuntu Mono Bold'
FONT_2 = ''
FONT_SIZE_1 = 16
FONT_SIZE_2 = 12

recognizer = TextToSpeechUARecognizer()

LANGUAGES_TO_DISPL = recognizer.get_languages_to_display()
LANGUAGES = recognizer.get_languages()

def run():
        
    sg.theme('Dark Blue 1')  # please make your windows colorful

    layout = [
                [sg.Text('TextToSpeech сonverts your text to audio', justification='center', pad=(50,20), size=(1000,3), font=(FONT_1,FONT_SIZE_1,'bold'))],
                [sg.Text('Paste your text here: ', font=(FONT_1,FONT_SIZE_2,'bold'), justification='left', size=(1000,1),)], 
                [sg.Multiline(key='-TEXT-', do_not_clear=True, size=(200,12), font=(FONT_1,FONT_SIZE_2, 'bold'))],
                [
                sg.Button(
                    'Clear', 
                    font=(FONT_1, FONT_SIZE_1), 
                    button_color='gray',
                    size=(20,2),
                    )
                ],
                [sg.Text('Select language', pad=(0,20))],
                [sg.Combo(LANGUAGES_TO_DISPL, size=(15,1), key='-LANG-', default_value='UK Ukrainian', font=(FONT_1,FONT_SIZE_1))],
                [
                sg.FileSaveAs(
                    button_text='Convert text to audio-file', 
                    file_types=(('ALL Files', '*.mp3'),), 
                    default_extension='.mp3', 
                    enable_events=True,
                    key='-SAVE-', 
                    pad=(2,50), 
                    size=(140,2), 
                    font=(FONT_1,FONT_SIZE_1),
                    button_color='green',
                    ),
                ],
                [
                sg.Button(
                    'Exit', 
                    size=(20,2), 
                    font=(FONT_1,FONT_SIZE_1),
                    button_color='red',
                    )
                ],
            ]
    window = sg.Window('TextToSpeech', layout, size=(1500,800), margins=(40,40), font=(FONT_1,FONT_SIZE_1,'bold'))

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        elif event == 'Clear':
            TEXT = ''
            window['-TEXT-'].update(TEXT)
            print('Field cleaned')
        
        elif event == '-SAVE-':
            print('save')
            FILENAME = values['-SAVE-']
            TEXT = values['-TEXT-']
            lang = str(values['-LANG-'][0]).lower()
            print(lang)
            if lang in LANGUAGES:
                LANG = lang
                print(LANG)
            else:
                print('bad lang...')
                sg.popup_ok('Select correct language!', title='TTS | Error', font=(FONT_1,FONT_SIZE_2,'bold'))
                continue

            if len(TEXT) > 1 and len(FILENAME) >= 5:
                sg.popup_auto_close('Wait...', title='TTS UA | Processing...', auto_close_duration=2, font=(FONT_1,FONT_SIZE_2,'bold'))
                rec_text = recognizer.recognize_text(text=TEXT, lang=LANG)
                recognizer.save_recognized_text(rec_text, FILENAME)
                print('Audio generated!')

                sg.popup(f'File saved here: {FILENAME}', title='Success!', font=(FONT_1,FONT_SIZE_2,'bold'))
                TEXT = ''
                FILENAME = ''
                window['-TEXT-'].update(TEXT)
            elif len(FILENAME)<5: 
                print('Fail, no filename')
            else:   
                print('Fail, no text...')
                
                sg.popup_ok('Paste your text!', title='TTS | Error', font=(FONT_1,FONT_SIZE_2,'bold'))



    window.close()
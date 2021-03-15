from tts_backend.text_to_speech import TextToSpeechUARecognizer

import PySimpleGUI as sg

import platform

oper_sys = platform.system()
print(oper_sys)

TEXT = ''
FILENAME = ''
FONT_1 = 'Ubuntu Mono Bold'
FONT_2 = ''
FONT_SIZE_1 = 16
FONT_SIZE_2 = 12

sg.theme('Dark Blue 1')  # please make your windows colorful

layout = [
            [sg.Text('TextToSpeech UA перетворить ваш текст в аудіо', justification='center', pad=(50,20), size=(1000,3), font=(FONT_1,FONT_SIZE_1,'bold'))],
            [sg.Text('Вставте ваш текст в це поле: ', font=(FONT_1,FONT_SIZE_2,'bold'), justification='left', size=(1000,1),)], 
            [sg.Multiline(key='-TEXT-', do_not_clear=True, size=(200,12), font=(FONT_1,FONT_SIZE_2, 'bold'))],
            [
             sg.Button(
                'Очистити', 
                font=(FONT_1, FONT_SIZE_1), 
                button_color='gray',
                size=(20,2),
                )
            ],
            [
             sg.FileSaveAs(
                button_text='Конвертувати текст в аудіо-файл', 
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
                'Вийти', 
                size=(20,2), 
                font=(FONT_1,FONT_SIZE_1),
                button_color='red',
                )
            ],
        ]
window = sg.Window('TextToSpeech UA', layout, size=(1500,700), margins=(40,40), font=(FONT_1,FONT_SIZE_1,'bold'))

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Вийти':
        break
    
    elif event == 'Очистити':
        TEXT = ''
        window['-TEXT-'].update(TEXT)
        print('Field cleaned')
    
    elif event == '-SAVE-':
        print('save')
        FILENAME = values['-SAVE-']
        TEXT = values['-TEXT-']
        print(FILENAME)

        if len(TEXT) > 1 and len(FILENAME) >= 5:
            recognizer = TextToSpeechUARecognizer(TEXT)
            sg.popup_auto_close('Створюємо mp3-файл, зачекайте...', title='TTS UA | Обробка...', auto_close_duration=2, font=(FONT_1,FONT_SIZE_2,'bold'))
            rec_text = recognizer.recognize_text_ua()
            recognizer.save_recognized_text(rec_text, FILENAME)
            print('Audio generated!')

            sg.popup(f'Файл збережено за адресою: {FILENAME}', title='Успіх!', font=(FONT_1,FONT_SIZE_2,'bold'))
            TEXT = ''
            FILENAME = ''
            window['-TEXT-'].update(TEXT)
        else:    
            print('Fail, no text...')
            
            sg.popup_ok('Вставте ваш текст!', title='TTS UA | Помилка', font=(FONT_1,FONT_SIZE_2,'bold'))



window.close()
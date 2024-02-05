import speech_recognition as sr
r = sr.Recognizer()
print("Говорите...")
def main():            
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Добавлено для улучшения распознавания речи в условиях шума
        audio = r.listen(source)

    try:
        print(r.recognize_google(audio, language='ru-RU'))
    except sr.UnknownValueError:
        print("Говорите внятно")
    except sr.RequestError as e:
        print("Не удалось запросить результаты от Speech Recognition service; {0}".format(e))

while True:
    main()

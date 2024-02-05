import speech_recognition as sr
# Открываем файл в режиме добавления
r = sr.Recognizer()
print("Говорите...\n CTR:+C - Остановка программы")
def main():            
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Добавлено для улучшения распознавания речи в условиях шума
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio, language='ru-RU'))
        with open('Logs.txt', 'a') as file:
        # Получаем ввод от пользователя
            text = r.recognize_google(audio, language='ru-RU')
        # Записываем ввод в файл и переходим на новую строку
            file.write(f"{text}\n")
    except sr.UnknownValueError:
        print("Говорите внятно")
    except sr.RequestError as e:
        print("Не удалось запросить результаты от Speech Recognition service; {0}".format(e))

while True:
    main()

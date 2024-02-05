import speech_recognition as sr

r = sr.Recognizer()
print("Говорите...\n CTR:+C - Остановка программы")

def main():            
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(text)
        if text.lower() == 'стоп':
            input("Программа остановлена по команде пользователя.")
            return False
        with open('Logs.txt', 'a') as file:
            file.write(f"{text}\n")
    except sr.UnknownValueError:
        print("Говорите внятно")
    except sr.RequestError as e:
        print("Не удалось запросить результаты от Speech Recognition service; {0}".format(e))
    return True

while main():
    pass
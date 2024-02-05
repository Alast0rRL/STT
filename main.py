import speech_recognition as sr
import datetime

# Получаем текущую дату
now = datetime.datetime.now()

# Выводим дату в формате DD-MM-YYYY
r = sr.Recognizer()
print("Говорите...\n CTR:+C - Остановка программы")
with open('Logs.txt', 'a') as file:
            file.write(f"\n{now.strftime("%d-%m-%Y %H:%M")}\n")
def main():            
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(text)
        if text.lower() == 'выключить':
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
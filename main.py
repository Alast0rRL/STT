# -*- coding: cp1251 -*-
import pyperclip
import time
import speech_recognition as sr
import datetime
import pyautogui
now = datetime.datetime.now()
r = sr.Recognizer()
print("��������...\n CTR:+C - ��������� ���������")
with open('Logs.txt', 'a') as file:
            file.write(f"\n{now.strftime("%d-%m-%Y %H:%M")}\n")
def main():            
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ru-RU')
        if text.lower() == '���������':
            input("��������� ����������� �� ������� ������������.")
            return False
        type_unicode(text)
        print(text)
        with open('Logs.txt', 'a') as file:
            file.write(f"{text}\n")
    except sr.UnknownValueError:
        print("�������� ������")
    except sr.RequestError as e:
        print("�� ������� ��������� ���������� �� Speech Recognition service; {0}".format(e))
    return True

def type_unicode(text):
    pyperclip.copy(text)
    time.sleep(0.2)  # �����, ����� ���� ����� ��� ����������� ������
    pyautogui.hotkey('ctrl', 'v')
while main():
    pass      

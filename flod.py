from doctest import testfile
from telnetlib import NAOCRD
from unittest import TextTestResult
import pyautogui as spam
import time
limite_msg = input("Enter n de mensagens:")
msg = input("escreva a mensagem que desja enviar:")
i = 0
time.sleep(2)
while i < int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")
i += 1


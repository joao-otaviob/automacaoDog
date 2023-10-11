 # Abrir o chrome
 # Entrar no site : https://walkdog.vercel.app/
 # Clicar em Quero ser dog 

import pyautogui
import time

pyautogui.PAUSE = (0.5)

pyautogui.press("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")


link = "https://walkdog.vercel.app/"
pyautogui.write(link)
pyautogui.press ("enter")

time.sleep (3)


pyautogui.click (x=523, y=752)

pyautogui.click (x=755, y=668)
pyautogui.write ("Matuzalem")
pyautogui.press ("tab")
pyautogui.write ("joao.otaviobarros@hotmail.com")
pyautogui.press("tab")
pyautogui.write ("11166644446")
pyautogui.press ("tab")
pyautogui.write ("54759-265")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write ("69")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press ("enter")
pyautogui.write("rasta")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press ("enter")
pyautogui.press ("enter")
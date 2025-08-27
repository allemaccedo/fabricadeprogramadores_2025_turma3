import mouseinfo, pyautogui, time

pyautogui.press("super")
pyautogui.write("google chrome")
pyautogui.press("enter")
pyautogui.click(526,61, duration=1)
time.sleep(1)
pyautogui.write("flamengo")
pyautogui.press("enter")
pyautogui.moveTo(321,195, duration=1)
pyautogui.click()
mouseinfo.mouseInfo()
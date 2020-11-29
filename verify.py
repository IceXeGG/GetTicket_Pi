import requests
from PIL import Image
from selenium.webdriver import ActionChains
import time
from io import BytesIO

class Code():
    def __init__(self, browser):
        self.browser = browser

        #擷取整個網頁頁面
    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

        #從擷取的網頁，裁剪出驗證碼圖片，並儲存到本地
    def get_touclick_img(self, name = 'captcha.png'):
        screenshot = self.get_screenshot()
        timenow = time.strftime("%Y%m%d%H%M%S") + ".png"
        screenshot.save(timenow)

    def main(self):
        self.get_touclick_img()

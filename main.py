from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json
import os
from verify import Code
from tkinter import *
import sys

sys.setrecursionlimit(2147483647)

TaxNo = '25148803'

#mainWin = Tk()

# 視窗標題
#mainWin.title("Hello")
# 視窗大小
#mainWin.geometry("480x140")
'''
def submit_click():
    global TaxNo
    TaxNo = tax_no_input.get()
    mainWin.quit()
def cancel_click():
    mainWin.quit()
    
tax_no_text = Label(mainWin,text="統一編號")
tax_no_input = Entry(mainWin,text="")
submit_button = Button(mainWin,text="確定變更",command=submit_click)
cancel_button = Button(mainWin,text="預設執行",command=cancel_click)

tax_no_text.grid(row=0,column=0)
tax_no_input.grid(row=0,column=1)
submit_button.grid(row=1,column=0)
cancel_button.grid(row=1,column=1)
'''
file_path = r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"' + " [--headless]" + " --remote-debugging-port=9222" + " --user-data-dir=" + "C:\selenum\AutomationProfile"
d = os.popen(file_path)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

class Buy_Ticket():
    def __init__(self):
        self.login_url = 'https://ecvip.pchome.com.tw/?0xe516d0101bfd000465be8905c437a1003767d4c4747a54897018c9bbbc63dd8abbb31dfb22f1aa364ab83701f9e653fc'#'https://kyfw.12306.cn/otn/login/init'        

    def login(self):
        browser.get(self.login_url)
        time.sleep(0.3)
        try:
            button = browser.find_elements_by_class_name('addBigCart')
            button[0].click()
            i=0
            while i!=len(button):
                button[i].click()
                i+=1
                time.sleep(0.3)
        except:
            self.book_ticket()
		
    def book_ticket(self):
        try:
            button = browser.find_element_by_class_name('check')
            button.click()
        except:
            browser.refresh()
            self.login()
            
    def pay(self):
        try:
            button2 = browser.find_element_by_partial_link_text('拍錢包')  
            browser.execute_script("arguments[0].click();", button2)
        except:
            self.delete_item()

    def delete_item(self):
        try:
            button3 = browser.find_element_by_id('warning-itchk_btn_btnDelete')
            button3.click()
            self.main()
        except:
            self.pay()
            
    def tax(self):
        try:
            button3 = browser.find_element_by_xpath("//*[@id='frmUserInfo']/dl[4]/dd[2]/div[1]/div[4]/label/input")#("公司戶電子發票")
            button3.click()
        except:
            self.tax()
            
    def taxNo(self):
        try:
            button3 = browser.find_element_by_id('TaxNo')
            button3.send_keys(TaxNo)
        except:
            self.taxNo()
            
    def submit(self):
        try:
            button = browser.find_element_by_id('btnSubmit')
            button.click()#確定送出
        except:
            self.error_home()

    def error_home(self):
        try:
            browser.find_element_by_id('indexMenu')
            self.main()
        except:
            self.submit()

    def Pi(self):
        try:
            button = browser.find_element_by_partial_link_text('繼續')
            button.click()
        except:
            self.empty_item()
            
    def empty_item(self):
        try:
            browser.find_element_by_id('btnPayment')
            self.main()
        except:
            self.Pi()
            
    def main(self):
        try:
            self.login()
            self.book_ticket()
            self.pay()
            self.tax()
            self.taxNo()
            self.submit()
            self.Pi()
            c = Code(browser)
            c.main()
            #browser.execute_script("window.open('https://ecvip.pchome.com.tw/?0xe516d0101bfd000465be8905c437a1003767d4c4747a54897018c9bbbc63dd8abbb31dfb22f1aa364ab83701f9e653fc')")
            #browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])
        except:
            self.main()
        
    def main2(self):
        try:
            browser.back()
            browser.back()
            #self.pay()
            #self.tax()
            self.submit()
            self.Pi()
            c = Code(browser)
            c.main()
        except:
            self.main()

if __name__ == '__main__':
    #mainWin.mainloop()
    browser = webdriver.Chrome(chrome_options=chrome_options)
    b = Buy_Ticket()
    b.main()
    while 1:
        try:
            b.main2()
        except:
            b.main()

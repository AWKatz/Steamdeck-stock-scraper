import smtplib # email alerts
import tkinter # popup alerts
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import messagebox
from datetime import datetime


browser_options = Options()
browser_options.add_argument("--headless=new")
url = "https://store.steampowered.com/sale/steamdeckrefurbished"

def start():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=browser_options)
    driver.get(url)
    return driver


def refresh(driver):
    driver.refresh()


def quit(driver):
    driver.quit()


def runner(driver):
    all_btn = driver.find_elements(By.XPATH, "//*[@id='SaleSection_33131']")
    x = all_btn[0].text
    x = x.split("00")[0]  ## HERE YOU CAN BREAKPOINT AND DETERMINE WHICH PART OF THE TEXT YOU ARE INTERESTED IN (E.G. STRIP FOR 64GB, 256GB ETC
    print(x)
    if "add" in x.lower():
print("\033[1;32m REFURBISHED STEAMDECK RESTOCKED  \n")
        
        # DISPLAY POPUP MESSAGE WHEN YOU CAN USE THE ADD TO CART BUTTON
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("REFURBISHED STEAMDECK RESTOCKED!", "https://store.steampowered.com/sale/steamdeckrefurbished")
        
        # SMTP EMAIL FOR STOCK ALERTS 
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("EMAILADDRESS@gmail.com", "GMAIL APP PASSWORD (not your regular login password)")
        message = "REFURBISHED STEAMDECK RESTOCKED! https://store.steampowered.com/sale/steamdeckrefurbished"
        s.sendmail("EMAILADDRESS@gmail.com", "EMAILADDRESS@gmail.com", message)
        s.quit()
        status = 1

    else:
        print(x)
        print(datetime.now())
        status = 0
    return status


def get_my_deck():
    c= 0
    driver = start()
    time.sleep(10) ## DO NOT EDIT
    print("Started Scraper")
    while True:
        try:
            if c<11:
                status = runner(driver)
                if status == 1:
                    break
                time.sleep(300) ## CHECK THE URL EVERY 5MIN (300sec)
                c = c+1
                refresh(driver)
            else:
                print("Rebooting")
                quit(driver)
                time.sleep(20) ## DO NOT EDIT
                c = 0
                driver = start()
        except Exception as e:
            print(e)
            driver.quit()
            time.sleep(20) ## DO NOT EDIT
            get_my_deck()


get_my_deck()

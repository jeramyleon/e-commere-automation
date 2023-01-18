from selenium import webdriver

# initialize webdriver
driver = webdriver.Chrome('C:/bin/chrome-driver3.exe')

# Open URL and maximize window
driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()


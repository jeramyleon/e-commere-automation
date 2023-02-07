import datetime
import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# initialize webdriver
driver = webdriver.Chrome('C:/Users/jeram/Downloads/chromedriver.exe')

# Open URL and maximize window
driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()

# phones button
phones = driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phones.click()

# iphone
iphone = driver.find_element_by_xpath('//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

# first picture
first_pic = driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

# next picture
next_click = driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')
for i in range(5):
    next_click.click()
    time.sleep(2)

# save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')
print(datetime.datetime.now(), ': screenshot')

# close
x_button = driver.find_element_by_xpath('//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

# quantity
quantity = driver.find_element_by_id('input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

# add to cart
add_to_cart = driver.find_element_by_id('button-cart')
add_to_cart.click()
time.sleep(1)

# laptop
laptops = driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver)
action.move_to_element(laptops).perform()
show_all = driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
show_all.click()
time.sleep(1)







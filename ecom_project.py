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

# pick quantity
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

# access all laptops and notebooks section
laptops = driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action = ActionChains(driver) # allows access to mouse control
action.move_to_element(laptops).perform() # mouse hovers over element we want to access
show_all = driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
show_all.click()
time.sleep(1)

# click on HP LP3065 laptop
hp = driver.find_element_by_xpath('//a[text()="HP LP3065"]')
hp.click()

# scroll down
add_to_button2 = driver.find_element_by_xpath('//button[@id="button-cart"]')
add_to_button2.location_once_scrolled_into_view
time.sleep(1)

# select delivery date (December 31st, 2022)
calendar = driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar = driver.find_element_by_xpath('//th[@class="next"]')
month_year = driver.find_element_by_xpath('//th[@class="picker-switch"]')
while month_year.text != 'December 2022':
    next_click_calendar.click()
time.sleep(2)

calendar_date = driver.find_element_by_xpath('//td[text()="31"]')
calendar_date.click()
time.sleep(2)

# add to cart
add_to_button2.click()

# Checkout
go_to_cart = driver.find_element_by_id('cart-total')
go_to_cart.click()
time.sleep(1)

checkout = driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

# Checkout issue, IPhone is not in stock, so we will remove it from cart then resume checkout process
remove_iphone = driver.find_element_by_xpath('//button[@class="btn btn-danger"]')
remove_iphone.click()
time.sleep(1)

checkout = driver.find_element_by_xpath('//a[@class="btn btn-primary"]')
checkout.click()
time.sleep(1)

# Step 1: Checkout Options
guest_checkout = driver.find_element_by_xpath('//input[@value="guest"]')
guest_checkout.click()

continue_button = driver.find_element_by_xpath('//input[@value="Continue"]')
continue_button.click()

# Step 2: Billing Details















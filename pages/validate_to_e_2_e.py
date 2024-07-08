import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from Utilities.generates_logs import LogGen
from test_cases import test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_page:
    # Logger instance for logging information
    logs = LogGen.logger()

    # Locators for different elements on the webpage
    hotel_click_class_name = "menu_Hotels"
    select_city_id = "city"
    send_city_class_name = "[title='Where do you want to stay?']"
    drop_down_city_names_cln = "hw__nearbyTextWrapper font16"
    select_city_from_drop_down_xpath = '//ul[@role="listbox"]//li[1]'
    set_check_in_dates = "div[aria-label='Sun Jul 28 2024']"
    set_check_out_date = "div[aria-label='Wed Jul 31 2024']"
    apply_button_css = "primaryBtn b"
    apply_button = "[data-cy='HotelSearchWidget_310']"
    price_per_night_xpath = "//*[contains(text(),'Price per Night')]"
    select_rent_of_room_xpath = "//li[text()='₹5000+']"
    click_search_btn_id = "hsw_search_button"
    all_hotels_names_id = "hlistpg_hotel_name"
    breckfast_xpath = "//span[text()='Breakfast Included']//ancestor::span/label"
    ratings_xpath = "//span[text()='Very Good: 3.5+']//ancestor::span/label"
    views_select_xpath = "//span[text()='Mountain View']//ancestor::span/label"
    button_book_now_css = "button[class='appBtn filled large bkngOption__cta  ']"
    # Guest details info
    name_id = "fName"
    l_name_id = "lName"
    email_id = "email"
    mobile_no_id = "mNo"
    check_box_css = "span[class='checkboxWpr'] b"
    click_on_pay_now_css = "a[class='btnContinuePayment primaryBtn capText  ']"
    hotel_name_on_pay_page_css = "div h3"
    dates_on_pay_now_page_css = "p[class='prptChk__date']"

    def __init__(self, driver):
        # Constructor to initialize the driver
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_hotels(self):
        # Click on the Hotels menu
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.hotel_click_class_name))).click()
        self.logs.info(f"Element is {self.hotel_click_class_name} and click on Hotel")
    def city_select(self, city):
        # Select a city from the dropdown
        self.driver.find_element(By.ID, self.select_city_id).click()
        self.data = self.driver.find_element(By.CSS_SELECTOR, self.send_city_class_name)
        self.data.send_keys(city)
        time.sleep(2)  # Wait for the dropdown options to load
        self.driver.find_element(By.XPATH, self.select_city_from_drop_down_xpath).click()
        self.logs.info(f"Element is {self.select_city_from_drop_down_xpath}, and its selecting the city")

    def select_check_in_dates(self):
        # Select check-in date
        self.driver.find_element(By.CSS_SELECTOR, self.set_check_in_dates).click()
        self.logs.info(f"Element is {self.set_check_in_dates} and selecting the check in date")

    def select_check_out_date(self):
        # Select check-out date
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.set_check_out_date).click()
        self.logs.info(f"Element is {self.set_check_out_date} and selecting the check out date")

    def click_apply_btn(self):
        # Click the apply button
        self.driver.find_element(By.CSS_SELECTOR, self.apply_button).click()
        self.logs.info(f"Element is {self.apply_button} click on apply")
        time.sleep(2)

    def select_price_per_night(self):
        # Select price per night filter
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, self.price_per_night_xpath))).click()
        self.element = self.driver.find_element(By.XPATH, self.price_per_night_xpath)
        self.driver.execute_script("arguments[0].click();", self.element)
        self.driver.find_element(By.XPATH, self.select_rent_of_room_xpath).click()
        self.logs.info(f"Element is {self.select_rent_of_room_xpath} select the price per night ")
        time.sleep(2)

    def click_on_search_btn(self):
        # Click the search button
        self.driver.find_element(By.ID, self.click_search_btn_id).click()
        self.logs.info(f"Element is {self.click_search_btn_id} click on search button")

    def hotels_names(self):
        # Retrieve and handle hotel names from the search results
        self.driver.implicitly_wait(10)
        self.contains_all_hotels_name = []
        self.hotels = self.driver.find_elements(By.ID, self.all_hotels_names_id)
        for self.hotel in self.hotels:
            time.sleep(1)
            self.contains_all_hotels_name.append(self.hotel.text)
            if self.hotel.text == "Blanket Hotel & Spa Munnar":
                print(self.hotel.text)
                self.hotel.click()
                self.logs.info("click on search button")
                break
            else:
                self.logs.error("Your test case is fail check the screenshot")
                self.driver.save_screenshot(test_data.take_screenshot)

        print(self.contains_all_hotels_name)
        self.logs.info(f"Elements is {self.all_hotels_names_id} all hotels name are in one list and its compare the hotel that which user want")
        time.sleep(2)

    def select_filters(self):
        # Apply various filters for the hotel search
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.breckfast_xpath).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.ratings_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.views_select_xpath).click()
        time.sleep(3)
        self.logs.info(f"Element is {self.views_select_xpath} applied the filters")

    def handle_windows(self):
        # Handle multiple browser windows
        time.sleep(4)
        self.windows = self.driver.window_handles
        print(self.windows)
        self.driver.switch_to.window(self.windows[1])
        if self.driver.title == "Blanket Hotel & Spa Munnar | Hotel Details Page | MakeMyTrip.co":
            self.logs.info("Title is match")
        else:
            self.logs.error("Title is not match")
        self.logs.info("Switching the windows")

    def book_now_button(self):
        # Click the Book Now button
        self.driver.find_element(By.CSS_SELECTOR, self.button_book_now_css).click()
        self.logs.info(f"Element is {self.button_book_now_css} click on book now button")

    def enter_guest_details(self, name, l_name, email, mobile_no):
        # Enter guest details for booking
        self.wait.until(EC.visibility_of_element_located((By.ID, self.name_id))).send_keys(name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.l_name_id))).send_keys(l_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.email_id))).send_keys(email)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.mobile_no_id))).send_keys(mobile_no)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.check_box_css))).click()
        self.logs.info("Enter the guest user details name, last name, email and mobile number")

    def pay_now(self):
        # Click the Pay Now button
        self.driver.find_element(By.CSS_SELECTOR, self.click_on_pay_now_css).click()
        self.logs.info(f"Element is {self.click_on_pay_now_css} and click on pay now button")

    def compare_dates(self):
        # Compare dates on the pay now page
        self.all_date = []
        self.dates = self.driver.find_elements(By.CSS_SELECTOR, self.dates_on_pay_now_page_css)
        for self.date in self.dates:
            print(self.date.text)
            self.all_date.append(self.date.text)

        self.logs.info(f"Element is {self.dates_on_pay_now_page_css} and its hold the dates on pay now page")

import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By


class Home_page:

    hotel_click_class_name = "menu_Hotels"
    select_city_id = "city"
    send_city_class_name = "[title='Where do you want to stay?']"
    drop_down_city_names_cln = "hw__nearbyTextWrapper font16"
    select_city_from_drop_down_xpath = '//ul[@role="listbox"]//li[1]'
    set_check_in_dates = "div[aria-label='Sun Jul 28 2024']"
    set_check_out_date = "div[aria-label='Wed Jul 31 2024']"
    apply_button_css = "primaryBtn b"
    price_per_night_xpath = "//span[text()='Price per Night']"
    select_rent_of_room_xpath = "//li[text()='₹5000+']"
    click_search_btn_id = "hsw_search_button"
    all_hotels_names_id = "hlistpg_hotel_name"
    breckfast_xpath = "//span[text()='Breakfast Included']//ancestor::span/label"
    ratings_xpath = "//span[text()='Very Good: 3.5+']//ancestor::span/label"
    views_select_xpath = "//span[text()='Mountain View']//ancestor::span/label"
    button_book_now_css = "button[class='appBtn filled large bkngOption__cta  ']"
    #guest details info
    name_id = "fName"
    l_name_id= "lName"
    email_id = "email"
    mobile_no_id= "mNo"
    check_box_css = "span[class='checkboxWpr'] b"
    click_on_pay_now_css = "a[class='btnContinuePayment primaryBtn capText  ']"
    hotel_name_on_pay_page_css = "div h3"



    def __init__(self, driver):
        self.driver = driver


    def click_hotels(self):
        self.driver.find_element(By.CLASS_NAME, self.hotel_click_class_name).click()

    def city_select(self, city):
        self.driver.find_element(By.ID, self.select_city_id).click()
        self.data = self.driver.find_element(By.CSS_SELECTOR, self.send_city_class_name)
        self.data.send_keys(city)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_city_from_drop_down_xpath).click()


    def select_check_in_dates(self):
        self.driver.find_element(By.CSS_SELECTOR, self.set_check_in_dates).click()


    def select_check_out_date(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.set_check_out_date).click()


    def click_apply_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-cy='HotelSearchWidget_310']").click()
        time.sleep(2)

    def select_price_per_night(self):
        self.driver.find_element(By.XPATH, self.price_per_night_xpath).click()
        self.driver.find_element(By.XPATH, self.select_rent_of_room_xpath).click()
        time.sleep(2)

    def click_on_search_btn(self):
        self.driver.find_element(By.ID,  self.click_search_btn_id).click()

    def hotels_names(self):
        self.contains_all_hotesl_name = []
        self.hotels = self.driver.find_elements(By.ID, self.all_hotels_names_id)
        for self.hotel in self.hotels:
            time.sleep(2)
            self.contains_all_hotesl_name.append(self.hotel.text)
            if self.hotel.text == "Blanket Hotel & Spa Munnar":
                self.hotel.click()
        print(self.contains_all_hotesl_name)

    def select_fileters(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,  self.breckfast_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.ratings_xpath).click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, self.views_select_xpath).click()
        time.sleep(2)

    def handle_windows(self):
        self.windows = self.driver.window_handles
        self.driver.switch_to.window(self.windows[1])
        print(self.driver.title)

    def book_now_button(self):
        self.driver.find_element(By.CSS_SELECTOR,  self.button_book_now_css).click()
        time.sleep(2)

    def enter_guest_details(self):
        self.driver.find_element(By.ID,self.name_id).send_keys("Piyush")
        self.driver.find_element(By.ID, self.l_name_id).send_keys("dravyakar")
        self.driver.find_element(By.ID, self.email_id).send_keys("dravyakar@gmail.com")
        self.driver.find_element(By.ID, self.mobile_no_id).send_keys("8411878794")
        self.driver.find_element(By.CSS_SELECTOR, self.check_box_css).click()


    def pay_now(self):
        self.driver.find_element(By.CSS_SELECTOR ,self.click_on_pay_now_css).click()

    def compare_dates(self):
        self.all_date = []
        self.dates = self.driver.find_elements(By.CSS_SELECTOR, "p[class='prptChk__date']")
        for self.date in self.dates:
            print(self.date.text)
            self.all_date.append(self.date.text)


















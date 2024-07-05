import time

from selenium.webdriver.common.by import By

from pages.select_date_city_home_page import Home_page


class Test_home_page:
    city_class = "hsw_inputField font16"

    def test_select_date_city(self,setup):
        self.driver = setup
        self.home_page = Home_page(self.driver)
        self.home_page.click_hotels()
        self.home_page.city_select("Munnar")
        self.home_page.select_check_in_dates()
        self.home_page.select_check_out_date()
        self.home_page.select_price_per_night()
        self.home_page.click_on_search_btn()
        time.sleep(3)
        self.home_page.select_fileters()
        self.home_page.hotels_names()
        self.home_page.handle_windows()
        self.home_page.book_now_button()
        self.home_page.enter_guest_details()
        self.home_page.pay_now()
        self.home_page.compare_dates()
        self.hotel_name = self.driver.find_element(By.CSS_SELECTOR,self.home_page.hotel_name_on_pay_page_css)
        assert self.hotel_name.text == "Blanket Hotel & Spa Munnar"
        assert self.home_page.all_date in ["Sun Jul 28 2024", "Wed Jul 31 2024"], "Dates are not match"









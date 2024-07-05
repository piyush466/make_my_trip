# Import the necessary modules and classes
# import time
import time

from selenium.webdriver.common.by import By
from test_cases import test_data
from Utilities.generates_logs import LogGen
from pages.select_date_city_home_page import Home_page


class Test_home_page:
    city_class = "hsw_inputField font16"
    logs = LogGen.logger()

    def test_select_date_city(self, setup):
        # Initialize the driver and home page object
        self.driver = setup
        self.home_page = Home_page(self.driver)

        # Click on the hotels tab
        self.home_page.click_hotels()
        # Select the city
        self.home_page.city_select(test_data.city)

        # Select check-in dates
        self.home_page.select_check_in_dates()

        # Select check-out dates
        self.home_page.select_check_out_date()

        # Select price per night filter
        self.home_page.select_price_per_night()

        # Click on the search button
        self.home_page.click_on_search_btn()

        # Wait for 3 seconds to load the search results
        time.sleep(3)

        # Select filters for the hotels
        self.home_page.select_fileters()

        # Get the list of hotel names
        self.home_page.hotels_names()

        # Handle new windows if any are opened
        self.home_page.handle_windows()

        # Click on the 'Book Now' button for the selected hotel
        self.home_page.book_now_button()

        # Enter guest details
        self.home_page.enter_guest_details(test_data.name, test_data.l_name, test_data.email, test_data.mobile_no)

        # Click on the 'Pay Now' button
        self.home_page.pay_now()

        # Compare check-in and check-out dates
        self.home_page.compare_dates()

        # Log that the assertion is starting
        self.logs.info("********Assertion Started******")

        # Find the hotel name element on the payment page
        self.hotel_name = self.driver.find_element(By.CSS_SELECTOR, self.home_page.hotel_name_on_pay_page_css)

        # Assert that the hotel name is correct

        assert self.hotel_name.text == "Blanket Hotel & Spa Munnar"

        assert self.home_page.all_date == ['Sun 28 Jul 2024', 'Wed 31 Jul 2024'], "Dates do not match"

import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage


import main


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_choose_comfort_option(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_button_order_a_taxi()
        routes_page.click_on_confort_price_option()
        comfort_rate = routes_page.get_comfort_price_option().text
        confort_text = "Comfort"
        assert comfort_rate in confort_text


    def test_fill_phone_number(self):
        self.test_choose_comfort_option()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_button()
        routes_page.set_field_phone_number(data.phone_number)
        assert data.phone_number == routes_page.get_field_phone_number().get_attribute("value")
        routes_page.click_next_button_popup()
        confirmation_code = main.retrieve_phone_code(self.driver)
        routes_page.set_field_confirmation_code(confirmation_code)
        assert confirmation_code == routes_page.get_field_confirmation_code().get_attribute("value")
        routes_page.click_on_submit_button()

    def test_payment_method(self):
        self.test_fill_phone_number()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_on_checkout_button()
        routes_pages.click_on_add_credit_card_button()
        routes_pages.set_credit_card_number_field(data.card_number)
        assert  data.card_number == routes_pages.get_credit_card_number_field().get_attribute("value")
        routes_pages.set_cvv_code_field(data.card_code)
        assert data.card_code == routes_pages.get_cvv_code_field().get_attribute("value")
        routes_pages.get_cvv_code_field().send_keys(Keys.TAB)
        routes_pages.click_on_add_button()
        routes_pages.click_on_credit_card_window()

    def test_message_for_driver(self):
        self.test_payment_method()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.get_message_for_driver()
        routes_pages.set_message_for_driver(data.message_for_driver)
        assert data.message_for_driver == routes_pages.get_message_for_driver().get_attribute("value")

    def test_choose_blanket_and_tissue(self):
        self.test_message_for_driver()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_on_choose_blanket_and_tissue()


    def test_order_ice_cream(self):
        self.test_choose_blanket_and_tissue()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_on_order_ice_cream()
        routes_pages.click_on_order_ice_cream()

    def test_taxi_request(self):
        self.test_order_ice_cream()
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.click_on_taxi_request()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
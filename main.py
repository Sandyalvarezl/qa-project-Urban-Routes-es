import data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import main


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_order_a_taxi = (By.CSS_SELECTOR, ".button.round")
    comfort_price_option =  (By.XPATH, "//div[@class='tcard-title' and text() = 'Comfort']")
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    field_phone_number = (By.ID, "phone")
    next_button_popup = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]/form/div[2]/button")
    field_confirmation_code = (By.ID, "code")
    submit_button = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]")
    checkout_button = (By.CLASS_NAME, 'pp-text')
    add_credit_card_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]")
    Credit_card_number_field = (By.ID, "number")
    cvv_code_field = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input")
    add_button = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/form/div[3]/button[1]")
    close_credit_card_window = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
    message_for_driver = (By.ID, "comment")
    choose_blanket_and_tissue = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    order_ice_cream = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")
    taxi_request = (By.ID, "gtx-trans")






    #close_phone_number_popup = (By.CLASS_NAME, "")

    def __init__(self, driver):
        self.driver = driver

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.from_field).send_keys(to_address)
        WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_button_order_a_taxi (self):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(self.button_order_a_taxi))

    def click_on_button_order_a_taxi(self):
        self.get_button_order_a_taxi().click()

    def get_comfort_price_option(self):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(self.comfort_price_option))

    def click_on_confort_price_option(self):
        self.get_comfort_price_option().click()

    def get_field_phone_number(self):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(self.field_phone_number))

    def set_field_phone_number(self, phone_number):
        self.get_field_phone_number().send_keys(phone_number)

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.phone_number_button)
        )
    def click_phone_number_button(self):
        self.get_phone_number_button().click()
   # def click_on_field_phone_number(self):
        #self.get_field_phone_number().click()

    def get_next_button_popup (self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.next_button_popup)
        )

    def click_next_button_popup(self):
        self.get_next_button_popup().click()

    def get_field_confirmation_code(self):
        return WebDriverWait(self.driver, 7). until(
            EC.element_to_be_clickable(self.field_confirmation_code)
        )
    def set_field_confirmation_code(self, code):
        self.get_field_confirmation_code().send_keys(code)

    def get_submit_button(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.submit_button)
        )
    def click_on_submit_button(self):
        self.get_submit_button().click()


    def get_checkout_button(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.checkout_button)
        )

    def click_on_checkout_button(self):
        self.get_checkout_button().click()


    def  get_add_credit_card_button(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.add_credit_card_button)
        )

    def click_on_add_credit_card_button(self):
        self.get_add_credit_card_button().click()


    def get_credit_card_number_field(self):
        return WebDriverWait(self.driver,7).until(
            EC.element_to_be_clickable(self.Credit_card_number_field)
        )

    def set_credit_card_number_field(self, credit_card):
        self.get_credit_card_number_field().send_keys(credit_card)

    def get_cvv_code_field(self):
        return WebDriverWait(self.driver,7).until(
            EC.element_to_be_clickable(self.cvv_code_field)
        )

    def set_cvv_code_field(self, cvv_code):
        self.get_cvv_code_field().send_keys(cvv_code)


    def get_add_button(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_on_add_button(self):
        self.get_add_button().click()

    def get_close_credit_card_window(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.close_credit_card_window)
        )

    def click_on_credit_card_window(self):
        self.get_close_credit_card_window().click()


    def get_message_for_driver(self):
        return WebDriverWait(self.driver, 7).until(
            EC.visibility_of_element_located(self.message_for_driver)
        )

    def set_message_for_driver(self, message):
        self.get_message_for_driver().send_keys(message)

    def get_choose_blanket_and_tissue(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.choose_blanket_and_tissue)
        )

    def click_on_choose_blanket_and_tissue(self):
        self.get_choose_blanket_and_tissue().click()

    def get_order_ice_cream(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.order_ice_cream)
        )

    def click_on_order_ice_cream(self):
        self.get_order_ice_cream().click()


    def get_taxi_request(self):
        return WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.order_ice_cream)
        )

    def click_on_taxi_request(self):
        self.get_taxi_request().click()


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

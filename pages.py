
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
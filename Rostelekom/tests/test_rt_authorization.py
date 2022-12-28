from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from tests_data import Valid_Data
from tests_data import Invalid_Data
from tests.locators import RTPanelNaviBar
from tests.locators import RTAutorizationLocators
from tests.locators import RTAutorizationAllerts
from tests.locators import RTRegistrationLocators
import allure

fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()

@allure.story('Тесты Авторизации на RT')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('F:/chromebdriver/chromedriver.exe')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()


# TC-RT-011 Проверка кликабельности кнопок формы регистрации по вариантам авторизации и изменение полей для ввода
    @allure.feature('Проверка кликабельности кнопок выбора типа авторизации')
    def clicable_navi_bar_test(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_LS))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_LS)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_MAIL))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_MAIL)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_LOGIN))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_LOGIN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RTPanelNaviBar.LOCATOR_NAVI_BAR_TELEPHONE))).click()
        assert self.driver.find_element(By.XPATH, RTPanelNaviBar.LOCATOR_FORM_TELEPHONE)

# TC-RT-012 Осуществление авторизации пользователя кнопкой "Почта" по электронной почте(некорректный адрес почты)
    @allure.feature('Авторизация с не корректным Email')
    def autorization_invalid_email_test(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# TC-RT-013 Осуществление авторизации пользователя кнопкой "Номер" по номеру телефона (некорректный номер телефона)
    @allure.feature('Авторизация с некорректным номером телефона')
    def autorization_invalid_phoneNumber_test(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.invalid_phoneNumber)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# TC-RT-014 Осуществление авторизации пользователя кнопкой "Номер" по номеру телефона при некорректном пароле
    @allure.feature('Авторизация с некорректным паролем')
    def autorization_invalid_password_test(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Valid_Data.valid_phoneNumber)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR)
        assert self.driver.find_element(By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_INVALID_EMAIL)

# TC-RT-015 Осуществление авторизации пользователя кнопкой "Логин" по логину (уязвимость XSS)
    @allure.feature('Авторизация с XSS')
    def autorization_xss_in_login_test(self):
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_USER).send_keys(
            Invalid_Data.xss)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTAutorizationLocators.LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN).click()
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, RTAutorizationAllerts.LOCATOR_ERROR_TEXT_XSS)))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from tests_data import Valid_Data
from tests_data import Invalid_Data
from tests.locators import RTRegistrationLocators
from tests.locators import RTRegistrationsAllerts
import allure


fake_name = Faker().name()
fake_email = Faker().email()
fake_password = Faker().password()

@allure.story('TP-6645 / Тесты Регистрации на RT')
class TestValidRegistrationRT:

    def setup(self):
        self.open()

    def open(self):
        self.driver = webdriver.Chrome('/Users/dmitrijparsin/webdriver/chromedriver_107')
        self.driver.get("https://b2c.passport.rt.ru")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER)))
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_REGISTER).click()


    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

# это база
    def eto_baza_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_ENTER_CODE)

# TC-RT-001 Регистрация пользователя по электронной почте(пароль длинной в 21 символ)
    @allure.feature('Регистрация с паролем из 21 символа')
    def registration_user_with_pass_21char_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_21_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-002 Регистрация пользователя по номеру телефона (поле "email" заполнено без домена)
    @allure.feature('Регистрация с Email без домена')
    def registration_user_with_email_without_domain_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.email_without_domain)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-003 Регистрация пользователя по номеру телефона (поле "Имя" содержить 31 символ)
    @allure.feature('Регистрация с именем из 31 символа')
    def registration_user_with_firstname_31char_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Invalid_Data.first_name_31_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-004 Регистрация пользователя по номеру телефона (поле "Имя" содержить 1 символ)
    @allure.feature('Регистрация с именем из 1 символа')
    def registration_user_with_firstname_1char_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Invalid_Data.first_name_1_char)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-005 Регистрация пользователя по номеру телефона (обязательное поле "email или мобильный телефон" не заполнено)
    @allure.feature('Регистрация с незаполненным обязательным полем Email или Телефон')
    def registration_user_with_not_filled_email_or_mobile_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-006 Регистрация пользователя по номеру телефона (обязательное поле "Фамилия" не заполнено)
    @allure.feature('Регистрация с незаполненным обязательным полем Фамилия')
    def registration_user_with_not_filled_lastname_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-007 Регистрация пользователя по номеру телефона (обязательное поле "Имя" не заполнено)
    @allure.feature('Регистрация с незаполненным обязательным полем Имя')
    def registration_user_with_not_filled_firstname_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-008 Регистрация пользователя по номеру телефона
    # (все обязательные поля заполнены. Поле "Пароль" и поле "Подтверждение пароля имеют разные значения)
    @allure.feature('Регистрация с несовпадающими паролями')
    def registration_user_with_non_matching_passwords_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Valid_Data.valid_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-009 Регистрация пользователя по номеру телефона
    # (все обязательные поля заполнены. Поле "Пароль" и поле "Подтверждение пароля" не содержит
    # обязательный элемент цифру или спецсимвол)
    @allure.feature('Регистрация с паролем не содержащем цифру')
    def registration_user_with_password_not_contain_digit_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Valid_Data.valid_last_name)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.password_not_contain_digit)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)

# TC-RT-010 Регистрация пользователя по номеру телефона (поле "Фамилия" содержит 31 символ)
    @allure.feature('Регистрация с фамилией из 31 символа')
    def registration_user_with_lastname_31char_test(self):
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_FIRSTNAME).send_keys(
            Valid_Data.valid_first_name)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_LASTNAME).send_keys(
            Invalid_Data.last_name_31_char)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL).send_keys(
            Invalid_Data.fake_email)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.ID, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM).send_keys(
            Invalid_Data.fake_password)
        self.driver.find_element(By.XPATH, RTRegistrationLocators.LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, RTRegistrationsAllerts.LOCATOR_RT_REGISTRATION_ALLERTS_ERROR)
from faker import Faker

class Valid_Data:
    valid_first_name = 'Иван'
    valid_last_name = 'Иванов'
    valid_password = 'Olga2660038'
    valid_phoneNumber = '+79157200039'

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'И'
    first_name_31_char = 'Иванвававававававававававававав'
    last_name_1_char = 'И'
    last_name_31_char = 'Ивановвапровлстипрянаыларвеупфы'
    password_21_char = 'Qazwsxedcrfvtgbyhnujm0'
    password_no_Lower = 'qwertyu0'
    password_9_char = 'Qwertyu0p'
    password_not_contain_digit = "Qwertyui"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'test_rt@.ru'
    invalid_phoneNumber = '+79999999999'

#Запуск теста: python -m pytest -v --driver Chrome --driver-path F:/chromedriver/chromedriver.exe
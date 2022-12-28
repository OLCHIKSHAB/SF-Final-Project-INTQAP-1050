class RTAutorizationLocators():
    LOCATOR_RT_AUTORIZATION_USER = 'username'
    LOCATOR_RT_AUTORIZATION_PASSWORD = "password"
    LOCATOR_RT_AUTORIZATION_BUTTON_LOGIN = "kc-login"
    LOCATOR_RT_AUTORIZATION_BUTTON_REGISTER = "kc-register"

class RTRegistrationLocators:
    LOCATOR_RT_REGISTRATION_BUTTON_REGISTER = "kc-register"
    LOCATOR_RT_REGISTRATION_FIRSTNAME = "//input[@name='firstName']"
    LOCATOR_RT_REGISTRATION_LASTNAME = "//input[@name='lastName']"
    LOCATOR_RT_REGISTRATION_NUMBER_OR_EMAIL = "address"
    LOCATOR_RT_REGISTRATION_PASSWORD = "password"
    LOCATOR_RT_REGISTRATION_PASSWORD_CONFIRM = "password-confirm"
    LOCATOR_RT_REGISTRATION_BUTTON_SUBMIT = "//button[@type='submit']"
    LOCATOR_RT_REGISTRATION_ENTER_CODE = "rt-code-1"

class RTRegistrationsAllerts:
    LOCATOR_RT_REGISTRATION_ALLERTS_ERROR = "//span[@class='rt-input-container__meta rt-input-container__meta--error']"

class RTPanelNaviBar:
    LOCATOR_NAVI_BAR_TELEPHONE = '//*[@id="t-btn-tab-phone"]'
    LOCATOR_FORM_TELEPHONE = "//span[contains(text(), 'Мобильный телефон')]"
    LOCATOR_NAVI_BAR_MAIL = '//*[@id="t-btn-tab-mail"]'
    LOCATOR_FORM_MAIL = "//span[contains(text(), 'Электронная почта')]"
    LOCATOR_NAVI_BAR_LOGIN = '//*[@id="t-btn-tab-login"]'
    LOCATOR_FORM_LOGIN = "//span[contains(text(), 'Логин')]"
    LOCATOR_NAVI_BAR_LS = '//*[@id="t-btn-tab-ls"]'
    LOCATOR_FORM_LS = "//span[contains(text(), 'Лицевой счёт')]"

class RTAutorizationAllerts:
    LOCATOR_RT_AUTORIZATION_ALLERTS_ERROR = '//*[@id="form-error-message"]'
    LOCATOR_ERROR_TEXT_INVALID_EMAIL = "//span[contains(text(), 'Неверный логин или пароль')]"
    LOCATOR_ERROR_TEXT_XSS = "//h2[contains(text(), 'Ваш запрос был отклонен из соображений безопасности.')]"
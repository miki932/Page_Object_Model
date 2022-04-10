from selenium.webdriver.common.by import By


class LoginLocators:
    # Object Repository:
    LOGIN_PAGE_TITLE = "Swag Labs"
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    INVALID_PASSWORD = "12345"
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "//*[@id='login_button_container']")

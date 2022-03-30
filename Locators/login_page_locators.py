from selenium.webdriver.common.by import By


class Login_Locators:
    # Object Repository:
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.ID, "//*[@id='login_button_container']")

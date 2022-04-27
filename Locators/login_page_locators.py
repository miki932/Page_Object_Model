from selenium.webdriver.common.by import By


class LoginLocators:
    # Object Repository:
    LOGIN_PAGE_TITLE = "Swag Labs"
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")

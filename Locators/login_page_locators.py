from selenium.webdriver.common.by import By


class LoginLocators:
    # Object Repository:
    LOGIN_PAGE_TITLE = "Swag Labs"
    EMAIL = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOCKED_OUT_ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    BAD_PASSWORD_OR_USERNAME_ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

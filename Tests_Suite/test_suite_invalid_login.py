import pytest
from Tests.test_login_page import TestLogin


@pytest.mark.qase_case_id("CASE_ID")
def invalid_login(init_driver):
    test_login = TestLogin(init_driver)
    test_login.test_invalid_login()

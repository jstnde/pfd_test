from seleniumbase import BaseCase
from datetime import datetime


class LoginPage(BaseCase):
    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "custom_screenshots/" + \
                            datetime.now().strftime(datetime_format) + \
                            "/login_page"

    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    submit_btn = "//input[@type='submit' and @value='Submit']"

    input_value_invalid_username = "ProductManager123"
    error_text = "User does not exist!"
    error_span = "/html/body/div/main/form/span"
    error_expected_style = "color: red;"

    def open_page(self):
        self.open("https://localhost:44323")

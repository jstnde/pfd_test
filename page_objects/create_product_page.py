from seleniumbase import BaseCase
from datetime import datetime


class CreateProductPage(BaseCase):
    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "custom_screenshots/" + \
                            datetime.now().strftime(datetime_format) + \
                            "/create_product_page"

    input_field_username = "input#uname"
    input_field_password = "input#upass"
    input_value_username = "ProductManager"
    input_value_password = "passProduct"
    submit_btn = "//input[@type='submit']"
    a_create = "Create Product"

    product_file_path = "./data/logo.jpg"
    input_field_file = "#filetoupload"
    input_field_title = "#ProductTitle"
    input_value_title = "Bottom Baggy Jeans"
    input_field_price = "#price"
    input_value_price = "59.99"
    expected_page_title = "View Products"
    page_title = ".PageTitle"

    input_value_invalid_price = "1000.00"

    def open_page(self):
        self.open("https://localhost:44323")

    def login(self):
        self.open_page()
        self.send_keys(self.input_field_username, self.input_value_username)
        self.send_keys(self.input_field_password, self.input_value_password)
        self.click(self.submit_btn)

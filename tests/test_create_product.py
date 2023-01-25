from page_objects.create_product_page import CreateProductPage


class CreateProductTest(CreateProductPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.login()

        self.save_screenshot("products_page",
                             CreateProductPage.custom_screenshot_dir)

        self.click_link(CreateProductPage.a_create)

        self.save_screenshot("create_product_page",
                             CreateProductPage.custom_screenshot_dir)

    # Test Case 3 : Create Product
    def test_create_product(self):
        print("Test Case 3 : Create Product")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Image Uploaded")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input test title value : '" + CreateProductPage.input_value_username + "'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("3. Input test price value : '$" + CreateProductPage.input_value_price + "'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("filled_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        self.click(CreateProductPage.submit_btn)

        print("4. Press submit button")

        self.scroll_to_bottom()
        self.save_screenshot("updated_products_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_create_product")

        self.assert_text(CreateProductPage.expected_page_title, CreateProductPage.page_title)

        print("User redirected to Products page")

        self.assert_true(self.is_text_visible(CreateProductPage.input_value_title))

        print("Product created and shown in Products page")
        print("Test is Successful")

    # Test Case 4 : Image Upload Validation
    def test_image_validation(self):
        print("Test Case 4 : Image Upload Validation")
        print("1. Image Not Uploaded")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input test title : '" + CreateProductPage.input_value_title + "'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("3. Input test price value : '$" + CreateProductPage.input_value_price + "'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_image_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_image_validation")

        self.click(CreateProductPage.submit_btn)

        print("4. Click Submit Button")

        self.save_screenshot("error_image_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_image_validation")

        self.assert_title_contains("Create")

        print("Product not created")
        print("Test is Successful")

    # Test Case 5 : Title Field Validation
    def test_title_validation(self):
        print("Test Case 5 : Title Field Validation")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Image Uploaded")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_price)

        print("2. Input test price value : '$" + CreateProductPage.input_value_price + "'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("empty_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        self.click(CreateProductPage.submit_btn)

        print("3. Click Submit Button")

        self.save_screenshot("error_title_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_title_validation")

        self.assert_title_contains("Create")

        print("Product not created")
        print("Test is Successful")

    # Test Case 6 : Price Field Range Validation
    def test_price_validation(self):
        print("Test Case 6 : Price Field Range Validation")
        self.choose_file(CreateProductPage.input_field_file, CreateProductPage.product_file_path)

        print("1. Image Uploaded")

        self.type(CreateProductPage.input_field_title, CreateProductPage.input_value_title)

        print("2. Input Test Title : '" + CreateProductPage.input_value_title + "'")

        self.type(CreateProductPage.input_field_price, CreateProductPage.input_value_invalid_price)

        print("3. Input test price value : '$" + CreateProductPage.input_value_invalid_price + "'")

        self.scroll_to(CreateProductPage.input_field_price)
        self.save_screenshot("invalid_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        self.click(CreateProductPage.submit_btn)

        print("4. Click Submit Button")

        self.save_screenshot("error_price_create_product_page",
                             CreateProductPage.custom_screenshot_dir +
                             "/test_price_validation")

        self.assert_title_contains("Create")

        print("Product not created")
        print("Test is Successful")

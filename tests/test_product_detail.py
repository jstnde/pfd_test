from page_objects.product_detail_page import ProductDetailPage


class ProductDetailTest(ProductDetailPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()

        self.open_page()

    # Test Case 7 : Edit Product
    def test_edit_product(self):
        print("Test case 7 : Edit Product")
        self.click(ProductDetailPage.product_desc)
        self.save_screenshot("before_product_edited",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_edit_product")
        print("1. Clicks into product : 'TOP WITH ASYMMETRIC HEM'")
        self.click_link(ProductDetailPage.a_update)
        print("2. Click into the Update button in Product Details page")
        self.clear(ProductDetailPage.title_field)
        self.type(ProductDetailPage.title_field, ProductDetailPage.title_value)
        print("3. Input New title : 'Bottom Baggy Beans'")
        self.clear(ProductDetailPage.price_field)
        self.type(ProductDetailPage.price_field, ProductDetailPage.price_value)
        print("4. Input New Price : '420.00'")
        self.click(ProductDetailPage.submit_btn)
        print("5. Click Submit")
        self.open_page()
        self.click(ProductDetailPage.newlyupdated_product)
        self.save_screenshot("after_product_edited",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_edit_product")

        self.assert_text(ProductDetailPage.title_value, ProductDetailPage.title_field)
        print("Product Title value has been changed")
        self.assert_text(ProductDetailPage.price_value, ProductDetailPage.price_field)
        print("Price Value has been changed")
        print("Test is Successful")

        # changing back the test case to original
        self.click_link(ProductDetailPage.a_update)
        self.clear(ProductDetailPage.title_field)
        self.type(ProductDetailPage.title_field, "TOP WITH ASYMMETRIC HEM")
        self.type(ProductDetailPage.price_field, "79.90")
        self.click(ProductDetailPage.submit_btn)
    # Test Case 8 : Uneditable ID Validation
    def test_id_validation(self):
        print("Test case 8 : Uneditable ID Validation")
        self.click(ProductDetailPage.product_desc2)
        self.save_screenshot("before_id_edited",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_id_validation")
        print("1. Clicks into product : 'Bottom Baggy Jeans'")
        self.click_link(ProductDetailPage.a_update)
        print("2. Click update in product details")
        self.type(ProductDetailPage.id_field, ProductDetailPage.id_value)
        print("3. Input new ID : '11'")
        self.click(ProductDetailPage.submit_btn)
        print("4. Click Submit")
        self.open_page()
        self.click(ProductDetailPage.product_desc2)
        self.save_screenshot("tests_test_create_product.py__CreateProductTest__test_image_validation_1_0.png",
                             "assets")
        self.assert_text(ProductDetailPage.correct_id, ProductDetailPage.id_field)
        print("Product ID unable to change")
        print("Test successful")

    # Test Case 9 : Uneditable Date Validation
    def test_date_validation(self):
        print("Test Case 9 : Uneditable Date Validation")
        self.click(ProductDetailPage.product_desc3)
        self.save_screenshot("before_date_edited",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_date_validation")
        print("1. Clicks into product : 'BLAZER WITH ROLL-UP CUFFS'")
        self.click_link(ProductDetailPage.a_update)
        self.type(ProductDetailPage.effective_field, ProductDetailPage.newdateval)
        print("2. Input New date value : '2022-03-02'")
        self.click(ProductDetailPage.submit_btn)
        print("3. Click Submit")
        self.open_page()
        self.click(ProductDetailPage.product_desc3)
        print("4. Checks if date has changed")
        self.assert_text(ProductDetailPage.effective_value, ProductDetailPage.effective_field2)
        print("Product Date unabled to change")
        print("Test Successful")

    # Test Case 10 : Obsolete Button
    def test_obsolete_button(self):
        print("Test Case 10 : Obsolete Button")
        self.click(ProductDetailPage.product_desc4)
        self.save_screenshot("before_obsolete_button",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_obsolete_button")
        print("1. Clicks into Product : 'NEON JACKET'")
        self.add_js_code(ProductDetailPage.js_footer_hide)

        self.click(ProductDetailPage.obsolete_btn)
        print("2. Clicks Obsolete button")
        self.open_page()
        self.click(ProductDetailPage.product_desc4)
        self.save_screenshot("after_obsolete_button",
                             ProductDetailPage.custom_screenshot_dir +
                             "/test_obsolete_button")
        self.assert_attribute(ProductDetailPage.effective_field2, "style", ProductDetailPage.expected_style)
        print("Styling for the Date has changed from Red to Green")
        print("Test is Successful")
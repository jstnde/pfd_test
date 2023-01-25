from seleniumbase import BaseCase
from datetime import datetime


class ProductDetailPage(BaseCase):
    datetime_format = "%d%m%Y"
    custom_screenshot_dir = "custom_screenshots/" + \
                            datetime.now().strftime(datetime_format) + \
                            "/product_detail_page"




    submit_btn = "//input[@type='submit']"
    a_update = "Update Details"
    title_field = "#ProductTitle"
    title_value = "Bottom Baggy Beans"
    price_field = "#Price"
    price_value = 420

    id_field = "#ProductId"
    id_value = "11"
    correct_id = "10"

    effective_value = "2022-04-01"
    newdateval = "2022-03-02"
    product_desc = ".gallery:contains('TOP WITH ASYMMETRIC HEM')"
    newlyupdated_product = ".gallery:contains('Bottom Baggy Beans')"
    product_desc2 = ".gallery:contains('Bottom Baggy Jeans')"
    product_desc3 = ".gallery:contains('BLAZER WITH ROLL-UP CUFFS')"
    product_desc4 = ".gallery:contains('NEON JACKET')"
    js_footer_hide = "document.getElementsByClassName('container')[2].hidden = true"
    obsolete_btn = "//input[@value='Obsolete' and @class= 'btn btn-primary']"
    effective_field = "#EffectiveDate"
    effective_field2 = "#date"
    expected_style = "background-color: red; color: white;"


    def open_page(self):
        self.get("https://localhost:44323/Product")



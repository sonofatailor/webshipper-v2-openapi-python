# coding: utf-8

"""
    Webshipper V2 REST API

       <p>     The Webshipper API is a RESTful JSON API that gives full control over your Webshipper account. The API is scoped to your <em>account name</em>,     and is accessed via the endpoint <em>https://&lt;account name&gt;.api.webshipper.io/v2/</em>. Your <em>account name</em> is the same as you see when you access the Webshipper web UI     at <em>https://&lt;account name&gt;.webshipper.io</em>.   </p>    <p>     This API conforms to the <a href=\"http://jsonapi.org/\">JSON API standard</a> with the following conventions:     <ul>       <li>Resources are identified with the attribute <code>id</code>, which is a server-side generated sequential integer</li>       <li>Resource types are pluralised and underscored, like <code>order_lines</code></li>       <li>The API has a fixed page limit of 30 records. To fetch more records use the query parameter <code>page[number]</code></li>       <li>All resources have the attributes <code>created_at</code> and <code>updated_at</code> which are ISO 8601 timestamps like <code>2018-03-07T14:01:18.000Z</code> </li>       <li>All country codes are <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes</li>     </ul>   </p>     <p> It is also possible to download the documentation in the OpenAPI 3.0 <a href=\"?download_openapi=1\">here</a> </p>    <div class=\"alert alert-info\">     <i class=\"fa fa-info mr-2\"></i>     Webshipper <em>strongly</em> recommends using a client library for utilising this API. Refer to jsonapi.org's list of     <a href=\"http://jsonapi.org/implementations/#client-libraries\">jsonapi.org's list of client libraries</a> to find one for your language.   </div> 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from webshipperv2.models.orders_get200_response import OrdersGet200Response

class TestOrdersGet200Response(unittest.TestCase):
    """OrdersGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrdersGet200Response:
        """Test OrdersGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrdersGet200Response`
        """
        model = OrdersGet200Response()
        if include_optional:
            return OrdersGet200Response(
                data = [
                    webshipperv2.models._orders_get_200_response_data_inner._orders_get_200_response_data_inner(
                        attributes = webshipperv2.models.orders.orders(
                            order_channel_id = 56, 
                            status = '', 
                            ext_ref = '', 
                            visible_ref = '', 
                            drop_point = webshipperv2.models.drop_points.drop_points(
                                drop_point_id = '', 
                                name = '', 
                                address_1 = '', 
                                address_2 = '', 
                                zip = '', 
                                city = '', 
                                country_code = '', 
                                state = '', 
                                phone = '', 
                                carrier_code = '', 
                                routing_code = '', 
                                longitude = '', 
                                latitude = '', 
                                created_at = '', 
                                updated_at = '', 
                                opening_hours = '', ), 
                            original_shipping = webshipperv2.models.original_shipping.original_shipping(), 
                            order_lines = [
                                webshipperv2.models.order_lines.order_lines(
                                    sku = '', 
                                    description = '', 
                                    quantity = 56, 
                                    location = '', 
                                    tarif_number = '', 
                                    country_of_origin = '', 
                                    unit_price = 1.337, 
                                    package_id = 56, 
                                    discounted_unit_price = '', 
                                    discount_value = 1.337, 
                                    discount_type = 56, 
                                    vat_percent = 1.337, 
                                    order_id = 56, 
                                    status = 56, 
                                    ext_ref = '', 
                                    weight = 1.337, 
                                    weight_unit = '', 
                                    created_at = '', 
                                    updated_at = '', 
                                    is_virtual = True, 
                                    dangerous_goods_details = webshipperv2.models.dangerous_goods_details.dangerous_goods_details(), )
                                ], 
                            delivery_address = webshipperv2.models.shipping_addresses.shipping_addresses(
                                att_contact = '', 
                                company_name = '', 
                                address_1 = '', 
                                address_2 = '', 
                                country_code = '', 
                                state = '', 
                                phone = '', 
                                email = '', 
                                zip = '', 
                                city = '', 
                                vat_no = '', 
                                address_type = '', 
                                ext_location = '', 
                                voec = '', 
                                eori = '', 
                                sprn = '', 
                                ioss = '', 
                                fda = '', 
                                duns = '', 
                                personal_customs_no = '', 
                                company_customs_numbers = '', ), 
                            sender_address = webshipperv2.models.shipping_addresses.shipping_addresses(
                                att_contact = '', 
                                company_name = '', 
                                address_1 = '', 
                                address_2 = '', 
                                country_code = '', 
                                state = '', 
                                phone = '', 
                                email = '', 
                                zip = '', 
                                city = '', 
                                vat_no = '', 
                                address_type = '', 
                                ext_location = '', 
                                voec = '', 
                                eori = '', 
                                sprn = '', 
                                ioss = '', 
                                fda = '', 
                                duns = '', 
                                personal_customs_no = '', 
                                company_customs_numbers = '', ), 
                            billing_address = , 
                            sold_from_address = , 
                            currency = '', 
                            internal_comment = '', 
                            external_comment = '', 
                            error_message = webshipperv2.models.error_message.error_message(), 
                            slip = '', 
                            base64 = '', 
                            updated_at = '', 
                            created_at = '', 
                            lock_state = '', 
                            source = '', 
                            tags = [
                                ''
                                ], 
                            error_class = '', 
                            slip_printed = True, 
                            label_printed = True, 
                            create_shipment_automatically = '', 
                            latest_activity = '', 
                            latest_status_event = '', 
                            shipping_rate_id = 56, 
                            csv_upload_id = 56, ), )
                    ]
            )
        else:
            return OrdersGet200Response(
        )
        """

    def testOrdersGet200Response(self):
        """Test OrdersGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

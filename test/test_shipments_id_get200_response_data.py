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

from webshipperv2.models.shipments_id_get200_response_data import ShipmentsIdGet200ResponseData

class TestShipmentsIdGet200ResponseData(unittest.TestCase):
    """ShipmentsIdGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShipmentsIdGet200ResponseData:
        """Test ShipmentsIdGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShipmentsIdGet200ResponseData`
        """
        model = ShipmentsIdGet200ResponseData()
        if include_optional:
            return ShipmentsIdGet200ResponseData(
                id = 56,
                type = 'shipments',
                attributes = webshipperv2.models.shipments.shipments(
                    reference = '', 
                    comment = '', 
                    service_code = '', 
                    is_return = True, 
                    packages = [
                        webshipperv2.models.packages.packages(
                            weight = 1.337, 
                            weight_unit = 'g', 
                            dimensions = '', 
                            service_attributes = '', 
                            add_ons = '', 
                            colli_type = '', 
                            predefined_barcode = '', )
                        ], 
                    delivery_address = webshipperv2.models.delivery_address.delivery_address(), 
                    sender_address = webshipperv2.models.sender_address.sender_address(), 
                    billing_address = webshipperv2.models.billing_address.billing_address(), 
                    pickup_address = webshipperv2.models.pickup_address.pickup_address(), 
                    return_address = webshipperv2.models.return_address.return_address(), 
                    service_attributes = [
                        ''
                        ], 
                    add_ons = [
                        ''
                        ], 
                    sms_notification = '', 
                    email_notification = '', 
                    included_documents = '', 
                    drop_point = '', 
                    tracking_links = [
                        webshipperv2.models.shipments_tracking_links_inner.shipments_tracking_links_inner(
                            url = '', 
                            number = '', 
                            latest_transit_event = '', 
                            tracking_events = '', )
                        ], 
                    fulfill_immediately = '', 
                    test_mode = True, 
                    dutiable = True, 
                    created_at = '', 
                    ext_ref = '', 
                    original_shipment_id = 56, 
                    send_time = '', 
                    status = 56, 
                    latest_update_time = '', 
                    supports_updates = '', 
                    additional_attributes = '', 
                    cost_price = 1.337, 
                    sales_price = 1.337, 
                    currency = '', 
                    manual_order_shipment_creation = '', 
                    carrier_type_name = '', 
                    carrier_alias = '', 
                    carrier_id = 56, 
                    invoice_settings = '', 
                    latest_activity = '', 
                    latest_status_event = '', 
                    shadow_booking_as_parent = '', 
                    source = 56, 
                    document_template = '', 
                    csv_upload_id = 56, 
                    omit_print = True, 
                    original_shipment = '', )
            )
        else:
            return ShipmentsIdGet200ResponseData(
        )
        """

    def testShipmentsIdGet200ResponseData(self):
        """Test ShipmentsIdGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

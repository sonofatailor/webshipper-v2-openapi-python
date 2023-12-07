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

from webshipperv2.models.waybills_id_get200_response_included_inner_data import WaybillsIdGet200ResponseIncludedInnerData

class TestWaybillsIdGet200ResponseIncludedInnerData(unittest.TestCase):
    """WaybillsIdGet200ResponseIncludedInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WaybillsIdGet200ResponseIncludedInnerData:
        """Test WaybillsIdGet200ResponseIncludedInnerData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WaybillsIdGet200ResponseIncludedInnerData`
        """
        model = WaybillsIdGet200ResponseIncludedInnerData()
        if include_optional:
            return WaybillsIdGet200ResponseIncludedInnerData(
                alias = '',
                services = '',
                attrs = '',
                prefer_zpl = True,
                created_at = '',
                updated_at = '',
                is_approved = True,
                approved_service_codes = '',
                service_parameter_enums = '',
                barcode_notification_behavior = 56,
                barcode_notification_mail = '',
                has_active_cost_sheet = '',
                delete_at_carrier = True,
                test_mode = True,
                logo = '',
                logo_url = '',
                print_error_label = True,
                ftp_configuration_id = 56,
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
                company_customs_numbers = '',
                uuid = '',
                approved = True,
                is_online = True,
                last_connected = '',
                prevent_multiple_shipments = True
            )
        else:
            return WaybillsIdGet200ResponseIncludedInnerData(
        )
        """

    def testWaybillsIdGet200ResponseIncludedInnerData(self):
        """Test WaybillsIdGet200ResponseIncludedInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from openapi_client.models.csv_mappings_id_get200_response_included_inner_data import CsvMappingsIdGet200ResponseIncludedInnerData

class TestCsvMappingsIdGet200ResponseIncludedInnerData(unittest.TestCase):
    """CsvMappingsIdGet200ResponseIncludedInnerData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CsvMappingsIdGet200ResponseIncludedInnerData:
        """Test CsvMappingsIdGet200ResponseIncludedInnerData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CsvMappingsIdGet200ResponseIncludedInnerData`
        """
        model = CsvMappingsIdGet200ResponseIncludedInnerData()
        if include_optional:
            return CsvMappingsIdGet200ResponseIncludedInnerData(
                alias = '',
                services = '',
                attrs = [
                    ''
                    ],
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
                channel_label = '',
                additional_parameters = openapi_client.models.additional_parameters.additional_parameters(),
                slip_print_mode = '',
                return_label_print_mode = '',
                shipping_label_print_mode = '',
                document_print_mode = '',
                configuration_token = '',
                sync_status = 56,
                failed_sync_count = 56,
                fulfill_automatically = True,
                drop_point_limit = 56,
                create_shipment_automatically = True,
                health = '',
                convert_currency_on_rate_quotes = True,
                sync_additional_attributes_to_shipments = True,
                auto_order_import = True
            )
        else:
            return CsvMappingsIdGet200ResponseIncludedInnerData(
        )
        """

    def testCsvMappingsIdGet200ResponseIncludedInnerData(self):
        """Test CsvMappingsIdGet200ResponseIncludedInnerData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

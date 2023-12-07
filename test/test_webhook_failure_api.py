# coding: utf-8

"""
    Webshipper V2 REST API

       <p>     The Webshipper API is a RESTful JSON API that gives full control over your Webshipper account. The API is scoped to your <em>account name</em>,     and is accessed via the endpoint <em>https://&lt;account name&gt;.api.webshipper.io/v2/</em>. Your <em>account name</em> is the same as you see when you access the Webshipper web UI     at <em>https://&lt;account name&gt;.webshipper.io</em>.   </p>    <p>     This API conforms to the <a href=\"http://jsonapi.org/\">JSON API standard</a> with the following conventions:     <ul>       <li>Resources are identified with the attribute <code>id</code>, which is a server-side generated sequential integer</li>       <li>Resource types are pluralised and underscored, like <code>order_lines</code></li>       <li>The API has a fixed page limit of 30 records. To fetch more records use the query parameter <code>page[number]</code></li>       <li>All resources have the attributes <code>created_at</code> and <code>updated_at</code> which are ISO 8601 timestamps like <code>2018-03-07T14:01:18.000Z</code> </li>       <li>All country codes are <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes</li>     </ul>   </p>     <p> It is also possible to download the documentation in the OpenAPI 3.0 <a href=\"?download_openapi=1\">here</a> </p>    <div class=\"alert alert-info\">     <i class=\"fa fa-info mr-2\"></i>     Webshipper <em>strongly</em> recommends using a client library for utilising this API. Refer to jsonapi.org's list of     <a href=\"http://jsonapi.org/implementations/#client-libraries\">jsonapi.org's list of client libraries</a> to find one for your language.   </div> 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.webhook_failure_api import WebhookFailureApi


class TestWebhookFailureApi(unittest.TestCase):
    """WebhookFailureApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhookFailureApi()

    def tearDown(self) -> None:
        pass

    def test_webhook_failures_get(self) -> None:
        """Test case for webhook_failures_get

        List all Webhook Failures
        """
        pass

    def test_webhook_failures_id_delete(self) -> None:
        """Test case for webhook_failures_id_delete

        Delete a Webhook Failure
        """
        pass

    def test_webhook_failures_id_get(self) -> None:
        """Test case for webhook_failures_id_get

        Show a single Webhook Failure
        """
        pass

    def test_webhook_failures_id_patch(self) -> None:
        """Test case for webhook_failures_id_patch

        Update a Webhook Failure
        """
        pass

    def test_webhook_failures_post(self) -> None:
        """Test case for webhook_failures_post

        Create a Webhook Failure
        """
        pass


if __name__ == '__main__':
    unittest.main()

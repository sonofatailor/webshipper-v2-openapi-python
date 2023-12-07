# openapi_client.ServiceQuoteApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_quotes_post**](ServiceQuoteApi.md#service_quotes_post) | **POST** /service_quotes | Create a Service Quote


# **service_quotes_post**
> ServiceQuotesPost204Response service_quotes_post(service_quotes_post_request)

Create a Service Quote

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.service_quotes_post204_response import ServiceQuotesPost204Response
from openapi_client.models.service_quotes_post_request import ServiceQuotesPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://.api.webshipper.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://.api.webshipper.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceQuoteApi(api_client)
    service_quotes_post_request = {"data":{"type":"service_quotes","attributes":{"carrier_id":1,"is_return":false,"send_time":"2023-02-13T11:58:52+01:00","delivery_address":{"address_1":"Søndergade 2B","zip":"8600","city":"Silkeborg","country_code":"DK"},"sender_address":{"address_1":"Lyngbygade 8","zip":"8600","city":"Silkeborg","country_code":"DK"},"packages":[{"weight":500,"weight_unit":"g","dimensions":{"width":15,"length":15,"height":15,"unit":"cm"}}]}}} # ServiceQuotesPostRequest | 

    try:
        # Create a Service Quote
        api_response = api_instance.service_quotes_post(service_quotes_post_request)
        print("The response of ServiceQuoteApi->service_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceQuoteApi->service_quotes_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_quotes_post_request** | [**ServiceQuotesPostRequest**](ServiceQuotesPostRequest.md)|  | 

### Return type

[**ServiceQuotesPost204Response**](ServiceQuotesPost204Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


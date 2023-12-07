# webshipperv2.RateQuoteApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rate_quotes_post**](RateQuoteApi.md#rate_quotes_post) | **POST** /rate_quotes | Create a Rate Quote


# **rate_quotes_post**
> RateQuotesPost204Response rate_quotes_post(rate_quotes_post_request)

Create a Rate Quote

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.rate_quotes_post204_response import RateQuotesPost204Response
from webshipperv2.models.rate_quotes_post_request import RateQuotesPostRequest
from webshipperv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://.api.webshipper.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = webshipperv2.Configuration(
    host = "https://.api.webshipper.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = webshipperv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with webshipperv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webshipperv2.RateQuoteApi(api_client)
    rate_quotes_post_request = {"data":{"type":"rate_quotes","attributes":{"order_channel_id":16,"price":199,"weight":100,"delivery_address":{"zip":"7400","country_code":"DK"},"items":[{"quantity":5,"sku":"sku123"}]}}} # RateQuotesPostRequest | 

    try:
        # Create a Rate Quote
        api_response = api_instance.rate_quotes_post(rate_quotes_post_request)
        print("The response of RateQuoteApi->rate_quotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateQuoteApi->rate_quotes_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_quotes_post_request** | [**RateQuotesPostRequest**](RateQuotesPostRequest.md)|  | 

### Return type

[**RateQuotesPost204Response**](RateQuotesPost204Response.md)

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


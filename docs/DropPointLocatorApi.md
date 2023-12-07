# webshipperv2.DropPointLocatorApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drop_point_locators_post**](DropPointLocatorApi.md#drop_point_locators_post) | **POST** /drop_point_locators | Search for drop points


# **drop_point_locators_post**
> DropPointLocatorsPost204Response drop_point_locators_post(drop_point_locators_post_request)

Search for drop points

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.drop_point_locators_post204_response import DropPointLocatorsPost204Response
from webshipperv2.models.drop_point_locators_post_request import DropPointLocatorsPostRequest
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
    api_instance = webshipperv2.DropPointLocatorApi(api_client)
    drop_point_locators_post_request = {"data":{"type":"drop_point_locators","attributes":{"carrier_id":1,"service_code":"PARCELSHOP","delivery_address":{"address_1":"Lyngbygade 8","zip":"8600","city":"Silkeborg","country_code":"DK"}}}} # DropPointLocatorsPostRequest | 

    try:
        # Search for drop points
        api_response = api_instance.drop_point_locators_post(drop_point_locators_post_request)
        print("The response of DropPointLocatorApi->drop_point_locators_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DropPointLocatorApi->drop_point_locators_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drop_point_locators_post_request** | [**DropPointLocatorsPostRequest**](DropPointLocatorsPostRequest.md)|  | 

### Return type

[**DropPointLocatorsPost204Response**](DropPointLocatorsPost204Response.md)

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


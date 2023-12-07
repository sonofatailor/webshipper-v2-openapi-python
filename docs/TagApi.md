# webshipperv2.TagApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagApi.md#tags_get) | **GET** /tags | List all Tags


# **tags_get**
> TagsGet200Response tags_get(filter_id=filter_id)

List all Tags

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.tags_get200_response import TagsGet200Response
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
    api_instance = webshipperv2.TagApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Tags
        api_response = api_instance.tags_get(filter_id=filter_id)
        print("The response of TagApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->tags_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**TagsGet200Response**](TagsGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# webshipperv2.LocalAttributeEnumsApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**local_attr_enums_get**](LocalAttributeEnumsApi.md#local_attr_enums_get) | **GET** /local_attr_enums | List all Local Attribute Enumss
[**local_attr_enums_id_get**](LocalAttributeEnumsApi.md#local_attr_enums_id_get) | **GET** /local_attr_enums/{id} | Show a single Local Attribute Enums


# **local_attr_enums_get**
> LocalAttrEnumsGet200Response local_attr_enums_get(filter_id=filter_id)

List all Local Attribute Enumss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.local_attr_enums_get200_response import LocalAttrEnumsGet200Response
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
    api_instance = webshipperv2.LocalAttributeEnumsApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Local Attribute Enumss
        api_response = api_instance.local_attr_enums_get(filter_id=filter_id)
        print("The response of LocalAttributeEnumsApi->local_attr_enums_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalAttributeEnumsApi->local_attr_enums_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**LocalAttrEnumsGet200Response**](LocalAttrEnumsGet200Response.md)

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

# **local_attr_enums_id_get**
> LocalAttrEnumsIdGet200Response local_attr_enums_id_get(id)

Show a single Local Attribute Enums

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.local_attr_enums_id_get200_response import LocalAttrEnumsIdGet200Response
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
    api_instance = webshipperv2.LocalAttributeEnumsApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Local Attribute Enums
        api_response = api_instance.local_attr_enums_id_get(id)
        print("The response of LocalAttributeEnumsApi->local_attr_enums_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalAttributeEnumsApi->local_attr_enums_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LocalAttrEnumsIdGet200Response**](LocalAttrEnumsIdGet200Response.md)

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


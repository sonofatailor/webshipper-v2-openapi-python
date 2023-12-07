# openapi_client.OrderChannelTypeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_channel_types_get**](OrderChannelTypeApi.md#order_channel_types_get) | **GET** /order_channel_types | List all Order Channel Types
[**order_channel_types_id_get**](OrderChannelTypeApi.md#order_channel_types_id_get) | **GET** /order_channel_types/{id} | Show a single Order Channel Type


# **order_channel_types_get**
> OrderChannelTypesGet200Response order_channel_types_get(filter_id=filter_id, filter_by_name=filter_by_name)

List all Order Channel Types

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channel_types_get200_response import OrderChannelTypesGet200Response
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
    api_instance = openapi_client.OrderChannelTypeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_by_name = 'filter_by_name_example' # str | Filter by by_name (optional)

    try:
        # List all Order Channel Types
        api_response = api_instance.order_channel_types_get(filter_id=filter_id, filter_by_name=filter_by_name)
        print("The response of OrderChannelTypeApi->order_channel_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelTypeApi->order_channel_types_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_by_name** | **str**| Filter by by_name | [optional] 

### Return type

[**OrderChannelTypesGet200Response**](OrderChannelTypesGet200Response.md)

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

# **order_channel_types_id_get**
> OrderChannelTypesIdGet200Response order_channel_types_id_get(id)

Show a single Order Channel Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channel_types_id_get200_response import OrderChannelTypesIdGet200Response
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
    api_instance = openapi_client.OrderChannelTypeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Order Channel Type
        api_response = api_instance.order_channel_types_id_get(id)
        print("The response of OrderChannelTypeApi->order_channel_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelTypeApi->order_channel_types_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderChannelTypesIdGet200Response**](OrderChannelTypesIdGet200Response.md)

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


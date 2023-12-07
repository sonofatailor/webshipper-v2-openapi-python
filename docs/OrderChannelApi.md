# openapi_client.OrderChannelApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_channels_get**](OrderChannelApi.md#order_channels_get) | **GET** /order_channels | List all Order Channels
[**order_channels_id_delete**](OrderChannelApi.md#order_channels_id_delete) | **DELETE** /order_channels/{id} | Delete a Order Channel
[**order_channels_id_get**](OrderChannelApi.md#order_channels_id_get) | **GET** /order_channels/{id} | Show a single Order Channel
[**order_channels_id_patch**](OrderChannelApi.md#order_channels_id_patch) | **PATCH** /order_channels/{id} | Update a Order Channel
[**order_channels_post**](OrderChannelApi.md#order_channels_post) | **POST** /order_channels | Create a Order Channel


# **order_channels_get**
> OrderChannelsGet200Response order_channels_get(filter_id=filter_id, filter_attr=filter_attr)

List all Order Channels

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channels_get200_response import OrderChannelsGet200Response
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
    api_instance = openapi_client.OrderChannelApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_attr = 'filter_attr_example' # str | Filter by attr (optional)

    try:
        # List all Order Channels
        api_response = api_instance.order_channels_get(filter_id=filter_id, filter_attr=filter_attr)
        print("The response of OrderChannelApi->order_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelApi->order_channels_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_attr** | **str**| Filter by attr | [optional] 

### Return type

[**OrderChannelsGet200Response**](OrderChannelsGet200Response.md)

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

# **order_channels_id_delete**
> OrderChannelsIdGet200Response order_channels_id_delete(id)

Delete a Order Channel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channels_id_get200_response import OrderChannelsIdGet200Response
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
    api_instance = openapi_client.OrderChannelApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Order Channel
        api_response = api_instance.order_channels_id_delete(id)
        print("The response of OrderChannelApi->order_channels_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelApi->order_channels_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderChannelsIdGet200Response**](OrderChannelsIdGet200Response.md)

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

# **order_channels_id_get**
> OrderChannelsIdGet200Response order_channels_id_get(id)

Show a single Order Channel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channels_id_get200_response import OrderChannelsIdGet200Response
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
    api_instance = openapi_client.OrderChannelApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Order Channel
        api_response = api_instance.order_channels_id_get(id)
        print("The response of OrderChannelApi->order_channels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelApi->order_channels_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderChannelsIdGet200Response**](OrderChannelsIdGet200Response.md)

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

# **order_channels_id_patch**
> OrderChannelsIdGet200Response order_channels_id_patch(id, order_channels_id_patch_request)

Update a Order Channel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channels_id_get200_response import OrderChannelsIdGet200Response
from openapi_client.models.order_channels_id_patch_request import OrderChannelsIdPatchRequest
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
    api_instance = openapi_client.OrderChannelApi(api_client)
    id = 56 # int | 
    order_channels_id_patch_request = openapi_client.OrderChannelsIdPatchRequest() # OrderChannelsIdPatchRequest | 

    try:
        # Update a Order Channel
        api_response = api_instance.order_channels_id_patch(id, order_channels_id_patch_request)
        print("The response of OrderChannelApi->order_channels_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelApi->order_channels_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **order_channels_id_patch_request** | [**OrderChannelsIdPatchRequest**](OrderChannelsIdPatchRequest.md)|  | 

### Return type

[**OrderChannelsIdGet200Response**](OrderChannelsIdGet200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_channels_post**
> OrderChannelsIdGet200Response order_channels_post(order_channels_post_request)

Create a Order Channel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.order_channels_id_get200_response import OrderChannelsIdGet200Response
from openapi_client.models.order_channels_post_request import OrderChannelsPostRequest
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
    api_instance = openapi_client.OrderChannelApi(api_client)
    order_channels_post_request = openapi_client.OrderChannelsPostRequest() # OrderChannelsPostRequest | 

    try:
        # Create a Order Channel
        api_response = api_instance.order_channels_post(order_channels_post_request)
        print("The response of OrderChannelApi->order_channels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelApi->order_channels_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_channels_post_request** | [**OrderChannelsPostRequest**](OrderChannelsPostRequest.md)|  | 

### Return type

[**OrderChannelsIdGet200Response**](OrderChannelsIdGet200Response.md)

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


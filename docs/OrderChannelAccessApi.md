# webshipperv2.OrderChannelAccessApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_channel_accesses_get**](OrderChannelAccessApi.md#order_channel_accesses_get) | **GET** /order_channel_accesses | List all Order Channel Accesss
[**order_channel_accesses_id_delete**](OrderChannelAccessApi.md#order_channel_accesses_id_delete) | **DELETE** /order_channel_accesses/{id} | Delete a Order Channel Access
[**order_channel_accesses_id_get**](OrderChannelAccessApi.md#order_channel_accesses_id_get) | **GET** /order_channel_accesses/{id} | Show a single Order Channel Access
[**order_channel_accesses_id_patch**](OrderChannelAccessApi.md#order_channel_accesses_id_patch) | **PATCH** /order_channel_accesses/{id} | Update a Order Channel Access
[**order_channel_accesses_post**](OrderChannelAccessApi.md#order_channel_accesses_post) | **POST** /order_channel_accesses | Create a Order Channel Access


# **order_channel_accesses_get**
> OrderChannelAccessesGet200Response order_channel_accesses_get(filter_id=filter_id)

List all Order Channel Accesss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.order_channel_accesses_get200_response import OrderChannelAccessesGet200Response
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
    api_instance = webshipperv2.OrderChannelAccessApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Order Channel Accesss
        api_response = api_instance.order_channel_accesses_get(filter_id=filter_id)
        print("The response of OrderChannelAccessApi->order_channel_accesses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelAccessApi->order_channel_accesses_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**OrderChannelAccessesGet200Response**](OrderChannelAccessesGet200Response.md)

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

# **order_channel_accesses_id_delete**
> OrderChannelAccessesIdGet200Response order_channel_accesses_id_delete(id)

Delete a Order Channel Access

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.order_channel_accesses_id_get200_response import OrderChannelAccessesIdGet200Response
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
    api_instance = webshipperv2.OrderChannelAccessApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Order Channel Access
        api_response = api_instance.order_channel_accesses_id_delete(id)
        print("The response of OrderChannelAccessApi->order_channel_accesses_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelAccessApi->order_channel_accesses_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderChannelAccessesIdGet200Response**](OrderChannelAccessesIdGet200Response.md)

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

# **order_channel_accesses_id_get**
> OrderChannelAccessesIdGet200Response order_channel_accesses_id_get(id)

Show a single Order Channel Access

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.order_channel_accesses_id_get200_response import OrderChannelAccessesIdGet200Response
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
    api_instance = webshipperv2.OrderChannelAccessApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Order Channel Access
        api_response = api_instance.order_channel_accesses_id_get(id)
        print("The response of OrderChannelAccessApi->order_channel_accesses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelAccessApi->order_channel_accesses_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrderChannelAccessesIdGet200Response**](OrderChannelAccessesIdGet200Response.md)

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

# **order_channel_accesses_id_patch**
> OrderChannelAccessesIdGet200Response order_channel_accesses_id_patch(id, order_channel_accesses_id_patch_request)

Update a Order Channel Access

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.order_channel_accesses_id_get200_response import OrderChannelAccessesIdGet200Response
from webshipperv2.models.order_channel_accesses_id_patch_request import OrderChannelAccessesIdPatchRequest
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
    api_instance = webshipperv2.OrderChannelAccessApi(api_client)
    id = 56 # int | 
    order_channel_accesses_id_patch_request = webshipperv2.OrderChannelAccessesIdPatchRequest() # OrderChannelAccessesIdPatchRequest | 

    try:
        # Update a Order Channel Access
        api_response = api_instance.order_channel_accesses_id_patch(id, order_channel_accesses_id_patch_request)
        print("The response of OrderChannelAccessApi->order_channel_accesses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelAccessApi->order_channel_accesses_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **order_channel_accesses_id_patch_request** | [**OrderChannelAccessesIdPatchRequest**](OrderChannelAccessesIdPatchRequest.md)|  | 

### Return type

[**OrderChannelAccessesIdGet200Response**](OrderChannelAccessesIdGet200Response.md)

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

# **order_channel_accesses_post**
> OrderChannelAccessesIdGet200Response order_channel_accesses_post(order_channel_accesses_post_request)

Create a Order Channel Access

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.order_channel_accesses_id_get200_response import OrderChannelAccessesIdGet200Response
from webshipperv2.models.order_channel_accesses_post_request import OrderChannelAccessesPostRequest
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
    api_instance = webshipperv2.OrderChannelAccessApi(api_client)
    order_channel_accesses_post_request = webshipperv2.OrderChannelAccessesPostRequest() # OrderChannelAccessesPostRequest | 

    try:
        # Create a Order Channel Access
        api_response = api_instance.order_channel_accesses_post(order_channel_accesses_post_request)
        print("The response of OrderChannelAccessApi->order_channel_accesses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderChannelAccessApi->order_channel_accesses_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_channel_accesses_post_request** | [**OrderChannelAccessesPostRequest**](OrderChannelAccessesPostRequest.md)|  | 

### Return type

[**OrderChannelAccessesIdGet200Response**](OrderChannelAccessesIdGet200Response.md)

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


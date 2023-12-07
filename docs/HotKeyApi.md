# openapi_client.HotKeyApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hot_keys_get**](HotKeyApi.md#hot_keys_get) | **GET** /hot_keys | List all HotKeys
[**hot_keys_id_delete**](HotKeyApi.md#hot_keys_id_delete) | **DELETE** /hot_keys/{id} | Delete a HotKey
[**hot_keys_id_get**](HotKeyApi.md#hot_keys_id_get) | **GET** /hot_keys/{id} | Show a single HotKey
[**hot_keys_id_patch**](HotKeyApi.md#hot_keys_id_patch) | **PATCH** /hot_keys/{id} | Update a HotKey
[**hot_keys_post**](HotKeyApi.md#hot_keys_post) | **POST** /hot_keys | Create a HotKey


# **hot_keys_get**
> HotKeysGet200Response hot_keys_get(filter_id=filter_id)

List all HotKeys

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.hot_keys_get200_response import HotKeysGet200Response
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
    api_instance = openapi_client.HotKeyApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all HotKeys
        api_response = api_instance.hot_keys_get(filter_id=filter_id)
        print("The response of HotKeyApi->hot_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotKeyApi->hot_keys_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**HotKeysGet200Response**](HotKeysGet200Response.md)

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

# **hot_keys_id_delete**
> HotKeysIdGet200Response hot_keys_id_delete(id)

Delete a HotKey

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.hot_keys_id_get200_response import HotKeysIdGet200Response
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
    api_instance = openapi_client.HotKeyApi(api_client)
    id = 56 # int | 

    try:
        # Delete a HotKey
        api_response = api_instance.hot_keys_id_delete(id)
        print("The response of HotKeyApi->hot_keys_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotKeyApi->hot_keys_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HotKeysIdGet200Response**](HotKeysIdGet200Response.md)

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

# **hot_keys_id_get**
> HotKeysIdGet200Response hot_keys_id_get(id)

Show a single HotKey

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.hot_keys_id_get200_response import HotKeysIdGet200Response
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
    api_instance = openapi_client.HotKeyApi(api_client)
    id = 56 # int | 

    try:
        # Show a single HotKey
        api_response = api_instance.hot_keys_id_get(id)
        print("The response of HotKeyApi->hot_keys_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotKeyApi->hot_keys_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HotKeysIdGet200Response**](HotKeysIdGet200Response.md)

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

# **hot_keys_id_patch**
> HotKeysIdGet200Response hot_keys_id_patch(id, hot_keys_id_patch_request)

Update a HotKey

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.hot_keys_id_get200_response import HotKeysIdGet200Response
from openapi_client.models.hot_keys_id_patch_request import HotKeysIdPatchRequest
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
    api_instance = openapi_client.HotKeyApi(api_client)
    id = 56 # int | 
    hot_keys_id_patch_request = openapi_client.HotKeysIdPatchRequest() # HotKeysIdPatchRequest | 

    try:
        # Update a HotKey
        api_response = api_instance.hot_keys_id_patch(id, hot_keys_id_patch_request)
        print("The response of HotKeyApi->hot_keys_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotKeyApi->hot_keys_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **hot_keys_id_patch_request** | [**HotKeysIdPatchRequest**](HotKeysIdPatchRequest.md)|  | 

### Return type

[**HotKeysIdGet200Response**](HotKeysIdGet200Response.md)

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

# **hot_keys_post**
> HotKeysIdGet200Response hot_keys_post(hot_keys_post_request)

Create a HotKey

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.hot_keys_id_get200_response import HotKeysIdGet200Response
from openapi_client.models.hot_keys_post_request import HotKeysPostRequest
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
    api_instance = openapi_client.HotKeyApi(api_client)
    hot_keys_post_request = openapi_client.HotKeysPostRequest() # HotKeysPostRequest | 

    try:
        # Create a HotKey
        api_response = api_instance.hot_keys_post(hot_keys_post_request)
        print("The response of HotKeyApi->hot_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotKeyApi->hot_keys_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hot_keys_post_request** | [**HotKeysPostRequest**](HotKeysPostRequest.md)|  | 

### Return type

[**HotKeysIdGet200Response**](HotKeysIdGet200Response.md)

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


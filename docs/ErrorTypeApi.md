# webshipperv2.ErrorTypeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error_types_get**](ErrorTypeApi.md#error_types_get) | **GET** /error_types | List all Error Types
[**error_types_id_delete**](ErrorTypeApi.md#error_types_id_delete) | **DELETE** /error_types/{id} | Delete a Error Type
[**error_types_id_get**](ErrorTypeApi.md#error_types_id_get) | **GET** /error_types/{id} | Show a single Error Type
[**error_types_id_patch**](ErrorTypeApi.md#error_types_id_patch) | **PATCH** /error_types/{id} | Update a Error Type
[**error_types_post**](ErrorTypeApi.md#error_types_post) | **POST** /error_types | Create a Error Type


# **error_types_get**
> ErrorTypesGet200Response error_types_get(filter_id=filter_id)

List all Error Types

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.error_types_get200_response import ErrorTypesGet200Response
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
    api_instance = webshipperv2.ErrorTypeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Error Types
        api_response = api_instance.error_types_get(filter_id=filter_id)
        print("The response of ErrorTypeApi->error_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorTypeApi->error_types_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ErrorTypesGet200Response**](ErrorTypesGet200Response.md)

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

# **error_types_id_delete**
> ErrorTypesIdGet200Response error_types_id_delete(id)

Delete a Error Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.error_types_id_get200_response import ErrorTypesIdGet200Response
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
    api_instance = webshipperv2.ErrorTypeApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Error Type
        api_response = api_instance.error_types_id_delete(id)
        print("The response of ErrorTypeApi->error_types_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorTypeApi->error_types_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ErrorTypesIdGet200Response**](ErrorTypesIdGet200Response.md)

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

# **error_types_id_get**
> ErrorTypesIdGet200Response error_types_id_get(id)

Show a single Error Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.error_types_id_get200_response import ErrorTypesIdGet200Response
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
    api_instance = webshipperv2.ErrorTypeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Error Type
        api_response = api_instance.error_types_id_get(id)
        print("The response of ErrorTypeApi->error_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorTypeApi->error_types_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ErrorTypesIdGet200Response**](ErrorTypesIdGet200Response.md)

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

# **error_types_id_patch**
> ErrorTypesIdGet200Response error_types_id_patch(id, error_types_id_patch_request)

Update a Error Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.error_types_id_get200_response import ErrorTypesIdGet200Response
from webshipperv2.models.error_types_id_patch_request import ErrorTypesIdPatchRequest
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
    api_instance = webshipperv2.ErrorTypeApi(api_client)
    id = 56 # int | 
    error_types_id_patch_request = webshipperv2.ErrorTypesIdPatchRequest() # ErrorTypesIdPatchRequest | 

    try:
        # Update a Error Type
        api_response = api_instance.error_types_id_patch(id, error_types_id_patch_request)
        print("The response of ErrorTypeApi->error_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorTypeApi->error_types_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **error_types_id_patch_request** | [**ErrorTypesIdPatchRequest**](ErrorTypesIdPatchRequest.md)|  | 

### Return type

[**ErrorTypesIdGet200Response**](ErrorTypesIdGet200Response.md)

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

# **error_types_post**
> ErrorTypesIdGet200Response error_types_post(error_types_post_request)

Create a Error Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.error_types_id_get200_response import ErrorTypesIdGet200Response
from webshipperv2.models.error_types_post_request import ErrorTypesPostRequest
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
    api_instance = webshipperv2.ErrorTypeApi(api_client)
    error_types_post_request = webshipperv2.ErrorTypesPostRequest() # ErrorTypesPostRequest | 

    try:
        # Create a Error Type
        api_response = api_instance.error_types_post(error_types_post_request)
        print("The response of ErrorTypeApi->error_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ErrorTypeApi->error_types_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_types_post_request** | [**ErrorTypesPostRequest**](ErrorTypesPostRequest.md)|  | 

### Return type

[**ErrorTypesIdGet200Response**](ErrorTypesIdGet200Response.md)

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


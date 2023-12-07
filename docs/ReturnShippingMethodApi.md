# webshipperv2.ReturnShippingMethodApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_shipping_methods_get**](ReturnShippingMethodApi.md#return_shipping_methods_get) | **GET** /return_shipping_methods | List all Return Shipping Methods
[**return_shipping_methods_id_delete**](ReturnShippingMethodApi.md#return_shipping_methods_id_delete) | **DELETE** /return_shipping_methods/{id} | Delete a Return Shipping Method
[**return_shipping_methods_id_get**](ReturnShippingMethodApi.md#return_shipping_methods_id_get) | **GET** /return_shipping_methods/{id} | Show a single Return Shipping Method
[**return_shipping_methods_id_patch**](ReturnShippingMethodApi.md#return_shipping_methods_id_patch) | **PATCH** /return_shipping_methods/{id} | Update a Return Shipping Method
[**return_shipping_methods_post**](ReturnShippingMethodApi.md#return_shipping_methods_post) | **POST** /return_shipping_methods | Create a Return Shipping Method


# **return_shipping_methods_get**
> ReturnShippingMethodsGet200Response return_shipping_methods_get(filter_id=filter_id)

List all Return Shipping Methods

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.return_shipping_methods_get200_response import ReturnShippingMethodsGet200Response
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
    api_instance = webshipperv2.ReturnShippingMethodApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Return Shipping Methods
        api_response = api_instance.return_shipping_methods_get(filter_id=filter_id)
        print("The response of ReturnShippingMethodApi->return_shipping_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnShippingMethodApi->return_shipping_methods_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ReturnShippingMethodsGet200Response**](ReturnShippingMethodsGet200Response.md)

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

# **return_shipping_methods_id_delete**
> ReturnShippingMethodsIdGet200Response return_shipping_methods_id_delete(id)

Delete a Return Shipping Method

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.return_shipping_methods_id_get200_response import ReturnShippingMethodsIdGet200Response
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
    api_instance = webshipperv2.ReturnShippingMethodApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Return Shipping Method
        api_response = api_instance.return_shipping_methods_id_delete(id)
        print("The response of ReturnShippingMethodApi->return_shipping_methods_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnShippingMethodApi->return_shipping_methods_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnShippingMethodsIdGet200Response**](ReturnShippingMethodsIdGet200Response.md)

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

# **return_shipping_methods_id_get**
> ReturnShippingMethodsIdGet200Response return_shipping_methods_id_get(id)

Show a single Return Shipping Method

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.return_shipping_methods_id_get200_response import ReturnShippingMethodsIdGet200Response
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
    api_instance = webshipperv2.ReturnShippingMethodApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Return Shipping Method
        api_response = api_instance.return_shipping_methods_id_get(id)
        print("The response of ReturnShippingMethodApi->return_shipping_methods_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnShippingMethodApi->return_shipping_methods_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnShippingMethodsIdGet200Response**](ReturnShippingMethodsIdGet200Response.md)

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

# **return_shipping_methods_id_patch**
> ReturnShippingMethodsIdGet200Response return_shipping_methods_id_patch(id, return_shipping_methods_id_patch_request)

Update a Return Shipping Method

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.return_shipping_methods_id_get200_response import ReturnShippingMethodsIdGet200Response
from webshipperv2.models.return_shipping_methods_id_patch_request import ReturnShippingMethodsIdPatchRequest
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
    api_instance = webshipperv2.ReturnShippingMethodApi(api_client)
    id = 56 # int | 
    return_shipping_methods_id_patch_request = webshipperv2.ReturnShippingMethodsIdPatchRequest() # ReturnShippingMethodsIdPatchRequest | 

    try:
        # Update a Return Shipping Method
        api_response = api_instance.return_shipping_methods_id_patch(id, return_shipping_methods_id_patch_request)
        print("The response of ReturnShippingMethodApi->return_shipping_methods_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnShippingMethodApi->return_shipping_methods_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **return_shipping_methods_id_patch_request** | [**ReturnShippingMethodsIdPatchRequest**](ReturnShippingMethodsIdPatchRequest.md)|  | 

### Return type

[**ReturnShippingMethodsIdGet200Response**](ReturnShippingMethodsIdGet200Response.md)

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

# **return_shipping_methods_post**
> ReturnShippingMethodsIdGet200Response return_shipping_methods_post(return_shipping_methods_post_request)

Create a Return Shipping Method

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.return_shipping_methods_id_get200_response import ReturnShippingMethodsIdGet200Response
from webshipperv2.models.return_shipping_methods_post_request import ReturnShippingMethodsPostRequest
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
    api_instance = webshipperv2.ReturnShippingMethodApi(api_client)
    return_shipping_methods_post_request = webshipperv2.ReturnShippingMethodsPostRequest() # ReturnShippingMethodsPostRequest | 

    try:
        # Create a Return Shipping Method
        api_response = api_instance.return_shipping_methods_post(return_shipping_methods_post_request)
        print("The response of ReturnShippingMethodApi->return_shipping_methods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnShippingMethodApi->return_shipping_methods_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_shipping_methods_post_request** | [**ReturnShippingMethodsPostRequest**](ReturnShippingMethodsPostRequest.md)|  | 

### Return type

[**ReturnShippingMethodsIdGet200Response**](ReturnShippingMethodsIdGet200Response.md)

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


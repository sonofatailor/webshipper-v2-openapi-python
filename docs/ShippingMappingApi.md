# webshipperv2.ShippingMappingApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipping_mappings_get**](ShippingMappingApi.md#shipping_mappings_get) | **GET** /shipping_mappings | List all Shipping Mappings
[**shipping_mappings_id_delete**](ShippingMappingApi.md#shipping_mappings_id_delete) | **DELETE** /shipping_mappings/{id} | Delete a Shipping Mapping
[**shipping_mappings_id_get**](ShippingMappingApi.md#shipping_mappings_id_get) | **GET** /shipping_mappings/{id} | Show a single Shipping Mapping
[**shipping_mappings_id_patch**](ShippingMappingApi.md#shipping_mappings_id_patch) | **PATCH** /shipping_mappings/{id} | Update a Shipping Mapping
[**shipping_mappings_post**](ShippingMappingApi.md#shipping_mappings_post) | **POST** /shipping_mappings | Create a Shipping Mapping


# **shipping_mappings_get**
> ShippingMappingsGet200Response shipping_mappings_get(filter_id=filter_id, filter_order_channel_id=filter_order_channel_id, filter_order_channel=filter_order_channel, filter_shipping_code=filter_shipping_code)

List all Shipping Mappings

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_mappings_get200_response import ShippingMappingsGet200Response
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
    api_instance = webshipperv2.ShippingMappingApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_order_channel_id = 'filter_order_channel_id_example' # str | Filter by order_channel_id (optional)
    filter_order_channel = 'filter_order_channel_example' # str | Filter by order_channel (optional)
    filter_shipping_code = 'filter_shipping_code_example' # str | Filter by shipping_code (optional)

    try:
        # List all Shipping Mappings
        api_response = api_instance.shipping_mappings_get(filter_id=filter_id, filter_order_channel_id=filter_order_channel_id, filter_order_channel=filter_order_channel, filter_shipping_code=filter_shipping_code)
        print("The response of ShippingMappingApi->shipping_mappings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMappingApi->shipping_mappings_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_order_channel_id** | **str**| Filter by order_channel_id | [optional] 
 **filter_order_channel** | **str**| Filter by order_channel | [optional] 
 **filter_shipping_code** | **str**| Filter by shipping_code | [optional] 

### Return type

[**ShippingMappingsGet200Response**](ShippingMappingsGet200Response.md)

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

# **shipping_mappings_id_delete**
> ShippingMappingsIdGet200Response shipping_mappings_id_delete(id)

Delete a Shipping Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_mappings_id_get200_response import ShippingMappingsIdGet200Response
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
    api_instance = webshipperv2.ShippingMappingApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Shipping Mapping
        api_response = api_instance.shipping_mappings_id_delete(id)
        print("The response of ShippingMappingApi->shipping_mappings_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMappingApi->shipping_mappings_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingMappingsIdGet200Response**](ShippingMappingsIdGet200Response.md)

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

# **shipping_mappings_id_get**
> ShippingMappingsIdGet200Response shipping_mappings_id_get(id)

Show a single Shipping Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_mappings_id_get200_response import ShippingMappingsIdGet200Response
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
    api_instance = webshipperv2.ShippingMappingApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipping Mapping
        api_response = api_instance.shipping_mappings_id_get(id)
        print("The response of ShippingMappingApi->shipping_mappings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMappingApi->shipping_mappings_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingMappingsIdGet200Response**](ShippingMappingsIdGet200Response.md)

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

# **shipping_mappings_id_patch**
> ShippingMappingsIdGet200Response shipping_mappings_id_patch(id, shipping_mappings_id_patch_request)

Update a Shipping Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_mappings_id_get200_response import ShippingMappingsIdGet200Response
from webshipperv2.models.shipping_mappings_id_patch_request import ShippingMappingsIdPatchRequest
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
    api_instance = webshipperv2.ShippingMappingApi(api_client)
    id = 56 # int | 
    shipping_mappings_id_patch_request = webshipperv2.ShippingMappingsIdPatchRequest() # ShippingMappingsIdPatchRequest | 

    try:
        # Update a Shipping Mapping
        api_response = api_instance.shipping_mappings_id_patch(id, shipping_mappings_id_patch_request)
        print("The response of ShippingMappingApi->shipping_mappings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMappingApi->shipping_mappings_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shipping_mappings_id_patch_request** | [**ShippingMappingsIdPatchRequest**](ShippingMappingsIdPatchRequest.md)|  | 

### Return type

[**ShippingMappingsIdGet200Response**](ShippingMappingsIdGet200Response.md)

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

# **shipping_mappings_post**
> ShippingMappingsIdGet200Response shipping_mappings_post(shipping_mappings_post_request)

Create a Shipping Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_mappings_id_get200_response import ShippingMappingsIdGet200Response
from webshipperv2.models.shipping_mappings_post_request import ShippingMappingsPostRequest
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
    api_instance = webshipperv2.ShippingMappingApi(api_client)
    shipping_mappings_post_request = webshipperv2.ShippingMappingsPostRequest() # ShippingMappingsPostRequest | 

    try:
        # Create a Shipping Mapping
        api_response = api_instance.shipping_mappings_post(shipping_mappings_post_request)
        print("The response of ShippingMappingApi->shipping_mappings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingMappingApi->shipping_mappings_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_mappings_post_request** | [**ShippingMappingsPostRequest**](ShippingMappingsPostRequest.md)|  | 

### Return type

[**ShippingMappingsIdGet200Response**](ShippingMappingsIdGet200Response.md)

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


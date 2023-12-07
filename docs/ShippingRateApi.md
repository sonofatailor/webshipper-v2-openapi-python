# openapi_client.ShippingRateApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipping_rates_get**](ShippingRateApi.md#shipping_rates_get) | **GET** /shipping_rates | List all Shipping Rates
[**shipping_rates_id_delete**](ShippingRateApi.md#shipping_rates_id_delete) | **DELETE** /shipping_rates/{id} | Delete a Shipping Rate
[**shipping_rates_id_get**](ShippingRateApi.md#shipping_rates_id_get) | **GET** /shipping_rates/{id} | Show a single Shipping Rate
[**shipping_rates_id_patch**](ShippingRateApi.md#shipping_rates_id_patch) | **PATCH** /shipping_rates/{id} | Update a Shipping Rate
[**shipping_rates_post**](ShippingRateApi.md#shipping_rates_post) | **POST** /shipping_rates | Create a Shipping Rate


# **shipping_rates_get**
> ShippingRatesGet200Response shipping_rates_get(filter_id=filter_id, filter_order_channel_id=filter_order_channel_id, filter_is_return=filter_is_return, filter_is_hidden=filter_is_hidden, filter_service_code=filter_service_code, filter_shadow_bookings=filter_shadow_bookings)

List all Shipping Rates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.shipping_rates_get200_response import ShippingRatesGet200Response
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
    api_instance = openapi_client.ShippingRateApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_order_channel_id = 'filter_order_channel_id_example' # str | Filter by order_channel_id (optional)
    filter_is_return = 'filter_is_return_example' # str | Filter by is_return (optional)
    filter_is_hidden = 'filter_is_hidden_example' # str | Filter by is_hidden (optional)
    filter_service_code = 'filter_service_code_example' # str | Filter by service_code (optional)
    filter_shadow_bookings = 'filter_shadow_bookings_example' # str | Filter by shadow_bookings (optional)

    try:
        # List all Shipping Rates
        api_response = api_instance.shipping_rates_get(filter_id=filter_id, filter_order_channel_id=filter_order_channel_id, filter_is_return=filter_is_return, filter_is_hidden=filter_is_hidden, filter_service_code=filter_service_code, filter_shadow_bookings=filter_shadow_bookings)
        print("The response of ShippingRateApi->shipping_rates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateApi->shipping_rates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_order_channel_id** | **str**| Filter by order_channel_id | [optional] 
 **filter_is_return** | **str**| Filter by is_return | [optional] 
 **filter_is_hidden** | **str**| Filter by is_hidden | [optional] 
 **filter_service_code** | **str**| Filter by service_code | [optional] 
 **filter_shadow_bookings** | **str**| Filter by shadow_bookings | [optional] 

### Return type

[**ShippingRatesGet200Response**](ShippingRatesGet200Response.md)

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

# **shipping_rates_id_delete**
> ShippingRatesIdGet200Response shipping_rates_id_delete(id)

Delete a Shipping Rate

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.shipping_rates_id_get200_response import ShippingRatesIdGet200Response
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
    api_instance = openapi_client.ShippingRateApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Shipping Rate
        api_response = api_instance.shipping_rates_id_delete(id)
        print("The response of ShippingRateApi->shipping_rates_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateApi->shipping_rates_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingRatesIdGet200Response**](ShippingRatesIdGet200Response.md)

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

# **shipping_rates_id_get**
> ShippingRatesIdGet200Response shipping_rates_id_get(id)

Show a single Shipping Rate

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.shipping_rates_id_get200_response import ShippingRatesIdGet200Response
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
    api_instance = openapi_client.ShippingRateApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipping Rate
        api_response = api_instance.shipping_rates_id_get(id)
        print("The response of ShippingRateApi->shipping_rates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateApi->shipping_rates_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingRatesIdGet200Response**](ShippingRatesIdGet200Response.md)

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

# **shipping_rates_id_patch**
> ShippingRatesIdGet200Response shipping_rates_id_patch(id, shipping_rates_id_patch_request)

Update a Shipping Rate

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.shipping_rates_id_get200_response import ShippingRatesIdGet200Response
from openapi_client.models.shipping_rates_id_patch_request import ShippingRatesIdPatchRequest
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
    api_instance = openapi_client.ShippingRateApi(api_client)
    id = 56 # int | 
    shipping_rates_id_patch_request = openapi_client.ShippingRatesIdPatchRequest() # ShippingRatesIdPatchRequest | 

    try:
        # Update a Shipping Rate
        api_response = api_instance.shipping_rates_id_patch(id, shipping_rates_id_patch_request)
        print("The response of ShippingRateApi->shipping_rates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateApi->shipping_rates_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shipping_rates_id_patch_request** | [**ShippingRatesIdPatchRequest**](ShippingRatesIdPatchRequest.md)|  | 

### Return type

[**ShippingRatesIdGet200Response**](ShippingRatesIdGet200Response.md)

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

# **shipping_rates_post**
> ShippingRatesIdGet200Response shipping_rates_post(shipping_rates_post_request)

Create a Shipping Rate

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.shipping_rates_id_get200_response import ShippingRatesIdGet200Response
from openapi_client.models.shipping_rates_post_request import ShippingRatesPostRequest
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
    api_instance = openapi_client.ShippingRateApi(api_client)
    shipping_rates_post_request = openapi_client.ShippingRatesPostRequest() # ShippingRatesPostRequest | 

    try:
        # Create a Shipping Rate
        api_response = api_instance.shipping_rates_post(shipping_rates_post_request)
        print("The response of ShippingRateApi->shipping_rates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateApi->shipping_rates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_rates_post_request** | [**ShippingRatesPostRequest**](ShippingRatesPostRequest.md)|  | 

### Return type

[**ShippingRatesIdGet200Response**](ShippingRatesIdGet200Response.md)

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


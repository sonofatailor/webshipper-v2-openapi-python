# webshipperv2.ShippingRateExpressionApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressions_get**](ShippingRateExpressionApi.md#expressions_get) | **GET** /expressions | List all Shipping Rate Expressions
[**expressions_id_delete**](ShippingRateExpressionApi.md#expressions_id_delete) | **DELETE** /expressions/{id} | Delete a Shipping Rate Expression
[**expressions_id_get**](ShippingRateExpressionApi.md#expressions_id_get) | **GET** /expressions/{id} | Show a single Shipping Rate Expression
[**expressions_id_patch**](ShippingRateExpressionApi.md#expressions_id_patch) | **PATCH** /expressions/{id} | Update a Shipping Rate Expression
[**expressions_post**](ShippingRateExpressionApi.md#expressions_post) | **POST** /expressions | Create a Shipping Rate Expression


# **expressions_get**
> ExpressionsGet200Response expressions_get(filter_id=filter_id)

List all Shipping Rate Expressions

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.expressions_get200_response import ExpressionsGet200Response
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
    api_instance = webshipperv2.ShippingRateExpressionApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Shipping Rate Expressions
        api_response = api_instance.expressions_get(filter_id=filter_id)
        print("The response of ShippingRateExpressionApi->expressions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateExpressionApi->expressions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ExpressionsGet200Response**](ExpressionsGet200Response.md)

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

# **expressions_id_delete**
> ExpressionsIdGet200Response expressions_id_delete(id)

Delete a Shipping Rate Expression

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.expressions_id_get200_response import ExpressionsIdGet200Response
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
    api_instance = webshipperv2.ShippingRateExpressionApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Shipping Rate Expression
        api_response = api_instance.expressions_id_delete(id)
        print("The response of ShippingRateExpressionApi->expressions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateExpressionApi->expressions_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExpressionsIdGet200Response**](ExpressionsIdGet200Response.md)

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

# **expressions_id_get**
> ExpressionsIdGet200Response expressions_id_get(id)

Show a single Shipping Rate Expression

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.expressions_id_get200_response import ExpressionsIdGet200Response
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
    api_instance = webshipperv2.ShippingRateExpressionApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipping Rate Expression
        api_response = api_instance.expressions_id_get(id)
        print("The response of ShippingRateExpressionApi->expressions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateExpressionApi->expressions_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExpressionsIdGet200Response**](ExpressionsIdGet200Response.md)

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

# **expressions_id_patch**
> ExpressionsIdGet200Response expressions_id_patch(id, expressions_id_patch_request)

Update a Shipping Rate Expression

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.expressions_id_get200_response import ExpressionsIdGet200Response
from webshipperv2.models.expressions_id_patch_request import ExpressionsIdPatchRequest
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
    api_instance = webshipperv2.ShippingRateExpressionApi(api_client)
    id = 56 # int | 
    expressions_id_patch_request = webshipperv2.ExpressionsIdPatchRequest() # ExpressionsIdPatchRequest | 

    try:
        # Update a Shipping Rate Expression
        api_response = api_instance.expressions_id_patch(id, expressions_id_patch_request)
        print("The response of ShippingRateExpressionApi->expressions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateExpressionApi->expressions_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **expressions_id_patch_request** | [**ExpressionsIdPatchRequest**](ExpressionsIdPatchRequest.md)|  | 

### Return type

[**ExpressionsIdGet200Response**](ExpressionsIdGet200Response.md)

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

# **expressions_post**
> ExpressionsIdGet200Response expressions_post(expressions_post_request)

Create a Shipping Rate Expression

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.expressions_id_get200_response import ExpressionsIdGet200Response
from webshipperv2.models.expressions_post_request import ExpressionsPostRequest
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
    api_instance = webshipperv2.ShippingRateExpressionApi(api_client)
    expressions_post_request = webshipperv2.ExpressionsPostRequest() # ExpressionsPostRequest | 

    try:
        # Create a Shipping Rate Expression
        api_response = api_instance.expressions_post(expressions_post_request)
        print("The response of ShippingRateExpressionApi->expressions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRateExpressionApi->expressions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expressions_post_request** | [**ExpressionsPostRequest**](ExpressionsPostRequest.md)|  | 

### Return type

[**ExpressionsIdGet200Response**](ExpressionsIdGet200Response.md)

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


# openapi_client.OtherApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brands_get**](OtherApi.md#brands_get) | **GET** /brands | List all Others
[**brands_id_delete**](OtherApi.md#brands_id_delete) | **DELETE** /brands/{id} | Delete a Other
[**brands_id_get**](OtherApi.md#brands_id_get) | **GET** /brands/{id} | Show a single Other
[**brands_id_patch**](OtherApi.md#brands_id_patch) | **PATCH** /brands/{id} | Update a Other
[**brands_post**](OtherApi.md#brands_post) | **POST** /brands | Create a Other
[**return_refund_methods_get**](OtherApi.md#return_refund_methods_get) | **GET** /return_refund_methods | List all Others
[**return_refund_methods_id_delete**](OtherApi.md#return_refund_methods_id_delete) | **DELETE** /return_refund_methods/{id} | Delete a Other
[**return_refund_methods_id_get**](OtherApi.md#return_refund_methods_id_get) | **GET** /return_refund_methods/{id} | Show a single Other
[**return_refund_methods_id_patch**](OtherApi.md#return_refund_methods_id_patch) | **PATCH** /return_refund_methods/{id} | Update a Other
[**return_refund_methods_post**](OtherApi.md#return_refund_methods_post) | **POST** /return_refund_methods | Create a Other


# **brands_get**
> BrandsGet200Response brands_get()

List all Others

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.brands_get200_response import BrandsGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)

    try:
        # List all Others
        api_response = api_instance.brands_get()
        print("The response of OtherApi->brands_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->brands_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BrandsGet200Response**](BrandsGet200Response.md)

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

# **brands_id_delete**
> BrandsIdGet200Response brands_id_delete(id)

Delete a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.brands_id_get200_response import BrandsIdGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Other
        api_response = api_instance.brands_id_delete(id)
        print("The response of OtherApi->brands_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->brands_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BrandsIdGet200Response**](BrandsIdGet200Response.md)

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

# **brands_id_get**
> BrandsIdGet200Response brands_id_get(id)

Show a single Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.brands_id_get200_response import BrandsIdGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Other
        api_response = api_instance.brands_id_get(id)
        print("The response of OtherApi->brands_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->brands_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BrandsIdGet200Response**](BrandsIdGet200Response.md)

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

# **brands_id_patch**
> BrandsIdGet200Response brands_id_patch(id, brands_id_patch_request)

Update a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.brands_id_get200_response import BrandsIdGet200Response
from openapi_client.models.brands_id_patch_request import BrandsIdPatchRequest
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 
    brands_id_patch_request = openapi_client.BrandsIdPatchRequest() # BrandsIdPatchRequest | 

    try:
        # Update a Other
        api_response = api_instance.brands_id_patch(id, brands_id_patch_request)
        print("The response of OtherApi->brands_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->brands_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **brands_id_patch_request** | [**BrandsIdPatchRequest**](BrandsIdPatchRequest.md)|  | 

### Return type

[**BrandsIdGet200Response**](BrandsIdGet200Response.md)

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

# **brands_post**
> BrandsIdGet200Response brands_post(brands_post_request)

Create a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.brands_id_get200_response import BrandsIdGet200Response
from openapi_client.models.brands_post_request import BrandsPostRequest
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
    api_instance = openapi_client.OtherApi(api_client)
    brands_post_request = openapi_client.BrandsPostRequest() # BrandsPostRequest | 

    try:
        # Create a Other
        api_response = api_instance.brands_post(brands_post_request)
        print("The response of OtherApi->brands_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->brands_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brands_post_request** | [**BrandsPostRequest**](BrandsPostRequest.md)|  | 

### Return type

[**BrandsIdGet200Response**](BrandsIdGet200Response.md)

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

# **return_refund_methods_get**
> ReturnRefundMethodsGet200Response return_refund_methods_get(filter_id=filter_id)

List all Others

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_refund_methods_get200_response import ReturnRefundMethodsGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Others
        api_response = api_instance.return_refund_methods_get(filter_id=filter_id)
        print("The response of OtherApi->return_refund_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->return_refund_methods_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ReturnRefundMethodsGet200Response**](ReturnRefundMethodsGet200Response.md)

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

# **return_refund_methods_id_delete**
> ReturnRefundMethodsIdGet200Response return_refund_methods_id_delete(id)

Delete a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_refund_methods_id_get200_response import ReturnRefundMethodsIdGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Other
        api_response = api_instance.return_refund_methods_id_delete(id)
        print("The response of OtherApi->return_refund_methods_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->return_refund_methods_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnRefundMethodsIdGet200Response**](ReturnRefundMethodsIdGet200Response.md)

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

# **return_refund_methods_id_get**
> ReturnRefundMethodsIdGet200Response return_refund_methods_id_get(id)

Show a single Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_refund_methods_id_get200_response import ReturnRefundMethodsIdGet200Response
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Other
        api_response = api_instance.return_refund_methods_id_get(id)
        print("The response of OtherApi->return_refund_methods_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->return_refund_methods_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnRefundMethodsIdGet200Response**](ReturnRefundMethodsIdGet200Response.md)

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

# **return_refund_methods_id_patch**
> ReturnRefundMethodsIdGet200Response return_refund_methods_id_patch(id, return_refund_methods_id_patch_request)

Update a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_refund_methods_id_get200_response import ReturnRefundMethodsIdGet200Response
from openapi_client.models.return_refund_methods_id_patch_request import ReturnRefundMethodsIdPatchRequest
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
    api_instance = openapi_client.OtherApi(api_client)
    id = 56 # int | 
    return_refund_methods_id_patch_request = openapi_client.ReturnRefundMethodsIdPatchRequest() # ReturnRefundMethodsIdPatchRequest | 

    try:
        # Update a Other
        api_response = api_instance.return_refund_methods_id_patch(id, return_refund_methods_id_patch_request)
        print("The response of OtherApi->return_refund_methods_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->return_refund_methods_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **return_refund_methods_id_patch_request** | [**ReturnRefundMethodsIdPatchRequest**](ReturnRefundMethodsIdPatchRequest.md)|  | 

### Return type

[**ReturnRefundMethodsIdGet200Response**](ReturnRefundMethodsIdGet200Response.md)

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

# **return_refund_methods_post**
> ReturnRefundMethodsIdGet200Response return_refund_methods_post(return_refund_methods_post_request)

Create a Other

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_refund_methods_id_get200_response import ReturnRefundMethodsIdGet200Response
from openapi_client.models.return_refund_methods_post_request import ReturnRefundMethodsPostRequest
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
    api_instance = openapi_client.OtherApi(api_client)
    return_refund_methods_post_request = openapi_client.ReturnRefundMethodsPostRequest() # ReturnRefundMethodsPostRequest | 

    try:
        # Create a Other
        api_response = api_instance.return_refund_methods_post(return_refund_methods_post_request)
        print("The response of OtherApi->return_refund_methods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OtherApi->return_refund_methods_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_refund_methods_post_request** | [**ReturnRefundMethodsPostRequest**](ReturnRefundMethodsPostRequest.md)|  | 

### Return type

[**ReturnRefundMethodsIdGet200Response**](ReturnRefundMethodsIdGet200Response.md)

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


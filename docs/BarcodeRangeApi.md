# openapi_client.BarcodeRangeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode_ranges_get**](BarcodeRangeApi.md#barcode_ranges_get) | **GET** /barcode_ranges | List all Barcode Ranges
[**barcode_ranges_id_delete**](BarcodeRangeApi.md#barcode_ranges_id_delete) | **DELETE** /barcode_ranges/{id} | Delete a Barcode Range
[**barcode_ranges_id_get**](BarcodeRangeApi.md#barcode_ranges_id_get) | **GET** /barcode_ranges/{id} | Show a single Barcode Range
[**barcode_ranges_id_patch**](BarcodeRangeApi.md#barcode_ranges_id_patch) | **PATCH** /barcode_ranges/{id} | Update a Barcode Range
[**barcode_ranges_post**](BarcodeRangeApi.md#barcode_ranges_post) | **POST** /barcode_ranges | Create a Barcode Range


# **barcode_ranges_get**
> BarcodeRangesGet200Response barcode_ranges_get(filter_id=filter_id)

List all Barcode Ranges

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.barcode_ranges_get200_response import BarcodeRangesGet200Response
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
    api_instance = openapi_client.BarcodeRangeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Barcode Ranges
        api_response = api_instance.barcode_ranges_get(filter_id=filter_id)
        print("The response of BarcodeRangeApi->barcode_ranges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodeRangeApi->barcode_ranges_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**BarcodeRangesGet200Response**](BarcodeRangesGet200Response.md)

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

# **barcode_ranges_id_delete**
> BarcodeRangesIdGet200Response barcode_ranges_id_delete(id)

Delete a Barcode Range

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.barcode_ranges_id_get200_response import BarcodeRangesIdGet200Response
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
    api_instance = openapi_client.BarcodeRangeApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Barcode Range
        api_response = api_instance.barcode_ranges_id_delete(id)
        print("The response of BarcodeRangeApi->barcode_ranges_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodeRangeApi->barcode_ranges_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BarcodeRangesIdGet200Response**](BarcodeRangesIdGet200Response.md)

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

# **barcode_ranges_id_get**
> BarcodeRangesIdGet200Response barcode_ranges_id_get(id)

Show a single Barcode Range

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.barcode_ranges_id_get200_response import BarcodeRangesIdGet200Response
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
    api_instance = openapi_client.BarcodeRangeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Barcode Range
        api_response = api_instance.barcode_ranges_id_get(id)
        print("The response of BarcodeRangeApi->barcode_ranges_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodeRangeApi->barcode_ranges_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BarcodeRangesIdGet200Response**](BarcodeRangesIdGet200Response.md)

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

# **barcode_ranges_id_patch**
> BarcodeRangesIdGet200Response barcode_ranges_id_patch(id, barcode_ranges_id_patch_request)

Update a Barcode Range

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.barcode_ranges_id_get200_response import BarcodeRangesIdGet200Response
from openapi_client.models.barcode_ranges_id_patch_request import BarcodeRangesIdPatchRequest
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
    api_instance = openapi_client.BarcodeRangeApi(api_client)
    id = 56 # int | 
    barcode_ranges_id_patch_request = openapi_client.BarcodeRangesIdPatchRequest() # BarcodeRangesIdPatchRequest | 

    try:
        # Update a Barcode Range
        api_response = api_instance.barcode_ranges_id_patch(id, barcode_ranges_id_patch_request)
        print("The response of BarcodeRangeApi->barcode_ranges_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodeRangeApi->barcode_ranges_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **barcode_ranges_id_patch_request** | [**BarcodeRangesIdPatchRequest**](BarcodeRangesIdPatchRequest.md)|  | 

### Return type

[**BarcodeRangesIdGet200Response**](BarcodeRangesIdGet200Response.md)

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

# **barcode_ranges_post**
> BarcodeRangesIdGet200Response barcode_ranges_post(barcode_ranges_post_request)

Create a Barcode Range

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.barcode_ranges_id_get200_response import BarcodeRangesIdGet200Response
from openapi_client.models.barcode_ranges_post_request import BarcodeRangesPostRequest
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
    api_instance = openapi_client.BarcodeRangeApi(api_client)
    barcode_ranges_post_request = openapi_client.BarcodeRangesPostRequest() # BarcodeRangesPostRequest | 

    try:
        # Create a Barcode Range
        api_response = api_instance.barcode_ranges_post(barcode_ranges_post_request)
        print("The response of BarcodeRangeApi->barcode_ranges_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarcodeRangeApi->barcode_ranges_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode_ranges_post_request** | [**BarcodeRangesPostRequest**](BarcodeRangesPostRequest.md)|  | 

### Return type

[**BarcodeRangesIdGet200Response**](BarcodeRangesIdGet200Response.md)

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


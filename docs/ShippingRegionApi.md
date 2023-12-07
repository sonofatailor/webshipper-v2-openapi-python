# openapi_client.ShippingRegionApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regions_get**](ShippingRegionApi.md#regions_get) | **GET** /regions | List all Shipping Regions
[**regions_id_delete**](ShippingRegionApi.md#regions_id_delete) | **DELETE** /regions/{id} | Delete a Shipping Region
[**regions_id_get**](ShippingRegionApi.md#regions_id_get) | **GET** /regions/{id} | Show a single Shipping Region
[**regions_id_patch**](ShippingRegionApi.md#regions_id_patch) | **PATCH** /regions/{id} | Update a Shipping Region
[**regions_post**](ShippingRegionApi.md#regions_post) | **POST** /regions | Create a Shipping Region


# **regions_get**
> RegionsGet200Response regions_get(filter_id=filter_id)

List all Shipping Regions

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.regions_get200_response import RegionsGet200Response
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
    api_instance = openapi_client.ShippingRegionApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Shipping Regions
        api_response = api_instance.regions_get(filter_id=filter_id)
        print("The response of ShippingRegionApi->regions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionApi->regions_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**RegionsGet200Response**](RegionsGet200Response.md)

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

# **regions_id_delete**
> RegionsIdGet200Response regions_id_delete(id)

Delete a Shipping Region

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.regions_id_get200_response import RegionsIdGet200Response
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
    api_instance = openapi_client.ShippingRegionApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Shipping Region
        api_response = api_instance.regions_id_delete(id)
        print("The response of ShippingRegionApi->regions_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionApi->regions_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RegionsIdGet200Response**](RegionsIdGet200Response.md)

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

# **regions_id_get**
> RegionsIdGet200Response regions_id_get(id)

Show a single Shipping Region

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.regions_id_get200_response import RegionsIdGet200Response
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
    api_instance = openapi_client.ShippingRegionApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipping Region
        api_response = api_instance.regions_id_get(id)
        print("The response of ShippingRegionApi->regions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionApi->regions_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RegionsIdGet200Response**](RegionsIdGet200Response.md)

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

# **regions_id_patch**
> RegionsIdGet200Response regions_id_patch(id, regions_id_patch_request)

Update a Shipping Region

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.regions_id_get200_response import RegionsIdGet200Response
from openapi_client.models.regions_id_patch_request import RegionsIdPatchRequest
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
    api_instance = openapi_client.ShippingRegionApi(api_client)
    id = 56 # int | 
    regions_id_patch_request = openapi_client.RegionsIdPatchRequest() # RegionsIdPatchRequest | 

    try:
        # Update a Shipping Region
        api_response = api_instance.regions_id_patch(id, regions_id_patch_request)
        print("The response of ShippingRegionApi->regions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionApi->regions_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **regions_id_patch_request** | [**RegionsIdPatchRequest**](RegionsIdPatchRequest.md)|  | 

### Return type

[**RegionsIdGet200Response**](RegionsIdGet200Response.md)

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

# **regions_post**
> RegionsIdGet200Response regions_post(regions_post_request)

Create a Shipping Region

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.regions_id_get200_response import RegionsIdGet200Response
from openapi_client.models.regions_post_request import RegionsPostRequest
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
    api_instance = openapi_client.ShippingRegionApi(api_client)
    regions_post_request = openapi_client.RegionsPostRequest() # RegionsPostRequest | 

    try:
        # Create a Shipping Region
        api_response = api_instance.regions_post(regions_post_request)
        print("The response of ShippingRegionApi->regions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingRegionApi->regions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions_post_request** | [**RegionsPostRequest**](RegionsPostRequest.md)|  | 

### Return type

[**RegionsIdGet200Response**](RegionsIdGet200Response.md)

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


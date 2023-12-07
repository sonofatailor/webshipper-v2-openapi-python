# openapi_client.PickupApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pickups_get**](PickupApi.md#pickups_get) | **GET** /pickups | List all Pickups
[**pickups_id_delete**](PickupApi.md#pickups_id_delete) | **DELETE** /pickups/{id} | Delete a Pickup
[**pickups_id_get**](PickupApi.md#pickups_id_get) | **GET** /pickups/{id} | Show a single Pickup
[**pickups_id_patch**](PickupApi.md#pickups_id_patch) | **PATCH** /pickups/{id} | Update a Pickup
[**pickups_post**](PickupApi.md#pickups_post) | **POST** /pickups | Create a Pickup


# **pickups_get**
> PickupsGet200Response pickups_get(filter_id=filter_id)

List all Pickups

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.pickups_get200_response import PickupsGet200Response
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
    api_instance = openapi_client.PickupApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Pickups
        api_response = api_instance.pickups_get(filter_id=filter_id)
        print("The response of PickupApi->pickups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->pickups_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**PickupsGet200Response**](PickupsGet200Response.md)

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

# **pickups_id_delete**
> PickupsIdGet200Response pickups_id_delete(id)

Delete a Pickup

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.pickups_id_get200_response import PickupsIdGet200Response
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
    api_instance = openapi_client.PickupApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Pickup
        api_response = api_instance.pickups_id_delete(id)
        print("The response of PickupApi->pickups_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->pickups_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PickupsIdGet200Response**](PickupsIdGet200Response.md)

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

# **pickups_id_get**
> PickupsIdGet200Response pickups_id_get(id)

Show a single Pickup

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.pickups_id_get200_response import PickupsIdGet200Response
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
    api_instance = openapi_client.PickupApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Pickup
        api_response = api_instance.pickups_id_get(id)
        print("The response of PickupApi->pickups_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->pickups_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PickupsIdGet200Response**](PickupsIdGet200Response.md)

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

# **pickups_id_patch**
> PickupsIdGet200Response pickups_id_patch(id, pickups_id_patch_request)

Update a Pickup

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.pickups_id_get200_response import PickupsIdGet200Response
from openapi_client.models.pickups_id_patch_request import PickupsIdPatchRequest
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
    api_instance = openapi_client.PickupApi(api_client)
    id = 56 # int | 
    pickups_id_patch_request = openapi_client.PickupsIdPatchRequest() # PickupsIdPatchRequest | 

    try:
        # Update a Pickup
        api_response = api_instance.pickups_id_patch(id, pickups_id_patch_request)
        print("The response of PickupApi->pickups_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->pickups_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **pickups_id_patch_request** | [**PickupsIdPatchRequest**](PickupsIdPatchRequest.md)|  | 

### Return type

[**PickupsIdGet200Response**](PickupsIdGet200Response.md)

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

# **pickups_post**
> PickupsIdGet200Response pickups_post(pickups_post_request)

Create a Pickup

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.pickups_id_get200_response import PickupsIdGet200Response
from openapi_client.models.pickups_post_request import PickupsPostRequest
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
    api_instance = openapi_client.PickupApi(api_client)
    pickups_post_request = openapi_client.PickupsPostRequest() # PickupsPostRequest | 

    try:
        # Create a Pickup
        api_response = api_instance.pickups_post(pickups_post_request)
        print("The response of PickupApi->pickups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->pickups_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickups_post_request** | [**PickupsPostRequest**](PickupsPostRequest.md)|  | 

### Return type

[**PickupsIdGet200Response**](PickupsIdGet200Response.md)

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


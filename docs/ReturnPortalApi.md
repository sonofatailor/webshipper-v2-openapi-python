# openapi_client.ReturnPortalApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_portals_get**](ReturnPortalApi.md#return_portals_get) | **GET** /return_portals | List all Return Portals
[**return_portals_id_delete**](ReturnPortalApi.md#return_portals_id_delete) | **DELETE** /return_portals/{id} | Delete a Return Portal
[**return_portals_id_get**](ReturnPortalApi.md#return_portals_id_get) | **GET** /return_portals/{id} | Show a single Return Portal
[**return_portals_id_patch**](ReturnPortalApi.md#return_portals_id_patch) | **PATCH** /return_portals/{id} | Update a Return Portal
[**return_portals_post**](ReturnPortalApi.md#return_portals_post) | **POST** /return_portals | Create a Return Portal


# **return_portals_get**
> ReturnPortalsGet200Response return_portals_get(filter_id=filter_id)

List all Return Portals

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_portals_get200_response import ReturnPortalsGet200Response
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
    api_instance = openapi_client.ReturnPortalApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Return Portals
        api_response = api_instance.return_portals_get(filter_id=filter_id)
        print("The response of ReturnPortalApi->return_portals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPortalApi->return_portals_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ReturnPortalsGet200Response**](ReturnPortalsGet200Response.md)

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

# **return_portals_id_delete**
> ReturnPortalsIdGet200Response return_portals_id_delete(id)

Delete a Return Portal

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_portals_id_get200_response import ReturnPortalsIdGet200Response
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
    api_instance = openapi_client.ReturnPortalApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Return Portal
        api_response = api_instance.return_portals_id_delete(id)
        print("The response of ReturnPortalApi->return_portals_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPortalApi->return_portals_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnPortalsIdGet200Response**](ReturnPortalsIdGet200Response.md)

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

# **return_portals_id_get**
> ReturnPortalsIdGet200Response return_portals_id_get(id)

Show a single Return Portal

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_portals_id_get200_response import ReturnPortalsIdGet200Response
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
    api_instance = openapi_client.ReturnPortalApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Return Portal
        api_response = api_instance.return_portals_id_get(id)
        print("The response of ReturnPortalApi->return_portals_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPortalApi->return_portals_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnPortalsIdGet200Response**](ReturnPortalsIdGet200Response.md)

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

# **return_portals_id_patch**
> ReturnPortalsIdGet200Response return_portals_id_patch(id, return_portals_id_patch_request)

Update a Return Portal

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_portals_id_get200_response import ReturnPortalsIdGet200Response
from openapi_client.models.return_portals_id_patch_request import ReturnPortalsIdPatchRequest
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
    api_instance = openapi_client.ReturnPortalApi(api_client)
    id = 56 # int | 
    return_portals_id_patch_request = openapi_client.ReturnPortalsIdPatchRequest() # ReturnPortalsIdPatchRequest | 

    try:
        # Update a Return Portal
        api_response = api_instance.return_portals_id_patch(id, return_portals_id_patch_request)
        print("The response of ReturnPortalApi->return_portals_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPortalApi->return_portals_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **return_portals_id_patch_request** | [**ReturnPortalsIdPatchRequest**](ReturnPortalsIdPatchRequest.md)|  | 

### Return type

[**ReturnPortalsIdGet200Response**](ReturnPortalsIdGet200Response.md)

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

# **return_portals_post**
> ReturnPortalsIdGet200Response return_portals_post(return_portals_post_request)

Create a Return Portal

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.return_portals_id_get200_response import ReturnPortalsIdGet200Response
from openapi_client.models.return_portals_post_request import ReturnPortalsPostRequest
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
    api_instance = openapi_client.ReturnPortalApi(api_client)
    return_portals_post_request = openapi_client.ReturnPortalsPostRequest() # ReturnPortalsPostRequest | 

    try:
        # Create a Return Portal
        api_response = api_instance.return_portals_post(return_portals_post_request)
        print("The response of ReturnPortalApi->return_portals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnPortalApi->return_portals_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_portals_post_request** | [**ReturnPortalsPostRequest**](ReturnPortalsPostRequest.md)|  | 

### Return type

[**ReturnPortalsIdGet200Response**](ReturnPortalsIdGet200Response.md)

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


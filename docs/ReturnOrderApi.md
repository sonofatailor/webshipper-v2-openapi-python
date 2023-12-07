# webshipperv2.ReturnOrderApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**returns_get**](ReturnOrderApi.md#returns_get) | **GET** /returns | List all Return Orders
[**returns_id_delete**](ReturnOrderApi.md#returns_id_delete) | **DELETE** /returns/{id} | Delete a Return Order
[**returns_id_get**](ReturnOrderApi.md#returns_id_get) | **GET** /returns/{id} | Show a single Return Order
[**returns_id_patch**](ReturnOrderApi.md#returns_id_patch) | **PATCH** /returns/{id} | Update a Return Order
[**returns_post**](ReturnOrderApi.md#returns_post) | **POST** /returns | Create a Return Order


# **returns_get**
> ReturnsGet200Response returns_get(filter_id=filter_id, filter_secret=filter_secret, filter_activity_type=filter_activity_type, filter_status=filter_status, filter_portal_id=filter_portal_id, filter_free_text=filter_free_text, filter_return_causes=filter_return_causes)

List all Return Orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.returns_get200_response import ReturnsGet200Response
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
    api_instance = webshipperv2.ReturnOrderApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_secret = 'filter_secret_example' # str | Filter by secret (optional)
    filter_activity_type = 'filter_activity_type_example' # str | Filter by activity_type (optional)
    filter_status = 'filter_status_example' # str | Filter by status (optional)
    filter_portal_id = 'filter_portal_id_example' # str | Filter by portal_id (optional)
    filter_free_text = 'filter_free_text_example' # str | Filter by free_text (optional)
    filter_return_causes = 'filter_return_causes_example' # str | Filter by return_causes (optional)

    try:
        # List all Return Orders
        api_response = api_instance.returns_get(filter_id=filter_id, filter_secret=filter_secret, filter_activity_type=filter_activity_type, filter_status=filter_status, filter_portal_id=filter_portal_id, filter_free_text=filter_free_text, filter_return_causes=filter_return_causes)
        print("The response of ReturnOrderApi->returns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnOrderApi->returns_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_secret** | **str**| Filter by secret | [optional] 
 **filter_activity_type** | **str**| Filter by activity_type | [optional] 
 **filter_status** | **str**| Filter by status | [optional] 
 **filter_portal_id** | **str**| Filter by portal_id | [optional] 
 **filter_free_text** | **str**| Filter by free_text | [optional] 
 **filter_return_causes** | **str**| Filter by return_causes | [optional] 

### Return type

[**ReturnsGet200Response**](ReturnsGet200Response.md)

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

# **returns_id_delete**
> ReturnsIdGet200Response returns_id_delete(id)

Delete a Return Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.returns_id_get200_response import ReturnsIdGet200Response
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
    api_instance = webshipperv2.ReturnOrderApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Return Order
        api_response = api_instance.returns_id_delete(id)
        print("The response of ReturnOrderApi->returns_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnOrderApi->returns_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnsIdGet200Response**](ReturnsIdGet200Response.md)

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

# **returns_id_get**
> ReturnsIdGet200Response returns_id_get(id)

Show a single Return Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.returns_id_get200_response import ReturnsIdGet200Response
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
    api_instance = webshipperv2.ReturnOrderApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Return Order
        api_response = api_instance.returns_id_get(id)
        print("The response of ReturnOrderApi->returns_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnOrderApi->returns_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReturnsIdGet200Response**](ReturnsIdGet200Response.md)

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

# **returns_id_patch**
> ReturnsIdGet200Response returns_id_patch(id, returns_id_patch_request)

Update a Return Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.returns_id_get200_response import ReturnsIdGet200Response
from webshipperv2.models.returns_id_patch_request import ReturnsIdPatchRequest
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
    api_instance = webshipperv2.ReturnOrderApi(api_client)
    id = 56 # int | 
    returns_id_patch_request = webshipperv2.ReturnsIdPatchRequest() # ReturnsIdPatchRequest | 

    try:
        # Update a Return Order
        api_response = api_instance.returns_id_patch(id, returns_id_patch_request)
        print("The response of ReturnOrderApi->returns_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnOrderApi->returns_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **returns_id_patch_request** | [**ReturnsIdPatchRequest**](ReturnsIdPatchRequest.md)|  | 

### Return type

[**ReturnsIdGet200Response**](ReturnsIdGet200Response.md)

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

# **returns_post**
> ReturnsIdGet200Response returns_post(returns_post_request)

Create a Return Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.returns_id_get200_response import ReturnsIdGet200Response
from webshipperv2.models.returns_post_request import ReturnsPostRequest
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
    api_instance = webshipperv2.ReturnOrderApi(api_client)
    returns_post_request = webshipperv2.ReturnsPostRequest() # ReturnsPostRequest | 

    try:
        # Create a Return Order
        api_response = api_instance.returns_post(returns_post_request)
        print("The response of ReturnOrderApi->returns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnOrderApi->returns_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_post_request** | [**ReturnsPostRequest**](ReturnsPostRequest.md)|  | 

### Return type

[**ReturnsIdGet200Response**](ReturnsIdGet200Response.md)

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


# openapi_client.TriggerApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_get**](TriggerApi.md#triggers_get) | **GET** /triggers | List all Triggers
[**triggers_id_delete**](TriggerApi.md#triggers_id_delete) | **DELETE** /triggers/{id} | Delete a Trigger
[**triggers_id_get**](TriggerApi.md#triggers_id_get) | **GET** /triggers/{id} | Show a single Trigger
[**triggers_id_patch**](TriggerApi.md#triggers_id_patch) | **PATCH** /triggers/{id} | Update a Trigger
[**triggers_post**](TriggerApi.md#triggers_post) | **POST** /triggers | Create a Trigger


# **triggers_get**
> TriggersGet200Response triggers_get(filter_id=filter_id)

List all Triggers

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.triggers_get200_response import TriggersGet200Response
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
    api_instance = openapi_client.TriggerApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Triggers
        api_response = api_instance.triggers_get(filter_id=filter_id)
        print("The response of TriggerApi->triggers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggerApi->triggers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**TriggersGet200Response**](TriggersGet200Response.md)

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

# **triggers_id_delete**
> TriggersIdGet200Response triggers_id_delete(id)

Delete a Trigger

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.triggers_id_get200_response import TriggersIdGet200Response
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
    api_instance = openapi_client.TriggerApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Trigger
        api_response = api_instance.triggers_id_delete(id)
        print("The response of TriggerApi->triggers_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggerApi->triggers_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TriggersIdGet200Response**](TriggersIdGet200Response.md)

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

# **triggers_id_get**
> TriggersIdGet200Response triggers_id_get(id)

Show a single Trigger

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.triggers_id_get200_response import TriggersIdGet200Response
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
    api_instance = openapi_client.TriggerApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Trigger
        api_response = api_instance.triggers_id_get(id)
        print("The response of TriggerApi->triggers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggerApi->triggers_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TriggersIdGet200Response**](TriggersIdGet200Response.md)

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

# **triggers_id_patch**
> TriggersIdGet200Response triggers_id_patch(id, triggers_id_patch_request)

Update a Trigger

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.triggers_id_get200_response import TriggersIdGet200Response
from openapi_client.models.triggers_id_patch_request import TriggersIdPatchRequest
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
    api_instance = openapi_client.TriggerApi(api_client)
    id = 56 # int | 
    triggers_id_patch_request = openapi_client.TriggersIdPatchRequest() # TriggersIdPatchRequest | 

    try:
        # Update a Trigger
        api_response = api_instance.triggers_id_patch(id, triggers_id_patch_request)
        print("The response of TriggerApi->triggers_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggerApi->triggers_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **triggers_id_patch_request** | [**TriggersIdPatchRequest**](TriggersIdPatchRequest.md)|  | 

### Return type

[**TriggersIdGet200Response**](TriggersIdGet200Response.md)

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

# **triggers_post**
> TriggersIdGet200Response triggers_post(triggers_post_request)

Create a Trigger

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.triggers_id_get200_response import TriggersIdGet200Response
from openapi_client.models.triggers_post_request import TriggersPostRequest
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
    api_instance = openapi_client.TriggerApi(api_client)
    triggers_post_request = openapi_client.TriggersPostRequest() # TriggersPostRequest | 

    try:
        # Create a Trigger
        api_response = api_instance.triggers_post(triggers_post_request)
        print("The response of TriggerApi->triggers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggerApi->triggers_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triggers_post_request** | [**TriggersPostRequest**](TriggersPostRequest.md)|  | 

### Return type

[**TriggersIdGet200Response**](TriggersIdGet200Response.md)

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


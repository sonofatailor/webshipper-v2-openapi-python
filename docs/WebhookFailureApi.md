# openapi_client.WebhookFailureApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_failures_get**](WebhookFailureApi.md#webhook_failures_get) | **GET** /webhook_failures | List all Webhook Failures
[**webhook_failures_id_delete**](WebhookFailureApi.md#webhook_failures_id_delete) | **DELETE** /webhook_failures/{id} | Delete a Webhook Failure
[**webhook_failures_id_get**](WebhookFailureApi.md#webhook_failures_id_get) | **GET** /webhook_failures/{id} | Show a single Webhook Failure
[**webhook_failures_id_patch**](WebhookFailureApi.md#webhook_failures_id_patch) | **PATCH** /webhook_failures/{id} | Update a Webhook Failure
[**webhook_failures_post**](WebhookFailureApi.md#webhook_failures_post) | **POST** /webhook_failures | Create a Webhook Failure


# **webhook_failures_get**
> WebhookFailuresGet200Response webhook_failures_get(filter_id=filter_id)

List all Webhook Failures

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_failures_get200_response import WebhookFailuresGet200Response
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
    api_instance = openapi_client.WebhookFailureApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Webhook Failures
        api_response = api_instance.webhook_failures_get(filter_id=filter_id)
        print("The response of WebhookFailureApi->webhook_failures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookFailureApi->webhook_failures_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**WebhookFailuresGet200Response**](WebhookFailuresGet200Response.md)

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

# **webhook_failures_id_delete**
> WebhookFailuresIdGet200Response webhook_failures_id_delete(id)

Delete a Webhook Failure

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_failures_id_get200_response import WebhookFailuresIdGet200Response
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
    api_instance = openapi_client.WebhookFailureApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Webhook Failure
        api_response = api_instance.webhook_failures_id_delete(id)
        print("The response of WebhookFailureApi->webhook_failures_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookFailureApi->webhook_failures_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebhookFailuresIdGet200Response**](WebhookFailuresIdGet200Response.md)

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

# **webhook_failures_id_get**
> WebhookFailuresIdGet200Response webhook_failures_id_get(id)

Show a single Webhook Failure

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_failures_id_get200_response import WebhookFailuresIdGet200Response
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
    api_instance = openapi_client.WebhookFailureApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Webhook Failure
        api_response = api_instance.webhook_failures_id_get(id)
        print("The response of WebhookFailureApi->webhook_failures_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookFailureApi->webhook_failures_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebhookFailuresIdGet200Response**](WebhookFailuresIdGet200Response.md)

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

# **webhook_failures_id_patch**
> WebhookFailuresIdGet200Response webhook_failures_id_patch(id, webhook_failures_id_patch_request)

Update a Webhook Failure

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_failures_id_get200_response import WebhookFailuresIdGet200Response
from openapi_client.models.webhook_failures_id_patch_request import WebhookFailuresIdPatchRequest
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
    api_instance = openapi_client.WebhookFailureApi(api_client)
    id = 56 # int | 
    webhook_failures_id_patch_request = openapi_client.WebhookFailuresIdPatchRequest() # WebhookFailuresIdPatchRequest | 

    try:
        # Update a Webhook Failure
        api_response = api_instance.webhook_failures_id_patch(id, webhook_failures_id_patch_request)
        print("The response of WebhookFailureApi->webhook_failures_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookFailureApi->webhook_failures_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **webhook_failures_id_patch_request** | [**WebhookFailuresIdPatchRequest**](WebhookFailuresIdPatchRequest.md)|  | 

### Return type

[**WebhookFailuresIdGet200Response**](WebhookFailuresIdGet200Response.md)

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

# **webhook_failures_post**
> WebhookFailuresIdGet200Response webhook_failures_post(webhook_failures_post_request)

Create a Webhook Failure

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhook_failures_id_get200_response import WebhookFailuresIdGet200Response
from openapi_client.models.webhook_failures_post_request import WebhookFailuresPostRequest
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
    api_instance = openapi_client.WebhookFailureApi(api_client)
    webhook_failures_post_request = openapi_client.WebhookFailuresPostRequest() # WebhookFailuresPostRequest | 

    try:
        # Create a Webhook Failure
        api_response = api_instance.webhook_failures_post(webhook_failures_post_request)
        print("The response of WebhookFailureApi->webhook_failures_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookFailureApi->webhook_failures_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_failures_post_request** | [**WebhookFailuresPostRequest**](WebhookFailuresPostRequest.md)|  | 

### Return type

[**WebhookFailuresIdGet200Response**](WebhookFailuresIdGet200Response.md)

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


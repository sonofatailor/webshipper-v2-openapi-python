# openapi_client.WebhookApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_get**](WebhookApi.md#webhooks_get) | **GET** /webhooks | List all Webhooks
[**webhooks_id_delete**](WebhookApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Delete a Webhook
[**webhooks_id_get**](WebhookApi.md#webhooks_id_get) | **GET** /webhooks/{id} | Show a single Webhook
[**webhooks_id_patch**](WebhookApi.md#webhooks_id_patch) | **PATCH** /webhooks/{id} | Update a Webhook
[**webhooks_post**](WebhookApi.md#webhooks_post) | **POST** /webhooks | Create a Webhook


# **webhooks_get**
> WebhooksGet200Response webhooks_get(filter_id=filter_id)

List all Webhooks

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhooks_get200_response import WebhooksGet200Response
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
    api_instance = openapi_client.WebhookApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Webhooks
        api_response = api_instance.webhooks_get(filter_id=filter_id)
        print("The response of WebhookApi->webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**WebhooksGet200Response**](WebhooksGet200Response.md)

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

# **webhooks_id_delete**
> WebhooksIdGet200Response webhooks_id_delete(id)

Delete a Webhook

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhooks_id_get200_response import WebhooksIdGet200Response
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
    api_instance = openapi_client.WebhookApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Webhook
        api_response = api_instance.webhooks_id_delete(id)
        print("The response of WebhookApi->webhooks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebhooksIdGet200Response**](WebhooksIdGet200Response.md)

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

# **webhooks_id_get**
> WebhooksIdGet200Response webhooks_id_get(id)

Show a single Webhook

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhooks_id_get200_response import WebhooksIdGet200Response
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
    api_instance = openapi_client.WebhookApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Webhook
        api_response = api_instance.webhooks_id_get(id)
        print("The response of WebhookApi->webhooks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebhooksIdGet200Response**](WebhooksIdGet200Response.md)

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

# **webhooks_id_patch**
> WebhooksIdGet200Response webhooks_id_patch(id, webhooks_id_patch_request)

Update a Webhook

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhooks_id_get200_response import WebhooksIdGet200Response
from openapi_client.models.webhooks_id_patch_request import WebhooksIdPatchRequest
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
    api_instance = openapi_client.WebhookApi(api_client)
    id = 56 # int | 
    webhooks_id_patch_request = openapi_client.WebhooksIdPatchRequest() # WebhooksIdPatchRequest | 

    try:
        # Update a Webhook
        api_response = api_instance.webhooks_id_patch(id, webhooks_id_patch_request)
        print("The response of WebhookApi->webhooks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **webhooks_id_patch_request** | [**WebhooksIdPatchRequest**](WebhooksIdPatchRequest.md)|  | 

### Return type

[**WebhooksIdGet200Response**](WebhooksIdGet200Response.md)

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

# **webhooks_post**
> WebhooksIdGet200Response webhooks_post(webhooks_post_request)

Create a Webhook

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.webhooks_id_get200_response import WebhooksIdGet200Response
from openapi_client.models.webhooks_post_request import WebhooksPostRequest
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
    api_instance = openapi_client.WebhookApi(api_client)
    webhooks_post_request = openapi_client.WebhooksPostRequest() # WebhooksPostRequest | 

    try:
        # Create a Webhook
        api_response = api_instance.webhooks_post(webhooks_post_request)
        print("The response of WebhookApi->webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->webhooks_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_post_request** | [**WebhooksPostRequest**](WebhooksPostRequest.md)|  | 

### Return type

[**WebhooksIdGet200Response**](WebhooksIdGet200Response.md)

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


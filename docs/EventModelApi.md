# webshipperv2.EventModelApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_models_get**](EventModelApi.md#event_models_get) | **GET** /event_models | List all EventModels
[**event_models_id_delete**](EventModelApi.md#event_models_id_delete) | **DELETE** /event_models/{id} | Delete a EventModel
[**event_models_id_get**](EventModelApi.md#event_models_id_get) | **GET** /event_models/{id} | Show a single EventModel
[**event_models_id_patch**](EventModelApi.md#event_models_id_patch) | **PATCH** /event_models/{id} | Update a EventModel
[**event_models_post**](EventModelApi.md#event_models_post) | **POST** /event_models | Create a EventModel


# **event_models_get**
> EventModelsGet200Response event_models_get(filter_id=filter_id)

List all EventModels

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.event_models_get200_response import EventModelsGet200Response
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
    api_instance = webshipperv2.EventModelApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all EventModels
        api_response = api_instance.event_models_get(filter_id=filter_id)
        print("The response of EventModelApi->event_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventModelApi->event_models_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**EventModelsGet200Response**](EventModelsGet200Response.md)

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

# **event_models_id_delete**
> EventModelsIdGet200Response event_models_id_delete(id)

Delete a EventModel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.event_models_id_get200_response import EventModelsIdGet200Response
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
    api_instance = webshipperv2.EventModelApi(api_client)
    id = 56 # int | 

    try:
        # Delete a EventModel
        api_response = api_instance.event_models_id_delete(id)
        print("The response of EventModelApi->event_models_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventModelApi->event_models_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EventModelsIdGet200Response**](EventModelsIdGet200Response.md)

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

# **event_models_id_get**
> EventModelsIdGet200Response event_models_id_get(id)

Show a single EventModel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.event_models_id_get200_response import EventModelsIdGet200Response
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
    api_instance = webshipperv2.EventModelApi(api_client)
    id = 56 # int | 

    try:
        # Show a single EventModel
        api_response = api_instance.event_models_id_get(id)
        print("The response of EventModelApi->event_models_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventModelApi->event_models_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EventModelsIdGet200Response**](EventModelsIdGet200Response.md)

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

# **event_models_id_patch**
> EventModelsIdGet200Response event_models_id_patch(id, event_models_id_patch_request)

Update a EventModel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.event_models_id_get200_response import EventModelsIdGet200Response
from webshipperv2.models.event_models_id_patch_request import EventModelsIdPatchRequest
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
    api_instance = webshipperv2.EventModelApi(api_client)
    id = 56 # int | 
    event_models_id_patch_request = webshipperv2.EventModelsIdPatchRequest() # EventModelsIdPatchRequest | 

    try:
        # Update a EventModel
        api_response = api_instance.event_models_id_patch(id, event_models_id_patch_request)
        print("The response of EventModelApi->event_models_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventModelApi->event_models_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **event_models_id_patch_request** | [**EventModelsIdPatchRequest**](EventModelsIdPatchRequest.md)|  | 

### Return type

[**EventModelsIdGet200Response**](EventModelsIdGet200Response.md)

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

# **event_models_post**
> EventModelsIdGet200Response event_models_post(event_models_post_request)

Create a EventModel

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.event_models_id_get200_response import EventModelsIdGet200Response
from webshipperv2.models.event_models_post_request import EventModelsPostRequest
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
    api_instance = webshipperv2.EventModelApi(api_client)
    event_models_post_request = webshipperv2.EventModelsPostRequest() # EventModelsPostRequest | 

    try:
        # Create a EventModel
        api_response = api_instance.event_models_post(event_models_post_request)
        print("The response of EventModelApi->event_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventModelApi->event_models_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_models_post_request** | [**EventModelsPostRequest**](EventModelsPostRequest.md)|  | 

### Return type

[**EventModelsIdGet200Response**](EventModelsIdGet200Response.md)

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


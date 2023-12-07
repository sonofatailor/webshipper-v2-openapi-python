# webshipperv2.AutomationApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automations_get**](AutomationApi.md#automations_get) | **GET** /automations | List all Automations
[**automations_id_delete**](AutomationApi.md#automations_id_delete) | **DELETE** /automations/{id} | Delete a Automation
[**automations_id_get**](AutomationApi.md#automations_id_get) | **GET** /automations/{id} | Show a single Automation
[**automations_id_patch**](AutomationApi.md#automations_id_patch) | **PATCH** /automations/{id} | Update a Automation
[**automations_post**](AutomationApi.md#automations_post) | **POST** /automations | Create a Automation


# **automations_get**
> AutomationsGet200Response automations_get(filter_id=filter_id)

List all Automations

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_get200_response import AutomationsGet200Response
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
    api_instance = webshipperv2.AutomationApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Automations
        api_response = api_instance.automations_get(filter_id=filter_id)
        print("The response of AutomationApi->automations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->automations_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**AutomationsGet200Response**](AutomationsGet200Response.md)

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

# **automations_id_delete**
> AutomationsIdGet200Response automations_id_delete(id)

Delete a Automation

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_id_get200_response import AutomationsIdGet200Response
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
    api_instance = webshipperv2.AutomationApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Automation
        api_response = api_instance.automations_id_delete(id)
        print("The response of AutomationApi->automations_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->automations_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AutomationsIdGet200Response**](AutomationsIdGet200Response.md)

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

# **automations_id_get**
> AutomationsIdGet200Response automations_id_get(id)

Show a single Automation

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_id_get200_response import AutomationsIdGet200Response
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
    api_instance = webshipperv2.AutomationApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Automation
        api_response = api_instance.automations_id_get(id)
        print("The response of AutomationApi->automations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->automations_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AutomationsIdGet200Response**](AutomationsIdGet200Response.md)

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

# **automations_id_patch**
> AutomationsIdGet200Response automations_id_patch(id, automations_id_patch_request)

Update a Automation

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_id_get200_response import AutomationsIdGet200Response
from webshipperv2.models.automations_id_patch_request import AutomationsIdPatchRequest
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
    api_instance = webshipperv2.AutomationApi(api_client)
    id = 56 # int | 
    automations_id_patch_request = webshipperv2.AutomationsIdPatchRequest() # AutomationsIdPatchRequest | 

    try:
        # Update a Automation
        api_response = api_instance.automations_id_patch(id, automations_id_patch_request)
        print("The response of AutomationApi->automations_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->automations_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **automations_id_patch_request** | [**AutomationsIdPatchRequest**](AutomationsIdPatchRequest.md)|  | 

### Return type

[**AutomationsIdGet200Response**](AutomationsIdGet200Response.md)

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

# **automations_post**
> AutomationsIdGet200Response automations_post(automations_post_request)

Create a Automation

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_id_get200_response import AutomationsIdGet200Response
from webshipperv2.models.automations_post_request import AutomationsPostRequest
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
    api_instance = webshipperv2.AutomationApi(api_client)
    automations_post_request = webshipperv2.AutomationsPostRequest() # AutomationsPostRequest | 

    try:
        # Create a Automation
        api_response = api_instance.automations_post(automations_post_request)
        print("The response of AutomationApi->automations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->automations_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automations_post_request** | [**AutomationsPostRequest**](AutomationsPostRequest.md)|  | 

### Return type

[**AutomationsIdGet200Response**](AutomationsIdGet200Response.md)

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


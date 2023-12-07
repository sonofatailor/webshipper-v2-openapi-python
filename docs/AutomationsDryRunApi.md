# webshipperv2.AutomationsDryRunApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automations_dry_runs_get**](AutomationsDryRunApi.md#automations_dry_runs_get) | **GET** /automations_dry_runs | List all Automations Dry Runs
[**automations_dry_runs_id_delete**](AutomationsDryRunApi.md#automations_dry_runs_id_delete) | **DELETE** /automations_dry_runs/{id} | Delete a Automations Dry Run
[**automations_dry_runs_id_get**](AutomationsDryRunApi.md#automations_dry_runs_id_get) | **GET** /automations_dry_runs/{id} | Show a single Automations Dry Run
[**automations_dry_runs_id_patch**](AutomationsDryRunApi.md#automations_dry_runs_id_patch) | **PATCH** /automations_dry_runs/{id} | Update a Automations Dry Run
[**automations_dry_runs_post**](AutomationsDryRunApi.md#automations_dry_runs_post) | **POST** /automations_dry_runs | Create a Automations Dry Run


# **automations_dry_runs_get**
> AutomationsDryRunsGet200Response automations_dry_runs_get(filter_id=filter_id)

List all Automations Dry Runs

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_dry_runs_get200_response import AutomationsDryRunsGet200Response
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
    api_instance = webshipperv2.AutomationsDryRunApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Automations Dry Runs
        api_response = api_instance.automations_dry_runs_get(filter_id=filter_id)
        print("The response of AutomationsDryRunApi->automations_dry_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsDryRunApi->automations_dry_runs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**AutomationsDryRunsGet200Response**](AutomationsDryRunsGet200Response.md)

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

# **automations_dry_runs_id_delete**
> AutomationsDryRunsIdGet200Response automations_dry_runs_id_delete(id)

Delete a Automations Dry Run

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_dry_runs_id_get200_response import AutomationsDryRunsIdGet200Response
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
    api_instance = webshipperv2.AutomationsDryRunApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Automations Dry Run
        api_response = api_instance.automations_dry_runs_id_delete(id)
        print("The response of AutomationsDryRunApi->automations_dry_runs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsDryRunApi->automations_dry_runs_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AutomationsDryRunsIdGet200Response**](AutomationsDryRunsIdGet200Response.md)

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

# **automations_dry_runs_id_get**
> AutomationsDryRunsIdGet200Response automations_dry_runs_id_get(id)

Show a single Automations Dry Run

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_dry_runs_id_get200_response import AutomationsDryRunsIdGet200Response
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
    api_instance = webshipperv2.AutomationsDryRunApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Automations Dry Run
        api_response = api_instance.automations_dry_runs_id_get(id)
        print("The response of AutomationsDryRunApi->automations_dry_runs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsDryRunApi->automations_dry_runs_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AutomationsDryRunsIdGet200Response**](AutomationsDryRunsIdGet200Response.md)

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

# **automations_dry_runs_id_patch**
> AutomationsDryRunsIdGet200Response automations_dry_runs_id_patch(id, automations_dry_runs_id_patch_request)

Update a Automations Dry Run

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_dry_runs_id_get200_response import AutomationsDryRunsIdGet200Response
from webshipperv2.models.automations_dry_runs_id_patch_request import AutomationsDryRunsIdPatchRequest
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
    api_instance = webshipperv2.AutomationsDryRunApi(api_client)
    id = 56 # int | 
    automations_dry_runs_id_patch_request = webshipperv2.AutomationsDryRunsIdPatchRequest() # AutomationsDryRunsIdPatchRequest | 

    try:
        # Update a Automations Dry Run
        api_response = api_instance.automations_dry_runs_id_patch(id, automations_dry_runs_id_patch_request)
        print("The response of AutomationsDryRunApi->automations_dry_runs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsDryRunApi->automations_dry_runs_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **automations_dry_runs_id_patch_request** | [**AutomationsDryRunsIdPatchRequest**](AutomationsDryRunsIdPatchRequest.md)|  | 

### Return type

[**AutomationsDryRunsIdGet200Response**](AutomationsDryRunsIdGet200Response.md)

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

# **automations_dry_runs_post**
> AutomationsDryRunsIdGet200Response automations_dry_runs_post(automations_dry_runs_post_request)

Create a Automations Dry Run

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.automations_dry_runs_id_get200_response import AutomationsDryRunsIdGet200Response
from webshipperv2.models.automations_dry_runs_post_request import AutomationsDryRunsPostRequest
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
    api_instance = webshipperv2.AutomationsDryRunApi(api_client)
    automations_dry_runs_post_request = webshipperv2.AutomationsDryRunsPostRequest() # AutomationsDryRunsPostRequest | 

    try:
        # Create a Automations Dry Run
        api_response = api_instance.automations_dry_runs_post(automations_dry_runs_post_request)
        print("The response of AutomationsDryRunApi->automations_dry_runs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsDryRunApi->automations_dry_runs_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automations_dry_runs_post_request** | [**AutomationsDryRunsPostRequest**](AutomationsDryRunsPostRequest.md)|  | 

### Return type

[**AutomationsDryRunsIdGet200Response**](AutomationsDryRunsIdGet200Response.md)

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


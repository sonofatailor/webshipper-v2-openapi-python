# openapi_client.SlipTemplateApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slip_templates_get**](SlipTemplateApi.md#slip_templates_get) | **GET** /slip_templates | List all Slip Templates
[**slip_templates_id_delete**](SlipTemplateApi.md#slip_templates_id_delete) | **DELETE** /slip_templates/{id} | Delete a Slip Template
[**slip_templates_id_get**](SlipTemplateApi.md#slip_templates_id_get) | **GET** /slip_templates/{id} | Show a single Slip Template
[**slip_templates_id_patch**](SlipTemplateApi.md#slip_templates_id_patch) | **PATCH** /slip_templates/{id} | Update a Slip Template
[**slip_templates_post**](SlipTemplateApi.md#slip_templates_post) | **POST** /slip_templates | Create a Slip Template


# **slip_templates_get**
> SlipTemplatesGet200Response slip_templates_get(filter_id=filter_id, filter_returns_only=filter_returns_only)

List all Slip Templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.slip_templates_get200_response import SlipTemplatesGet200Response
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
    api_instance = openapi_client.SlipTemplateApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_returns_only = 'filter_returns_only_example' # str | Filter by returns_only (optional)

    try:
        # List all Slip Templates
        api_response = api_instance.slip_templates_get(filter_id=filter_id, filter_returns_only=filter_returns_only)
        print("The response of SlipTemplateApi->slip_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplateApi->slip_templates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_returns_only** | **str**| Filter by returns_only | [optional] 

### Return type

[**SlipTemplatesGet200Response**](SlipTemplatesGet200Response.md)

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

# **slip_templates_id_delete**
> SlipTemplatesIdGet200Response slip_templates_id_delete(id)

Delete a Slip Template

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.slip_templates_id_get200_response import SlipTemplatesIdGet200Response
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
    api_instance = openapi_client.SlipTemplateApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Slip Template
        api_response = api_instance.slip_templates_id_delete(id)
        print("The response of SlipTemplateApi->slip_templates_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplateApi->slip_templates_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SlipTemplatesIdGet200Response**](SlipTemplatesIdGet200Response.md)

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

# **slip_templates_id_get**
> SlipTemplatesIdGet200Response slip_templates_id_get(id)

Show a single Slip Template

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.slip_templates_id_get200_response import SlipTemplatesIdGet200Response
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
    api_instance = openapi_client.SlipTemplateApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Slip Template
        api_response = api_instance.slip_templates_id_get(id)
        print("The response of SlipTemplateApi->slip_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplateApi->slip_templates_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SlipTemplatesIdGet200Response**](SlipTemplatesIdGet200Response.md)

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

# **slip_templates_id_patch**
> SlipTemplatesIdGet200Response slip_templates_id_patch(id, slip_templates_id_patch_request)

Update a Slip Template

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.slip_templates_id_get200_response import SlipTemplatesIdGet200Response
from openapi_client.models.slip_templates_id_patch_request import SlipTemplatesIdPatchRequest
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
    api_instance = openapi_client.SlipTemplateApi(api_client)
    id = 56 # int | 
    slip_templates_id_patch_request = openapi_client.SlipTemplatesIdPatchRequest() # SlipTemplatesIdPatchRequest | 

    try:
        # Update a Slip Template
        api_response = api_instance.slip_templates_id_patch(id, slip_templates_id_patch_request)
        print("The response of SlipTemplateApi->slip_templates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplateApi->slip_templates_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **slip_templates_id_patch_request** | [**SlipTemplatesIdPatchRequest**](SlipTemplatesIdPatchRequest.md)|  | 

### Return type

[**SlipTemplatesIdGet200Response**](SlipTemplatesIdGet200Response.md)

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

# **slip_templates_post**
> SlipTemplatesIdGet200Response slip_templates_post(slip_templates_post_request)

Create a Slip Template

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.slip_templates_id_get200_response import SlipTemplatesIdGet200Response
from openapi_client.models.slip_templates_post_request import SlipTemplatesPostRequest
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
    api_instance = openapi_client.SlipTemplateApi(api_client)
    slip_templates_post_request = openapi_client.SlipTemplatesPostRequest() # SlipTemplatesPostRequest | 

    try:
        # Create a Slip Template
        api_response = api_instance.slip_templates_post(slip_templates_post_request)
        print("The response of SlipTemplateApi->slip_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplateApi->slip_templates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slip_templates_post_request** | [**SlipTemplatesPostRequest**](SlipTemplatesPostRequest.md)|  | 

### Return type

[**SlipTemplatesIdGet200Response**](SlipTemplatesIdGet200Response.md)

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


# webshipperv2.SlipTemplatePreviewApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slip_template_previews_get**](SlipTemplatePreviewApi.md#slip_template_previews_get) | **GET** /slip_template_previews | List all Slip Template Previews
[**slip_template_previews_id_delete**](SlipTemplatePreviewApi.md#slip_template_previews_id_delete) | **DELETE** /slip_template_previews/{id} | Delete a Slip Template Preview
[**slip_template_previews_id_get**](SlipTemplatePreviewApi.md#slip_template_previews_id_get) | **GET** /slip_template_previews/{id} | Show a single Slip Template Preview
[**slip_template_previews_id_patch**](SlipTemplatePreviewApi.md#slip_template_previews_id_patch) | **PATCH** /slip_template_previews/{id} | Update a Slip Template Preview
[**slip_template_previews_post**](SlipTemplatePreviewApi.md#slip_template_previews_post) | **POST** /slip_template_previews | Create a Slip Template Preview


# **slip_template_previews_get**
> SlipTemplatePreviewsGet200Response slip_template_previews_get(filter_id=filter_id)

List all Slip Template Previews

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.slip_template_previews_get200_response import SlipTemplatePreviewsGet200Response
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
    api_instance = webshipperv2.SlipTemplatePreviewApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Slip Template Previews
        api_response = api_instance.slip_template_previews_get(filter_id=filter_id)
        print("The response of SlipTemplatePreviewApi->slip_template_previews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplatePreviewApi->slip_template_previews_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**SlipTemplatePreviewsGet200Response**](SlipTemplatePreviewsGet200Response.md)

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

# **slip_template_previews_id_delete**
> SlipTemplatePreviewsIdGet200Response slip_template_previews_id_delete(id)

Delete a Slip Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.slip_template_previews_id_get200_response import SlipTemplatePreviewsIdGet200Response
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
    api_instance = webshipperv2.SlipTemplatePreviewApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Slip Template Preview
        api_response = api_instance.slip_template_previews_id_delete(id)
        print("The response of SlipTemplatePreviewApi->slip_template_previews_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplatePreviewApi->slip_template_previews_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SlipTemplatePreviewsIdGet200Response**](SlipTemplatePreviewsIdGet200Response.md)

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

# **slip_template_previews_id_get**
> SlipTemplatePreviewsIdGet200Response slip_template_previews_id_get(id)

Show a single Slip Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.slip_template_previews_id_get200_response import SlipTemplatePreviewsIdGet200Response
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
    api_instance = webshipperv2.SlipTemplatePreviewApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Slip Template Preview
        api_response = api_instance.slip_template_previews_id_get(id)
        print("The response of SlipTemplatePreviewApi->slip_template_previews_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplatePreviewApi->slip_template_previews_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SlipTemplatePreviewsIdGet200Response**](SlipTemplatePreviewsIdGet200Response.md)

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

# **slip_template_previews_id_patch**
> SlipTemplatePreviewsIdGet200Response slip_template_previews_id_patch(id, slip_template_previews_id_patch_request)

Update a Slip Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.slip_template_previews_id_get200_response import SlipTemplatePreviewsIdGet200Response
from webshipperv2.models.slip_template_previews_id_patch_request import SlipTemplatePreviewsIdPatchRequest
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
    api_instance = webshipperv2.SlipTemplatePreviewApi(api_client)
    id = 56 # int | 
    slip_template_previews_id_patch_request = webshipperv2.SlipTemplatePreviewsIdPatchRequest() # SlipTemplatePreviewsIdPatchRequest | 

    try:
        # Update a Slip Template Preview
        api_response = api_instance.slip_template_previews_id_patch(id, slip_template_previews_id_patch_request)
        print("The response of SlipTemplatePreviewApi->slip_template_previews_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplatePreviewApi->slip_template_previews_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **slip_template_previews_id_patch_request** | [**SlipTemplatePreviewsIdPatchRequest**](SlipTemplatePreviewsIdPatchRequest.md)|  | 

### Return type

[**SlipTemplatePreviewsIdGet200Response**](SlipTemplatePreviewsIdGet200Response.md)

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

# **slip_template_previews_post**
> SlipTemplatePreviewsIdGet200Response slip_template_previews_post(slip_template_previews_post_request)

Create a Slip Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.slip_template_previews_id_get200_response import SlipTemplatePreviewsIdGet200Response
from webshipperv2.models.slip_template_previews_post_request import SlipTemplatePreviewsPostRequest
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
    api_instance = webshipperv2.SlipTemplatePreviewApi(api_client)
    slip_template_previews_post_request = webshipperv2.SlipTemplatePreviewsPostRequest() # SlipTemplatePreviewsPostRequest | 

    try:
        # Create a Slip Template Preview
        api_response = api_instance.slip_template_previews_post(slip_template_previews_post_request)
        print("The response of SlipTemplatePreviewApi->slip_template_previews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlipTemplatePreviewApi->slip_template_previews_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slip_template_previews_post_request** | [**SlipTemplatePreviewsPostRequest**](SlipTemplatePreviewsPostRequest.md)|  | 

### Return type

[**SlipTemplatePreviewsIdGet200Response**](SlipTemplatePreviewsIdGet200Response.md)

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


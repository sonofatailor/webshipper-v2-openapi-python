# webshipperv2.ReportTypeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_types_get**](ReportTypeApi.md#report_types_get) | **GET** /report_types | List all Report Types
[**report_types_id_delete**](ReportTypeApi.md#report_types_id_delete) | **DELETE** /report_types/{id} | Delete a Report Type
[**report_types_id_get**](ReportTypeApi.md#report_types_id_get) | **GET** /report_types/{id} | Show a single Report Type
[**report_types_id_patch**](ReportTypeApi.md#report_types_id_patch) | **PATCH** /report_types/{id} | Update a Report Type
[**report_types_post**](ReportTypeApi.md#report_types_post) | **POST** /report_types | Create a Report Type


# **report_types_get**
> ReportTypesGet200Response report_types_get(filter_id=filter_id)

List all Report Types

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.report_types_get200_response import ReportTypesGet200Response
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
    api_instance = webshipperv2.ReportTypeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Report Types
        api_response = api_instance.report_types_get(filter_id=filter_id)
        print("The response of ReportTypeApi->report_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportTypeApi->report_types_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**ReportTypesGet200Response**](ReportTypesGet200Response.md)

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

# **report_types_id_delete**
> ReportTypesIdGet200Response report_types_id_delete(id)

Delete a Report Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.report_types_id_get200_response import ReportTypesIdGet200Response
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
    api_instance = webshipperv2.ReportTypeApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Report Type
        api_response = api_instance.report_types_id_delete(id)
        print("The response of ReportTypeApi->report_types_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportTypeApi->report_types_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReportTypesIdGet200Response**](ReportTypesIdGet200Response.md)

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

# **report_types_id_get**
> ReportTypesIdGet200Response report_types_id_get(id)

Show a single Report Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.report_types_id_get200_response import ReportTypesIdGet200Response
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
    api_instance = webshipperv2.ReportTypeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Report Type
        api_response = api_instance.report_types_id_get(id)
        print("The response of ReportTypeApi->report_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportTypeApi->report_types_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReportTypesIdGet200Response**](ReportTypesIdGet200Response.md)

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

# **report_types_id_patch**
> ReportTypesIdGet200Response report_types_id_patch(id, report_types_id_patch_request)

Update a Report Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.report_types_id_get200_response import ReportTypesIdGet200Response
from webshipperv2.models.report_types_id_patch_request import ReportTypesIdPatchRequest
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
    api_instance = webshipperv2.ReportTypeApi(api_client)
    id = 56 # int | 
    report_types_id_patch_request = webshipperv2.ReportTypesIdPatchRequest() # ReportTypesIdPatchRequest | 

    try:
        # Update a Report Type
        api_response = api_instance.report_types_id_patch(id, report_types_id_patch_request)
        print("The response of ReportTypeApi->report_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportTypeApi->report_types_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **report_types_id_patch_request** | [**ReportTypesIdPatchRequest**](ReportTypesIdPatchRequest.md)|  | 

### Return type

[**ReportTypesIdGet200Response**](ReportTypesIdGet200Response.md)

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

# **report_types_post**
> ReportTypesIdGet200Response report_types_post(report_types_post_request)

Create a Report Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.report_types_id_get200_response import ReportTypesIdGet200Response
from webshipperv2.models.report_types_post_request import ReportTypesPostRequest
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
    api_instance = webshipperv2.ReportTypeApi(api_client)
    report_types_post_request = webshipperv2.ReportTypesPostRequest() # ReportTypesPostRequest | 

    try:
        # Create a Report Type
        api_response = api_instance.report_types_post(report_types_post_request)
        print("The response of ReportTypeApi->report_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportTypeApi->report_types_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_types_post_request** | [**ReportTypesPostRequest**](ReportTypesPostRequest.md)|  | 

### Return type

[**ReportTypesIdGet200Response**](ReportTypesIdGet200Response.md)

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


# openapi_client.PrinterJobApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**printer_jobs_get**](PrinterJobApi.md#printer_jobs_get) | **GET** /printer_jobs | List all Printer Jobs
[**printer_jobs_id_delete**](PrinterJobApi.md#printer_jobs_id_delete) | **DELETE** /printer_jobs/{id} | Delete a Printer Job
[**printer_jobs_id_get**](PrinterJobApi.md#printer_jobs_id_get) | **GET** /printer_jobs/{id} | Show a single Printer Job
[**printer_jobs_id_patch**](PrinterJobApi.md#printer_jobs_id_patch) | **PATCH** /printer_jobs/{id} | Update a Printer Job
[**printer_jobs_post**](PrinterJobApi.md#printer_jobs_post) | **POST** /printer_jobs | Create a Printer Job


# **printer_jobs_get**
> PrinterJobsGet200Response printer_jobs_get(filter_id=filter_id, filter_printer_client_id=filter_printer_client_id, filter_created_at=filter_created_at, filter_completed=filter_completed, filter_error=filter_error, filter_try_count=filter_try_count, filter_printer_id=filter_printer_id)

List all Printer Jobs

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.printer_jobs_get200_response import PrinterJobsGet200Response
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
    api_instance = openapi_client.PrinterJobApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_printer_client_id = 'filter_printer_client_id_example' # str | Filter by printer_client_id (optional)
    filter_created_at = 'filter_created_at_example' # str | Filter by created_at (optional)
    filter_completed = 'filter_completed_example' # str | Filter by completed (optional)
    filter_error = 'filter_error_example' # str | Filter by error (optional)
    filter_try_count = 'filter_try_count_example' # str | Filter by try_count (optional)
    filter_printer_id = 'filter_printer_id_example' # str | Filter by printer_id (optional)

    try:
        # List all Printer Jobs
        api_response = api_instance.printer_jobs_get(filter_id=filter_id, filter_printer_client_id=filter_printer_client_id, filter_created_at=filter_created_at, filter_completed=filter_completed, filter_error=filter_error, filter_try_count=filter_try_count, filter_printer_id=filter_printer_id)
        print("The response of PrinterJobApi->printer_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterJobApi->printer_jobs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_printer_client_id** | **str**| Filter by printer_client_id | [optional] 
 **filter_created_at** | **str**| Filter by created_at | [optional] 
 **filter_completed** | **str**| Filter by completed | [optional] 
 **filter_error** | **str**| Filter by error | [optional] 
 **filter_try_count** | **str**| Filter by try_count | [optional] 
 **filter_printer_id** | **str**| Filter by printer_id | [optional] 

### Return type

[**PrinterJobsGet200Response**](PrinterJobsGet200Response.md)

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

# **printer_jobs_id_delete**
> PrinterJobsIdGet200Response printer_jobs_id_delete(id)

Delete a Printer Job

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.printer_jobs_id_get200_response import PrinterJobsIdGet200Response
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
    api_instance = openapi_client.PrinterJobApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Printer Job
        api_response = api_instance.printer_jobs_id_delete(id)
        print("The response of PrinterJobApi->printer_jobs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterJobApi->printer_jobs_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PrinterJobsIdGet200Response**](PrinterJobsIdGet200Response.md)

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

# **printer_jobs_id_get**
> PrinterJobsIdGet200Response printer_jobs_id_get(id)

Show a single Printer Job

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.printer_jobs_id_get200_response import PrinterJobsIdGet200Response
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
    api_instance = openapi_client.PrinterJobApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Printer Job
        api_response = api_instance.printer_jobs_id_get(id)
        print("The response of PrinterJobApi->printer_jobs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterJobApi->printer_jobs_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PrinterJobsIdGet200Response**](PrinterJobsIdGet200Response.md)

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

# **printer_jobs_id_patch**
> PrinterJobsIdGet200Response printer_jobs_id_patch(id, printer_jobs_id_patch_request)

Update a Printer Job

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.printer_jobs_id_get200_response import PrinterJobsIdGet200Response
from openapi_client.models.printer_jobs_id_patch_request import PrinterJobsIdPatchRequest
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
    api_instance = openapi_client.PrinterJobApi(api_client)
    id = 56 # int | 
    printer_jobs_id_patch_request = openapi_client.PrinterJobsIdPatchRequest() # PrinterJobsIdPatchRequest | 

    try:
        # Update a Printer Job
        api_response = api_instance.printer_jobs_id_patch(id, printer_jobs_id_patch_request)
        print("The response of PrinterJobApi->printer_jobs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterJobApi->printer_jobs_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **printer_jobs_id_patch_request** | [**PrinterJobsIdPatchRequest**](PrinterJobsIdPatchRequest.md)|  | 

### Return type

[**PrinterJobsIdGet200Response**](PrinterJobsIdGet200Response.md)

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

# **printer_jobs_post**
> PrinterJobsIdGet200Response printer_jobs_post(printer_jobs_post_request)

Create a Printer Job

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.printer_jobs_id_get200_response import PrinterJobsIdGet200Response
from openapi_client.models.printer_jobs_post_request import PrinterJobsPostRequest
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
    api_instance = openapi_client.PrinterJobApi(api_client)
    printer_jobs_post_request = openapi_client.PrinterJobsPostRequest() # PrinterJobsPostRequest | 

    try:
        # Create a Printer Job
        api_response = api_instance.printer_jobs_post(printer_jobs_post_request)
        print("The response of PrinterJobApi->printer_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterJobApi->printer_jobs_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_jobs_post_request** | [**PrinterJobsPostRequest**](PrinterJobsPostRequest.md)|  | 

### Return type

[**PrinterJobsIdGet200Response**](PrinterJobsIdGet200Response.md)

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


# openapi_client.PrintBulkSlipsApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_printer_jobs_get**](PrintBulkSlipsApi.md#bulk_printer_jobs_get) | **GET** /bulk_printer_jobs | List all Print Bulk Slipss
[**bulk_printer_jobs_id_delete**](PrintBulkSlipsApi.md#bulk_printer_jobs_id_delete) | **DELETE** /bulk_printer_jobs/{id} | Delete a Print Bulk Slips
[**bulk_printer_jobs_id_get**](PrintBulkSlipsApi.md#bulk_printer_jobs_id_get) | **GET** /bulk_printer_jobs/{id} | Show a single Print Bulk Slips
[**bulk_printer_jobs_id_patch**](PrintBulkSlipsApi.md#bulk_printer_jobs_id_patch) | **PATCH** /bulk_printer_jobs/{id} | Update a Print Bulk Slips
[**bulk_printer_jobs_post**](PrintBulkSlipsApi.md#bulk_printer_jobs_post) | **POST** /bulk_printer_jobs | Create a Print Bulk Slips


# **bulk_printer_jobs_get**
> BulkPrinterJobsGet200Response bulk_printer_jobs_get(filter_id=filter_id)

List all Print Bulk Slipss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.bulk_printer_jobs_get200_response import BulkPrinterJobsGet200Response
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
    api_instance = openapi_client.PrintBulkSlipsApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Print Bulk Slipss
        api_response = api_instance.bulk_printer_jobs_get(filter_id=filter_id)
        print("The response of PrintBulkSlipsApi->bulk_printer_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintBulkSlipsApi->bulk_printer_jobs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**BulkPrinterJobsGet200Response**](BulkPrinterJobsGet200Response.md)

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

# **bulk_printer_jobs_id_delete**
> BulkPrinterJobsIdGet200Response bulk_printer_jobs_id_delete(id)

Delete a Print Bulk Slips

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.bulk_printer_jobs_id_get200_response import BulkPrinterJobsIdGet200Response
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
    api_instance = openapi_client.PrintBulkSlipsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Print Bulk Slips
        api_response = api_instance.bulk_printer_jobs_id_delete(id)
        print("The response of PrintBulkSlipsApi->bulk_printer_jobs_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintBulkSlipsApi->bulk_printer_jobs_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkPrinterJobsIdGet200Response**](BulkPrinterJobsIdGet200Response.md)

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

# **bulk_printer_jobs_id_get**
> BulkPrinterJobsIdGet200Response bulk_printer_jobs_id_get(id)

Show a single Print Bulk Slips

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.bulk_printer_jobs_id_get200_response import BulkPrinterJobsIdGet200Response
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
    api_instance = openapi_client.PrintBulkSlipsApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Print Bulk Slips
        api_response = api_instance.bulk_printer_jobs_id_get(id)
        print("The response of PrintBulkSlipsApi->bulk_printer_jobs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintBulkSlipsApi->bulk_printer_jobs_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkPrinterJobsIdGet200Response**](BulkPrinterJobsIdGet200Response.md)

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

# **bulk_printer_jobs_id_patch**
> BulkPrinterJobsIdGet200Response bulk_printer_jobs_id_patch(id, bulk_printer_jobs_id_patch_request)

Update a Print Bulk Slips

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.bulk_printer_jobs_id_get200_response import BulkPrinterJobsIdGet200Response
from openapi_client.models.bulk_printer_jobs_id_patch_request import BulkPrinterJobsIdPatchRequest
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
    api_instance = openapi_client.PrintBulkSlipsApi(api_client)
    id = 56 # int | 
    bulk_printer_jobs_id_patch_request = openapi_client.BulkPrinterJobsIdPatchRequest() # BulkPrinterJobsIdPatchRequest | 

    try:
        # Update a Print Bulk Slips
        api_response = api_instance.bulk_printer_jobs_id_patch(id, bulk_printer_jobs_id_patch_request)
        print("The response of PrintBulkSlipsApi->bulk_printer_jobs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintBulkSlipsApi->bulk_printer_jobs_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **bulk_printer_jobs_id_patch_request** | [**BulkPrinterJobsIdPatchRequest**](BulkPrinterJobsIdPatchRequest.md)|  | 

### Return type

[**BulkPrinterJobsIdGet200Response**](BulkPrinterJobsIdGet200Response.md)

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

# **bulk_printer_jobs_post**
> BulkPrinterJobsIdGet200Response bulk_printer_jobs_post(bulk_printer_jobs_post_request)

Create a Print Bulk Slips

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.bulk_printer_jobs_id_get200_response import BulkPrinterJobsIdGet200Response
from openapi_client.models.bulk_printer_jobs_post_request import BulkPrinterJobsPostRequest
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
    api_instance = openapi_client.PrintBulkSlipsApi(api_client)
    bulk_printer_jobs_post_request = openapi_client.BulkPrinterJobsPostRequest() # BulkPrinterJobsPostRequest | 

    try:
        # Create a Print Bulk Slips
        api_response = api_instance.bulk_printer_jobs_post(bulk_printer_jobs_post_request)
        print("The response of PrintBulkSlipsApi->bulk_printer_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintBulkSlipsApi->bulk_printer_jobs_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_printer_jobs_post_request** | [**BulkPrinterJobsPostRequest**](BulkPrinterJobsPostRequest.md)|  | 

### Return type

[**BulkPrinterJobsIdGet200Response**](BulkPrinterJobsIdGet200Response.md)

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


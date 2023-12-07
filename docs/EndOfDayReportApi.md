# webshipperv2.EndOfDayReportApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_of_day_reports_get**](EndOfDayReportApi.md#end_of_day_reports_get) | **GET** /end_of_day_reports | List all End-of-day reports
[**end_of_day_reports_id_delete**](EndOfDayReportApi.md#end_of_day_reports_id_delete) | **DELETE** /end_of_day_reports/{id} | Delete a End-of-day report
[**end_of_day_reports_id_get**](EndOfDayReportApi.md#end_of_day_reports_id_get) | **GET** /end_of_day_reports/{id} | Show a single End-of-day report
[**end_of_day_reports_id_patch**](EndOfDayReportApi.md#end_of_day_reports_id_patch) | **PATCH** /end_of_day_reports/{id} | Update a End-of-day report
[**end_of_day_reports_post**](EndOfDayReportApi.md#end_of_day_reports_post) | **POST** /end_of_day_reports | Create a End-of-day report


# **end_of_day_reports_get**
> EndOfDayReportsGet200Response end_of_day_reports_get(filter_id=filter_id)

List all End-of-day reports

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.end_of_day_reports_get200_response import EndOfDayReportsGet200Response
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
    api_instance = webshipperv2.EndOfDayReportApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all End-of-day reports
        api_response = api_instance.end_of_day_reports_get(filter_id=filter_id)
        print("The response of EndOfDayReportApi->end_of_day_reports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndOfDayReportApi->end_of_day_reports_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**EndOfDayReportsGet200Response**](EndOfDayReportsGet200Response.md)

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

# **end_of_day_reports_id_delete**
> EndOfDayReportsIdGet200Response end_of_day_reports_id_delete(id)

Delete a End-of-day report

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.end_of_day_reports_id_get200_response import EndOfDayReportsIdGet200Response
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
    api_instance = webshipperv2.EndOfDayReportApi(api_client)
    id = 56 # int | 

    try:
        # Delete a End-of-day report
        api_response = api_instance.end_of_day_reports_id_delete(id)
        print("The response of EndOfDayReportApi->end_of_day_reports_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndOfDayReportApi->end_of_day_reports_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EndOfDayReportsIdGet200Response**](EndOfDayReportsIdGet200Response.md)

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

# **end_of_day_reports_id_get**
> EndOfDayReportsIdGet200Response end_of_day_reports_id_get(id)

Show a single End-of-day report

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.end_of_day_reports_id_get200_response import EndOfDayReportsIdGet200Response
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
    api_instance = webshipperv2.EndOfDayReportApi(api_client)
    id = 56 # int | 

    try:
        # Show a single End-of-day report
        api_response = api_instance.end_of_day_reports_id_get(id)
        print("The response of EndOfDayReportApi->end_of_day_reports_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndOfDayReportApi->end_of_day_reports_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EndOfDayReportsIdGet200Response**](EndOfDayReportsIdGet200Response.md)

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

# **end_of_day_reports_id_patch**
> EndOfDayReportsIdGet200Response end_of_day_reports_id_patch(id, end_of_day_reports_id_patch_request)

Update a End-of-day report

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.end_of_day_reports_id_get200_response import EndOfDayReportsIdGet200Response
from webshipperv2.models.end_of_day_reports_id_patch_request import EndOfDayReportsIdPatchRequest
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
    api_instance = webshipperv2.EndOfDayReportApi(api_client)
    id = 56 # int | 
    end_of_day_reports_id_patch_request = webshipperv2.EndOfDayReportsIdPatchRequest() # EndOfDayReportsIdPatchRequest | 

    try:
        # Update a End-of-day report
        api_response = api_instance.end_of_day_reports_id_patch(id, end_of_day_reports_id_patch_request)
        print("The response of EndOfDayReportApi->end_of_day_reports_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndOfDayReportApi->end_of_day_reports_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end_of_day_reports_id_patch_request** | [**EndOfDayReportsIdPatchRequest**](EndOfDayReportsIdPatchRequest.md)|  | 

### Return type

[**EndOfDayReportsIdGet200Response**](EndOfDayReportsIdGet200Response.md)

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

# **end_of_day_reports_post**
> EndOfDayReportsIdGet200Response end_of_day_reports_post(end_of_day_reports_post_request)

Create a End-of-day report

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.end_of_day_reports_id_get200_response import EndOfDayReportsIdGet200Response
from webshipperv2.models.end_of_day_reports_post_request import EndOfDayReportsPostRequest
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
    api_instance = webshipperv2.EndOfDayReportApi(api_client)
    end_of_day_reports_post_request = webshipperv2.EndOfDayReportsPostRequest() # EndOfDayReportsPostRequest | 

    try:
        # Create a End-of-day report
        api_response = api_instance.end_of_day_reports_post(end_of_day_reports_post_request)
        print("The response of EndOfDayReportApi->end_of_day_reports_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndOfDayReportApi->end_of_day_reports_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_of_day_reports_post_request** | [**EndOfDayReportsPostRequest**](EndOfDayReportsPostRequest.md)|  | 

### Return type

[**EndOfDayReportsIdGet200Response**](EndOfDayReportsIdGet200Response.md)

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


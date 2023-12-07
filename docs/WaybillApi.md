# webshipperv2.WaybillApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waybills_get**](WaybillApi.md#waybills_get) | **GET** /waybills | List all Waybills
[**waybills_id_delete**](WaybillApi.md#waybills_id_delete) | **DELETE** /waybills/{id} | Delete a Waybill
[**waybills_id_get**](WaybillApi.md#waybills_id_get) | **GET** /waybills/{id} | Show a single Waybill
[**waybills_id_patch**](WaybillApi.md#waybills_id_patch) | **PATCH** /waybills/{id} | Update a Waybill
[**waybills_post**](WaybillApi.md#waybills_post) | **POST** /waybills | Create a Waybill


# **waybills_get**
> WaybillsGet200Response waybills_get(filter_id=filter_id, filter_status=filter_status, filter_carrier=filter_carrier)

List all Waybills

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.waybills_get200_response import WaybillsGet200Response
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
    api_instance = webshipperv2.WaybillApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_status = 'filter_status_example' # str | Filter by status (optional)
    filter_carrier = 'filter_carrier_example' # str | Filter by carrier (optional)

    try:
        # List all Waybills
        api_response = api_instance.waybills_get(filter_id=filter_id, filter_status=filter_status, filter_carrier=filter_carrier)
        print("The response of WaybillApi->waybills_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillApi->waybills_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_status** | **str**| Filter by status | [optional] 
 **filter_carrier** | **str**| Filter by carrier | [optional] 

### Return type

[**WaybillsGet200Response**](WaybillsGet200Response.md)

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

# **waybills_id_delete**
> WaybillsIdGet200Response waybills_id_delete(id)

Delete a Waybill

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.waybills_id_get200_response import WaybillsIdGet200Response
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
    api_instance = webshipperv2.WaybillApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Waybill
        api_response = api_instance.waybills_id_delete(id)
        print("The response of WaybillApi->waybills_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillApi->waybills_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WaybillsIdGet200Response**](WaybillsIdGet200Response.md)

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

# **waybills_id_get**
> WaybillsIdGet200Response waybills_id_get(id)

Show a single Waybill

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.waybills_id_get200_response import WaybillsIdGet200Response
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
    api_instance = webshipperv2.WaybillApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Waybill
        api_response = api_instance.waybills_id_get(id)
        print("The response of WaybillApi->waybills_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillApi->waybills_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WaybillsIdGet200Response**](WaybillsIdGet200Response.md)

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

# **waybills_id_patch**
> WaybillsIdGet200Response waybills_id_patch(id, waybills_id_patch_request)

Update a Waybill

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.waybills_id_get200_response import WaybillsIdGet200Response
from webshipperv2.models.waybills_id_patch_request import WaybillsIdPatchRequest
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
    api_instance = webshipperv2.WaybillApi(api_client)
    id = 56 # int | 
    waybills_id_patch_request = webshipperv2.WaybillsIdPatchRequest() # WaybillsIdPatchRequest | 

    try:
        # Update a Waybill
        api_response = api_instance.waybills_id_patch(id, waybills_id_patch_request)
        print("The response of WaybillApi->waybills_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillApi->waybills_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **waybills_id_patch_request** | [**WaybillsIdPatchRequest**](WaybillsIdPatchRequest.md)|  | 

### Return type

[**WaybillsIdGet200Response**](WaybillsIdGet200Response.md)

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

# **waybills_post**
> WaybillsIdGet200Response waybills_post(waybills_post_request)

Create a Waybill

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.waybills_id_get200_response import WaybillsIdGet200Response
from webshipperv2.models.waybills_post_request import WaybillsPostRequest
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
    api_instance = webshipperv2.WaybillApi(api_client)
    waybills_post_request = webshipperv2.WaybillsPostRequest() # WaybillsPostRequest | 

    try:
        # Create a Waybill
        api_response = api_instance.waybills_post(waybills_post_request)
        print("The response of WaybillApi->waybills_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WaybillApi->waybills_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waybills_post_request** | [**WaybillsPostRequest**](WaybillsPostRequest.md)|  | 

### Return type

[**WaybillsIdGet200Response**](WaybillsIdGet200Response.md)

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


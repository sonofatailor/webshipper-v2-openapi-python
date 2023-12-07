# webshipperv2.BulkImportOrdersApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_import_orders_get**](BulkImportOrdersApi.md#bulk_import_orders_get) | **GET** /bulk_import_orders | List all Bulk import orderss
[**bulk_import_orders_id_delete**](BulkImportOrdersApi.md#bulk_import_orders_id_delete) | **DELETE** /bulk_import_orders/{id} | Delete a Bulk import orders
[**bulk_import_orders_id_get**](BulkImportOrdersApi.md#bulk_import_orders_id_get) | **GET** /bulk_import_orders/{id} | Show a single Bulk import orders
[**bulk_import_orders_id_patch**](BulkImportOrdersApi.md#bulk_import_orders_id_patch) | **PATCH** /bulk_import_orders/{id} | Update a Bulk import orders
[**bulk_import_orders_post**](BulkImportOrdersApi.md#bulk_import_orders_post) | **POST** /bulk_import_orders | Create a Bulk import orders


# **bulk_import_orders_get**
> BulkImportOrdersGet200Response bulk_import_orders_get(filter_id=filter_id)

List all Bulk import orderss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.bulk_import_orders_get200_response import BulkImportOrdersGet200Response
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
    api_instance = webshipperv2.BulkImportOrdersApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Bulk import orderss
        api_response = api_instance.bulk_import_orders_get(filter_id=filter_id)
        print("The response of BulkImportOrdersApi->bulk_import_orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportOrdersApi->bulk_import_orders_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**BulkImportOrdersGet200Response**](BulkImportOrdersGet200Response.md)

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

# **bulk_import_orders_id_delete**
> BulkImportOrdersIdGet200Response bulk_import_orders_id_delete(id)

Delete a Bulk import orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.bulk_import_orders_id_get200_response import BulkImportOrdersIdGet200Response
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
    api_instance = webshipperv2.BulkImportOrdersApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Bulk import orders
        api_response = api_instance.bulk_import_orders_id_delete(id)
        print("The response of BulkImportOrdersApi->bulk_import_orders_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportOrdersApi->bulk_import_orders_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkImportOrdersIdGet200Response**](BulkImportOrdersIdGet200Response.md)

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

# **bulk_import_orders_id_get**
> BulkImportOrdersIdGet200Response bulk_import_orders_id_get(id)

Show a single Bulk import orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.bulk_import_orders_id_get200_response import BulkImportOrdersIdGet200Response
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
    api_instance = webshipperv2.BulkImportOrdersApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Bulk import orders
        api_response = api_instance.bulk_import_orders_id_get(id)
        print("The response of BulkImportOrdersApi->bulk_import_orders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportOrdersApi->bulk_import_orders_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkImportOrdersIdGet200Response**](BulkImportOrdersIdGet200Response.md)

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

# **bulk_import_orders_id_patch**
> BulkImportOrdersIdGet200Response bulk_import_orders_id_patch(id, bulk_import_orders_id_patch_request)

Update a Bulk import orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.bulk_import_orders_id_get200_response import BulkImportOrdersIdGet200Response
from webshipperv2.models.bulk_import_orders_id_patch_request import BulkImportOrdersIdPatchRequest
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
    api_instance = webshipperv2.BulkImportOrdersApi(api_client)
    id = 56 # int | 
    bulk_import_orders_id_patch_request = webshipperv2.BulkImportOrdersIdPatchRequest() # BulkImportOrdersIdPatchRequest | 

    try:
        # Update a Bulk import orders
        api_response = api_instance.bulk_import_orders_id_patch(id, bulk_import_orders_id_patch_request)
        print("The response of BulkImportOrdersApi->bulk_import_orders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportOrdersApi->bulk_import_orders_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **bulk_import_orders_id_patch_request** | [**BulkImportOrdersIdPatchRequest**](BulkImportOrdersIdPatchRequest.md)|  | 

### Return type

[**BulkImportOrdersIdGet200Response**](BulkImportOrdersIdGet200Response.md)

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

# **bulk_import_orders_post**
> BulkImportOrdersIdGet200Response bulk_import_orders_post(bulk_import_orders_post_request)

Create a Bulk import orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.bulk_import_orders_id_get200_response import BulkImportOrdersIdGet200Response
from webshipperv2.models.bulk_import_orders_post_request import BulkImportOrdersPostRequest
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
    api_instance = webshipperv2.BulkImportOrdersApi(api_client)
    bulk_import_orders_post_request = webshipperv2.BulkImportOrdersPostRequest() # BulkImportOrdersPostRequest | 

    try:
        # Create a Bulk import orders
        api_response = api_instance.bulk_import_orders_post(bulk_import_orders_post_request)
        print("The response of BulkImportOrdersApi->bulk_import_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkImportOrdersApi->bulk_import_orders_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_import_orders_post_request** | [**BulkImportOrdersPostRequest**](BulkImportOrdersPostRequest.md)|  | 

### Return type

[**BulkImportOrdersIdGet200Response**](BulkImportOrdersIdGet200Response.md)

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


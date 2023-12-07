# openapi_client.CSVMappingApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csv_mappings_get**](CSVMappingApi.md#csv_mappings_get) | **GET** /csv_mappings | List all CSV Mappings
[**csv_mappings_id_delete**](CSVMappingApi.md#csv_mappings_id_delete) | **DELETE** /csv_mappings/{id} | Delete a CSV Mapping
[**csv_mappings_id_get**](CSVMappingApi.md#csv_mappings_id_get) | **GET** /csv_mappings/{id} | Show a single CSV Mapping
[**csv_mappings_id_patch**](CSVMappingApi.md#csv_mappings_id_patch) | **PATCH** /csv_mappings/{id} | Update a CSV Mapping
[**csv_mappings_post**](CSVMappingApi.md#csv_mappings_post) | **POST** /csv_mappings | Create a CSV Mapping


# **csv_mappings_get**
> CsvMappingsGet200Response csv_mappings_get(filter_id=filter_id)

List all CSV Mappings

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.csv_mappings_get200_response import CsvMappingsGet200Response
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
    api_instance = openapi_client.CSVMappingApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all CSV Mappings
        api_response = api_instance.csv_mappings_get(filter_id=filter_id)
        print("The response of CSVMappingApi->csv_mappings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingApi->csv_mappings_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**CsvMappingsGet200Response**](CsvMappingsGet200Response.md)

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

# **csv_mappings_id_delete**
> CsvMappingsIdGet200Response csv_mappings_id_delete(id)

Delete a CSV Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.csv_mappings_id_get200_response import CsvMappingsIdGet200Response
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
    api_instance = openapi_client.CSVMappingApi(api_client)
    id = 56 # int | 

    try:
        # Delete a CSV Mapping
        api_response = api_instance.csv_mappings_id_delete(id)
        print("The response of CSVMappingApi->csv_mappings_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingApi->csv_mappings_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CsvMappingsIdGet200Response**](CsvMappingsIdGet200Response.md)

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

# **csv_mappings_id_get**
> CsvMappingsIdGet200Response csv_mappings_id_get(id)

Show a single CSV Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.csv_mappings_id_get200_response import CsvMappingsIdGet200Response
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
    api_instance = openapi_client.CSVMappingApi(api_client)
    id = 56 # int | 

    try:
        # Show a single CSV Mapping
        api_response = api_instance.csv_mappings_id_get(id)
        print("The response of CSVMappingApi->csv_mappings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingApi->csv_mappings_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CsvMappingsIdGet200Response**](CsvMappingsIdGet200Response.md)

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

# **csv_mappings_id_patch**
> CsvMappingsIdGet200Response csv_mappings_id_patch(id, csv_mappings_id_patch_request)

Update a CSV Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.csv_mappings_id_get200_response import CsvMappingsIdGet200Response
from openapi_client.models.csv_mappings_id_patch_request import CsvMappingsIdPatchRequest
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
    api_instance = openapi_client.CSVMappingApi(api_client)
    id = 56 # int | 
    csv_mappings_id_patch_request = openapi_client.CsvMappingsIdPatchRequest() # CsvMappingsIdPatchRequest | 

    try:
        # Update a CSV Mapping
        api_response = api_instance.csv_mappings_id_patch(id, csv_mappings_id_patch_request)
        print("The response of CSVMappingApi->csv_mappings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingApi->csv_mappings_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **csv_mappings_id_patch_request** | [**CsvMappingsIdPatchRequest**](CsvMappingsIdPatchRequest.md)|  | 

### Return type

[**CsvMappingsIdGet200Response**](CsvMappingsIdGet200Response.md)

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

# **csv_mappings_post**
> CsvMappingsIdGet200Response csv_mappings_post(csv_mappings_post_request)

Create a CSV Mapping

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.csv_mappings_id_get200_response import CsvMappingsIdGet200Response
from openapi_client.models.csv_mappings_post_request import CsvMappingsPostRequest
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
    api_instance = openapi_client.CSVMappingApi(api_client)
    csv_mappings_post_request = openapi_client.CsvMappingsPostRequest() # CsvMappingsPostRequest | 

    try:
        # Create a CSV Mapping
        api_response = api_instance.csv_mappings_post(csv_mappings_post_request)
        print("The response of CSVMappingApi->csv_mappings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingApi->csv_mappings_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_mappings_post_request** | [**CsvMappingsPostRequest**](CsvMappingsPostRequest.md)|  | 

### Return type

[**CsvMappingsIdGet200Response**](CsvMappingsIdGet200Response.md)

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


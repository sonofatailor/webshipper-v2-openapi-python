# openapi_client.CarrierTypeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**carrier_types_get**](CarrierTypeApi.md#carrier_types_get) | **GET** /carrier_types | List all Carrier Types
[**carrier_types_id_get**](CarrierTypeApi.md#carrier_types_id_get) | **GET** /carrier_types/{id} | Show a single Carrier Type


# **carrier_types_get**
> CarrierTypesGet200Response carrier_types_get(filter_id=filter_id, filter_carrier_code=filter_carrier_code, filter_carrier_group_id=filter_carrier_group_id)

List all Carrier Types

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.carrier_types_get200_response import CarrierTypesGet200Response
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
    api_instance = openapi_client.CarrierTypeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_carrier_code = 'filter_carrier_code_example' # str | Filter by carrier_code (optional)
    filter_carrier_group_id = 'filter_carrier_group_id_example' # str | Filter by carrier_group_id (optional)

    try:
        # List all Carrier Types
        api_response = api_instance.carrier_types_get(filter_id=filter_id, filter_carrier_code=filter_carrier_code, filter_carrier_group_id=filter_carrier_group_id)
        print("The response of CarrierTypeApi->carrier_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierTypeApi->carrier_types_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_carrier_code** | **str**| Filter by carrier_code | [optional] 
 **filter_carrier_group_id** | **str**| Filter by carrier_group_id | [optional] 

### Return type

[**CarrierTypesGet200Response**](CarrierTypesGet200Response.md)

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

# **carrier_types_id_get**
> CarrierTypesIdGet200Response carrier_types_id_get(id)

Show a single Carrier Type

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.carrier_types_id_get200_response import CarrierTypesIdGet200Response
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
    api_instance = openapi_client.CarrierTypeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Carrier Type
        api_response = api_instance.carrier_types_id_get(id)
        print("The response of CarrierTypeApi->carrier_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierTypeApi->carrier_types_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CarrierTypesIdGet200Response**](CarrierTypesIdGet200Response.md)

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


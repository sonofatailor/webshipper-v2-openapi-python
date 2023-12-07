# webshipperv2.CarrierApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**carriers_get**](CarrierApi.md#carriers_get) | **GET** /carriers | List all Carriers
[**carriers_id_delete**](CarrierApi.md#carriers_id_delete) | **DELETE** /carriers/{id} | Delete a Carrier
[**carriers_id_get**](CarrierApi.md#carriers_id_get) | **GET** /carriers/{id} | Show a single Carrier
[**carriers_id_patch**](CarrierApi.md#carriers_id_patch) | **PATCH** /carriers/{id} | Update a Carrier
[**carriers_post**](CarrierApi.md#carriers_post) | **POST** /carriers | Create a Carrier


# **carriers_get**
> CarriersGet200Response carriers_get(filter_id=filter_id, filter_billable=filter_billable, filter_carrier_type_codes=filter_carrier_type_codes, filter_carrier_group_id=filter_carrier_group_id)

List all Carriers

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.carriers_get200_response import CarriersGet200Response
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
    api_instance = webshipperv2.CarrierApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_billable = 'filter_billable_example' # str | Filter by billable (optional)
    filter_carrier_type_codes = 'filter_carrier_type_codes_example' # str | Filter by carrier_type_codes (optional)
    filter_carrier_group_id = 'filter_carrier_group_id_example' # str | Filter by carrier_group_id (optional)

    try:
        # List all Carriers
        api_response = api_instance.carriers_get(filter_id=filter_id, filter_billable=filter_billable, filter_carrier_type_codes=filter_carrier_type_codes, filter_carrier_group_id=filter_carrier_group_id)
        print("The response of CarrierApi->carriers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carriers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_billable** | **str**| Filter by billable | [optional] 
 **filter_carrier_type_codes** | **str**| Filter by carrier_type_codes | [optional] 
 **filter_carrier_group_id** | **str**| Filter by carrier_group_id | [optional] 

### Return type

[**CarriersGet200Response**](CarriersGet200Response.md)

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

# **carriers_id_delete**
> CarriersIdGet200Response carriers_id_delete(id)

Delete a Carrier

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.carriers_id_get200_response import CarriersIdGet200Response
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
    api_instance = webshipperv2.CarrierApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Carrier
        api_response = api_instance.carriers_id_delete(id)
        print("The response of CarrierApi->carriers_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carriers_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CarriersIdGet200Response**](CarriersIdGet200Response.md)

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

# **carriers_id_get**
> CarriersIdGet200Response carriers_id_get(id)

Show a single Carrier

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.carriers_id_get200_response import CarriersIdGet200Response
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
    api_instance = webshipperv2.CarrierApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Carrier
        api_response = api_instance.carriers_id_get(id)
        print("The response of CarrierApi->carriers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carriers_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CarriersIdGet200Response**](CarriersIdGet200Response.md)

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

# **carriers_id_patch**
> CarriersIdGet200Response carriers_id_patch(id, carriers_id_patch_request)

Update a Carrier

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.carriers_id_get200_response import CarriersIdGet200Response
from webshipperv2.models.carriers_id_patch_request import CarriersIdPatchRequest
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
    api_instance = webshipperv2.CarrierApi(api_client)
    id = 56 # int | 
    carriers_id_patch_request = webshipperv2.CarriersIdPatchRequest() # CarriersIdPatchRequest | 

    try:
        # Update a Carrier
        api_response = api_instance.carriers_id_patch(id, carriers_id_patch_request)
        print("The response of CarrierApi->carriers_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carriers_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **carriers_id_patch_request** | [**CarriersIdPatchRequest**](CarriersIdPatchRequest.md)|  | 

### Return type

[**CarriersIdGet200Response**](CarriersIdGet200Response.md)

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

# **carriers_post**
> CarriersIdGet200Response carriers_post(carriers_post_request)

Create a Carrier

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.carriers_id_get200_response import CarriersIdGet200Response
from webshipperv2.models.carriers_post_request import CarriersPostRequest
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
    api_instance = webshipperv2.CarrierApi(api_client)
    carriers_post_request = webshipperv2.CarriersPostRequest() # CarriersPostRequest | 

    try:
        # Create a Carrier
        api_response = api_instance.carriers_post(carriers_post_request)
        print("The response of CarrierApi->carriers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarrierApi->carriers_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carriers_post_request** | [**CarriersPostRequest**](CarriersPostRequest.md)|  | 

### Return type

[**CarriersIdGet200Response**](CarriersIdGet200Response.md)

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


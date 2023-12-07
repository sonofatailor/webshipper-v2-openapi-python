# openapi_client.EDIApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edis_get**](EDIApi.md#edis_get) | **GET** /edis | List all EDIs
[**edis_id_get**](EDIApi.md#edis_id_get) | **GET** /edis/{id} | Show a single EDI


# **edis_get**
> EdisGet200Response edis_get(filter_id=filter_id, filter_shipment_id=filter_shipment_id, filter_waybill_id=filter_waybill_id)

List all EDIs

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.edis_get200_response import EdisGet200Response
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
    api_instance = openapi_client.EDIApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_shipment_id = 'filter_shipment_id_example' # str | Filter by shipment_id (optional)
    filter_waybill_id = 'filter_waybill_id_example' # str | Filter by waybill_id (optional)

    try:
        # List all EDIs
        api_response = api_instance.edis_get(filter_id=filter_id, filter_shipment_id=filter_shipment_id, filter_waybill_id=filter_waybill_id)
        print("The response of EDIApi->edis_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EDIApi->edis_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_shipment_id** | **str**| Filter by shipment_id | [optional] 
 **filter_waybill_id** | **str**| Filter by waybill_id | [optional] 

### Return type

[**EdisGet200Response**](EdisGet200Response.md)

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

# **edis_id_get**
> EdisIdGet200Response edis_id_get(id)

Show a single EDI

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.edis_id_get200_response import EdisIdGet200Response
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
    api_instance = openapi_client.EDIApi(api_client)
    id = 56 # int | 

    try:
        # Show a single EDI
        api_response = api_instance.edis_id_get(id)
        print("The response of EDIApi->edis_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EDIApi->edis_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EdisIdGet200Response**](EdisIdGet200Response.md)

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


# webshipperv2.PrinterClientApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**printer_clients_get**](PrinterClientApi.md#printer_clients_get) | **GET** /printer_clients | List all Printer Clients
[**printer_clients_id_get**](PrinterClientApi.md#printer_clients_id_get) | **GET** /printer_clients/{id} | Show a single Printer Client
[**printer_clients_id_patch**](PrinterClientApi.md#printer_clients_id_patch) | **PATCH** /printer_clients/{id} | Update a Printer Client


# **printer_clients_get**
> PrinterClientsGet200Response printer_clients_get(filter_id=filter_id)

List all Printer Clients

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.printer_clients_get200_response import PrinterClientsGet200Response
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
    api_instance = webshipperv2.PrinterClientApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Printer Clients
        api_response = api_instance.printer_clients_get(filter_id=filter_id)
        print("The response of PrinterClientApi->printer_clients_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterClientApi->printer_clients_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**PrinterClientsGet200Response**](PrinterClientsGet200Response.md)

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

# **printer_clients_id_get**
> PrinterClientsIdGet200Response printer_clients_id_get(id)

Show a single Printer Client

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.printer_clients_id_get200_response import PrinterClientsIdGet200Response
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
    api_instance = webshipperv2.PrinterClientApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Printer Client
        api_response = api_instance.printer_clients_id_get(id)
        print("The response of PrinterClientApi->printer_clients_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterClientApi->printer_clients_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PrinterClientsIdGet200Response**](PrinterClientsIdGet200Response.md)

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

# **printer_clients_id_patch**
> PrinterClientsIdGet200Response printer_clients_id_patch(id, printer_clients_id_patch_request)

Update a Printer Client

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.printer_clients_id_get200_response import PrinterClientsIdGet200Response
from webshipperv2.models.printer_clients_id_patch_request import PrinterClientsIdPatchRequest
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
    api_instance = webshipperv2.PrinterClientApi(api_client)
    id = 56 # int | 
    printer_clients_id_patch_request = webshipperv2.PrinterClientsIdPatchRequest() # PrinterClientsIdPatchRequest | 

    try:
        # Update a Printer Client
        api_response = api_instance.printer_clients_id_patch(id, printer_clients_id_patch_request)
        print("The response of PrinterClientApi->printer_clients_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterClientApi->printer_clients_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **printer_clients_id_patch_request** | [**PrinterClientsIdPatchRequest**](PrinterClientsIdPatchRequest.md)|  | 

### Return type

[**PrinterClientsIdGet200Response**](PrinterClientsIdGet200Response.md)

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


# webshipperv2.ShipmentApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipments_get**](ShipmentApi.md#shipments_get) | **GET** /shipments | List all Shipments
[**shipments_id_get**](ShipmentApi.md#shipments_id_get) | **GET** /shipments/{id} | Show a single Shipment
[**shipments_post**](ShipmentApi.md#shipments_post) | **POST** /shipments | Create a Shipment


# **shipments_get**
> ShipmentsGet200Response shipments_get(filter_id=filter_id, filter_reference=filter_reference, filter_sorting_id=filter_sorting_id, filter_created_at=filter_created_at, filter_updated_at=filter_updated_at, filter_order=filter_order, filter_carrier=filter_carrier, filter_send_time=filter_send_time, filter_status=filter_status, filter_is_return=filter_is_return, filter_printer_client=filter_printer_client, filter_delivery_address=filter_delivery_address, filter_without_shadow_shipments=filter_without_shadow_shipments, filter_tracking_number=filter_tracking_number, filter_free_text=filter_free_text, filter_has_pickup=filter_has_pickup, filter_activity_type=filter_activity_type, filter_order_lines=filter_order_lines, filter_billing_contact=filter_billing_contact, filter_billing_email=filter_billing_email, filter_billing_company=filter_billing_company, filter_delivery_email=filter_delivery_email, filter_delivery_contact=filter_delivery_contact, filter_delivery_company=filter_delivery_company)

List all Shipments

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipments_get200_response import ShipmentsGet200Response
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
    api_instance = webshipperv2.ShipmentApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_reference = 'filter_reference_example' # str | Filter by reference (optional)
    filter_sorting_id = 'filter_sorting_id_example' # str | Filter by sorting_id (optional)
    filter_created_at = 'filter_created_at_example' # str | Filter by created_at (optional)
    filter_updated_at = 'filter_updated_at_example' # str | Filter by updated_at (optional)
    filter_order = 'filter_order_example' # str | Filter by order (optional)
    filter_carrier = 'filter_carrier_example' # str | Filter by carrier (optional)
    filter_send_time = 'filter_send_time_example' # str | Filter by send_time (optional)
    filter_status = 'filter_status_example' # str | Filter by status (optional)
    filter_is_return = 'filter_is_return_example' # str | Filter by is_return (optional)
    filter_printer_client = 'filter_printer_client_example' # str | Filter by printer_client (optional)
    filter_delivery_address = 'filter_delivery_address_example' # str | Filter by delivery_address (optional)
    filter_without_shadow_shipments = 'filter_without_shadow_shipments_example' # str | Filter by without_shadow_shipments (optional)
    filter_tracking_number = 'filter_tracking_number_example' # str | Filter by tracking_number (optional)
    filter_free_text = 'filter_free_text_example' # str | Filter by free_text (optional)
    filter_has_pickup = 'filter_has_pickup_example' # str | Filter by has_pickup (optional)
    filter_activity_type = 'filter_activity_type_example' # str | Filter by activity_type (optional)
    filter_order_lines = 'filter_order_lines_example' # str | Filter by order_lines (optional)
    filter_billing_contact = 'filter_billing_contact_example' # str | Filter by billing_contact (optional)
    filter_billing_email = 'filter_billing_email_example' # str | Filter by billing_email (optional)
    filter_billing_company = 'filter_billing_company_example' # str | Filter by billing_company (optional)
    filter_delivery_email = 'filter_delivery_email_example' # str | Filter by delivery_email (optional)
    filter_delivery_contact = 'filter_delivery_contact_example' # str | Filter by delivery_contact (optional)
    filter_delivery_company = 'filter_delivery_company_example' # str | Filter by delivery_company (optional)

    try:
        # List all Shipments
        api_response = api_instance.shipments_get(filter_id=filter_id, filter_reference=filter_reference, filter_sorting_id=filter_sorting_id, filter_created_at=filter_created_at, filter_updated_at=filter_updated_at, filter_order=filter_order, filter_carrier=filter_carrier, filter_send_time=filter_send_time, filter_status=filter_status, filter_is_return=filter_is_return, filter_printer_client=filter_printer_client, filter_delivery_address=filter_delivery_address, filter_without_shadow_shipments=filter_without_shadow_shipments, filter_tracking_number=filter_tracking_number, filter_free_text=filter_free_text, filter_has_pickup=filter_has_pickup, filter_activity_type=filter_activity_type, filter_order_lines=filter_order_lines, filter_billing_contact=filter_billing_contact, filter_billing_email=filter_billing_email, filter_billing_company=filter_billing_company, filter_delivery_email=filter_delivery_email, filter_delivery_contact=filter_delivery_contact, filter_delivery_company=filter_delivery_company)
        print("The response of ShipmentApi->shipments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipments_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_reference** | **str**| Filter by reference | [optional] 
 **filter_sorting_id** | **str**| Filter by sorting_id | [optional] 
 **filter_created_at** | **str**| Filter by created_at | [optional] 
 **filter_updated_at** | **str**| Filter by updated_at | [optional] 
 **filter_order** | **str**| Filter by order | [optional] 
 **filter_carrier** | **str**| Filter by carrier | [optional] 
 **filter_send_time** | **str**| Filter by send_time | [optional] 
 **filter_status** | **str**| Filter by status | [optional] 
 **filter_is_return** | **str**| Filter by is_return | [optional] 
 **filter_printer_client** | **str**| Filter by printer_client | [optional] 
 **filter_delivery_address** | **str**| Filter by delivery_address | [optional] 
 **filter_without_shadow_shipments** | **str**| Filter by without_shadow_shipments | [optional] 
 **filter_tracking_number** | **str**| Filter by tracking_number | [optional] 
 **filter_free_text** | **str**| Filter by free_text | [optional] 
 **filter_has_pickup** | **str**| Filter by has_pickup | [optional] 
 **filter_activity_type** | **str**| Filter by activity_type | [optional] 
 **filter_order_lines** | **str**| Filter by order_lines | [optional] 
 **filter_billing_contact** | **str**| Filter by billing_contact | [optional] 
 **filter_billing_email** | **str**| Filter by billing_email | [optional] 
 **filter_billing_company** | **str**| Filter by billing_company | [optional] 
 **filter_delivery_email** | **str**| Filter by delivery_email | [optional] 
 **filter_delivery_contact** | **str**| Filter by delivery_contact | [optional] 
 **filter_delivery_company** | **str**| Filter by delivery_company | [optional] 

### Return type

[**ShipmentsGet200Response**](ShipmentsGet200Response.md)

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

# **shipments_id_get**
> ShipmentsIdGet200Response shipments_id_get(id)

Show a single Shipment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipments_id_get200_response import ShipmentsIdGet200Response
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
    api_instance = webshipperv2.ShipmentApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipment
        api_response = api_instance.shipments_id_get(id)
        print("The response of ShipmentApi->shipments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipments_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShipmentsIdGet200Response**](ShipmentsIdGet200Response.md)

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

# **shipments_post**
> ShipmentsIdGet200Response shipments_post(shipments_post_request)

Create a Shipment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipments_id_get200_response import ShipmentsIdGet200Response
from webshipperv2.models.shipments_post_request import ShipmentsPostRequest
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
    api_instance = webshipperv2.ShipmentApi(api_client)
    shipments_post_request = {"data":{"type":"shipments","relationships":{"order":{"data":{"type":"orders","id":2341}},"printer_client":{"data":{"type":"printer_clients","id":12}}}}} # ShipmentsPostRequest | 

    try:
        # Create a Shipment
        api_response = api_instance.shipments_post(shipments_post_request)
        print("The response of ShipmentApi->shipments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipments_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipments_post_request** | [**ShipmentsPostRequest**](ShipmentsPostRequest.md)|  | 

### Return type

[**ShipmentsIdGet200Response**](ShipmentsIdGet200Response.md)

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


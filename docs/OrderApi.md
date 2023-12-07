# webshipperv2.OrderApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_get**](OrderApi.md#orders_get) | **GET** /orders | List all Orders
[**orders_id_delete**](OrderApi.md#orders_id_delete) | **DELETE** /orders/{id} | Delete a Order
[**orders_id_get**](OrderApi.md#orders_id_get) | **GET** /orders/{id} | Show a single Order
[**orders_id_patch**](OrderApi.md#orders_id_patch) | **PATCH** /orders/{id} | Update a Order
[**orders_post**](OrderApi.md#orders_post) | **POST** /orders | Create a Order


# **orders_get**
> OrdersGet200Response orders_get(filter_id=filter_id, filter_ext_ref=filter_ext_ref, filter_sorting_id=filter_sorting_id, filter_created_at=filter_created_at, filter_updated_at=filter_updated_at, filter_status=filter_status, filter_visible_ref=filter_visible_ref, filter_slip_printed=filter_slip_printed, filter_label_printed=filter_label_printed, filter_lock_state=filter_lock_state, filter_order_channel=filter_order_channel, filter_order_channel_id=filter_order_channel_id, filter_shipping_rate=filter_shipping_rate, filter_shipping_rate_id=filter_shipping_rate_id, filter_carrier=filter_carrier, filter_sku=filter_sku, filter_free_text=filter_free_text, filter_tag=filter_tag, filter_delivery_country_code=filter_delivery_country_code, filter_activity_type=filter_activity_type, filter_order_lines=filter_order_lines, filter_billing_contact=filter_billing_contact, filter_billing_company=filter_billing_company, filter_billing_email=filter_billing_email)

List all Orders

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.orders_get200_response import OrdersGet200Response
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
    api_instance = webshipperv2.OrderApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_ext_ref = 'filter_ext_ref_example' # str | Filter by ext_ref (optional)
    filter_sorting_id = 'filter_sorting_id_example' # str | Filter by sorting_id (optional)
    filter_created_at = 'filter_created_at_example' # str | Filter by created_at (optional)
    filter_updated_at = 'filter_updated_at_example' # str | Filter by updated_at (optional)
    filter_status = 'filter_status_example' # str | Filter by status (optional)
    filter_visible_ref = 'filter_visible_ref_example' # str | Filter by visible_ref (optional)
    filter_slip_printed = 'filter_slip_printed_example' # str | Filter by slip_printed (optional)
    filter_label_printed = 'filter_label_printed_example' # str | Filter by label_printed (optional)
    filter_lock_state = 'filter_lock_state_example' # str | Filter by lock_state (optional)
    filter_order_channel = 'filter_order_channel_example' # str | Filter by order_channel (optional)
    filter_order_channel_id = 'filter_order_channel_id_example' # str | Filter by order_channel_id (optional)
    filter_shipping_rate = 'filter_shipping_rate_example' # str | Filter by shipping_rate (optional)
    filter_shipping_rate_id = 'filter_shipping_rate_id_example' # str | Filter by shipping_rate_id (optional)
    filter_carrier = 'filter_carrier_example' # str | Filter by carrier (optional)
    filter_sku = 'filter_sku_example' # str | Filter by sku (optional)
    filter_free_text = 'filter_free_text_example' # str | Filter by free_text (optional)
    filter_tag = 'filter_tag_example' # str | Filter by tag (optional)
    filter_delivery_country_code = 'filter_delivery_country_code_example' # str | Filter by delivery_country_code (optional)
    filter_activity_type = 'filter_activity_type_example' # str | Filter by activity_type (optional)
    filter_order_lines = 'filter_order_lines_example' # str | Filter by order_lines (optional)
    filter_billing_contact = 'filter_billing_contact_example' # str | Filter by billing_contact (optional)
    filter_billing_company = 'filter_billing_company_example' # str | Filter by billing_company (optional)
    filter_billing_email = 'filter_billing_email_example' # str | Filter by billing_email (optional)

    try:
        # List all Orders
        api_response = api_instance.orders_get(filter_id=filter_id, filter_ext_ref=filter_ext_ref, filter_sorting_id=filter_sorting_id, filter_created_at=filter_created_at, filter_updated_at=filter_updated_at, filter_status=filter_status, filter_visible_ref=filter_visible_ref, filter_slip_printed=filter_slip_printed, filter_label_printed=filter_label_printed, filter_lock_state=filter_lock_state, filter_order_channel=filter_order_channel, filter_order_channel_id=filter_order_channel_id, filter_shipping_rate=filter_shipping_rate, filter_shipping_rate_id=filter_shipping_rate_id, filter_carrier=filter_carrier, filter_sku=filter_sku, filter_free_text=filter_free_text, filter_tag=filter_tag, filter_delivery_country_code=filter_delivery_country_code, filter_activity_type=filter_activity_type, filter_order_lines=filter_order_lines, filter_billing_contact=filter_billing_contact, filter_billing_company=filter_billing_company, filter_billing_email=filter_billing_email)
        print("The response of OrderApi->orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_ext_ref** | **str**| Filter by ext_ref | [optional] 
 **filter_sorting_id** | **str**| Filter by sorting_id | [optional] 
 **filter_created_at** | **str**| Filter by created_at | [optional] 
 **filter_updated_at** | **str**| Filter by updated_at | [optional] 
 **filter_status** | **str**| Filter by status | [optional] 
 **filter_visible_ref** | **str**| Filter by visible_ref | [optional] 
 **filter_slip_printed** | **str**| Filter by slip_printed | [optional] 
 **filter_label_printed** | **str**| Filter by label_printed | [optional] 
 **filter_lock_state** | **str**| Filter by lock_state | [optional] 
 **filter_order_channel** | **str**| Filter by order_channel | [optional] 
 **filter_order_channel_id** | **str**| Filter by order_channel_id | [optional] 
 **filter_shipping_rate** | **str**| Filter by shipping_rate | [optional] 
 **filter_shipping_rate_id** | **str**| Filter by shipping_rate_id | [optional] 
 **filter_carrier** | **str**| Filter by carrier | [optional] 
 **filter_sku** | **str**| Filter by sku | [optional] 
 **filter_free_text** | **str**| Filter by free_text | [optional] 
 **filter_tag** | **str**| Filter by tag | [optional] 
 **filter_delivery_country_code** | **str**| Filter by delivery_country_code | [optional] 
 **filter_activity_type** | **str**| Filter by activity_type | [optional] 
 **filter_order_lines** | **str**| Filter by order_lines | [optional] 
 **filter_billing_contact** | **str**| Filter by billing_contact | [optional] 
 **filter_billing_company** | **str**| Filter by billing_company | [optional] 
 **filter_billing_email** | **str**| Filter by billing_email | [optional] 

### Return type

[**OrdersGet200Response**](OrdersGet200Response.md)

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

# **orders_id_delete**
> OrdersIdGet200Response orders_id_delete(id)

Delete a Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.orders_id_get200_response import OrdersIdGet200Response
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
    api_instance = webshipperv2.OrderApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Order
        api_response = api_instance.orders_id_delete(id)
        print("The response of OrderApi->orders_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrdersIdGet200Response**](OrdersIdGet200Response.md)

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

# **orders_id_get**
> OrdersIdGet200Response orders_id_get(id)

Show a single Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.orders_id_get200_response import OrdersIdGet200Response
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
    api_instance = webshipperv2.OrderApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Order
        api_response = api_instance.orders_id_get(id)
        print("The response of OrderApi->orders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OrdersIdGet200Response**](OrdersIdGet200Response.md)

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

# **orders_id_patch**
> OrdersIdGet200Response orders_id_patch(id, orders_id_patch_request)

Update a Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.orders_id_get200_response import OrdersIdGet200Response
from webshipperv2.models.orders_id_patch_request import OrdersIdPatchRequest
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
    api_instance = webshipperv2.OrderApi(api_client)
    id = 56 # int | 
    orders_id_patch_request = webshipperv2.OrdersIdPatchRequest() # OrdersIdPatchRequest | 

    try:
        # Update a Order
        api_response = api_instance.orders_id_patch(id, orders_id_patch_request)
        print("The response of OrderApi->orders_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **orders_id_patch_request** | [**OrdersIdPatchRequest**](OrdersIdPatchRequest.md)|  | 

### Return type

[**OrdersIdGet200Response**](OrdersIdGet200Response.md)

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

# **orders_post**
> OrdersIdGet200Response orders_post(orders_post_request)

Create a Order

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.orders_id_get200_response import OrdersIdGet200Response
from webshipperv2.models.orders_post_request import OrdersPostRequest
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
    api_instance = webshipperv2.OrderApi(api_client)
    orders_post_request = {"data":{"type":"orders","attributes":{"drop_point":{"drop_point_id":12,"address_1":"Street 123","zip":"8600","city":"Silkeborg","country_code":"DK","carrier_code":"DUMMY"},"delivery_address":{"address_1":"Lyngbygade 8","zip":"8600","city":"Silkeborg","country_code":"DK"},"sender_address":{"address_1":"Example street 2","zip":"7400","city":"Herning","country_code":"DK"},"order_lines":[{"sku":"ZB420","description":"Zebra GK420d label printer","quantity":1,"location":"LOC 3563-67","tarif_number":"844332","country_of_origin":"DK","unit_price":24.0,"vat_percent":25.0,"order_id":12,"ext_ref":"342342","weight":500.0,"weight_unit":"g","discount_value":0.0,"discount_type":"fixed","discounted_unit_price":24.0}]},"relationships":{"order_channel":{"data":{"id":9,"type":"order_channels"}},"shipping_rate":{"data":{"id":6,"type":"shipping_rates"}}}}} # OrdersPostRequest | 

    try:
        # Create a Order
        api_response = api_instance.orders_post(orders_post_request)
        print("The response of OrderApi->orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->orders_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_post_request** | [**OrdersPostRequest**](OrdersPostRequest.md)|  | 

### Return type

[**OrdersIdGet200Response**](OrdersIdGet200Response.md)

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


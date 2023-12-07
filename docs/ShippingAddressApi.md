# webshipperv2.ShippingAddressApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipping_addresses_get**](ShippingAddressApi.md#shipping_addresses_get) | **GET** /shipping_addresses | List all Shipping Addresss
[**shipping_addresses_id_delete**](ShippingAddressApi.md#shipping_addresses_id_delete) | **DELETE** /shipping_addresses/{id} | Delete a Shipping Address
[**shipping_addresses_id_get**](ShippingAddressApi.md#shipping_addresses_id_get) | **GET** /shipping_addresses/{id} | Show a single Shipping Address
[**shipping_addresses_id_patch**](ShippingAddressApi.md#shipping_addresses_id_patch) | **PATCH** /shipping_addresses/{id} | Update a Shipping Address
[**shipping_addresses_post**](ShippingAddressApi.md#shipping_addresses_post) | **POST** /shipping_addresses | Create a Shipping Address


# **shipping_addresses_get**
> ShippingAddressesGet200Response shipping_addresses_get(filter_id=filter_id, filter_att_contact=filter_att_contact, filter_company_name=filter_company_name, filter_address_1=filter_address_1, filter_address_2=filter_address_2, filter_country_code=filter_country_code, filter_state=filter_state, filter_zip=filter_zip, filter_address_type=filter_address_type, filter_search=filter_search)

List all Shipping Addresss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_addresses_get200_response import ShippingAddressesGet200Response
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
    api_instance = webshipperv2.ShippingAddressApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_att_contact = 'filter_att_contact_example' # str | Filter by att_contact (optional)
    filter_company_name = 'filter_company_name_example' # str | Filter by company_name (optional)
    filter_address_1 = 'filter_address_1_example' # str | Filter by address_1 (optional)
    filter_address_2 = 'filter_address_2_example' # str | Filter by address_2 (optional)
    filter_country_code = 'filter_country_code_example' # str | Filter by country_code (optional)
    filter_state = 'filter_state_example' # str | Filter by state (optional)
    filter_zip = 'filter_zip_example' # str | Filter by zip (optional)
    filter_address_type = 'filter_address_type_example' # str | Filter by address_type (optional)
    filter_search = 'filter_search_example' # str | Filter by search (optional)

    try:
        # List all Shipping Addresss
        api_response = api_instance.shipping_addresses_get(filter_id=filter_id, filter_att_contact=filter_att_contact, filter_company_name=filter_company_name, filter_address_1=filter_address_1, filter_address_2=filter_address_2, filter_country_code=filter_country_code, filter_state=filter_state, filter_zip=filter_zip, filter_address_type=filter_address_type, filter_search=filter_search)
        print("The response of ShippingAddressApi->shipping_addresses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingAddressApi->shipping_addresses_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_att_contact** | **str**| Filter by att_contact | [optional] 
 **filter_company_name** | **str**| Filter by company_name | [optional] 
 **filter_address_1** | **str**| Filter by address_1 | [optional] 
 **filter_address_2** | **str**| Filter by address_2 | [optional] 
 **filter_country_code** | **str**| Filter by country_code | [optional] 
 **filter_state** | **str**| Filter by state | [optional] 
 **filter_zip** | **str**| Filter by zip | [optional] 
 **filter_address_type** | **str**| Filter by address_type | [optional] 
 **filter_search** | **str**| Filter by search | [optional] 

### Return type

[**ShippingAddressesGet200Response**](ShippingAddressesGet200Response.md)

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

# **shipping_addresses_id_delete**
> ShippingAddressesIdGet200Response shipping_addresses_id_delete(id)

Delete a Shipping Address

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_addresses_id_get200_response import ShippingAddressesIdGet200Response
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
    api_instance = webshipperv2.ShippingAddressApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Shipping Address
        api_response = api_instance.shipping_addresses_id_delete(id)
        print("The response of ShippingAddressApi->shipping_addresses_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingAddressApi->shipping_addresses_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingAddressesIdGet200Response**](ShippingAddressesIdGet200Response.md)

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

# **shipping_addresses_id_get**
> ShippingAddressesIdGet200Response shipping_addresses_id_get(id)

Show a single Shipping Address

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_addresses_id_get200_response import ShippingAddressesIdGet200Response
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
    api_instance = webshipperv2.ShippingAddressApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Shipping Address
        api_response = api_instance.shipping_addresses_id_get(id)
        print("The response of ShippingAddressApi->shipping_addresses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingAddressApi->shipping_addresses_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ShippingAddressesIdGet200Response**](ShippingAddressesIdGet200Response.md)

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

# **shipping_addresses_id_patch**
> ShippingAddressesIdGet200Response shipping_addresses_id_patch(id, shipping_addresses_id_patch_request)

Update a Shipping Address

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_addresses_id_get200_response import ShippingAddressesIdGet200Response
from webshipperv2.models.shipping_addresses_id_patch_request import ShippingAddressesIdPatchRequest
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
    api_instance = webshipperv2.ShippingAddressApi(api_client)
    id = 56 # int | 
    shipping_addresses_id_patch_request = webshipperv2.ShippingAddressesIdPatchRequest() # ShippingAddressesIdPatchRequest | 

    try:
        # Update a Shipping Address
        api_response = api_instance.shipping_addresses_id_patch(id, shipping_addresses_id_patch_request)
        print("The response of ShippingAddressApi->shipping_addresses_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingAddressApi->shipping_addresses_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shipping_addresses_id_patch_request** | [**ShippingAddressesIdPatchRequest**](ShippingAddressesIdPatchRequest.md)|  | 

### Return type

[**ShippingAddressesIdGet200Response**](ShippingAddressesIdGet200Response.md)

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

# **shipping_addresses_post**
> ShippingAddressesIdGet200Response shipping_addresses_post(shipping_addresses_post_request)

Create a Shipping Address

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.shipping_addresses_id_get200_response import ShippingAddressesIdGet200Response
from webshipperv2.models.shipping_addresses_post_request import ShippingAddressesPostRequest
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
    api_instance = webshipperv2.ShippingAddressApi(api_client)
    shipping_addresses_post_request = webshipperv2.ShippingAddressesPostRequest() # ShippingAddressesPostRequest | 

    try:
        # Create a Shipping Address
        api_response = api_instance.shipping_addresses_post(shipping_addresses_post_request)
        print("The response of ShippingAddressApi->shipping_addresses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingAddressApi->shipping_addresses_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_addresses_post_request** | [**ShippingAddressesPostRequest**](ShippingAddressesPostRequest.md)|  | 

### Return type

[**ShippingAddressesIdGet200Response**](ShippingAddressesIdGet200Response.md)

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


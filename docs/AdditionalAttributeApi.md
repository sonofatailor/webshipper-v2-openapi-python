# openapi_client.AdditionalAttributeApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**additional_attributes_get**](AdditionalAttributeApi.md#additional_attributes_get) | **GET** /additional_attributes | List all Additional Attributes
[**additional_attributes_id_delete**](AdditionalAttributeApi.md#additional_attributes_id_delete) | **DELETE** /additional_attributes/{id} | Delete a Additional Attribute
[**additional_attributes_id_get**](AdditionalAttributeApi.md#additional_attributes_id_get) | **GET** /additional_attributes/{id} | Show a single Additional Attribute
[**additional_attributes_id_patch**](AdditionalAttributeApi.md#additional_attributes_id_patch) | **PATCH** /additional_attributes/{id} | Update a Additional Attribute
[**additional_attributes_post**](AdditionalAttributeApi.md#additional_attributes_post) | **POST** /additional_attributes | Create a Additional Attribute


# **additional_attributes_get**
> AdditionalAttributesGet200Response additional_attributes_get(filter_id=filter_id)

List all Additional Attributes

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.additional_attributes_get200_response import AdditionalAttributesGet200Response
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
    api_instance = openapi_client.AdditionalAttributeApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Additional Attributes
        api_response = api_instance.additional_attributes_get(filter_id=filter_id)
        print("The response of AdditionalAttributeApi->additional_attributes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalAttributeApi->additional_attributes_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**AdditionalAttributesGet200Response**](AdditionalAttributesGet200Response.md)

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

# **additional_attributes_id_delete**
> AdditionalAttributesIdGet200Response additional_attributes_id_delete(id)

Delete a Additional Attribute

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.additional_attributes_id_get200_response import AdditionalAttributesIdGet200Response
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
    api_instance = openapi_client.AdditionalAttributeApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Additional Attribute
        api_response = api_instance.additional_attributes_id_delete(id)
        print("The response of AdditionalAttributeApi->additional_attributes_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalAttributeApi->additional_attributes_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdditionalAttributesIdGet200Response**](AdditionalAttributesIdGet200Response.md)

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

# **additional_attributes_id_get**
> AdditionalAttributesIdGet200Response additional_attributes_id_get(id)

Show a single Additional Attribute

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.additional_attributes_id_get200_response import AdditionalAttributesIdGet200Response
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
    api_instance = openapi_client.AdditionalAttributeApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Additional Attribute
        api_response = api_instance.additional_attributes_id_get(id)
        print("The response of AdditionalAttributeApi->additional_attributes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalAttributeApi->additional_attributes_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdditionalAttributesIdGet200Response**](AdditionalAttributesIdGet200Response.md)

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

# **additional_attributes_id_patch**
> AdditionalAttributesIdGet200Response additional_attributes_id_patch(id, additional_attributes_id_patch_request)

Update a Additional Attribute

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.additional_attributes_id_get200_response import AdditionalAttributesIdGet200Response
from openapi_client.models.additional_attributes_id_patch_request import AdditionalAttributesIdPatchRequest
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
    api_instance = openapi_client.AdditionalAttributeApi(api_client)
    id = 56 # int | 
    additional_attributes_id_patch_request = openapi_client.AdditionalAttributesIdPatchRequest() # AdditionalAttributesIdPatchRequest | 

    try:
        # Update a Additional Attribute
        api_response = api_instance.additional_attributes_id_patch(id, additional_attributes_id_patch_request)
        print("The response of AdditionalAttributeApi->additional_attributes_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalAttributeApi->additional_attributes_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **additional_attributes_id_patch_request** | [**AdditionalAttributesIdPatchRequest**](AdditionalAttributesIdPatchRequest.md)|  | 

### Return type

[**AdditionalAttributesIdGet200Response**](AdditionalAttributesIdGet200Response.md)

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

# **additional_attributes_post**
> AdditionalAttributesIdGet200Response additional_attributes_post(additional_attributes_post_request)

Create a Additional Attribute

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.additional_attributes_id_get200_response import AdditionalAttributesIdGet200Response
from openapi_client.models.additional_attributes_post_request import AdditionalAttributesPostRequest
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
    api_instance = openapi_client.AdditionalAttributeApi(api_client)
    additional_attributes_post_request = openapi_client.AdditionalAttributesPostRequest() # AdditionalAttributesPostRequest | 

    try:
        # Create a Additional Attribute
        api_response = api_instance.additional_attributes_post(additional_attributes_post_request)
        print("The response of AdditionalAttributeApi->additional_attributes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdditionalAttributeApi->additional_attributes_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_attributes_post_request** | [**AdditionalAttributesPostRequest**](AdditionalAttributesPostRequest.md)|  | 

### Return type

[**AdditionalAttributesIdGet200Response**](AdditionalAttributesIdGet200Response.md)

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


# openapi_client.HasDocumentsApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**has_documents_get**](HasDocumentsApi.md#has_documents_get) | **GET** /has_documents | List all Has Documentss
[**has_documents_id_delete**](HasDocumentsApi.md#has_documents_id_delete) | **DELETE** /has_documents/{id} | Delete a Has Documents
[**has_documents_id_get**](HasDocumentsApi.md#has_documents_id_get) | **GET** /has_documents/{id} | Show a single Has Documents
[**has_documents_id_patch**](HasDocumentsApi.md#has_documents_id_patch) | **PATCH** /has_documents/{id} | Update a Has Documents
[**has_documents_post**](HasDocumentsApi.md#has_documents_post) | **POST** /has_documents | Create a Has Documents


# **has_documents_get**
> HasDocumentsGet200Response has_documents_get(filter_id=filter_id)

List all Has Documentss

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.has_documents_get200_response import HasDocumentsGet200Response
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
    api_instance = openapi_client.HasDocumentsApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Has Documentss
        api_response = api_instance.has_documents_get(filter_id=filter_id)
        print("The response of HasDocumentsApi->has_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HasDocumentsApi->has_documents_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**HasDocumentsGet200Response**](HasDocumentsGet200Response.md)

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

# **has_documents_id_delete**
> HasDocumentsIdGet200Response has_documents_id_delete(id)

Delete a Has Documents

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.has_documents_id_get200_response import HasDocumentsIdGet200Response
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
    api_instance = openapi_client.HasDocumentsApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Has Documents
        api_response = api_instance.has_documents_id_delete(id)
        print("The response of HasDocumentsApi->has_documents_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HasDocumentsApi->has_documents_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HasDocumentsIdGet200Response**](HasDocumentsIdGet200Response.md)

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

# **has_documents_id_get**
> HasDocumentsIdGet200Response has_documents_id_get(id)

Show a single Has Documents

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.has_documents_id_get200_response import HasDocumentsIdGet200Response
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
    api_instance = openapi_client.HasDocumentsApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Has Documents
        api_response = api_instance.has_documents_id_get(id)
        print("The response of HasDocumentsApi->has_documents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HasDocumentsApi->has_documents_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HasDocumentsIdGet200Response**](HasDocumentsIdGet200Response.md)

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

# **has_documents_id_patch**
> HasDocumentsIdGet200Response has_documents_id_patch(id, has_documents_id_patch_request)

Update a Has Documents

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.has_documents_id_get200_response import HasDocumentsIdGet200Response
from openapi_client.models.has_documents_id_patch_request import HasDocumentsIdPatchRequest
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
    api_instance = openapi_client.HasDocumentsApi(api_client)
    id = 56 # int | 
    has_documents_id_patch_request = openapi_client.HasDocumentsIdPatchRequest() # HasDocumentsIdPatchRequest | 

    try:
        # Update a Has Documents
        api_response = api_instance.has_documents_id_patch(id, has_documents_id_patch_request)
        print("The response of HasDocumentsApi->has_documents_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HasDocumentsApi->has_documents_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **has_documents_id_patch_request** | [**HasDocumentsIdPatchRequest**](HasDocumentsIdPatchRequest.md)|  | 

### Return type

[**HasDocumentsIdGet200Response**](HasDocumentsIdGet200Response.md)

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

# **has_documents_post**
> HasDocumentsIdGet200Response has_documents_post(has_documents_post_request)

Create a Has Documents

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.has_documents_id_get200_response import HasDocumentsIdGet200Response
from openapi_client.models.has_documents_post_request import HasDocumentsPostRequest
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
    api_instance = openapi_client.HasDocumentsApi(api_client)
    has_documents_post_request = openapi_client.HasDocumentsPostRequest() # HasDocumentsPostRequest | 

    try:
        # Create a Has Documents
        api_response = api_instance.has_documents_post(has_documents_post_request)
        print("The response of HasDocumentsApi->has_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HasDocumentsApi->has_documents_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_documents_post_request** | [**HasDocumentsPostRequest**](HasDocumentsPostRequest.md)|  | 

### Return type

[**HasDocumentsIdGet200Response**](HasDocumentsIdGet200Response.md)

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


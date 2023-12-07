# webshipperv2.DocumentApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_get**](DocumentApi.md#documents_get) | **GET** /documents | List all Documents
[**documents_id_delete**](DocumentApi.md#documents_id_delete) | **DELETE** /documents/{id} | Delete a Document
[**documents_id_get**](DocumentApi.md#documents_id_get) | **GET** /documents/{id} | Show a single Document
[**documents_id_patch**](DocumentApi.md#documents_id_patch) | **PATCH** /documents/{id} | Update a Document
[**documents_post**](DocumentApi.md#documents_post) | **POST** /documents | Create a Document


# **documents_get**
> DocumentsGet200Response documents_get(filter_id=filter_id, filter_is_special=filter_is_special)

List all Documents

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.documents_get200_response import DocumentsGet200Response
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
    api_instance = webshipperv2.DocumentApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_is_special = 'filter_is_special_example' # str | Filter by is_special (optional)

    try:
        # List all Documents
        api_response = api_instance.documents_get(filter_id=filter_id, filter_is_special=filter_is_special)
        print("The response of DocumentApi->documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->documents_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_is_special** | **str**| Filter by is_special | [optional] 

### Return type

[**DocumentsGet200Response**](DocumentsGet200Response.md)

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

# **documents_id_delete**
> DocumentsIdGet200Response documents_id_delete(id)

Delete a Document

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.documents_id_get200_response import DocumentsIdGet200Response
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
    api_instance = webshipperv2.DocumentApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Document
        api_response = api_instance.documents_id_delete(id)
        print("The response of DocumentApi->documents_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->documents_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DocumentsIdGet200Response**](DocumentsIdGet200Response.md)

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

# **documents_id_get**
> DocumentsIdGet200Response documents_id_get(id)

Show a single Document

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.documents_id_get200_response import DocumentsIdGet200Response
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
    api_instance = webshipperv2.DocumentApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Document
        api_response = api_instance.documents_id_get(id)
        print("The response of DocumentApi->documents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->documents_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**DocumentsIdGet200Response**](DocumentsIdGet200Response.md)

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

# **documents_id_patch**
> DocumentsIdGet200Response documents_id_patch(id, documents_id_patch_request)

Update a Document

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.documents_id_get200_response import DocumentsIdGet200Response
from webshipperv2.models.documents_id_patch_request import DocumentsIdPatchRequest
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
    api_instance = webshipperv2.DocumentApi(api_client)
    id = 56 # int | 
    documents_id_patch_request = webshipperv2.DocumentsIdPatchRequest() # DocumentsIdPatchRequest | 

    try:
        # Update a Document
        api_response = api_instance.documents_id_patch(id, documents_id_patch_request)
        print("The response of DocumentApi->documents_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->documents_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **documents_id_patch_request** | [**DocumentsIdPatchRequest**](DocumentsIdPatchRequest.md)|  | 

### Return type

[**DocumentsIdGet200Response**](DocumentsIdGet200Response.md)

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

# **documents_post**
> DocumentsIdGet200Response documents_post(documents_post_request)

Create a Document

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.documents_id_get200_response import DocumentsIdGet200Response
from webshipperv2.models.documents_post_request import DocumentsPostRequest
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
    api_instance = webshipperv2.DocumentApi(api_client)
    documents_post_request = webshipperv2.DocumentsPostRequest() # DocumentsPostRequest | 

    try:
        # Create a Document
        api_response = api_instance.documents_post(documents_post_request)
        print("The response of DocumentApi->documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->documents_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_post_request** | [**DocumentsPostRequest**](DocumentsPostRequest.md)|  | 

### Return type

[**DocumentsIdGet200Response**](DocumentsIdGet200Response.md)

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


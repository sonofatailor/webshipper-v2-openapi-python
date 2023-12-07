# webshipperv2.AttachmentApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_get**](AttachmentApi.md#attachments_get) | **GET** /attachments | List all Attachments
[**attachments_id_delete**](AttachmentApi.md#attachments_id_delete) | **DELETE** /attachments/{id} | Delete a Attachment
[**attachments_id_get**](AttachmentApi.md#attachments_id_get) | **GET** /attachments/{id} | Show a single Attachment
[**attachments_id_patch**](AttachmentApi.md#attachments_id_patch) | **PATCH** /attachments/{id} | Update a Attachment
[**attachments_post**](AttachmentApi.md#attachments_post) | **POST** /attachments | Create a Attachment


# **attachments_get**
> AttachmentsGet200Response attachments_get(filter_id=filter_id)

List all Attachments

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.attachments_get200_response import AttachmentsGet200Response
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
    api_instance = webshipperv2.AttachmentApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Attachments
        api_response = api_instance.attachments_get(filter_id=filter_id)
        print("The response of AttachmentApi->attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentApi->attachments_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**AttachmentsGet200Response**](AttachmentsGet200Response.md)

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

# **attachments_id_delete**
> AttachmentsIdGet200Response attachments_id_delete(id)

Delete a Attachment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.attachments_id_get200_response import AttachmentsIdGet200Response
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
    api_instance = webshipperv2.AttachmentApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Attachment
        api_response = api_instance.attachments_id_delete(id)
        print("The response of AttachmentApi->attachments_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentApi->attachments_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AttachmentsIdGet200Response**](AttachmentsIdGet200Response.md)

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

# **attachments_id_get**
> AttachmentsIdGet200Response attachments_id_get(id)

Show a single Attachment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.attachments_id_get200_response import AttachmentsIdGet200Response
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
    api_instance = webshipperv2.AttachmentApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Attachment
        api_response = api_instance.attachments_id_get(id)
        print("The response of AttachmentApi->attachments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentApi->attachments_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AttachmentsIdGet200Response**](AttachmentsIdGet200Response.md)

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

# **attachments_id_patch**
> AttachmentsIdGet200Response attachments_id_patch(id, attachments_id_patch_request)

Update a Attachment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.attachments_id_get200_response import AttachmentsIdGet200Response
from webshipperv2.models.attachments_id_patch_request import AttachmentsIdPatchRequest
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
    api_instance = webshipperv2.AttachmentApi(api_client)
    id = 56 # int | 
    attachments_id_patch_request = webshipperv2.AttachmentsIdPatchRequest() # AttachmentsIdPatchRequest | 

    try:
        # Update a Attachment
        api_response = api_instance.attachments_id_patch(id, attachments_id_patch_request)
        print("The response of AttachmentApi->attachments_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentApi->attachments_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **attachments_id_patch_request** | [**AttachmentsIdPatchRequest**](AttachmentsIdPatchRequest.md)|  | 

### Return type

[**AttachmentsIdGet200Response**](AttachmentsIdGet200Response.md)

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

# **attachments_post**
> AttachmentsIdGet200Response attachments_post(attachments_post_request)

Create a Attachment

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.attachments_id_get200_response import AttachmentsIdGet200Response
from webshipperv2.models.attachments_post_request import AttachmentsPostRequest
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
    api_instance = webshipperv2.AttachmentApi(api_client)
    attachments_post_request = {"data":{"type":"attachments","relationships":{"document":{"data":{"type":"documents","id":532}},"has_documents":{"data":{"type":"orders","id":532}}}}} # AttachmentsPostRequest | 

    try:
        # Create a Attachment
        api_response = api_instance.attachments_post(attachments_post_request)
        print("The response of AttachmentApi->attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentApi->attachments_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_post_request** | [**AttachmentsPostRequest**](AttachmentsPostRequest.md)|  | 

### Return type

[**AttachmentsIdGet200Response**](AttachmentsIdGet200Response.md)

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


# webshipperv2.MailTemplatePreviewApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mail_template_previews_get**](MailTemplatePreviewApi.md#mail_template_previews_get) | **GET** /mail_template_previews | List all Mail Template Previews
[**mail_template_previews_id_delete**](MailTemplatePreviewApi.md#mail_template_previews_id_delete) | **DELETE** /mail_template_previews/{id} | Delete a Mail Template Preview
[**mail_template_previews_id_get**](MailTemplatePreviewApi.md#mail_template_previews_id_get) | **GET** /mail_template_previews/{id} | Show a single Mail Template Preview
[**mail_template_previews_id_patch**](MailTemplatePreviewApi.md#mail_template_previews_id_patch) | **PATCH** /mail_template_previews/{id} | Update a Mail Template Preview
[**mail_template_previews_post**](MailTemplatePreviewApi.md#mail_template_previews_post) | **POST** /mail_template_previews | Create a Mail Template Preview


# **mail_template_previews_get**
> MailTemplatePreviewsGet200Response mail_template_previews_get(filter_id=filter_id)

List all Mail Template Previews

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_template_previews_get200_response import MailTemplatePreviewsGet200Response
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
    api_instance = webshipperv2.MailTemplatePreviewApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all Mail Template Previews
        api_response = api_instance.mail_template_previews_get(filter_id=filter_id)
        print("The response of MailTemplatePreviewApi->mail_template_previews_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatePreviewApi->mail_template_previews_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**MailTemplatePreviewsGet200Response**](MailTemplatePreviewsGet200Response.md)

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

# **mail_template_previews_id_delete**
> MailTemplatePreviewsIdGet200Response mail_template_previews_id_delete(id)

Delete a Mail Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_template_previews_id_get200_response import MailTemplatePreviewsIdGet200Response
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
    api_instance = webshipperv2.MailTemplatePreviewApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Mail Template Preview
        api_response = api_instance.mail_template_previews_id_delete(id)
        print("The response of MailTemplatePreviewApi->mail_template_previews_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatePreviewApi->mail_template_previews_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MailTemplatePreviewsIdGet200Response**](MailTemplatePreviewsIdGet200Response.md)

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

# **mail_template_previews_id_get**
> MailTemplatePreviewsIdGet200Response mail_template_previews_id_get(id)

Show a single Mail Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_template_previews_id_get200_response import MailTemplatePreviewsIdGet200Response
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
    api_instance = webshipperv2.MailTemplatePreviewApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Mail Template Preview
        api_response = api_instance.mail_template_previews_id_get(id)
        print("The response of MailTemplatePreviewApi->mail_template_previews_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatePreviewApi->mail_template_previews_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MailTemplatePreviewsIdGet200Response**](MailTemplatePreviewsIdGet200Response.md)

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

# **mail_template_previews_id_patch**
> MailTemplatePreviewsIdGet200Response mail_template_previews_id_patch(id, mail_template_previews_id_patch_request)

Update a Mail Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_template_previews_id_get200_response import MailTemplatePreviewsIdGet200Response
from webshipperv2.models.mail_template_previews_id_patch_request import MailTemplatePreviewsIdPatchRequest
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
    api_instance = webshipperv2.MailTemplatePreviewApi(api_client)
    id = 56 # int | 
    mail_template_previews_id_patch_request = webshipperv2.MailTemplatePreviewsIdPatchRequest() # MailTemplatePreviewsIdPatchRequest | 

    try:
        # Update a Mail Template Preview
        api_response = api_instance.mail_template_previews_id_patch(id, mail_template_previews_id_patch_request)
        print("The response of MailTemplatePreviewApi->mail_template_previews_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatePreviewApi->mail_template_previews_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **mail_template_previews_id_patch_request** | [**MailTemplatePreviewsIdPatchRequest**](MailTemplatePreviewsIdPatchRequest.md)|  | 

### Return type

[**MailTemplatePreviewsIdGet200Response**](MailTemplatePreviewsIdGet200Response.md)

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

# **mail_template_previews_post**
> MailTemplatePreviewsIdGet200Response mail_template_previews_post(mail_template_previews_post_request)

Create a Mail Template Preview

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_template_previews_id_get200_response import MailTemplatePreviewsIdGet200Response
from webshipperv2.models.mail_template_previews_post_request import MailTemplatePreviewsPostRequest
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
    api_instance = webshipperv2.MailTemplatePreviewApi(api_client)
    mail_template_previews_post_request = webshipperv2.MailTemplatePreviewsPostRequest() # MailTemplatePreviewsPostRequest | 

    try:
        # Create a Mail Template Preview
        api_response = api_instance.mail_template_previews_post(mail_template_previews_post_request)
        print("The response of MailTemplatePreviewApi->mail_template_previews_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatePreviewApi->mail_template_previews_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_template_previews_post_request** | [**MailTemplatePreviewsPostRequest**](MailTemplatePreviewsPostRequest.md)|  | 

### Return type

[**MailTemplatePreviewsIdGet200Response**](MailTemplatePreviewsIdGet200Response.md)

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


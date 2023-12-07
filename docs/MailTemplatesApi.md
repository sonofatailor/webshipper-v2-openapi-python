# webshipperv2.MailTemplatesApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mail_templates_get**](MailTemplatesApi.md#mail_templates_get) | **GET** /mail_templates | List all Mail Templatess
[**mail_templates_id_delete**](MailTemplatesApi.md#mail_templates_id_delete) | **DELETE** /mail_templates/{id} | Delete a Mail Templates
[**mail_templates_id_get**](MailTemplatesApi.md#mail_templates_id_get) | **GET** /mail_templates/{id} | Show a single Mail Templates
[**mail_templates_id_patch**](MailTemplatesApi.md#mail_templates_id_patch) | **PATCH** /mail_templates/{id} | Update a Mail Templates
[**mail_templates_post**](MailTemplatesApi.md#mail_templates_post) | **POST** /mail_templates | Create a Mail Templates


# **mail_templates_get**
> MailTemplatesGet200Response mail_templates_get(filter_id=filter_id, filter_purpose=filter_purpose)

List all Mail Templatess

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_templates_get200_response import MailTemplatesGet200Response
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
    api_instance = webshipperv2.MailTemplatesApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_purpose = 'filter_purpose_example' # str | Filter by purpose (optional)

    try:
        # List all Mail Templatess
        api_response = api_instance.mail_templates_get(filter_id=filter_id, filter_purpose=filter_purpose)
        print("The response of MailTemplatesApi->mail_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->mail_templates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_purpose** | **str**| Filter by purpose | [optional] 

### Return type

[**MailTemplatesGet200Response**](MailTemplatesGet200Response.md)

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

# **mail_templates_id_delete**
> MailTemplatesIdGet200Response mail_templates_id_delete(id)

Delete a Mail Templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_templates_id_get200_response import MailTemplatesIdGet200Response
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
    api_instance = webshipperv2.MailTemplatesApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Mail Templates
        api_response = api_instance.mail_templates_id_delete(id)
        print("The response of MailTemplatesApi->mail_templates_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->mail_templates_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MailTemplatesIdGet200Response**](MailTemplatesIdGet200Response.md)

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

# **mail_templates_id_get**
> MailTemplatesIdGet200Response mail_templates_id_get(id)

Show a single Mail Templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_templates_id_get200_response import MailTemplatesIdGet200Response
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
    api_instance = webshipperv2.MailTemplatesApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Mail Templates
        api_response = api_instance.mail_templates_id_get(id)
        print("The response of MailTemplatesApi->mail_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->mail_templates_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MailTemplatesIdGet200Response**](MailTemplatesIdGet200Response.md)

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

# **mail_templates_id_patch**
> MailTemplatesIdGet200Response mail_templates_id_patch(id, mail_templates_id_patch_request)

Update a Mail Templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_templates_id_get200_response import MailTemplatesIdGet200Response
from webshipperv2.models.mail_templates_id_patch_request import MailTemplatesIdPatchRequest
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
    api_instance = webshipperv2.MailTemplatesApi(api_client)
    id = 56 # int | 
    mail_templates_id_patch_request = webshipperv2.MailTemplatesIdPatchRequest() # MailTemplatesIdPatchRequest | 

    try:
        # Update a Mail Templates
        api_response = api_instance.mail_templates_id_patch(id, mail_templates_id_patch_request)
        print("The response of MailTemplatesApi->mail_templates_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->mail_templates_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **mail_templates_id_patch_request** | [**MailTemplatesIdPatchRequest**](MailTemplatesIdPatchRequest.md)|  | 

### Return type

[**MailTemplatesIdGet200Response**](MailTemplatesIdGet200Response.md)

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

# **mail_templates_post**
> MailTemplatesIdGet200Response mail_templates_post(mail_templates_post_request)

Create a Mail Templates

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.mail_templates_id_get200_response import MailTemplatesIdGet200Response
from webshipperv2.models.mail_templates_post_request import MailTemplatesPostRequest
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
    api_instance = webshipperv2.MailTemplatesApi(api_client)
    mail_templates_post_request = webshipperv2.MailTemplatesPostRequest() # MailTemplatesPostRequest | 

    try:
        # Create a Mail Templates
        api_response = api_instance.mail_templates_post(mail_templates_post_request)
        print("The response of MailTemplatesApi->mail_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplatesApi->mail_templates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_templates_post_request** | [**MailTemplatesPostRequest**](MailTemplatesPostRequest.md)|  | 

### Return type

[**MailTemplatesIdGet200Response**](MailTemplatesIdGet200Response.md)

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


# openapi_client.UserGroupApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_groups_get**](UserGroupApi.md#user_groups_get) | **GET** /user_groups | List all User Groups
[**user_groups_id_delete**](UserGroupApi.md#user_groups_id_delete) | **DELETE** /user_groups/{id} | Delete a User Group
[**user_groups_id_get**](UserGroupApi.md#user_groups_id_get) | **GET** /user_groups/{id} | Show a single User Group
[**user_groups_id_patch**](UserGroupApi.md#user_groups_id_patch) | **PATCH** /user_groups/{id} | Update a User Group
[**user_groups_post**](UserGroupApi.md#user_groups_post) | **POST** /user_groups | Create a User Group


# **user_groups_get**
> UserGroupsGet200Response user_groups_get(filter_id=filter_id)

List all User Groups

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_groups_get200_response import UserGroupsGet200Response
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
    api_instance = openapi_client.UserGroupApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all User Groups
        api_response = api_instance.user_groups_get(filter_id=filter_id)
        print("The response of UserGroupApi->user_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->user_groups_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**UserGroupsGet200Response**](UserGroupsGet200Response.md)

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

# **user_groups_id_delete**
> UserGroupsIdGet200Response user_groups_id_delete(id)

Delete a User Group

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_groups_id_get200_response import UserGroupsIdGet200Response
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 56 # int | 

    try:
        # Delete a User Group
        api_response = api_instance.user_groups_id_delete(id)
        print("The response of UserGroupApi->user_groups_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->user_groups_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserGroupsIdGet200Response**](UserGroupsIdGet200Response.md)

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

# **user_groups_id_get**
> UserGroupsIdGet200Response user_groups_id_get(id)

Show a single User Group

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_groups_id_get200_response import UserGroupsIdGet200Response
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 56 # int | 

    try:
        # Show a single User Group
        api_response = api_instance.user_groups_id_get(id)
        print("The response of UserGroupApi->user_groups_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->user_groups_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserGroupsIdGet200Response**](UserGroupsIdGet200Response.md)

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

# **user_groups_id_patch**
> UserGroupsIdGet200Response user_groups_id_patch(id, user_groups_id_patch_request)

Update a User Group

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_groups_id_get200_response import UserGroupsIdGet200Response
from openapi_client.models.user_groups_id_patch_request import UserGroupsIdPatchRequest
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 56 # int | 
    user_groups_id_patch_request = openapi_client.UserGroupsIdPatchRequest() # UserGroupsIdPatchRequest | 

    try:
        # Update a User Group
        api_response = api_instance.user_groups_id_patch(id, user_groups_id_patch_request)
        print("The response of UserGroupApi->user_groups_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->user_groups_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **user_groups_id_patch_request** | [**UserGroupsIdPatchRequest**](UserGroupsIdPatchRequest.md)|  | 

### Return type

[**UserGroupsIdGet200Response**](UserGroupsIdGet200Response.md)

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

# **user_groups_post**
> UserGroupsIdGet200Response user_groups_post(user_groups_post_request)

Create a User Group

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_groups_id_get200_response import UserGroupsIdGet200Response
from openapi_client.models.user_groups_post_request import UserGroupsPostRequest
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
    api_instance = openapi_client.UserGroupApi(api_client)
    user_groups_post_request = openapi_client.UserGroupsPostRequest() # UserGroupsPostRequest | 

    try:
        # Create a User Group
        api_response = api_instance.user_groups_post(user_groups_post_request)
        print("The response of UserGroupApi->user_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->user_groups_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_groups_post_request** | [**UserGroupsPostRequest**](UserGroupsPostRequest.md)|  | 

### Return type

[**UserGroupsIdGet200Response**](UserGroupsIdGet200Response.md)

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


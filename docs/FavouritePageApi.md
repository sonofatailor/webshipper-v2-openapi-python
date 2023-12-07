# webshipperv2.FavouritePageApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favourite_pages_get**](FavouritePageApi.md#favourite_pages_get) | **GET** /favourite_pages | List all Favourite Pages
[**favourite_pages_id_delete**](FavouritePageApi.md#favourite_pages_id_delete) | **DELETE** /favourite_pages/{id} | Delete a Favourite Page
[**favourite_pages_id_get**](FavouritePageApi.md#favourite_pages_id_get) | **GET** /favourite_pages/{id} | Show a single Favourite Page
[**favourite_pages_id_patch**](FavouritePageApi.md#favourite_pages_id_patch) | **PATCH** /favourite_pages/{id} | Update a Favourite Page
[**favourite_pages_post**](FavouritePageApi.md#favourite_pages_post) | **POST** /favourite_pages | Create a Favourite Page


# **favourite_pages_get**
> FavouritePagesGet200Response favourite_pages_get(filter_id=filter_id, filter_user_id=filter_user_id)

List all Favourite Pages

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.favourite_pages_get200_response import FavouritePagesGet200Response
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
    api_instance = webshipperv2.FavouritePageApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_user_id = 'filter_user_id_example' # str | Filter by user_id (optional)

    try:
        # List all Favourite Pages
        api_response = api_instance.favourite_pages_get(filter_id=filter_id, filter_user_id=filter_user_id)
        print("The response of FavouritePageApi->favourite_pages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavouritePageApi->favourite_pages_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_user_id** | **str**| Filter by user_id | [optional] 

### Return type

[**FavouritePagesGet200Response**](FavouritePagesGet200Response.md)

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

# **favourite_pages_id_delete**
> FavouritePagesIdGet200Response favourite_pages_id_delete(id)

Delete a Favourite Page

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.favourite_pages_id_get200_response import FavouritePagesIdGet200Response
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
    api_instance = webshipperv2.FavouritePageApi(api_client)
    id = 56 # int | 

    try:
        # Delete a Favourite Page
        api_response = api_instance.favourite_pages_id_delete(id)
        print("The response of FavouritePageApi->favourite_pages_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavouritePageApi->favourite_pages_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FavouritePagesIdGet200Response**](FavouritePagesIdGet200Response.md)

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

# **favourite_pages_id_get**
> FavouritePagesIdGet200Response favourite_pages_id_get(id)

Show a single Favourite Page

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.favourite_pages_id_get200_response import FavouritePagesIdGet200Response
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
    api_instance = webshipperv2.FavouritePageApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Favourite Page
        api_response = api_instance.favourite_pages_id_get(id)
        print("The response of FavouritePageApi->favourite_pages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavouritePageApi->favourite_pages_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FavouritePagesIdGet200Response**](FavouritePagesIdGet200Response.md)

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

# **favourite_pages_id_patch**
> FavouritePagesIdGet200Response favourite_pages_id_patch(id, favourite_pages_id_patch_request)

Update a Favourite Page

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.favourite_pages_id_get200_response import FavouritePagesIdGet200Response
from webshipperv2.models.favourite_pages_id_patch_request import FavouritePagesIdPatchRequest
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
    api_instance = webshipperv2.FavouritePageApi(api_client)
    id = 56 # int | 
    favourite_pages_id_patch_request = webshipperv2.FavouritePagesIdPatchRequest() # FavouritePagesIdPatchRequest | 

    try:
        # Update a Favourite Page
        api_response = api_instance.favourite_pages_id_patch(id, favourite_pages_id_patch_request)
        print("The response of FavouritePageApi->favourite_pages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavouritePageApi->favourite_pages_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **favourite_pages_id_patch_request** | [**FavouritePagesIdPatchRequest**](FavouritePagesIdPatchRequest.md)|  | 

### Return type

[**FavouritePagesIdGet200Response**](FavouritePagesIdGet200Response.md)

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

# **favourite_pages_post**
> FavouritePagesIdGet200Response favourite_pages_post(favourite_pages_post_request)

Create a Favourite Page

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.favourite_pages_id_get200_response import FavouritePagesIdGet200Response
from webshipperv2.models.favourite_pages_post_request import FavouritePagesPostRequest
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
    api_instance = webshipperv2.FavouritePageApi(api_client)
    favourite_pages_post_request = webshipperv2.FavouritePagesPostRequest() # FavouritePagesPostRequest | 

    try:
        # Create a Favourite Page
        api_response = api_instance.favourite_pages_post(favourite_pages_post_request)
        print("The response of FavouritePageApi->favourite_pages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FavouritePageApi->favourite_pages_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favourite_pages_post_request** | [**FavouritePagesPostRequest**](FavouritePagesPostRequest.md)|  | 

### Return type

[**FavouritePagesIdGet200Response**](FavouritePagesIdGet200Response.md)

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


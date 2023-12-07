# openapi_client.OAuthAccessTokenApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_access_tokens_get**](OAuthAccessTokenApi.md#oauth_access_tokens_get) | **GET** /oauth_access_tokens | List all OAuth Access Tokens
[**oauth_access_tokens_id_get**](OAuthAccessTokenApi.md#oauth_access_tokens_id_get) | **GET** /oauth_access_tokens/{id} | Show a single OAuth Access Token


# **oauth_access_tokens_get**
> OauthAccessTokensGet200Response oauth_access_tokens_get(filter_id=filter_id)

List all OAuth Access Tokens

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.oauth_access_tokens_get200_response import OauthAccessTokensGet200Response
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
    api_instance = openapi_client.OAuthAccessTokenApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all OAuth Access Tokens
        api_response = api_instance.oauth_access_tokens_get(filter_id=filter_id)
        print("The response of OAuthAccessTokenApi->oauth_access_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthAccessTokenApi->oauth_access_tokens_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**OauthAccessTokensGet200Response**](OauthAccessTokensGet200Response.md)

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

# **oauth_access_tokens_id_get**
> OauthAccessTokensIdGet200Response oauth_access_tokens_id_get(id)

Show a single OAuth Access Token

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.oauth_access_tokens_id_get200_response import OauthAccessTokensIdGet200Response
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
    api_instance = openapi_client.OAuthAccessTokenApi(api_client)
    id = 56 # int | 

    try:
        # Show a single OAuth Access Token
        api_response = api_instance.oauth_access_tokens_id_get(id)
        print("The response of OAuthAccessTokenApi->oauth_access_tokens_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthAccessTokenApi->oauth_access_tokens_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OauthAccessTokensIdGet200Response**](OauthAccessTokensIdGet200Response.md)

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

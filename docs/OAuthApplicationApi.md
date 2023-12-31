# webshipperv2.OAuthApplicationApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_applications_get**](OAuthApplicationApi.md#oauth_applications_get) | **GET** /oauth_applications | List all OAuth Applications
[**oauth_applications_id_get**](OAuthApplicationApi.md#oauth_applications_id_get) | **GET** /oauth_applications/{id} | Show a single OAuth Application


# **oauth_applications_get**
> OauthApplicationsGet200Response oauth_applications_get(filter_id=filter_id, filter_uid=filter_uid, filter_active=filter_active)

List all OAuth Applications

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.oauth_applications_get200_response import OauthApplicationsGet200Response
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
    api_instance = webshipperv2.OAuthApplicationApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_uid = 'filter_uid_example' # str | Filter by uid (optional)
    filter_active = 'filter_active_example' # str | Filter by active (optional)

    try:
        # List all OAuth Applications
        api_response = api_instance.oauth_applications_get(filter_id=filter_id, filter_uid=filter_uid, filter_active=filter_active)
        print("The response of OAuthApplicationApi->oauth_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationApi->oauth_applications_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_uid** | **str**| Filter by uid | [optional] 
 **filter_active** | **str**| Filter by active | [optional] 

### Return type

[**OauthApplicationsGet200Response**](OauthApplicationsGet200Response.md)

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

# **oauth_applications_id_get**
> OauthApplicationsIdGet200Response oauth_applications_id_get(id)

Show a single OAuth Application

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.oauth_applications_id_get200_response import OauthApplicationsIdGet200Response
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
    api_instance = webshipperv2.OAuthApplicationApi(api_client)
    id = 56 # int | 

    try:
        # Show a single OAuth Application
        api_response = api_instance.oauth_applications_id_get(id)
        print("The response of OAuthApplicationApi->oauth_applications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationApi->oauth_applications_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**OauthApplicationsIdGet200Response**](OauthApplicationsIdGet200Response.md)

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


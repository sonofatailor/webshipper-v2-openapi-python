# webshipperv2.CSVMappingRuleApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csv_rules_get**](CSVMappingRuleApi.md#csv_rules_get) | **GET** /csv_rules | List all CSV Mapping Rules
[**csv_rules_id_delete**](CSVMappingRuleApi.md#csv_rules_id_delete) | **DELETE** /csv_rules/{id} | Delete a CSV Mapping Rule
[**csv_rules_id_get**](CSVMappingRuleApi.md#csv_rules_id_get) | **GET** /csv_rules/{id} | Show a single CSV Mapping Rule
[**csv_rules_id_patch**](CSVMappingRuleApi.md#csv_rules_id_patch) | **PATCH** /csv_rules/{id} | Update a CSV Mapping Rule
[**csv_rules_post**](CSVMappingRuleApi.md#csv_rules_post) | **POST** /csv_rules | Create a CSV Mapping Rule


# **csv_rules_get**
> CsvRulesGet200Response csv_rules_get(filter_id=filter_id)

List all CSV Mapping Rules

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_rules_get200_response import CsvRulesGet200Response
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
    api_instance = webshipperv2.CSVMappingRuleApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)

    try:
        # List all CSV Mapping Rules
        api_response = api_instance.csv_rules_get(filter_id=filter_id)
        print("The response of CSVMappingRuleApi->csv_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingRuleApi->csv_rules_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 

### Return type

[**CsvRulesGet200Response**](CsvRulesGet200Response.md)

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

# **csv_rules_id_delete**
> CsvRulesIdGet200Response csv_rules_id_delete(id)

Delete a CSV Mapping Rule

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_rules_id_get200_response import CsvRulesIdGet200Response
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
    api_instance = webshipperv2.CSVMappingRuleApi(api_client)
    id = 56 # int | 

    try:
        # Delete a CSV Mapping Rule
        api_response = api_instance.csv_rules_id_delete(id)
        print("The response of CSVMappingRuleApi->csv_rules_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingRuleApi->csv_rules_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CsvRulesIdGet200Response**](CsvRulesIdGet200Response.md)

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

# **csv_rules_id_get**
> CsvRulesIdGet200Response csv_rules_id_get(id)

Show a single CSV Mapping Rule

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_rules_id_get200_response import CsvRulesIdGet200Response
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
    api_instance = webshipperv2.CSVMappingRuleApi(api_client)
    id = 56 # int | 

    try:
        # Show a single CSV Mapping Rule
        api_response = api_instance.csv_rules_id_get(id)
        print("The response of CSVMappingRuleApi->csv_rules_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingRuleApi->csv_rules_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CsvRulesIdGet200Response**](CsvRulesIdGet200Response.md)

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

# **csv_rules_id_patch**
> CsvRulesIdGet200Response csv_rules_id_patch(id, csv_rules_id_patch_request)

Update a CSV Mapping Rule

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_rules_id_get200_response import CsvRulesIdGet200Response
from webshipperv2.models.csv_rules_id_patch_request import CsvRulesIdPatchRequest
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
    api_instance = webshipperv2.CSVMappingRuleApi(api_client)
    id = 56 # int | 
    csv_rules_id_patch_request = webshipperv2.CsvRulesIdPatchRequest() # CsvRulesIdPatchRequest | 

    try:
        # Update a CSV Mapping Rule
        api_response = api_instance.csv_rules_id_patch(id, csv_rules_id_patch_request)
        print("The response of CSVMappingRuleApi->csv_rules_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingRuleApi->csv_rules_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **csv_rules_id_patch_request** | [**CsvRulesIdPatchRequest**](CsvRulesIdPatchRequest.md)|  | 

### Return type

[**CsvRulesIdGet200Response**](CsvRulesIdGet200Response.md)

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

# **csv_rules_post**
> CsvRulesIdGet200Response csv_rules_post(csv_rules_post_request)

Create a CSV Mapping Rule

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_rules_id_get200_response import CsvRulesIdGet200Response
from webshipperv2.models.csv_rules_post_request import CsvRulesPostRequest
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
    api_instance = webshipperv2.CSVMappingRuleApi(api_client)
    csv_rules_post_request = webshipperv2.CsvRulesPostRequest() # CsvRulesPostRequest | 

    try:
        # Create a CSV Mapping Rule
        api_response = api_instance.csv_rules_post(csv_rules_post_request)
        print("The response of CSVMappingRuleApi->csv_rules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVMappingRuleApi->csv_rules_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_rules_post_request** | [**CsvRulesPostRequest**](CsvRulesPostRequest.md)|  | 

### Return type

[**CsvRulesIdGet200Response**](CsvRulesIdGet200Response.md)

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


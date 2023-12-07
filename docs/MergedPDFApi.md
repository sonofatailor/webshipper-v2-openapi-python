# webshipperv2.MergedPDFApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pdf_merges_id_get**](MergedPDFApi.md#pdf_merges_id_get) | **GET** /pdf_merges/{id} | Show a single Merged PDF
[**pdf_merges_post**](MergedPDFApi.md#pdf_merges_post) | **POST** /pdf_merges | Create a Merged PDF


# **pdf_merges_id_get**
> PdfMergesIdGet200Response pdf_merges_id_get(id)

Show a single Merged PDF

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.pdf_merges_id_get200_response import PdfMergesIdGet200Response
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
    api_instance = webshipperv2.MergedPDFApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Merged PDF
        api_response = api_instance.pdf_merges_id_get(id)
        print("The response of MergedPDFApi->pdf_merges_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergedPDFApi->pdf_merges_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PdfMergesIdGet200Response**](PdfMergesIdGet200Response.md)

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

# **pdf_merges_post**
> PdfMergesIdGet200Response pdf_merges_post(pdf_merges_post_request)

Create a Merged PDF

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.pdf_merges_id_get200_response import PdfMergesIdGet200Response
from webshipperv2.models.pdf_merges_post_request import PdfMergesPostRequest
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
    api_instance = webshipperv2.MergedPDFApi(api_client)
    pdf_merges_post_request = webshipperv2.PdfMergesPostRequest() # PdfMergesPostRequest | 

    try:
        # Create a Merged PDF
        api_response = api_instance.pdf_merges_post(pdf_merges_post_request)
        print("The response of MergedPDFApi->pdf_merges_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergedPDFApi->pdf_merges_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_merges_post_request** | [**PdfMergesPostRequest**](PdfMergesPostRequest.md)|  | 

### Return type

[**PdfMergesIdGet200Response**](PdfMergesIdGet200Response.md)

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


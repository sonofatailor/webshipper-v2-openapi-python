# webshipperv2.CSVUploadApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csv_uploads_post**](CSVUploadApi.md#csv_uploads_post) | **POST** /csv_uploads | Create a CSV Upload


# **csv_uploads_post**
> CsvUploadsPost204Response csv_uploads_post(csv_uploads_post_request)

Create a CSV Upload

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.csv_uploads_post204_response import CsvUploadsPost204Response
from webshipperv2.models.csv_uploads_post_request import CsvUploadsPostRequest
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
    api_instance = webshipperv2.CSVUploadApi(api_client)
    csv_uploads_post_request = webshipperv2.CsvUploadsPostRequest() # CsvUploadsPostRequest | 

    try:
        # Create a CSV Upload
        api_response = api_instance.csv_uploads_post(csv_uploads_post_request)
        print("The response of CSVUploadApi->csv_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSVUploadApi->csv_uploads_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_uploads_post_request** | [**CsvUploadsPostRequest**](CsvUploadsPostRequest.md)|  | 

### Return type

[**CsvUploadsPost204Response**](CsvUploadsPost204Response.md)

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


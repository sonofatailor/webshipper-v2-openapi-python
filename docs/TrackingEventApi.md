# webshipperv2.TrackingEventApi

All URIs are relative to *https://.api.webshipper.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tracking_events_get**](TrackingEventApi.md#tracking_events_get) | **GET** /tracking_events | List all Tracking Events
[**tracking_events_id_get**](TrackingEventApi.md#tracking_events_id_get) | **GET** /tracking_events/{id} | Show a single Tracking Event


# **tracking_events_get**
> TrackingEventsGet200Response tracking_events_get(filter_id=filter_id, filter_created_at=filter_created_at, filter_shipment_id=filter_shipment_id)

List all Tracking Events

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.tracking_events_get200_response import TrackingEventsGet200Response
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
    api_instance = webshipperv2.TrackingEventApi(api_client)
    filter_id = 'filter_id_example' # str | Filter by id (optional)
    filter_created_at = 'filter_created_at_example' # str | Filter by created_at (optional)
    filter_shipment_id = 'filter_shipment_id_example' # str | Filter by shipment_id (optional)

    try:
        # List all Tracking Events
        api_response = api_instance.tracking_events_get(filter_id=filter_id, filter_created_at=filter_created_at, filter_shipment_id=filter_shipment_id)
        print("The response of TrackingEventApi->tracking_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingEventApi->tracking_events_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **str**| Filter by id | [optional] 
 **filter_created_at** | **str**| Filter by created_at | [optional] 
 **filter_shipment_id** | **str**| Filter by shipment_id | [optional] 

### Return type

[**TrackingEventsGet200Response**](TrackingEventsGet200Response.md)

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

# **tracking_events_id_get**
> TrackingEventsIdGet200Response tracking_events_id_get(id)

Show a single Tracking Event

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import os
import webshipperv2
from webshipperv2.models.tracking_events_id_get200_response import TrackingEventsIdGet200Response
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
    api_instance = webshipperv2.TrackingEventApi(api_client)
    id = 56 # int | 

    try:
        # Show a single Tracking Event
        api_response = api_instance.tracking_events_id_get(id)
        print("The response of TrackingEventApi->tracking_events_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingEventApi->tracking_events_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TrackingEventsIdGet200Response**](TrackingEventsIdGet200Response.md)

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


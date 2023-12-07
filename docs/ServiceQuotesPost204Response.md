# ServiceQuotesPost204Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceQuotesPost204ResponseData**](ServiceQuotesPost204ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.service_quotes_post204_response import ServiceQuotesPost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotesPost204Response from a JSON string
service_quotes_post204_response_instance = ServiceQuotesPost204Response.from_json(json)
# print the JSON string representation of the object
print ServiceQuotesPost204Response.to_json()

# convert the object into a dict
service_quotes_post204_response_dict = service_quotes_post204_response_instance.to_dict()
# create an instance of ServiceQuotesPost204Response from a dict
service_quotes_post204_response_form_dict = service_quotes_post204_response.from_dict(service_quotes_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServiceQuotesPost204ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ServiceQuotes**](ServiceQuotes.md) |  | [optional] 

## Example

```python
from webshipperv2.models.service_quotes_post204_response_data import ServiceQuotesPost204ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotesPost204ResponseData from a JSON string
service_quotes_post204_response_data_instance = ServiceQuotesPost204ResponseData.from_json(json)
# print the JSON string representation of the object
print ServiceQuotesPost204ResponseData.to_json()

# convert the object into a dict
service_quotes_post204_response_data_dict = service_quotes_post204_response_data_instance.to_dict()
# create an instance of ServiceQuotesPost204ResponseData from a dict
service_quotes_post204_response_data_form_dict = service_quotes_post204_response_data.from_dict(service_quotes_post204_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



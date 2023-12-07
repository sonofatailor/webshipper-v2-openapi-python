# CsvUploadsPost204Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CsvUploadsPost204ResponseData**](CsvUploadsPost204ResponseData.md) |  | [optional] 
**relationships** | [**CsvRulesIdGet200ResponseRelationships**](CsvRulesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[CsvRulesIdGet200ResponseIncludedInner]**](CsvRulesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.csv_uploads_post204_response import CsvUploadsPost204Response

# TODO update the JSON string below
json = "{}"
# create an instance of CsvUploadsPost204Response from a JSON string
csv_uploads_post204_response_instance = CsvUploadsPost204Response.from_json(json)
# print the JSON string representation of the object
print CsvUploadsPost204Response.to_json()

# convert the object into a dict
csv_uploads_post204_response_dict = csv_uploads_post204_response_instance.to_dict()
# create an instance of CsvUploadsPost204Response from a dict
csv_uploads_post204_response_form_dict = csv_uploads_post204_response.from_dict(csv_uploads_post204_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



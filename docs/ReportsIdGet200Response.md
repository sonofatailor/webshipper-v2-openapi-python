# ReportsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportsIdGet200ResponseData**](ReportsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReportsIdGet200ResponseRelationships**](ReportsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ReportsIdGet200ResponseIncludedInner]**](ReportsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.reports_id_get200_response import ReportsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsIdGet200Response from a JSON string
reports_id_get200_response_instance = ReportsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReportsIdGet200Response.to_json()

# convert the object into a dict
reports_id_get200_response_dict = reports_id_get200_response_instance.to_dict()
# create an instance of ReportsIdGet200Response from a dict
reports_id_get200_response_form_dict = reports_id_get200_response.from_dict(reports_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



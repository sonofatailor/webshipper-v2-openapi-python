# ReportTypesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReportTypesIdGet200ResponseData**](ReportTypesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.report_types_id_get200_response import ReportTypesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTypesIdGet200Response from a JSON string
report_types_id_get200_response_instance = ReportTypesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReportTypesIdGet200Response.to_json()

# convert the object into a dict
report_types_id_get200_response_dict = report_types_id_get200_response_instance.to_dict()
# create an instance of ReportTypesIdGet200Response from a dict
report_types_id_get200_response_form_dict = report_types_id_get200_response.from_dict(report_types_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



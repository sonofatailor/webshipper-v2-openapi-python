# CustomsLinesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CustomsLines**](CustomsLines.md) |  | [optional] 

## Example

```python
from webshipperv2.models.customs_lines_id_get200_response_data import CustomsLinesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLinesIdGet200ResponseData from a JSON string
customs_lines_id_get200_response_data_instance = CustomsLinesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print CustomsLinesIdGet200ResponseData.to_json()

# convert the object into a dict
customs_lines_id_get200_response_data_dict = customs_lines_id_get200_response_data_instance.to_dict()
# create an instance of CustomsLinesIdGet200ResponseData from a dict
customs_lines_id_get200_response_data_form_dict = customs_lines_id_get200_response_data.from_dict(customs_lines_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PrintablesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.printables_id_get200_response_data import PrintablesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesIdGet200ResponseData from a JSON string
printables_id_get200_response_data_instance = PrintablesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print PrintablesIdGet200ResponseData.to_json()

# convert the object into a dict
printables_id_get200_response_data_dict = printables_id_get200_response_data_instance.to_dict()
# create an instance of PrintablesIdGet200ResponseData from a dict
printables_id_get200_response_data_form_dict = printables_id_get200_response_data.from_dict(printables_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



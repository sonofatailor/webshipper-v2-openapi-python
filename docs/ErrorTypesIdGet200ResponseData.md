# ErrorTypesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ErrorTypes**](ErrorTypes.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_types_id_get200_response_data import ErrorTypesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorTypesIdGet200ResponseData from a JSON string
error_types_id_get200_response_data_instance = ErrorTypesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ErrorTypesIdGet200ResponseData.to_json()

# convert the object into a dict
error_types_id_get200_response_data_dict = error_types_id_get200_response_data_instance.to_dict()
# create an instance of ErrorTypesIdGet200ResponseData from a dict
error_types_id_get200_response_data_form_dict = error_types_id_get200_response_data.from_dict(error_types_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



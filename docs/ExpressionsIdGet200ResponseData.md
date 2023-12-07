# ExpressionsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Expressions**](Expressions.md) |  | [optional] 

## Example

```python
from webshipperv2.models.expressions_id_get200_response_data import ExpressionsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionsIdGet200ResponseData from a JSON string
expressions_id_get200_response_data_instance = ExpressionsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ExpressionsIdGet200ResponseData.to_json()

# convert the object into a dict
expressions_id_get200_response_data_dict = expressions_id_get200_response_data_instance.to_dict()
# create an instance of ExpressionsIdGet200ResponseData from a dict
expressions_id_get200_response_data_form_dict = expressions_id_get200_response_data.from_dict(expressions_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



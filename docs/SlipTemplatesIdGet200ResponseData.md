# SlipTemplatesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**SlipTemplates**](SlipTemplates.md) |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_id_get200_response_data import SlipTemplatesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesIdGet200ResponseData from a JSON string
slip_templates_id_get200_response_data_instance = SlipTemplatesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesIdGet200ResponseData.to_json()

# convert the object into a dict
slip_templates_id_get200_response_data_dict = slip_templates_id_get200_response_data_instance.to_dict()
# create an instance of SlipTemplatesIdGet200ResponseData from a dict
slip_templates_id_get200_response_data_form_dict = slip_templates_id_get200_response_data.from_dict(slip_templates_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



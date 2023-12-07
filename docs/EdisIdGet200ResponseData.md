# EdisIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Edis**](Edis.md) |  | [optional] 

## Example

```python
from webshipperv2.models.edis_id_get200_response_data import EdisIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of EdisIdGet200ResponseData from a JSON string
edis_id_get200_response_data_instance = EdisIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print EdisIdGet200ResponseData.to_json()

# convert the object into a dict
edis_id_get200_response_data_dict = edis_id_get200_response_data_instance.to_dict()
# create an instance of EdisIdGet200ResponseData from a dict
edis_id_get200_response_data_form_dict = edis_id_get200_response_data.from_dict(edis_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



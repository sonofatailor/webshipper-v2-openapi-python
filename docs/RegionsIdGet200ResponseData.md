# RegionsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Regions**](Regions.md) |  | [optional] 

## Example

```python
from openapi_client.models.regions_id_get200_response_data import RegionsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsIdGet200ResponseData from a JSON string
regions_id_get200_response_data_instance = RegionsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print RegionsIdGet200ResponseData.to_json()

# convert the object into a dict
regions_id_get200_response_data_dict = regions_id_get200_response_data_instance.to_dict()
# create an instance of RegionsIdGet200ResponseData from a dict
regions_id_get200_response_data_form_dict = regions_id_get200_response_data.from_dict(regions_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



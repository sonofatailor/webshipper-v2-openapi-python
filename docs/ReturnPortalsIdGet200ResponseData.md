# ReturnPortalsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ReturnPortals**](ReturnPortals.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_portals_id_get200_response_data import ReturnPortalsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsIdGet200ResponseData from a JSON string
return_portals_id_get200_response_data_instance = ReturnPortalsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsIdGet200ResponseData.to_json()

# convert the object into a dict
return_portals_id_get200_response_data_dict = return_portals_id_get200_response_data_instance.to_dict()
# create an instance of ReturnPortalsIdGet200ResponseData from a dict
return_portals_id_get200_response_data_form_dict = return_portals_id_get200_response_data.from_dict(return_portals_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



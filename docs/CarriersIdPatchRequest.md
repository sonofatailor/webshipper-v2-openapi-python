# CarriersIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CarriersIdGet200ResponseData**](CarriersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**CarriersIdGet200ResponseRelationships**](CarriersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carriers_id_patch_request import CarriersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersIdPatchRequest from a JSON string
carriers_id_patch_request_instance = CarriersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print CarriersIdPatchRequest.to_json()

# convert the object into a dict
carriers_id_patch_request_dict = carriers_id_patch_request_instance.to_dict()
# create an instance of CarriersIdPatchRequest from a dict
carriers_id_patch_request_form_dict = carriers_id_patch_request.from_dict(carriers_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



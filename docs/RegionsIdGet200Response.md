# RegionsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RegionsIdGet200ResponseData**](RegionsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**RegionsIdGet200ResponseRelationships**](RegionsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[RegionsIdGet200ResponseIncludedInner]**](RegionsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.regions_id_get200_response import RegionsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsIdGet200Response from a JSON string
regions_id_get200_response_instance = RegionsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print RegionsIdGet200Response.to_json()

# convert the object into a dict
regions_id_get200_response_dict = regions_id_get200_response_instance.to_dict()
# create an instance of RegionsIdGet200Response from a dict
regions_id_get200_response_form_dict = regions_id_get200_response.from_dict(regions_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LocalAttrsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LocalAttrsIdGet200ResponseData**](LocalAttrsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**LocalAttrsIdGet200ResponseRelationships**](LocalAttrsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[LocalAttrsIdGet200ResponseIncludedInner]**](LocalAttrsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.local_attrs_id_get200_response import LocalAttrsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrsIdGet200Response from a JSON string
local_attrs_id_get200_response_instance = LocalAttrsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print LocalAttrsIdGet200Response.to_json()

# convert the object into a dict
local_attrs_id_get200_response_dict = local_attrs_id_get200_response_instance.to_dict()
# create an instance of LocalAttrsIdGet200Response from a dict
local_attrs_id_get200_response_form_dict = local_attrs_id_get200_response.from_dict(local_attrs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



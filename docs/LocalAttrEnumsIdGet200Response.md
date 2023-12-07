# LocalAttrEnumsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LocalAttrEnumsIdGet200ResponseData**](LocalAttrEnumsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**LocalAttrEnumsIdGet200ResponseRelationships**](LocalAttrEnumsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[LocalAttrEnumsIdGet200ResponseIncludedInner]**](LocalAttrEnumsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.local_attr_enums_id_get200_response import LocalAttrEnumsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrEnumsIdGet200Response from a JSON string
local_attr_enums_id_get200_response_instance = LocalAttrEnumsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print LocalAttrEnumsIdGet200Response.to_json()

# convert the object into a dict
local_attr_enums_id_get200_response_dict = local_attr_enums_id_get200_response_instance.to_dict()
# create an instance of LocalAttrEnumsIdGet200Response from a dict
local_attr_enums_id_get200_response_form_dict = local_attr_enums_id_get200_response.from_dict(local_attr_enums_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



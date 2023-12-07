# LocalAttrEnumsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LocalAttrEnumsGet200ResponseDataInner]**](LocalAttrEnumsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.local_attr_enums_get200_response import LocalAttrEnumsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrEnumsGet200Response from a JSON string
local_attr_enums_get200_response_instance = LocalAttrEnumsGet200Response.from_json(json)
# print the JSON string representation of the object
print LocalAttrEnumsGet200Response.to_json()

# convert the object into a dict
local_attr_enums_get200_response_dict = local_attr_enums_get200_response_instance.to_dict()
# create an instance of LocalAttrEnumsGet200Response from a dict
local_attr_enums_get200_response_form_dict = local_attr_enums_get200_response.from_dict(local_attr_enums_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



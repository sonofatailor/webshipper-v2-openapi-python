# LocalAttrsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LocalAttrsGet200ResponseDataInner]**](LocalAttrsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.local_attrs_get200_response import LocalAttrsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LocalAttrsGet200Response from a JSON string
local_attrs_get200_response_instance = LocalAttrsGet200Response.from_json(json)
# print the JSON string representation of the object
print LocalAttrsGet200Response.to_json()

# convert the object into a dict
local_attrs_get200_response_dict = local_attrs_get200_response_instance.to_dict()
# create an instance of LocalAttrsGet200Response from a dict
local_attrs_get200_response_form_dict = local_attrs_get200_response.from_dict(local_attrs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



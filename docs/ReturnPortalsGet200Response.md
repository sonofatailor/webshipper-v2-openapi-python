# ReturnPortalsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReturnPortalsGet200ResponseDataInner]**](ReturnPortalsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_portals_get200_response import ReturnPortalsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsGet200Response from a JSON string
return_portals_get200_response_instance = ReturnPortalsGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsGet200Response.to_json()

# convert the object into a dict
return_portals_get200_response_dict = return_portals_get200_response_instance.to_dict()
# create an instance of ReturnPortalsGet200Response from a dict
return_portals_get200_response_form_dict = return_portals_get200_response.from_dict(return_portals_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReturnPortalsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnPortalsIdGet200ResponseData**](ReturnPortalsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnPortalsIdGet200ResponseRelationships**](ReturnPortalsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ReturnPortalsIdGet200ResponseIncludedInner]**](ReturnPortalsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_portals_id_get200_response import ReturnPortalsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsIdGet200Response from a JSON string
return_portals_id_get200_response_instance = ReturnPortalsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsIdGet200Response.to_json()

# convert the object into a dict
return_portals_id_get200_response_dict = return_portals_id_get200_response_instance.to_dict()
# create an instance of ReturnPortalsIdGet200Response from a dict
return_portals_id_get200_response_form_dict = return_portals_id_get200_response.from_dict(return_portals_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



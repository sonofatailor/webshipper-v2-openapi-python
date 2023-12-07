# StoresIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StoresIdGet200ResponseData**](StoresIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**StoresIdGet200ResponseRelationships**](StoresIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[StoresIdGet200ResponseIncludedInner]**](StoresIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_id_get200_response import StoresIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoresIdGet200Response from a JSON string
stores_id_get200_response_instance = StoresIdGet200Response.from_json(json)
# print the JSON string representation of the object
print StoresIdGet200Response.to_json()

# convert the object into a dict
stores_id_get200_response_dict = stores_id_get200_response_instance.to_dict()
# create an instance of StoresIdGet200Response from a dict
stores_id_get200_response_form_dict = stores_id_get200_response.from_dict(stores_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



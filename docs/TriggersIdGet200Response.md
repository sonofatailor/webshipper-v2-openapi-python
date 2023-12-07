# TriggersIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TriggersIdGet200ResponseData**](TriggersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ActionsIdGet200ResponseRelationships**](ActionsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ActionsIdGet200ResponseIncludedInner]**](ActionsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.triggers_id_get200_response import TriggersIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersIdGet200Response from a JSON string
triggers_id_get200_response_instance = TriggersIdGet200Response.from_json(json)
# print the JSON string representation of the object
print TriggersIdGet200Response.to_json()

# convert the object into a dict
triggers_id_get200_response_dict = triggers_id_get200_response_instance.to_dict()
# create an instance of TriggersIdGet200Response from a dict
triggers_id_get200_response_form_dict = triggers_id_get200_response.from_dict(triggers_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



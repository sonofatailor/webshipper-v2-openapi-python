# TriggersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TriggersGet200ResponseDataInner]**](TriggersGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.triggers_get200_response import TriggersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersGet200Response from a JSON string
triggers_get200_response_instance = TriggersGet200Response.from_json(json)
# print the JSON string representation of the object
print TriggersGet200Response.to_json()

# convert the object into a dict
triggers_get200_response_dict = triggers_get200_response_instance.to_dict()
# create an instance of TriggersGet200Response from a dict
triggers_get200_response_form_dict = triggers_get200_response.from_dict(triggers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



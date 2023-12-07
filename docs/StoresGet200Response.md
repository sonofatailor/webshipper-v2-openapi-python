# StoresGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StoresGet200ResponseDataInner]**](StoresGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.stores_get200_response import StoresGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoresGet200Response from a JSON string
stores_get200_response_instance = StoresGet200Response.from_json(json)
# print the JSON string representation of the object
print StoresGet200Response.to_json()

# convert the object into a dict
stores_get200_response_dict = stores_get200_response_instance.to_dict()
# create an instance of StoresGet200Response from a dict
stores_get200_response_form_dict = stores_get200_response.from_dict(stores_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReturnsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnsIdGet200ResponseData**](ReturnsIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**ReturnsIdGet200ResponseRelationships**](ReturnsIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[ReturnsIdGet200ResponseIncludedInner]**](ReturnsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.returns_id_get200_response import ReturnsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsIdGet200Response from a JSON string
returns_id_get200_response_instance = ReturnsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ReturnsIdGet200Response.to_json()

# convert the object into a dict
returns_id_get200_response_dict = returns_id_get200_response_instance.to_dict()
# create an instance of ReturnsIdGet200Response from a dict
returns_id_get200_response_form_dict = returns_id_get200_response.from_dict(returns_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



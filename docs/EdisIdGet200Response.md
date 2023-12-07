# EdisIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EdisIdGet200ResponseData**](EdisIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**EdisIdGet200ResponseRelationships**](EdisIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[EdisIdGet200ResponseIncludedInner]**](EdisIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.edis_id_get200_response import EdisIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EdisIdGet200Response from a JSON string
edis_id_get200_response_instance = EdisIdGet200Response.from_json(json)
# print the JSON string representation of the object
print EdisIdGet200Response.to_json()

# convert the object into a dict
edis_id_get200_response_dict = edis_id_get200_response_instance.to_dict()
# create an instance of EdisIdGet200Response from a dict
edis_id_get200_response_form_dict = edis_id_get200_response.from_dict(edis_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



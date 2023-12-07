# EdisGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EdisGet200ResponseDataInner]**](EdisGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.edis_get200_response import EdisGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EdisGet200Response from a JSON string
edis_get200_response_instance = EdisGet200Response.from_json(json)
# print the JSON string representation of the object
print EdisGet200Response.to_json()

# convert the object into a dict
edis_get200_response_dict = edis_get200_response_instance.to_dict()
# create an instance of EdisGet200Response from a dict
edis_get200_response_form_dict = edis_get200_response.from_dict(edis_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



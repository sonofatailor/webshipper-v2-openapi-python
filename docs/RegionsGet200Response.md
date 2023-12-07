# RegionsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RegionsGet200ResponseDataInner]**](RegionsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.regions_get200_response import RegionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsGet200Response from a JSON string
regions_get200_response_instance = RegionsGet200Response.from_json(json)
# print the JSON string representation of the object
print RegionsGet200Response.to_json()

# convert the object into a dict
regions_get200_response_dict = regions_get200_response_instance.to_dict()
# create an instance of RegionsGet200Response from a dict
regions_get200_response_form_dict = regions_get200_response.from_dict(regions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



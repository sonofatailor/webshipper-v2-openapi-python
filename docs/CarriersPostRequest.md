# CarriersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CarriersPostRequestData**](CarriersPostRequestData.md) |  | [optional] 
**relationships** | [**CarriersIdGet200ResponseRelationships**](CarriersIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carriers_post_request import CarriersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersPostRequest from a JSON string
carriers_post_request_instance = CarriersPostRequest.from_json(json)
# print the JSON string representation of the object
print CarriersPostRequest.to_json()

# convert the object into a dict
carriers_post_request_dict = carriers_post_request_instance.to_dict()
# create an instance of CarriersPostRequest from a dict
carriers_post_request_form_dict = carriers_post_request.from_dict(carriers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



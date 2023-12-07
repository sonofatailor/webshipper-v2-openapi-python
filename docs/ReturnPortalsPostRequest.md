# ReturnPortalsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReturnPortalsPostRequestData**](ReturnPortalsPostRequestData.md) |  | [optional] 
**relationships** | [**ReturnPortalsIdGet200ResponseRelationships**](ReturnPortalsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.return_portals_post_request import ReturnPortalsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsPostRequest from a JSON string
return_portals_post_request_instance = ReturnPortalsPostRequest.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsPostRequest.to_json()

# convert the object into a dict
return_portals_post_request_dict = return_portals_post_request_instance.to_dict()
# create an instance of ReturnPortalsPostRequest from a dict
return_portals_post_request_form_dict = return_portals_post_request.from_dict(return_portals_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



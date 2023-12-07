# ReturnPortalsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**ReturnPortals**](ReturnPortals.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_portals_post_request_data import ReturnPortalsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsPostRequestData from a JSON string
return_portals_post_request_data_instance = ReturnPortalsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsPostRequestData.to_json()

# convert the object into a dict
return_portals_post_request_data_dict = return_portals_post_request_data_instance.to_dict()
# create an instance of ReturnPortalsPostRequestData from a dict
return_portals_post_request_data_form_dict = return_portals_post_request_data.from_dict(return_portals_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



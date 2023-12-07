# RegionsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RegionsPostRequestData**](RegionsPostRequestData.md) |  | [optional] 
**relationships** | [**RegionsIdGet200ResponseRelationships**](RegionsIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from webshipperv2.models.regions_post_request import RegionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsPostRequest from a JSON string
regions_post_request_instance = RegionsPostRequest.from_json(json)
# print the JSON string representation of the object
print RegionsPostRequest.to_json()

# convert the object into a dict
regions_post_request_dict = regions_post_request_instance.to_dict()
# create an instance of RegionsPostRequest from a dict
regions_post_request_form_dict = regions_post_request.from_dict(regions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



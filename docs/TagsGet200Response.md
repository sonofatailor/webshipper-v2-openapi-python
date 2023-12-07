# TagsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TagsGet200ResponseDataInner]**](TagsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.tags_get200_response import TagsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TagsGet200Response from a JSON string
tags_get200_response_instance = TagsGet200Response.from_json(json)
# print the JSON string representation of the object
print TagsGet200Response.to_json()

# convert the object into a dict
tags_get200_response_dict = tags_get200_response_instance.to_dict()
# create an instance of TagsGet200Response from a dict
tags_get200_response_form_dict = tags_get200_response.from_dict(tags_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



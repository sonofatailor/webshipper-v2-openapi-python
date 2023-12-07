# RegionsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Regions**](Regions.md) |  | [optional] 

## Example

```python
from webshipperv2.models.regions_post_request_data import RegionsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsPostRequestData from a JSON string
regions_post_request_data_instance = RegionsPostRequestData.from_json(json)
# print the JSON string representation of the object
print RegionsPostRequestData.to_json()

# convert the object into a dict
regions_post_request_data_dict = regions_post_request_data_instance.to_dict()
# create an instance of RegionsPostRequestData from a dict
regions_post_request_data_form_dict = regions_post_request_data.from_dict(regions_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



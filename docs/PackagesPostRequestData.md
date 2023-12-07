# PackagesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Packages**](Packages.md) |  | [optional] 

## Example

```python
from webshipperv2.models.packages_post_request_data import PackagesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesPostRequestData from a JSON string
packages_post_request_data_instance = PackagesPostRequestData.from_json(json)
# print the JSON string representation of the object
print PackagesPostRequestData.to_json()

# convert the object into a dict
packages_post_request_data_dict = packages_post_request_data_instance.to_dict()
# create an instance of PackagesPostRequestData from a dict
packages_post_request_data_form_dict = packages_post_request_data.from_dict(packages_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



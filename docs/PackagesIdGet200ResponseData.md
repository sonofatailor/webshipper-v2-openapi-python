# PackagesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Packages**](Packages.md) |  | [optional] 

## Example

```python
from webshipperv2.models.packages_id_get200_response_data import PackagesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesIdGet200ResponseData from a JSON string
packages_id_get200_response_data_instance = PackagesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print PackagesIdGet200ResponseData.to_json()

# convert the object into a dict
packages_id_get200_response_data_dict = packages_id_get200_response_data_instance.to_dict()
# create an instance of PackagesIdGet200ResponseData from a dict
packages_id_get200_response_data_form_dict = packages_id_get200_response_data.from_dict(packages_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



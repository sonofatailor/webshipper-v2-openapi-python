# FavouritePages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path of the favourite page | [optional] 
**name** | **str** | Name of the favourite page | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.favourite_pages import FavouritePages

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePages from a JSON string
favourite_pages_instance = FavouritePages.from_json(json)
# print the JSON string representation of the object
print FavouritePages.to_json()

# convert the object into a dict
favourite_pages_dict = favourite_pages_instance.to_dict()
# create an instance of FavouritePages from a dict
favourite_pages_form_dict = favourite_pages.from_dict(favourite_pages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



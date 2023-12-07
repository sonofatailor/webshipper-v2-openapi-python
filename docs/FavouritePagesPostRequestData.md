# FavouritePagesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**FavouritePages**](FavouritePages.md) |  | [optional] 

## Example

```python
from webshipperv2.models.favourite_pages_post_request_data import FavouritePagesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePagesPostRequestData from a JSON string
favourite_pages_post_request_data_instance = FavouritePagesPostRequestData.from_json(json)
# print the JSON string representation of the object
print FavouritePagesPostRequestData.to_json()

# convert the object into a dict
favourite_pages_post_request_data_dict = favourite_pages_post_request_data_instance.to_dict()
# create an instance of FavouritePagesPostRequestData from a dict
favourite_pages_post_request_data_form_dict = favourite_pages_post_request_data.from_dict(favourite_pages_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



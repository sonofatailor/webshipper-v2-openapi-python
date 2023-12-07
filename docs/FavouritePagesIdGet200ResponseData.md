# FavouritePagesIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**FavouritePages**](FavouritePages.md) |  | [optional] 

## Example

```python
from webshipperv2.models.favourite_pages_id_get200_response_data import FavouritePagesIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePagesIdGet200ResponseData from a JSON string
favourite_pages_id_get200_response_data_instance = FavouritePagesIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print FavouritePagesIdGet200ResponseData.to_json()

# convert the object into a dict
favourite_pages_id_get200_response_data_dict = favourite_pages_id_get200_response_data_instance.to_dict()
# create an instance of FavouritePagesIdGet200ResponseData from a dict
favourite_pages_id_get200_response_data_form_dict = favourite_pages_id_get200_response_data.from_dict(favourite_pages_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



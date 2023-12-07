# FavouritePagesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FavouritePagesIdGet200ResponseData**](FavouritePagesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**FavouritePagesIdGet200ResponseRelationships**](FavouritePagesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.favourite_pages_id_patch_request import FavouritePagesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePagesIdPatchRequest from a JSON string
favourite_pages_id_patch_request_instance = FavouritePagesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print FavouritePagesIdPatchRequest.to_json()

# convert the object into a dict
favourite_pages_id_patch_request_dict = favourite_pages_id_patch_request_instance.to_dict()
# create an instance of FavouritePagesIdPatchRequest from a dict
favourite_pages_id_patch_request_form_dict = favourite_pages_id_patch_request.from_dict(favourite_pages_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



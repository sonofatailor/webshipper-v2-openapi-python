# FavouritePagesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FavouritePagesIdGet200ResponseData**](FavouritePagesIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**FavouritePagesIdGet200ResponseRelationships**](FavouritePagesIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[FavouritePagesIdGet200ResponseIncludedInner]**](FavouritePagesIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.favourite_pages_id_get200_response import FavouritePagesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePagesIdGet200Response from a JSON string
favourite_pages_id_get200_response_instance = FavouritePagesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print FavouritePagesIdGet200Response.to_json()

# convert the object into a dict
favourite_pages_id_get200_response_dict = favourite_pages_id_get200_response_instance.to_dict()
# create an instance of FavouritePagesIdGet200Response from a dict
favourite_pages_id_get200_response_form_dict = favourite_pages_id_get200_response.from_dict(favourite_pages_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FavouritePagesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FavouritePagesPostRequestData**](FavouritePagesPostRequestData.md) |  | [optional] 
**relationships** | [**FavouritePagesIdGet200ResponseRelationships**](FavouritePagesIdGet200ResponseRelationships.md) |  | [optional] 

## Example

```python
from openapi_client.models.favourite_pages_post_request import FavouritePagesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FavouritePagesPostRequest from a JSON string
favourite_pages_post_request_instance = FavouritePagesPostRequest.from_json(json)
# print the JSON string representation of the object
print FavouritePagesPostRequest.to_json()

# convert the object into a dict
favourite_pages_post_request_dict = favourite_pages_post_request_instance.to_dict()
# create an instance of FavouritePagesPostRequest from a dict
favourite_pages_post_request_form_dict = favourite_pages_post_request.from_dict(favourite_pages_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



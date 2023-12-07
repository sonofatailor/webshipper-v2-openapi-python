# OauthApplicationsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OauthApplicationsIdGet200ResponseData**](OauthApplicationsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.oauth_applications_id_get200_response import OauthApplicationsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OauthApplicationsIdGet200Response from a JSON string
oauth_applications_id_get200_response_instance = OauthApplicationsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print OauthApplicationsIdGet200Response.to_json()

# convert the object into a dict
oauth_applications_id_get200_response_dict = oauth_applications_id_get200_response_instance.to_dict()
# create an instance of OauthApplicationsIdGet200Response from a dict
oauth_applications_id_get200_response_form_dict = oauth_applications_id_get200_response.from_dict(oauth_applications_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



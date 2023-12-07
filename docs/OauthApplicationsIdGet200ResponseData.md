# OauthApplicationsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OauthApplications**](OauthApplications.md) |  | [optional] 

## Example

```python
from webshipperv2.models.oauth_applications_id_get200_response_data import OauthApplicationsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OauthApplicationsIdGet200ResponseData from a JSON string
oauth_applications_id_get200_response_data_instance = OauthApplicationsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OauthApplicationsIdGet200ResponseData.to_json()

# convert the object into a dict
oauth_applications_id_get200_response_data_dict = oauth_applications_id_get200_response_data_instance.to_dict()
# create an instance of OauthApplicationsIdGet200ResponseData from a dict
oauth_applications_id_get200_response_data_form_dict = oauth_applications_id_get200_response_data.from_dict(oauth_applications_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



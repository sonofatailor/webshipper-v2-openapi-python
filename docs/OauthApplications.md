# OauthApplications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Application name | [optional] 
**uid** | **str** | Unique id | [optional] 
**scopes** | **str** | The scopes which the OAuth application will be granted. | [optional] 
**redirect_uri** | **str** | OAuth redirect URI | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 

## Example

```python
from webshipperv2.models.oauth_applications import OauthApplications

# TODO update the JSON string below
json = "{}"
# create an instance of OauthApplications from a JSON string
oauth_applications_instance = OauthApplications.from_json(json)
# print the JSON string representation of the object
print OauthApplications.to_json()

# convert the object into a dict
oauth_applications_dict = oauth_applications_instance.to_dict()
# create an instance of OauthApplications from a dict
oauth_applications_form_dict = oauth_applications.from_dict(oauth_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



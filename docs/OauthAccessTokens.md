# OauthAccessTokens


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **str** | The scopes to which access is granted by the access token. | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**resource_owner_id** | **int** | Id of the owner | [optional] 
**expires_in** | **int** | Epoch timestamp of the expiration date for the token | [optional] 
**expired** | **str** |  | [optional] 
**token** | **str** | The access token | [optional] 
**revoked_at** | **str** | Datetime of the time the token was revoked - if revoked | [optional] 
**resource_owner** | **str** |  | [optional] 
**application_id** | **int** |  | [optional] 
**application** | **str** | The application to which this tokens grants access | [optional] 

## Example

```python
from webshipperv2.models.oauth_access_tokens import OauthAccessTokens

# TODO update the JSON string below
json = "{}"
# create an instance of OauthAccessTokens from a JSON string
oauth_access_tokens_instance = OauthAccessTokens.from_json(json)
# print the JSON string representation of the object
print OauthAccessTokens.to_json()

# convert the object into a dict
oauth_access_tokens_dict = oauth_access_tokens_instance.to_dict()
# create an instance of OauthAccessTokens from a dict
oauth_access_tokens_form_dict = oauth_access_tokens.from_dict(oauth_access_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



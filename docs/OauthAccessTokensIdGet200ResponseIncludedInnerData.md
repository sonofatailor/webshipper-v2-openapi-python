# OauthAccessTokensIdGet200ResponseIncludedInnerData


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
from webshipperv2.models.oauth_access_tokens_id_get200_response_included_inner_data import OauthAccessTokensIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of OauthAccessTokensIdGet200ResponseIncludedInnerData from a JSON string
oauth_access_tokens_id_get200_response_included_inner_data_instance = OauthAccessTokensIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print OauthAccessTokensIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
oauth_access_tokens_id_get200_response_included_inner_data_dict = oauth_access_tokens_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of OauthAccessTokensIdGet200ResponseIncludedInnerData from a dict
oauth_access_tokens_id_get200_response_included_inner_data_form_dict = oauth_access_tokens_id_get200_response_included_inner_data.from_dict(oauth_access_tokens_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



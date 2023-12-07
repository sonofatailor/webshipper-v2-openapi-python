# OauthAccessTokensIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OauthAccessTokensIdGet200ResponseData**](OauthAccessTokensIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**OauthAccessTokensIdGet200ResponseRelationships**](OauthAccessTokensIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[OauthAccessTokensIdGet200ResponseIncludedInner]**](OauthAccessTokensIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.oauth_access_tokens_id_get200_response import OauthAccessTokensIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OauthAccessTokensIdGet200Response from a JSON string
oauth_access_tokens_id_get200_response_instance = OauthAccessTokensIdGet200Response.from_json(json)
# print the JSON string representation of the object
print OauthAccessTokensIdGet200Response.to_json()

# convert the object into a dict
oauth_access_tokens_id_get200_response_dict = oauth_access_tokens_id_get200_response_instance.to_dict()
# create an instance of OauthAccessTokensIdGet200Response from a dict
oauth_access_tokens_id_get200_response_form_dict = oauth_access_tokens_id_get200_response.from_dict(oauth_access_tokens_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



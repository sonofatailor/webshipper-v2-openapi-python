# OauthAccessTokensIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**OauthAccessTokens**](OauthAccessTokens.md) |  | [optional] 

## Example

```python
from openapi_client.models.oauth_access_tokens_id_get200_response_data import OauthAccessTokensIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of OauthAccessTokensIdGet200ResponseData from a JSON string
oauth_access_tokens_id_get200_response_data_instance = OauthAccessTokensIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print OauthAccessTokensIdGet200ResponseData.to_json()

# convert the object into a dict
oauth_access_tokens_id_get200_response_data_dict = oauth_access_tokens_id_get200_response_data_instance.to_dict()
# create an instance of OauthAccessTokensIdGet200ResponseData from a dict
oauth_access_tokens_id_get200_response_data_form_dict = oauth_access_tokens_id_get200_response_data.from_dict(oauth_access_tokens_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



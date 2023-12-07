# ActionsPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Actions**](Actions.md) |  | [optional] 

## Example

```python
from webshipperv2.models.actions_post_request_data import ActionsPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsPostRequestData from a JSON string
actions_post_request_data_instance = ActionsPostRequestData.from_json(json)
# print the JSON string representation of the object
print ActionsPostRequestData.to_json()

# convert the object into a dict
actions_post_request_data_dict = actions_post_request_data_instance.to_dict()
# create an instance of ActionsPostRequestData from a dict
actions_post_request_data_form_dict = actions_post_request_data.from_dict(actions_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



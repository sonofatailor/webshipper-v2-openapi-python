# TriggersPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Triggers**](Triggers.md) |  | [optional] 

## Example

```python
from webshipperv2.models.triggers_post_request_data import TriggersPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TriggersPostRequestData from a JSON string
triggers_post_request_data_instance = TriggersPostRequestData.from_json(json)
# print the JSON string representation of the object
print TriggersPostRequestData.to_json()

# convert the object into a dict
triggers_post_request_data_dict = triggers_post_request_data_instance.to_dict()
# create an instance of TriggersPostRequestData from a dict
triggers_post_request_data_form_dict = triggers_post_request_data.from_dict(triggers_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



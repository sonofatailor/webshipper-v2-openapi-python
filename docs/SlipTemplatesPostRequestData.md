# SlipTemplatesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**SlipTemplates**](SlipTemplates.md) |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_post_request_data import SlipTemplatesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesPostRequestData from a JSON string
slip_templates_post_request_data_instance = SlipTemplatesPostRequestData.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesPostRequestData.to_json()

# convert the object into a dict
slip_templates_post_request_data_dict = slip_templates_post_request_data_instance.to_dict()
# create an instance of SlipTemplatesPostRequestData from a dict
slip_templates_post_request_data_form_dict = slip_templates_post_request_data.from_dict(slip_templates_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



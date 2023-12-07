# SlipTemplatesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SlipTemplatesPostRequestData**](SlipTemplatesPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_post_request import SlipTemplatesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesPostRequest from a JSON string
slip_templates_post_request_instance = SlipTemplatesPostRequest.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesPostRequest.to_json()

# convert the object into a dict
slip_templates_post_request_dict = slip_templates_post_request_instance.to_dict()
# create an instance of SlipTemplatesPostRequest from a dict
slip_templates_post_request_form_dict = slip_templates_post_request.from_dict(slip_templates_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



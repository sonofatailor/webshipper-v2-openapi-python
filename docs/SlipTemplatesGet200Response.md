# SlipTemplatesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SlipTemplatesGet200ResponseDataInner]**](SlipTemplatesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_get200_response import SlipTemplatesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesGet200Response from a JSON string
slip_templates_get200_response_instance = SlipTemplatesGet200Response.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesGet200Response.to_json()

# convert the object into a dict
slip_templates_get200_response_dict = slip_templates_get200_response_instance.to_dict()
# create an instance of SlipTemplatesGet200Response from a dict
slip_templates_get200_response_form_dict = slip_templates_get200_response.from_dict(slip_templates_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



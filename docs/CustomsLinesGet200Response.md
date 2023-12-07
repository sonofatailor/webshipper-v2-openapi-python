# CustomsLinesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CustomsLinesGet200ResponseDataInner]**](CustomsLinesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.customs_lines_get200_response import CustomsLinesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsLinesGet200Response from a JSON string
customs_lines_get200_response_instance = CustomsLinesGet200Response.from_json(json)
# print the JSON string representation of the object
print CustomsLinesGet200Response.to_json()

# convert the object into a dict
customs_lines_get200_response_dict = customs_lines_get200_response_instance.to_dict()
# create an instance of CustomsLinesGet200Response from a dict
customs_lines_get200_response_form_dict = customs_lines_get200_response.from_dict(customs_lines_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



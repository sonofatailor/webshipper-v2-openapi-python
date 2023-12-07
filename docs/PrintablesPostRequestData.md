# PrintablesPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.printables_post_request_data import PrintablesPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesPostRequestData from a JSON string
printables_post_request_data_instance = PrintablesPostRequestData.from_json(json)
# print the JSON string representation of the object
print PrintablesPostRequestData.to_json()

# convert the object into a dict
printables_post_request_data_dict = printables_post_request_data_instance.to_dict()
# create an instance of PrintablesPostRequestData from a dict
printables_post_request_data_form_dict = printables_post_request_data.from_dict(printables_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



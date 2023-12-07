# Printers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the printer. | [optional] 
**active** | **bool** | Determines if the printer is configured on the printer station | [optional] 
**last_connected** | **str** | Last connection time | [optional] 
**paper_width** | **float** | Paper width | [optional] 
**paper_height** | **float** | Paper height | [optional] 
**rotate_print_180** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.printers import Printers

# TODO update the JSON string below
json = "{}"
# create an instance of Printers from a JSON string
printers_instance = Printers.from_json(json)
# print the JSON string representation of the object
print Printers.to_json()

# convert the object into a dict
printers_dict = printers_instance.to_dict()
# create an instance of Printers from a dict
printers_form_dict = printers.from_dict(printers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



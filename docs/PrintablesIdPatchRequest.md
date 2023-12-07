# PrintablesIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrintablesIdGet200ResponseData**](PrintablesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.printables_id_patch_request import PrintablesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesIdPatchRequest from a JSON string
printables_id_patch_request_instance = PrintablesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print PrintablesIdPatchRequest.to_json()

# convert the object into a dict
printables_id_patch_request_dict = printables_id_patch_request_instance.to_dict()
# create an instance of PrintablesIdPatchRequest from a dict
printables_id_patch_request_form_dict = printables_id_patch_request.from_dict(printables_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



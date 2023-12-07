# PrintersIdGet200ResponseIncludedInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**data** | [**PrintersIdGet200ResponseIncludedInnerData**](PrintersIdGet200ResponseIncludedInnerData.md) |  | [optional] 

## Example

```python
from openapi_client.models.printers_id_get200_response_included_inner import PrintersIdGet200ResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersIdGet200ResponseIncludedInner from a JSON string
printers_id_get200_response_included_inner_instance = PrintersIdGet200ResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print PrintersIdGet200ResponseIncludedInner.to_json()

# convert the object into a dict
printers_id_get200_response_included_inner_dict = printers_id_get200_response_included_inner_instance.to_dict()
# create an instance of PrintersIdGet200ResponseIncludedInner from a dict
printers_id_get200_response_included_inner_form_dict = printers_id_get200_response_included_inner.from_dict(printers_id_get200_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



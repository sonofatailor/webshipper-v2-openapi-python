# PrintersIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique ID of the printer client | [optional] 
**approved** | **bool** | DEPRECATED | [optional] 
**alias** | **str** | Defaults to the host name of the machine running the client  | [optional] 
**is_online** | **bool** | Shows if the printer client is online | [optional] 
**last_connected** | **str** | Shows when the printer client was last connected | [optional] 
**prevent_multiple_shipments** | **bool** |  | [optional] 

## Example

```python
from webshipperv2.models.printers_id_get200_response_included_inner_data import PrintersIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersIdGet200ResponseIncludedInnerData from a JSON string
printers_id_get200_response_included_inner_data_instance = PrintersIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print PrintersIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
printers_id_get200_response_included_inner_data_dict = printers_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of PrintersIdGet200ResponseIncludedInnerData from a dict
printers_id_get200_response_included_inner_data_form_dict = printers_id_get200_response_included_inner_data.from_dict(printers_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



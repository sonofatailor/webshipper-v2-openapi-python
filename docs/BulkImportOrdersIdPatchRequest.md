# BulkImportOrdersIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkImportOrdersIdGet200ResponseData**](BulkImportOrdersIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders_id_patch_request import BulkImportOrdersIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersIdPatchRequest from a JSON string
bulk_import_orders_id_patch_request_instance = BulkImportOrdersIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersIdPatchRequest.to_json()

# convert the object into a dict
bulk_import_orders_id_patch_request_dict = bulk_import_orders_id_patch_request_instance.to_dict()
# create an instance of BulkImportOrdersIdPatchRequest from a dict
bulk_import_orders_id_patch_request_form_dict = bulk_import_orders_id_patch_request.from_dict(bulk_import_orders_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



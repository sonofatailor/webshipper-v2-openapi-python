# BulkImportOrdersIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkImportOrdersIdGet200ResponseData**](BulkImportOrdersIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders_id_get200_response import BulkImportOrdersIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersIdGet200Response from a JSON string
bulk_import_orders_id_get200_response_instance = BulkImportOrdersIdGet200Response.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersIdGet200Response.to_json()

# convert the object into a dict
bulk_import_orders_id_get200_response_dict = bulk_import_orders_id_get200_response_instance.to_dict()
# create an instance of BulkImportOrdersIdGet200Response from a dict
bulk_import_orders_id_get200_response_form_dict = bulk_import_orders_id_get200_response.from_dict(bulk_import_orders_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



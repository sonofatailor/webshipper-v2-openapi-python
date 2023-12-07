# BulkImportOrdersIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**BulkImportOrders**](BulkImportOrders.md) |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders_id_get200_response_data import BulkImportOrdersIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersIdGet200ResponseData from a JSON string
bulk_import_orders_id_get200_response_data_instance = BulkImportOrdersIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersIdGet200ResponseData.to_json()

# convert the object into a dict
bulk_import_orders_id_get200_response_data_dict = bulk_import_orders_id_get200_response_data_instance.to_dict()
# create an instance of BulkImportOrdersIdGet200ResponseData from a dict
bulk_import_orders_id_get200_response_data_form_dict = bulk_import_orders_id_get200_response_data.from_dict(bulk_import_orders_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



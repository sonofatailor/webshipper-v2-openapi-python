# BulkImportOrders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **str** | Order ids to import from the order channel | [optional] 
**order_channel_id** | **str** | Id of the order channel to import orders from | [optional] 
**var_async** | **str** | Run the import asyncronously, default is false unless importing more than one order or from more than one order channel | [optional] 
**reimport** | **str** | Reimport orders from the order channel. WARNING: This will overwrite any changes to the order made in Webshipper and import the order as it is in the order channel | [optional] 
**time_start** | **str** | Time from when orders should be imported, all orders after this time is imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel | [optional] 
**time_end** | **str** | Time to when orders should be imported, all orders before this time is imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel | [optional] 
**statuses** | **str** | Statuses of orders to import, all orders with the given statuses are imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel | [optional] 
**bulk_imports** | **str** | List of bulk imports with the same attributes as above. This can be used to import multiple orders from multiple order channels at once. Options specified in the root object is used globally, but is overridable by specififying the option for specific bulk_import in the list. | [optional] 
**source** | **str** | Source of the orders to import. This will default to API | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders import BulkImportOrders

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrders from a JSON string
bulk_import_orders_instance = BulkImportOrders.from_json(json)
# print the JSON string representation of the object
print BulkImportOrders.to_json()

# convert the object into a dict
bulk_import_orders_dict = bulk_import_orders_instance.to_dict()
# create an instance of BulkImportOrders from a dict
bulk_import_orders_form_dict = bulk_import_orders.from_dict(bulk_import_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



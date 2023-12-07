# BulkImportOrdersPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**BulkImportOrders**](BulkImportOrders.md) |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders_post_request_data import BulkImportOrdersPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersPostRequestData from a JSON string
bulk_import_orders_post_request_data_instance = BulkImportOrdersPostRequestData.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersPostRequestData.to_json()

# convert the object into a dict
bulk_import_orders_post_request_data_dict = bulk_import_orders_post_request_data_instance.to_dict()
# create an instance of BulkImportOrdersPostRequestData from a dict
bulk_import_orders_post_request_data_form_dict = bulk_import_orders_post_request_data.from_dict(bulk_import_orders_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



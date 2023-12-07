# BulkImportOrdersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkImportOrdersPostRequestData**](BulkImportOrdersPostRequestData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 

## Example

```python
from webshipperv2.models.bulk_import_orders_post_request import BulkImportOrdersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersPostRequest from a JSON string
bulk_import_orders_post_request_instance = BulkImportOrdersPostRequest.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersPostRequest.to_json()

# convert the object into a dict
bulk_import_orders_post_request_dict = bulk_import_orders_post_request_instance.to_dict()
# create an instance of BulkImportOrdersPostRequest from a dict
bulk_import_orders_post_request_form_dict = bulk_import_orders_post_request.from_dict(bulk_import_orders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



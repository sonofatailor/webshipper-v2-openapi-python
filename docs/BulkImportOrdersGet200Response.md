# BulkImportOrdersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BulkImportOrdersGet200ResponseDataInner]**](BulkImportOrdersGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_import_orders_get200_response import BulkImportOrdersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkImportOrdersGet200Response from a JSON string
bulk_import_orders_get200_response_instance = BulkImportOrdersGet200Response.from_json(json)
# print the JSON string representation of the object
print BulkImportOrdersGet200Response.to_json()

# convert the object into a dict
bulk_import_orders_get200_response_dict = bulk_import_orders_get200_response_instance.to_dict()
# create an instance of BulkImportOrdersGet200Response from a dict
bulk_import_orders_get200_response_form_dict = bulk_import_orders_get200_response.from_dict(bulk_import_orders_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



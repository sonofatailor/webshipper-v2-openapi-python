# ReturnsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**AdditionalAttributesIdGet200ResponseRelationshipsOrder**](AdditionalAttributesIdGet200ResponseRelationshipsOrder.md) |  | [optional] 
**portal** | [**ReturnRefundMethodsIdGet200ResponseRelationshipsPortal**](ReturnRefundMethodsIdGet200ResponseRelationshipsPortal.md) |  | [optional] 
**shipping_method** | [**ReturnsIdGet200ResponseRelationshipsShippingMethod**](ReturnsIdGet200ResponseRelationshipsShippingMethod.md) |  | [optional] 
**refund_method** | [**ReturnsIdGet200ResponseRelationshipsRefundMethod**](ReturnsIdGet200ResponseRelationshipsRefundMethod.md) |  | [optional] 
**shipment** | [**EdisIdGet200ResponseRelationshipsShipment**](EdisIdGet200ResponseRelationshipsShipment.md) |  | [optional] 

## Example

```python
from openapi_client.models.returns_id_get200_response_relationships import ReturnsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsIdGet200ResponseRelationships from a JSON string
returns_id_get200_response_relationships_instance = ReturnsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ReturnsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
returns_id_get200_response_relationships_dict = returns_id_get200_response_relationships_instance.to_dict()
# create an instance of ReturnsIdGet200ResponseRelationships from a dict
returns_id_get200_response_relationships_form_dict = returns_id_get200_response_relationships.from_dict(returns_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



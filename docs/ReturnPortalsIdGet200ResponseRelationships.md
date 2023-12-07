# ReturnPortalsIdGet200ResponseRelationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_channel** | [**CsvMappingsIdGet200ResponseRelationshipsOrderChannel**](CsvMappingsIdGet200ResponseRelationshipsOrderChannel.md) |  | [optional] 
**slip_template** | [**OrderChannelsIdGet200ResponseRelationshipsSlipTemplate**](OrderChannelsIdGet200ResponseRelationshipsSlipTemplate.md) |  | [optional] 
**mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 
**confirmation_mail_template** | [**ReturnPortalsIdGet200ResponseRelationshipsMailTemplate**](ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.md) |  | [optional] 
**return_address** | [**CarriersIdGet200ResponseRelationshipsSenderAddress**](CarriersIdGet200ResponseRelationshipsSenderAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.return_portals_id_get200_response_relationships import ReturnPortalsIdGet200ResponseRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnPortalsIdGet200ResponseRelationships from a JSON string
return_portals_id_get200_response_relationships_instance = ReturnPortalsIdGet200ResponseRelationships.from_json(json)
# print the JSON string representation of the object
print ReturnPortalsIdGet200ResponseRelationships.to_json()

# convert the object into a dict
return_portals_id_get200_response_relationships_dict = return_portals_id_get200_response_relationships_instance.to_dict()
# create an instance of ReturnPortalsIdGet200ResponseRelationships from a dict
return_portals_id_get200_response_relationships_form_dict = return_portals_id_get200_response_relationships.from_dict(return_portals_id_get200_response_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



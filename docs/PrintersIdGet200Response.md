# PrintersIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrintersIdGet200ResponseData**](PrintersIdGet200ResponseData.md) |  | [optional] 
**relationships** | [**PrintersIdGet200ResponseRelationships**](PrintersIdGet200ResponseRelationships.md) |  | [optional] 
**included** | [**List[PrintersIdGet200ResponseIncludedInner]**](PrintersIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printers_id_get200_response import PrintersIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersIdGet200Response from a JSON string
printers_id_get200_response_instance = PrintersIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PrintersIdGet200Response.to_json()

# convert the object into a dict
printers_id_get200_response_dict = printers_id_get200_response_instance.to_dict()
# create an instance of PrintersIdGet200Response from a dict
printers_id_get200_response_form_dict = printers_id_get200_response.from_dict(printers_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



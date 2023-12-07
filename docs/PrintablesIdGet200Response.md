# PrintablesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PrintablesIdGet200ResponseData**](PrintablesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.printables_id_get200_response import PrintablesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesIdGet200Response from a JSON string
printables_id_get200_response_instance = PrintablesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print PrintablesIdGet200Response.to_json()

# convert the object into a dict
printables_id_get200_response_dict = printables_id_get200_response_instance.to_dict()
# create an instance of PrintablesIdGet200Response from a dict
printables_id_get200_response_form_dict = printables_id_get200_response.from_dict(printables_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



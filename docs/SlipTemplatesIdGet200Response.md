# SlipTemplatesIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SlipTemplatesIdGet200ResponseData**](SlipTemplatesIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.slip_templates_id_get200_response import SlipTemplatesIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SlipTemplatesIdGet200Response from a JSON string
slip_templates_id_get200_response_instance = SlipTemplatesIdGet200Response.from_json(json)
# print the JSON string representation of the object
print SlipTemplatesIdGet200Response.to_json()

# convert the object into a dict
slip_templates_id_get200_response_dict = slip_templates_id_get200_response_instance.to_dict()
# create an instance of SlipTemplatesIdGet200Response from a dict
slip_templates_id_get200_response_form_dict = slip_templates_id_get200_response.from_dict(slip_templates_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



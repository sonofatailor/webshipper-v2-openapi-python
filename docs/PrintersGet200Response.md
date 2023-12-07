# PrintersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrintersGet200ResponseDataInner]**](PrintersGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.printers_get200_response import PrintersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrintersGet200Response from a JSON string
printers_get200_response_instance = PrintersGet200Response.from_json(json)
# print the JSON string representation of the object
print PrintersGet200Response.to_json()

# convert the object into a dict
printers_get200_response_dict = printers_get200_response_instance.to_dict()
# create an instance of PrintersGet200Response from a dict
printers_get200_response_form_dict = printers_get200_response.from_dict(printers_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



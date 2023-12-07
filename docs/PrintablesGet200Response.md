# PrintablesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrintablesGet200ResponseDataInner]**](PrintablesGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.printables_get200_response import PrintablesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PrintablesGet200Response from a JSON string
printables_get200_response_instance = PrintablesGet200Response.from_json(json)
# print the JSON string representation of the object
print PrintablesGet200Response.to_json()

# convert the object into a dict
printables_get200_response_dict = printables_get200_response_instance.to_dict()
# create an instance of PrintablesGet200Response from a dict
printables_get200_response_form_dict = printables_get200_response.from_dict(printables_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



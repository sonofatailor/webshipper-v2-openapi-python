# ReportsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportsGet200ResponseDataInner]**](ReportsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.reports_get200_response import ReportsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsGet200Response from a JSON string
reports_get200_response_instance = ReportsGet200Response.from_json(json)
# print the JSON string representation of the object
print ReportsGet200Response.to_json()

# convert the object into a dict
reports_get200_response_dict = reports_get200_response_instance.to_dict()
# create an instance of ReportsGet200Response from a dict
reports_get200_response_form_dict = reports_get200_response.from_dict(reports_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



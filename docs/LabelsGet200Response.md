# LabelsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LabelsGet200ResponseDataInner]**](LabelsGet200ResponseDataInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.labels_get200_response import LabelsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsGet200Response from a JSON string
labels_get200_response_instance = LabelsGet200Response.from_json(json)
# print the JSON string representation of the object
print LabelsGet200Response.to_json()

# convert the object into a dict
labels_get200_response_dict = labels_get200_response_instance.to_dict()
# create an instance of LabelsGet200Response from a dict
labels_get200_response_form_dict = labels_get200_response.from_dict(labels_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



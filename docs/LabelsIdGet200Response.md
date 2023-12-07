# LabelsIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LabelsIdGet200ResponseData**](LabelsIdGet200ResponseData.md) |  | [optional] 
**relationships** | **object** |  | [optional] 
**included** | [**List[BrandsIdGet200ResponseIncludedInner]**](BrandsIdGet200ResponseIncludedInner.md) |  | [optional] 

## Example

```python
from webshipperv2.models.labels_id_get200_response import LabelsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsIdGet200Response from a JSON string
labels_id_get200_response_instance = LabelsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print LabelsIdGet200Response.to_json()

# convert the object into a dict
labels_id_get200_response_dict = labels_id_get200_response_instance.to_dict()
# create an instance of LabelsIdGet200Response from a dict
labels_id_get200_response_form_dict = labels_id_get200_response.from_dict(labels_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



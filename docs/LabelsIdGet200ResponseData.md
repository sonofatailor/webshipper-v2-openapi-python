# LabelsIdGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Labels**](Labels.md) |  | [optional] 

## Example

```python
from webshipperv2.models.labels_id_get200_response_data import LabelsIdGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsIdGet200ResponseData from a JSON string
labels_id_get200_response_data_instance = LabelsIdGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print LabelsIdGet200ResponseData.to_json()

# convert the object into a dict
labels_id_get200_response_data_dict = labels_id_get200_response_data_instance.to_dict()
# create an instance of LabelsIdGet200ResponseData from a dict
labels_id_get200_response_data_form_dict = labels_id_get200_response_data.from_dict(labels_id_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



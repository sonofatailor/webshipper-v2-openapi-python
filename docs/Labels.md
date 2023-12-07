# Labels


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**label_size** | **int** | Size of the label. Enum with possible values: &#39;100X150&#39;, &#39;100X192&#39;. | [optional] 
**label_format** | **int** | Label format. Enum with possible values: &#39;PDF&#39;, &#39;ZPL&#39;. | [optional] 
**var_base64** | **str** | Base64 encoding of the pdf document. (Can be an array, see the description above) | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from webshipperv2.models.labels import Labels

# TODO update the JSON string below
json = "{}"
# create an instance of Labels from a JSON string
labels_instance = Labels.from_json(json)
# print the JSON string representation of the object
print Labels.to_json()

# convert the object into a dict
labels_dict = labels_instance.to_dict()
# create an instance of Labels from a dict
labels_form_dict = labels.from_dict(labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Edis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Must be one of &#39;pending&#39;, &#39;on_hold&#39; or &#39;sent&#39; | [optional] 
**data** | **str** | The file contents (as text) | [optional] 
**encoding** | **int** | Must be either &#39;utf8&#39; or &#39;ascii&#39; | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**carrier_code** | **str** | Text-based code representing the carrier type. | [optional] [readonly] 

## Example

```python
from webshipperv2.models.edis import Edis

# TODO update the JSON string below
json = "{}"
# create an instance of Edis from a JSON string
edis_instance = Edis.from_json(json)
# print the JSON string representation of the object
print Edis.to_json()

# convert the object into a dict
edis_dict = edis_instance.to_dict()
# create an instance of Edis from a dict
edis_form_dict = edis.from_dict(edis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



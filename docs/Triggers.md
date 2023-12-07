# Triggers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | WEL expression for the trigger | [optional] 
**expression_ast** | **str** |  | [optional] 
**model_type** | **str** | Model for the trigger. E.g. Order | [optional] 
**event** | **str** | &lt;code&gt;created&lt;/code&gt; or &lt;code&gt;updated&lt;/code&gt; | [optional] 
**timing** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.triggers import Triggers

# TODO update the JSON string below
json = "{}"
# create an instance of Triggers from a JSON string
triggers_instance = Triggers.from_json(json)
# print the JSON string representation of the object
print Triggers.to_json()

# convert the object into a dict
triggers_dict = triggers_instance.to_dict()
# create an instance of Triggers from a dict
triggers_form_dict = triggers.from_dict(triggers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



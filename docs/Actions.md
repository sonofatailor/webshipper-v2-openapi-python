# Actions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_type** | **str** | Name of a supported job: &lt;ul&gt; &lt;li&gt; CreateShipmentJob &lt;/li&gt; &lt;/ul&gt; | [optional] 
**var_async** | **bool** | If true, this action runs as a background process, if not it runs immediately | [optional] 
**additional_attributes** | **List[str]** | Array of objects containing keys &lt;code&gt;attr_values&lt;/code&gt; and &lt;code&gt;attr_value&lt;/code&gt; | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.actions import Actions

# TODO update the JSON string below
json = "{}"
# create an instance of Actions from a JSON string
actions_instance = Actions.from_json(json)
# print the JSON string representation of the object
print Actions.to_json()

# convert the object into a dict
actions_dict = actions_instance.to_dict()
# create an instance of Actions from a dict
actions_form_dict = actions.from_dict(actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



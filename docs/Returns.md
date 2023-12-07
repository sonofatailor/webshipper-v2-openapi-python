# Returns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | One of pending, sent, arrived, processed, error or approved | [optional] 
**error_message** | **str** |  | [optional] 
**return_lines** | **List[str]** | Array of ReturnLine objects. Contains fields order_line_id, quantity, cause_id, cause_description and images. When creating, images should be an array of data uri containing the base64 encoding of the image, example: &lt;em&gt;data:image/jpeg;base64,AAQSkZJ......RgABAQEAlgCWAAD&lt;/em&gt; | [optional] 
**var_base64** | **str** | Base 64 encoding of return slip | [optional] 
**secret** | **str** | Read only token for publicly accessing status of the return order | [optional] [readonly] 
**internal_comment** | **str** |  | [optional] 
**latest_activity** | **str** |  | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from openapi_client.models.returns import Returns

# TODO update the JSON string below
json = "{}"
# create an instance of Returns from a JSON string
returns_instance = Returns.from_json(json)
# print the JSON string representation of the object
print Returns.to_json()

# convert the object into a dict
returns_dict = returns_instance.to_dict()
# create an instance of Returns from a dict
returns_form_dict = returns.from_dict(returns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



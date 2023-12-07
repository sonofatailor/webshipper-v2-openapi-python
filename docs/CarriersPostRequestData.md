# CarriersPostRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**attributes** | [**Carriers**](Carriers.md) |  | [optional] 

## Example

```python
from webshipperv2.models.carriers_post_request_data import CarriersPostRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CarriersPostRequestData from a JSON string
carriers_post_request_data_instance = CarriersPostRequestData.from_json(json)
# print the JSON string representation of the object
print CarriersPostRequestData.to_json()

# convert the object into a dict
carriers_post_request_data_dict = carriers_post_request_data_instance.to_dict()
# create an instance of CarriersPostRequestData from a dict
carriers_post_request_data_form_dict = carriers_post_request_data.from_dict(carriers_post_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



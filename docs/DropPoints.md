# DropPoints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_point_id** | **str** | The carriers ID of the drop point. | [optional] 
**name** | **str** | Name of the drop point | [optional] 
**address_1** | **str** | Address line 1 of the drop point | [optional] 
**address_2** | **str** | Address line 2 of the drop point | [optional] 
**zip** | **str** | Zip code for the drop point | [optional] 
**city** | **str** | City for the drop point | [optional] 
**country_code** | **str** | Country Code for the drop point. ISO 3166-1 Alfa 2  | [optional] 
**state** | **str** | State code. ISO 3166-2 Alfa 2 | [optional] 
**phone** | **str** | Phone of the drop point | [optional] 
**carrier_code** | **str** | Text base code to identify the carrier of the drop point ( not mandatory ) | [optional] 
**routing_code** | **str** | Routing code for the drop point. | [optional] 
**longitude** | **str** | Longitude | [optional] 
**latitude** | **str** | Latitude | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**opening_hours** | **str** | Opening hours for the drop point. Days are 0-indexed, starting with Monday as 0 | [optional] [readonly] 

## Example

```python
from openapi_client.models.drop_points import DropPoints

# TODO update the JSON string below
json = "{}"
# create an instance of DropPoints from a JSON string
drop_points_instance = DropPoints.from_json(json)
# print the JSON string representation of the object
print DropPoints.to_json()

# convert the object into a dict
drop_points_dict = drop_points_instance.to_dict()
# create an instance of DropPoints from a dict
drop_points_form_dict = drop_points.from_dict(drop_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



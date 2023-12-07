# Packages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** | Weight of the package | [optional] 
**weight_unit** | **str** | One of &#39;g&#39;, &#39;oz&#39;, &#39;lbs&#39; and &#39;kg&#39;  | [optional] 
**dimensions** | **str** |  | [optional] 
**service_attributes** | **str** |  | [optional] 
**add_ons** | **str** |  | [optional] 
**colli_type** | **str** | Colli type of the package. Can be used to specify if the colli is a pallet, package, letter, etc. Should use values from the supported_colli_types field from the service quote/list response for the given service. | [optional] 
**predefined_barcode** | **str** | A predefined SSCC barcode. Can be used if the barcode already has been created outside of Webshipper. | [optional] 

## Example

```python
from openapi_client.models.packages import Packages

# TODO update the JSON string below
json = "{}"
# create an instance of Packages from a JSON string
packages_instance = Packages.from_json(json)
# print the JSON string representation of the object
print Packages.to_json()

# convert the object into a dict
packages_dict = packages_instance.to_dict()
# create an instance of Packages from a dict
packages_form_dict = packages.from_dict(packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



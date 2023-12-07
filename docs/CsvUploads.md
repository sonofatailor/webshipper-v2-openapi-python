# CsvUploads


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported** | **List[str]** | A list of ids of the imported records | [optional] [readonly] 
**input** | **str** | The raw CSV data | [optional] 
**input_url** | **str** |  | [optional] 
**import_errors** | **List[str]** | A list of error messages for items that could not be imported | [optional] [readonly] 
**var_async** | **bool** | If set to true, the import will be performed in background. Highly recommended for imports larger than 100 rows. | [optional] 
**make_exportable** | **bool** |  | [optional] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from webshipperv2.models.csv_uploads import CsvUploads

# TODO update the JSON string below
json = "{}"
# create an instance of CsvUploads from a JSON string
csv_uploads_instance = CsvUploads.from_json(json)
# print the JSON string representation of the object
print CsvUploads.to_json()

# convert the object into a dict
csv_uploads_dict = csv_uploads_instance.to_dict()
# create an instance of CsvUploads from a dict
csv_uploads_form_dict = csv_uploads.from_dict(csv_uploads_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



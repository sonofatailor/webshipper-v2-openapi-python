# AttachmentsIdGet200ResponseIncludedInnerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** | Id of the shipment it belongs to | [optional] 
**document_size** | **str** | Enum for the paper size. valid values: &lt;code&gt;A4&lt;/code&gt; | [optional] 
**document_format** | **str** | Enum for the document format. Valid values: &lt;code&gt;PDF&lt;/code&gt; | [optional] 
**var_base64** | **str** | Base64 representation of the document. Only required when creating. | [optional] 
**is_special** | **bool** | Used to indicate if this document is a special document, like static customs documents. Special documents will be displayed in Webshipper under Settings &gt; Documents. | [optional] 
**name** | **str** | Used for special documents | [optional] 
**description** | **str** | Used for special documents | [optional] 
**document_type** | **int** | One of: &#39;shipping_document&#39;, &#39;other&#39;, &#39;customs_document&#39;, &#39;invoice&#39;, &#39;certificate&#39;, &#39;proforma&#39;, &#39;nafta_certificate&#39;, &#39;commercial&#39;, &#39;awb&#39;. Documents returned from the carrier are always shipping_document.  | [optional] 
**is_paperless** | **bool** | Used to indicate if a shipment is paperless | [optional] 
**updated_at** | **str** | The time when resource was last updated or when it was created if it was never updated | [optional] [readonly] 
**created_at** | **str** | The time when the resource was created | [optional] [readonly] 

## Example

```python
from webshipperv2.models.attachments_id_get200_response_included_inner_data import AttachmentsIdGet200ResponseIncludedInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsIdGet200ResponseIncludedInnerData from a JSON string
attachments_id_get200_response_included_inner_data_instance = AttachmentsIdGet200ResponseIncludedInnerData.from_json(json)
# print the JSON string representation of the object
print AttachmentsIdGet200ResponseIncludedInnerData.to_json()

# convert the object into a dict
attachments_id_get200_response_included_inner_data_dict = attachments_id_get200_response_included_inner_data_instance.to_dict()
# create an instance of AttachmentsIdGet200ResponseIncludedInnerData from a dict
attachments_id_get200_response_included_inner_data_form_dict = attachments_id_get200_response_included_inner_data.from_dict(attachments_id_get200_response_included_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



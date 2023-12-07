# ServiceQuotes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True if quote was successful | [optional] [readonly] 
**carrier_id** | **int** | The id of the carrier to quote | [optional] 
**service_code** | **str** | Service code of the carrier. This is optional. When omitted, all supported services will be returned. | [optional] 
**send_time** | **str** | ISO 8601 formatted | [optional] 
**send_date** | **str** |  | [optional] 
**packages** | **List[str]** | Array of objects, each containing key &lt;code&gt;weight&lt;/code&gt;. At least one package is required. | [optional] 
**delivery_address** | **object** | Delivery address for the quote | [optional] 
**sender_address** | **object** | Sender address for the quote | [optional] 
**services** | **List[str]** | Read only. Populated in response with an array of objects containing the following keys: &lt;ul class&#x3D;&#39;list-doc&#39;&gt;  &lt;li&gt;&lt;code&gt;service_name&lt;/code&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;service_code&lt;/code&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;is_return&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;supports_paperless&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;requires_drop_point&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;cost_price&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;currency&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;vat_percent&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;estimated_delivery_date_from&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;estimated_delivery_date_to&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;    &lt;code&gt;add_ons&lt;/code&gt; &lt;div class&#x3D;&#39;text-muted&#39;&gt;Array containing objects&lt;/div&gt;   &lt;ul class&#x3D;&#39;list-doc&#39;&gt;     &lt;li&gt;&lt;code&gt;add_on_name&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;add_on_code&lt;/code&gt;&lt;/li&gt;   &lt;/ul&gt; &lt;/li&gt;    &lt;li&gt;&lt;code&gt;parameters&lt;/code&gt;&lt;/li&gt; &lt;div class&#x3D;&#39;text-muted&#39;&gt;Array containing objects&lt;/div&gt;    &lt;ul class&#x3D;&#39;list-doc&#39;&gt;     &lt;li&gt;&lt;code&gt;attr_name&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;attr_key&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;attr_type&lt;/code&gt;&lt;/li&gt;    &lt;/ul&gt;    &lt;li&gt;&lt;code&gt;country_combinations&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;barcode_requirement&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;waybill_requirement&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;booking_quote_info&lt;/code&gt;&lt;/li&gt;    &lt;li&gt;&lt;code&gt;supported_colli_types&lt;/code&gt;&lt;/li&gt;  &lt;/ul&gt; | [optional] [readonly] 
**add_ons** | **str** | Carrier add-ons for the quote | [optional] 
**service_attributes** | **str** | Service attributes for the carrier | [optional] 
**is_return** | **str** | Determines if you are quoting for return (inbound) services or standard (outbound) services. | [optional] 
**dutiable** | **str** | Determines if the goods for the quote are dutiable | [optional] 
**cost_sheet_id** | **str** | Used if you want only a price from a specific cost sheet | [optional] 
**timeout** | **str** | Timeout for request in seconds. Will default to 15 seconds | [optional] 

## Example

```python
from openapi_client.models.service_quotes import ServiceQuotes

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotes from a JSON string
service_quotes_instance = ServiceQuotes.from_json(json)
# print the JSON string representation of the object
print ServiceQuotes.to_json()

# convert the object into a dict
service_quotes_dict = service_quotes_instance.to_dict()
# create an instance of ServiceQuotes from a dict
service_quotes_form_dict = service_quotes.from_dict(service_quotes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



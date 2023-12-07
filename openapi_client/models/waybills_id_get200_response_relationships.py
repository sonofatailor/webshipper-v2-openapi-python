# coding: utf-8

"""
    Webshipper V2 REST API

       <p>     The Webshipper API is a RESTful JSON API that gives full control over your Webshipper account. The API is scoped to your <em>account name</em>,     and is accessed via the endpoint <em>https://&lt;account name&gt;.api.webshipper.io/v2/</em>. Your <em>account name</em> is the same as you see when you access the Webshipper web UI     at <em>https://&lt;account name&gt;.webshipper.io</em>.   </p>    <p>     This API conforms to the <a href=\"http://jsonapi.org/\">JSON API standard</a> with the following conventions:     <ul>       <li>Resources are identified with the attribute <code>id</code>, which is a server-side generated sequential integer</li>       <li>Resource types are pluralised and underscored, like <code>order_lines</code></li>       <li>The API has a fixed page limit of 30 records. To fetch more records use the query parameter <code>page[number]</code></li>       <li>All resources have the attributes <code>created_at</code> and <code>updated_at</code> which are ISO 8601 timestamps like <code>2018-03-07T14:01:18.000Z</code> </li>       <li>All country codes are <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes</li>     </ul>   </p>     <p> It is also possible to download the documentation in the OpenAPI 3.0 <a href=\"?download_openapi=1\">here</a> </p>    <div class=\"alert alert-info\">     <i class=\"fa fa-info mr-2\"></i>     Webshipper <em>strongly</em> recommends using a client library for utilising this API. Refer to jsonapi.org's list of     <a href=\"http://jsonapi.org/implementations/#client-libraries\">jsonapi.org's list of client libraries</a> to find one for your language.   </div> 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from openapi_client.models.barcode_ranges_id_get200_response_relationships_carrier import BarcodeRangesIdGet200ResponseRelationshipsCarrier
from openapi_client.models.carriers_id_get200_response_relationships_sender_address import CarriersIdGet200ResponseRelationshipsSenderAddress
from openapi_client.models.orders_id_get200_response_relationships_printer_client import OrdersIdGet200ResponseRelationshipsPrinterClient
from openapi_client.models.shipments_id_get200_response_relationships_document_template import ShipmentsIdGet200ResponseRelationshipsDocumentTemplate
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WaybillsIdGet200ResponseRelationships(BaseModel):
    """
    WaybillsIdGet200ResponseRelationships
    """ # noqa: E501
    carrier: Optional[BarcodeRangesIdGet200ResponseRelationshipsCarrier] = None
    sold_to_address: Optional[CarriersIdGet200ResponseRelationshipsSenderAddress] = None
    sender_address: Optional[CarriersIdGet200ResponseRelationshipsSenderAddress] = None
    document_template: Optional[ShipmentsIdGet200ResponseRelationshipsDocumentTemplate] = None
    printer_client: Optional[OrdersIdGet200ResponseRelationshipsPrinterClient] = None
    __properties: ClassVar[List[str]] = ["carrier", "sold_to_address", "sender_address", "document_template", "printer_client"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WaybillsIdGet200ResponseRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of carrier
        if self.carrier:
            _dict['carrier'] = self.carrier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sold_to_address
        if self.sold_to_address:
            _dict['sold_to_address'] = self.sold_to_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender_address
        if self.sender_address:
            _dict['sender_address'] = self.sender_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_template
        if self.document_template:
            _dict['document_template'] = self.document_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of printer_client
        if self.printer_client:
            _dict['printer_client'] = self.printer_client.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WaybillsIdGet200ResponseRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrier": BarcodeRangesIdGet200ResponseRelationshipsCarrier.from_dict(obj.get("carrier")) if obj.get("carrier") is not None else None,
            "sold_to_address": CarriersIdGet200ResponseRelationshipsSenderAddress.from_dict(obj.get("sold_to_address")) if obj.get("sold_to_address") is not None else None,
            "sender_address": CarriersIdGet200ResponseRelationshipsSenderAddress.from_dict(obj.get("sender_address")) if obj.get("sender_address") is not None else None,
            "document_template": ShipmentsIdGet200ResponseRelationshipsDocumentTemplate.from_dict(obj.get("document_template")) if obj.get("document_template") is not None else None,
            "printer_client": OrdersIdGet200ResponseRelationshipsPrinterClient.from_dict(obj.get("printer_client")) if obj.get("printer_client") is not None else None
        })
        return _obj



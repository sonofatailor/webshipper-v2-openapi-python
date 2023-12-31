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
from pydantic import Field
from webshipperv2.models.additional_attributes_id_get200_response_relationships_order import AdditionalAttributesIdGet200ResponseRelationshipsOrder
from webshipperv2.models.barcode_ranges_id_get200_response_relationships_carrier import BarcodeRangesIdGet200ResponseRelationshipsCarrier
from webshipperv2.models.edis_id_get200_response_relationships_shipment import EdisIdGet200ResponseRelationshipsShipment
from webshipperv2.models.orders_id_get200_response_relationships_printer_client import OrdersIdGet200ResponseRelationshipsPrinterClient
from webshipperv2.models.orders_id_get200_response_relationships_shipping_rate import OrdersIdGet200ResponseRelationshipsShippingRate
from webshipperv2.models.return_portals_id_get200_response_relationships_mail_template import ReturnPortalsIdGet200ResponseRelationshipsMailTemplate
from webshipperv2.models.shipments_id_get200_response_relationships_document_template import ShipmentsIdGet200ResponseRelationshipsDocumentTemplate
from webshipperv2.models.shipments_id_get200_response_relationships_pickup import ShipmentsIdGet200ResponseRelationshipsPickup
from webshipperv2.models.shipments_id_get200_response_relationships_return import ShipmentsIdGet200ResponseRelationshipsReturn
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ShipmentsIdGet200ResponseRelationships(BaseModel):
    """
    ShipmentsIdGet200ResponseRelationships
    """ # noqa: E501
    carrier: Optional[BarcodeRangesIdGet200ResponseRelationshipsCarrier] = None
    order: Optional[AdditionalAttributesIdGet200ResponseRelationshipsOrder] = None
    shipping_rate: Optional[OrdersIdGet200ResponseRelationshipsShippingRate] = None
    printer_client: Optional[OrdersIdGet200ResponseRelationshipsPrinterClient] = None
    original_shipment: Optional[EdisIdGet200ResponseRelationshipsShipment] = None
    pickup: Optional[ShipmentsIdGet200ResponseRelationshipsPickup] = None
    shadow_shipment: Optional[EdisIdGet200ResponseRelationshipsShipment] = None
    var_return: Optional[ShipmentsIdGet200ResponseRelationshipsReturn] = Field(default=None, alias="return")
    document_template: Optional[ShipmentsIdGet200ResponseRelationshipsDocumentTemplate] = None
    mail_template: Optional[ReturnPortalsIdGet200ResponseRelationshipsMailTemplate] = None
    return_label_mail_template: Optional[ReturnPortalsIdGet200ResponseRelationshipsMailTemplate] = None
    __properties: ClassVar[List[str]] = ["carrier", "order", "shipping_rate", "printer_client", "original_shipment", "pickup", "shadow_shipment", "return", "document_template", "mail_template", "return_label_mail_template"]

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
        """Create an instance of ShipmentsIdGet200ResponseRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_rate
        if self.shipping_rate:
            _dict['shipping_rate'] = self.shipping_rate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of printer_client
        if self.printer_client:
            _dict['printer_client'] = self.printer_client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_shipment
        if self.original_shipment:
            _dict['original_shipment'] = self.original_shipment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pickup
        if self.pickup:
            _dict['pickup'] = self.pickup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shadow_shipment
        if self.shadow_shipment:
            _dict['shadow_shipment'] = self.shadow_shipment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_return
        if self.var_return:
            _dict['return'] = self.var_return.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_template
        if self.document_template:
            _dict['document_template'] = self.document_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mail_template
        if self.mail_template:
            _dict['mail_template'] = self.mail_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of return_label_mail_template
        if self.return_label_mail_template:
            _dict['return_label_mail_template'] = self.return_label_mail_template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ShipmentsIdGet200ResponseRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrier": BarcodeRangesIdGet200ResponseRelationshipsCarrier.from_dict(obj.get("carrier")) if obj.get("carrier") is not None else None,
            "order": AdditionalAttributesIdGet200ResponseRelationshipsOrder.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "shipping_rate": OrdersIdGet200ResponseRelationshipsShippingRate.from_dict(obj.get("shipping_rate")) if obj.get("shipping_rate") is not None else None,
            "printer_client": OrdersIdGet200ResponseRelationshipsPrinterClient.from_dict(obj.get("printer_client")) if obj.get("printer_client") is not None else None,
            "original_shipment": EdisIdGet200ResponseRelationshipsShipment.from_dict(obj.get("original_shipment")) if obj.get("original_shipment") is not None else None,
            "pickup": ShipmentsIdGet200ResponseRelationshipsPickup.from_dict(obj.get("pickup")) if obj.get("pickup") is not None else None,
            "shadow_shipment": EdisIdGet200ResponseRelationshipsShipment.from_dict(obj.get("shadow_shipment")) if obj.get("shadow_shipment") is not None else None,
            "return": ShipmentsIdGet200ResponseRelationshipsReturn.from_dict(obj.get("return")) if obj.get("return") is not None else None,
            "document_template": ShipmentsIdGet200ResponseRelationshipsDocumentTemplate.from_dict(obj.get("document_template")) if obj.get("document_template") is not None else None,
            "mail_template": ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.from_dict(obj.get("mail_template")) if obj.get("mail_template") is not None else None,
            "return_label_mail_template": ReturnPortalsIdGet200ResponseRelationshipsMailTemplate.from_dict(obj.get("return_label_mail_template")) if obj.get("return_label_mail_template") is not None else None
        })
        return _obj



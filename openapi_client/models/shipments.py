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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.packages import Packages
from openapi_client.models.shipments_tracking_links_inner import ShipmentsTrackingLinksInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Shipments(BaseModel):
    """
    Shipments
    """ # noqa: E501
    reference: Optional[StrictStr] = Field(default=None, description="The reference you want to identify the shipment form. For example order number.")
    comment: Optional[StrictStr] = Field(default=None, description="An optional comment for the carrier")
    service_code: Optional[StrictStr] = Field(default=None, description="The carrier's service code. This should only be assigned if you are not using a shipping rate.")
    is_return: Optional[StrictBool] = Field(default=None, description="Determines whether the shipment is a return shipment.")
    packages: Optional[List[Packages]] = Field(default=None, description="Flattened array of packages to be sent. At least one package is mandatory. For structure refer to 'Package' entity")
    delivery_address: Optional[Union[str, Any]] = Field(default=None, description="Flattened Shipping Address representing the delivery address for the shipment. <br><strong>Duplicated from order if order relation given.</strong>.")
    sender_address: Optional[Union[str, Any]] = Field(default=None, description="Flattened Shipping Address representing the sender address of shipment. <br><strong>Duplicated from order if order relation given.</strong>.")
    billing_address: Optional[Union[str, Any]] = Field(default=None, description="Flattened Shipping Address representing the billing address of shipment. Duplicated from delivery address if empty. <br><strong>Duplicated from order if order relation given.</strong>.")
    pickup_address: Optional[Union[str, Any]] = Field(default=None, description="Flattened Shipping Address representing the pickup address of shipment. Is necessary for some carriers. This is duplicated from sender address if empty. <br><strong>Duplicated from order if order relation given.</strong>.")
    return_address: Optional[Union[str, Any]] = Field(default=None, description="Flattened Shipping Address represnting return addres of shipment. Will be duplicated from sender address if empty ( Not used by all carriers ). <br><strong>Duplicated from order if order relation given.</strong>.")
    service_attributes: Optional[List[StrictStr]] = Field(default=None, description="Array of hashes to assign parameters for any specific carrier service. It is only required if you are <strong>not</strong> using shipping rates and the service has additional required parameters. The hash must have the keys attr_key and attr_value. The type of attr_value should match the attr_type defined by the parameter. To see all possible attributes, please see the list of parameters from the carrier service. <strongShould only be assigned if you are not using a shipping rate</strong>.")
    add_ons: Optional[List[StrictStr]] = Field(default=None, description="Array of add-ons. Add-ons are simply arrays of strings. To see possible add-ons, please refer to the carrier services. <strong>Should only be assigned if you are not using a shipping rate</strong>.")
    sms_notification: Optional[StrictStr] = Field(default=None, description="Must be passed if the carrier should be allowed to send SMS notifications. It should be assigned with a hash including the key phone containing the phone number to be notified. <strong>Should only be assigned if you are not using a shipping rate</strong>.")
    email_notification: Optional[StrictStr] = Field(default=None, description="Must be passed if the carrier should be allowed to send e-mail notifications. It should be assigned with a hash including the key email containing the e-mail address to be notified. <strong>Should only be assigned if you are not using a shipping rate</strong>.")
    included_documents: Optional[StrictStr] = Field(default=None, description="Flattened array of Document - can be used to upload documents to the shipment which will be sent to the carrier.")
    drop_point: Optional[StrictStr] = Field(default=None, description="Flattened Drop Point - should only be assigned if you are sending to a drop point.")
    tracking_links: Optional[List[ShipmentsTrackingLinksInner]] = Field(default=None, description="An array of objects with the keys:       <ul>         <li><code>url</code>: The full URL to the tracking page.</li>         <li><code>number</code>: The tracking identifier.</li>         <li><code>latest_transit_event</code>: The latest tracking/transit event. Same options as Tracking Event statuses.</li>         <li><code>tracking_events</code>: Array of objects. Object has same attributes as the Tracking Event resource</li>       </ul>       ")
    fulfill_immediately: Optional[StrictStr] = Field(default=None, description="Deprecated")
    test_mode: Optional[StrictBool] = None
    dutiable: Optional[StrictBool] = None
    created_at: Optional[StrictStr] = Field(default=None, description="The time when the resource was created")
    ext_ref: Optional[StrictStr] = Field(default=None, description="The external (carrier) reference")
    original_shipment_id: Optional[StrictInt] = None
    send_time: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    latest_update_time: Optional[StrictStr] = None
    supports_updates: Optional[StrictStr] = None
    additional_attributes: Optional[StrictStr] = Field(default=None, description="Flattened hash with optional key/value pairs.")
    cost_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost price of the shipment, either directly from the carrier or from a cost sheet")
    sales_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The price presented to the customer in checkout")
    currency: Optional[StrictStr] = None
    manual_order_shipment_creation: Optional[StrictStr] = None
    carrier_type_name: Optional[StrictStr] = Field(default=None, description="Webshipper defined name of the carrier type")
    carrier_alias: Optional[StrictStr] = Field(default=None, description="Carrier alias set by the user in Webshipper")
    carrier_id: Optional[StrictInt] = Field(default=None, description="ID of the carrier")
    invoice_settings: Optional[StrictStr] = None
    latest_activity: Optional[StrictStr] = None
    latest_status_event: Optional[StrictStr] = None
    shadow_booking_as_parent: Optional[StrictStr] = None
    source: Optional[StrictInt] = None
    document_template: Optional[StrictStr] = None
    csv_upload_id: Optional[StrictInt] = None
    omit_print: Optional[StrictBool] = None
    original_shipment: Optional[StrictStr] = Field(default=None, description="An optional link to the original shipment, when creating a return-shipment")
    __properties: ClassVar[List[str]] = ["reference", "comment", "service_code", "is_return", "packages", "delivery_address", "sender_address", "billing_address", "pickup_address", "return_address", "service_attributes", "add_ons", "sms_notification", "email_notification", "included_documents", "drop_point", "tracking_links", "fulfill_immediately", "test_mode", "dutiable", "created_at", "ext_ref", "original_shipment_id", "send_time", "status", "latest_update_time", "supports_updates", "additional_attributes", "cost_price", "sales_price", "currency", "manual_order_shipment_creation", "carrier_type_name", "carrier_alias", "carrier_id", "invoice_settings", "latest_activity", "latest_status_event", "shadow_booking_as_parent", "source", "document_template", "csv_upload_id", "omit_print", "original_shipment"]

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
        """Create an instance of Shipments from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "carrier_type_name",
                "carrier_alias",
                "carrier_id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in packages (list)
        _items = []
        if self.packages:
            for _item in self.packages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['packages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tracking_links (list)
        _items = []
        if self.tracking_links:
            for _item in self.tracking_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tracking_links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Shipments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "comment": obj.get("comment"),
            "service_code": obj.get("service_code"),
            "is_return": obj.get("is_return"),
            "packages": [Packages.from_dict(_item) for _item in obj.get("packages")] if obj.get("packages") is not None else None,
            "delivery_address": obj.get("delivery_address"),
            "sender_address": obj.get("sender_address"),
            "billing_address": obj.get("billing_address"),
            "pickup_address": obj.get("pickup_address"),
            "return_address": obj.get("return_address"),
            "service_attributes": obj.get("service_attributes"),
            "add_ons": obj.get("add_ons"),
            "sms_notification": obj.get("sms_notification"),
            "email_notification": obj.get("email_notification"),
            "included_documents": obj.get("included_documents"),
            "drop_point": obj.get("drop_point"),
            "tracking_links": [ShipmentsTrackingLinksInner.from_dict(_item) for _item in obj.get("tracking_links")] if obj.get("tracking_links") is not None else None,
            "fulfill_immediately": obj.get("fulfill_immediately"),
            "test_mode": obj.get("test_mode"),
            "dutiable": obj.get("dutiable"),
            "created_at": obj.get("created_at"),
            "ext_ref": obj.get("ext_ref"),
            "original_shipment_id": obj.get("original_shipment_id"),
            "send_time": obj.get("send_time"),
            "status": obj.get("status"),
            "latest_update_time": obj.get("latest_update_time"),
            "supports_updates": obj.get("supports_updates"),
            "additional_attributes": obj.get("additional_attributes"),
            "cost_price": obj.get("cost_price"),
            "sales_price": obj.get("sales_price"),
            "currency": obj.get("currency"),
            "manual_order_shipment_creation": obj.get("manual_order_shipment_creation"),
            "carrier_type_name": obj.get("carrier_type_name"),
            "carrier_alias": obj.get("carrier_alias"),
            "carrier_id": obj.get("carrier_id"),
            "invoice_settings": obj.get("invoice_settings"),
            "latest_activity": obj.get("latest_activity"),
            "latest_status_event": obj.get("latest_status_event"),
            "shadow_booking_as_parent": obj.get("shadow_booking_as_parent"),
            "source": obj.get("source"),
            "document_template": obj.get("document_template"),
            "csv_upload_id": obj.get("csv_upload_id"),
            "omit_print": obj.get("omit_print"),
            "original_shipment": obj.get("original_shipment")
        })
        return _obj


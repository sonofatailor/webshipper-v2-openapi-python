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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderChannels(BaseModel):
    """
    OrderChannels
    """ # noqa: E501
    channel_label: Optional[StrictStr] = Field(default=None, description="Label to identify the order channel.")
    attrs: Optional[List[StrictStr]] = Field(default=None, description="Array of hashed with keys: <code>attr_key</code>, <code>attr_value</code>, <code>attr_name</code>, <code>attr_type</code>, <code>is_required</code>, <code>only_visible_on_creation</code> </code>enums</code>. See       documentation for Local Attributes")
    additional_parameters: Optional[Union[str, Any]] = Field(default=None, description="Optional hash, this is used when creating new order channels.")
    slip_print_mode: Optional[StrictStr] = Field(default=None, description="Possible values: 'dont_print', 'print_immediately' or 'print_with_shipment'.")
    return_label_print_mode: Optional[StrictStr] = Field(default=None, description="Possible values: 'dont_print', 'print_immediately'.")
    shipping_label_print_mode: Optional[StrictStr] = Field(default=None, description="Possible values: 'dont_print', 'print_immediately'.")
    document_print_mode: Optional[StrictStr] = Field(default=None, description="Possible values: 'dont_print', 'print_immediately'.")
    logo: Optional[StrictStr] = Field(default=None, description="Base64 representation of the logo of the order channel.")
    configuration_token: Optional[StrictStr] = Field(default=None, description="Token to use for Webshipper modules. Tokens will only be generated for modules that require a configuration token.")
    sync_status: Optional[StrictInt] = Field(default=None, description="Determines if the order channel is currently synchronising. Possible values are: <code>synchronize</code>, <code>suspended</code>, <code>paused</code>.")
    failed_sync_count: Optional[StrictInt] = Field(default=None, description="Shows if recent synchronisation events have failed.")
    fulfill_automatically: Optional[StrictBool] = Field(default=None, description="Whether or not to fulfill the order in the original order channel when a shipment is created. Default: true")
    drop_point_limit: Optional[StrictInt] = None
    create_shipment_automatically: Optional[StrictBool] = None
    health: Optional[StrictStr] = None
    convert_currency_on_rate_quotes: Optional[StrictBool] = None
    sync_additional_attributes_to_shipments: Optional[StrictBool] = None
    auto_order_import: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["channel_label", "attrs", "additional_parameters", "slip_print_mode", "return_label_print_mode", "shipping_label_print_mode", "document_print_mode", "logo", "configuration_token", "sync_status", "failed_sync_count", "fulfill_automatically", "drop_point_limit", "create_shipment_automatically", "health", "convert_currency_on_rate_quotes", "sync_additional_attributes_to_shipments", "auto_order_import"]

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
        """Create an instance of OrderChannels from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderChannels from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel_label": obj.get("channel_label"),
            "attrs": obj.get("attrs"),
            "additional_parameters": obj.get("additional_parameters"),
            "slip_print_mode": obj.get("slip_print_mode"),
            "return_label_print_mode": obj.get("return_label_print_mode"),
            "shipping_label_print_mode": obj.get("shipping_label_print_mode"),
            "document_print_mode": obj.get("document_print_mode"),
            "logo": obj.get("logo"),
            "configuration_token": obj.get("configuration_token"),
            "sync_status": obj.get("sync_status"),
            "failed_sync_count": obj.get("failed_sync_count"),
            "fulfill_automatically": obj.get("fulfill_automatically"),
            "drop_point_limit": obj.get("drop_point_limit"),
            "create_shipment_automatically": obj.get("create_shipment_automatically"),
            "health": obj.get("health"),
            "convert_currency_on_rate_quotes": obj.get("convert_currency_on_rate_quotes"),
            "sync_additional_attributes_to_shipments": obj.get("sync_additional_attributes_to_shipments"),
            "auto_order_import": obj.get("auto_order_import")
        })
        return _obj



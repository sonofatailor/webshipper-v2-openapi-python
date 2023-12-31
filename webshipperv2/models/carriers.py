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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Carriers(BaseModel):
    """
    Carriers
    """ # noqa: E501
    alias: Optional[StrictStr] = Field(default=None, description="Your name for the carrier")
    services: Optional[StrictStr] = Field(default=None, description="Array of services provided by this Carrier")
    attrs: Optional[StrictStr] = Field(default=None, description="Array of hashes with keys: <code>attr_key</code>, <code>attr_value</code>, <code>attr_name</code>, <code>attr_type</code>, <code>is_required</code>, <code>only_visible_on_creation</code>, </code>enums</code>. See       documentation for Local Attributes")
    prefer_zpl: Optional[StrictBool] = None
    created_at: Optional[StrictStr] = Field(default=None, description="The time when the resource was created")
    updated_at: Optional[StrictStr] = Field(default=None, description="The time when resource was last updated or when it was created if it was never updated")
    is_approved: Optional[StrictBool] = None
    approved_service_codes: Optional[StrictStr] = None
    service_parameter_enums: Optional[StrictStr] = None
    barcode_notification_behavior: Optional[StrictInt] = None
    barcode_notification_mail: Optional[StrictStr] = None
    has_active_cost_sheet: Optional[StrictStr] = None
    delete_at_carrier: Optional[StrictBool] = None
    test_mode: Optional[StrictBool] = None
    logo: Optional[StrictStr] = None
    logo_url: Optional[StrictStr] = None
    print_error_label: Optional[StrictBool] = None
    ftp_configuration_id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["alias", "services", "attrs", "prefer_zpl", "created_at", "updated_at", "is_approved", "approved_service_codes", "service_parameter_enums", "barcode_notification_behavior", "barcode_notification_mail", "has_active_cost_sheet", "delete_at_carrier", "test_mode", "logo", "logo_url", "print_error_label", "ftp_configuration_id"]

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
        """Create an instance of Carriers from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Carriers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alias": obj.get("alias"),
            "services": obj.get("services"),
            "attrs": obj.get("attrs"),
            "prefer_zpl": obj.get("prefer_zpl"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "is_approved": obj.get("is_approved"),
            "approved_service_codes": obj.get("approved_service_codes"),
            "service_parameter_enums": obj.get("service_parameter_enums"),
            "barcode_notification_behavior": obj.get("barcode_notification_behavior"),
            "barcode_notification_mail": obj.get("barcode_notification_mail"),
            "has_active_cost_sheet": obj.get("has_active_cost_sheet"),
            "delete_at_carrier": obj.get("delete_at_carrier"),
            "test_mode": obj.get("test_mode"),
            "logo": obj.get("logo"),
            "logo_url": obj.get("logo_url"),
            "print_error_label": obj.get("print_error_label"),
            "ftp_configuration_id": obj.get("ftp_configuration_id")
        })
        return _obj



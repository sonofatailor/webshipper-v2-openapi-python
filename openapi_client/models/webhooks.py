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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Webhooks(BaseModel):
    """
    Webhooks
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description="The HTTP endpoint to be called. Webhooks always use POST as the request method.")
    topic: Optional[StrictStr] = Field(default=None, description="Which event should trigger the webhooks. Supported topics:     <ul>       <li><strong>order/created</strong> triggered when an order is created.</li>       <li><strong>order/updated</strong> triggered when an order is updated.</li>       <li><strong>order/deleted</strong> triggered when an order was deleted.</li>       <li><strong>shipment/created</strong> triggered when a shipment is created.</li>       <li><strong>shipment/updated</strong> triggered when a shipment is updated.</li>       <li><strong>shipment/deleted</strong> triggered when a shipment was deleted.</li>       <li><strong>return/created</strong> triggered when a return is created.</li>       <li><strong>return/updated</strong> triggered when a return is updated.</li>       <li><strong>return/deleted</strong> triggered when a return was deleted.</li>       <li><strong>report/created</strong> triggered when a report is created.</li>       <li><strong>report/updated</strong> triggered when a report is updated.</li>       <li><strong>report/deleted</strong> triggered when a report was deleted.</li>       <li><strong>trackingevent/created</strong> triggered when a tracking event is created.</li>       <li><strong>trackingevent/updated</strong> triggered when a tracking event is updated.</li>       <li><strong>trackingevent/deleted</strong> triggered when a tracking event was deleted.</li>     </ul>")
    enabled: Optional[StrictBool] = Field(default=None, description="This is a boolean attribute that specifies whether the webhook is active.")
    secret: Optional[StrictStr] = Field(default=None, description="The secret used to sign the HMAC.")
    health: Optional[StrictStr] = None
    latest_error: Optional[StrictStr] = Field(default=None, description="The most recent error message.")
    condition: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(default=None, description="The time when the resource was created")
    updated_at: Optional[StrictStr] = Field(default=None, description="The time when resource was last updated or when it was created if it was never updated")
    carriers: Optional[StrictStr] = None
    order_channels: Optional[List[StrictStr]] = Field(default=None, description="Array of objects containing keys id and channel_label if condition describes a list of allowed order channels, <code>null</code> otherwise. ")
    __properties: ClassVar[List[str]] = ["url", "topic", "enabled", "secret", "health", "latest_error", "condition", "created_at", "updated_at", "carriers", "order_channels"]

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
        """Create an instance of Webhooks from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
                "order_channels",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Webhooks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "topic": obj.get("topic"),
            "enabled": obj.get("enabled"),
            "secret": obj.get("secret"),
            "health": obj.get("health"),
            "latest_error": obj.get("latest_error"),
            "condition": obj.get("condition"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "carriers": obj.get("carriers"),
            "order_channels": obj.get("order_channels")
        })
        return _obj



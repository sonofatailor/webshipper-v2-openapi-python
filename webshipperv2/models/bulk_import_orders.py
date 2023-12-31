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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BulkImportOrders(BaseModel):
    """
    BulkImportOrders
    """ # noqa: E501
    ids: Optional[StrictStr] = Field(default=None, description="Order ids to import from the order channel")
    order_channel_id: Optional[StrictStr] = Field(default=None, description="Id of the order channel to import orders from")
    var_async: Optional[StrictStr] = Field(default=None, description="Run the import asyncronously, default is false unless importing more than one order or from more than one order channel", alias="async")
    reimport: Optional[StrictStr] = Field(default=None, description="Reimport orders from the order channel. WARNING: This will overwrite any changes to the order made in Webshipper and import the order as it is in the order channel")
    time_start: Optional[StrictStr] = Field(default=None, description="Time from when orders should be imported, all orders after this time is imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel")
    time_end: Optional[StrictStr] = Field(default=None, description="Time to when orders should be imported, all orders before this time is imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel")
    statuses: Optional[StrictStr] = Field(default=None, description="Statuses of orders to import, all orders with the given statuses are imported from the order channel. This option is not supported by all order channels and there might be some limitations depending on the order channel")
    bulk_imports: Optional[StrictStr] = Field(default=None, description="List of bulk imports with the same attributes as above. This can be used to import multiple orders from multiple order channels at once. Options specified in the root object is used globally, but is overridable by specififying the option for specific bulk_import in the list.")
    source: Optional[StrictStr] = Field(default=None, description="Source of the orders to import. This will default to API")
    __properties: ClassVar[List[str]] = ["ids", "order_channel_id", "async", "reimport", "time_start", "time_end", "statuses", "bulk_imports", "source"]

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
        """Create an instance of BulkImportOrders from a JSON string"""
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
        """Create an instance of BulkImportOrders from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ids": obj.get("ids"),
            "order_channel_id": obj.get("order_channel_id"),
            "async": obj.get("async"),
            "reimport": obj.get("reimport"),
            "time_start": obj.get("time_start"),
            "time_end": obj.get("time_end"),
            "statuses": obj.get("statuses"),
            "bulk_imports": obj.get("bulk_imports"),
            "source": obj.get("source")
        })
        return _obj



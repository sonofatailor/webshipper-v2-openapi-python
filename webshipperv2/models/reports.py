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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Reports(BaseModel):
    """
    Reports
    """ # noqa: E501
    updated_at: Optional[StrictStr] = Field(default=None, description="The time when resource was last updated or when it was created if it was never updated")
    created_at: Optional[StrictStr] = Field(default=None, description="The time when the resource was created")
    start_time: Optional[StrictStr] = None
    end_time: Optional[StrictStr] = None
    output_formats: Optional[List[StrictStr]] = None
    parameters: Optional[Union[str, Any]] = None
    var_base64: Optional[StrictStr] = Field(default=None, alias="base64")
    pdf_download_url: Optional[StrictStr] = None
    xml_download_url: Optional[StrictStr] = None
    csv_download_url: Optional[StrictStr] = None
    json_download_url: Optional[StrictStr] = None
    xlsx_download_url: Optional[StrictStr] = None
    failed: Optional[StrictBool] = None
    order_ids: Optional[StrictStr] = None
    error_message: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["updated_at", "created_at", "start_time", "end_time", "output_formats", "parameters", "base64", "pdf_download_url", "xml_download_url", "csv_download_url", "json_download_url", "xlsx_download_url", "failed", "order_ids", "error_message"]

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
        """Create an instance of Reports from a JSON string"""
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
                "updated_at",
                "created_at",
                "var_base64",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Reports from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "output_formats": obj.get("output_formats"),
            "parameters": obj.get("parameters"),
            "base64": obj.get("base64"),
            "pdf_download_url": obj.get("pdf_download_url"),
            "xml_download_url": obj.get("xml_download_url"),
            "csv_download_url": obj.get("csv_download_url"),
            "json_download_url": obj.get("json_download_url"),
            "xlsx_download_url": obj.get("xlsx_download_url"),
            "failed": obj.get("failed"),
            "order_ids": obj.get("order_ids"),
            "error_message": obj.get("error_message")
        })
        return _obj



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

class SlipTemplates(BaseModel):
    """
    SlipTemplates
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name to identify the template.")
    slip_size: Optional[StrictInt] = Field(default=None, description="Size of the parcel slip. Possible values: <code>A4</code> and <code>4X6</code>")
    additional_content: Optional[StrictStr] = Field(default=None, description="Content after the table of order lines for A4-based parcel slips.")
    additional_content_align: Optional[StrictInt] = Field(default=None, description="Alignment of additional_content. Possible values: <code>center</code>, <code>right</code>, <code>left</code>")
    barcode_content: Optional[StrictStr] = Field(default=None, description="Content of the barcode")
    header_content: Optional[StrictStr] = Field(default=None, description="Content of the slip header")
    top_left_content_header: Optional[StrictStr] = Field(default=None, description="Header of the top left corner")
    top_right_content_header: Optional[StrictStr] = Field(default=None, description="Header of the top right corner")
    top_left_content: Optional[StrictStr] = Field(default=None, description="Content of the top left corner")
    top_right_content: Optional[StrictStr] = Field(default=None, description="Content of the top right corner")
    footer_content: Optional[StrictStr] = Field(default=None, description="Content of the footer")
    slip_template_columns: Optional[StrictStr] = Field(default=None, description="Array of columns. Column objects contains: <code>name</code><code>content</code>, <code>text_alignment</code>(right, left, center), <code>width</code> (in percentage)")
    table_color: Optional[StrictStr] = Field(default=None, description="HEX color including #")
    table_text_color: Optional[StrictStr] = Field(default=None, description="HEX color including #")
    updated_at: Optional[StrictStr] = Field(default=None, description="The time when resource was last updated or when it was created if it was never updated")
    created_at: Optional[StrictStr] = Field(default=None, description="The time when the resource was created")
    sort_key: Optional[StrictStr] = Field(default=None, description="The key to sort the order-lines by")
    returns_only: Optional[StrictBool] = None
    disable_inline_formatting: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["name", "slip_size", "additional_content", "additional_content_align", "barcode_content", "header_content", "top_left_content_header", "top_right_content_header", "top_left_content", "top_right_content", "footer_content", "slip_template_columns", "table_color", "table_text_color", "updated_at", "created_at", "sort_key", "returns_only", "disable_inline_formatting"]

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
        """Create an instance of SlipTemplates from a JSON string"""
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
                "updated_at",
                "created_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SlipTemplates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "slip_size": obj.get("slip_size"),
            "additional_content": obj.get("additional_content"),
            "additional_content_align": obj.get("additional_content_align"),
            "barcode_content": obj.get("barcode_content"),
            "header_content": obj.get("header_content"),
            "top_left_content_header": obj.get("top_left_content_header"),
            "top_right_content_header": obj.get("top_right_content_header"),
            "top_left_content": obj.get("top_left_content"),
            "top_right_content": obj.get("top_right_content"),
            "footer_content": obj.get("footer_content"),
            "slip_template_columns": obj.get("slip_template_columns"),
            "table_color": obj.get("table_color"),
            "table_text_color": obj.get("table_text_color"),
            "updated_at": obj.get("updated_at"),
            "created_at": obj.get("created_at"),
            "sort_key": obj.get("sort_key"),
            "returns_only": obj.get("returns_only"),
            "disable_inline_formatting": obj.get("disable_inline_formatting")
        })
        return _obj



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

class CsvMappings(BaseModel):
    """
    CsvMappings
    """ # noqa: E501
    separator: Optional[StrictStr] = Field(default=None, description="The seperator in the file. Normally ';' or ','")
    target_class: Optional[StrictStr] = Field(default=None, description="Must be one of the models <code>Order</code> or <code>Shipment</code>")
    grouped_by: Optional[StrictInt] = Field(default=None, description="Must be the index of the Order ID")
    grouped_path: Optional[StrictStr] = Field(default=None, description="The sub-model which you are grouping. For order: order_lines_attributes")
    includes_header: Optional[StrictBool] = Field(default=None, description="Determines if there is an ignorable header line in the file")
    lines_as_package: Optional[StrictBool] = None
    recreate_order_lines: Optional[StrictBool] = None
    separate_order_line_mapping: Optional[StrictBool] = None
    name: Optional[StrictStr] = Field(default=None, description="Name of the configuration")
    example_input: Optional[StrictStr] = Field(default=None, description="Example input to make it easier to create the mapping in the UI.")
    line_example_input: Optional[StrictStr] = None
    rules: Optional[List[StrictStr]] = Field(default=None, description="Array of flattened resources of the type CSV Rule")
    shipment_export_format: Optional[StrictStr] = None
    order_export_format: Optional[StrictStr] = None
    create_shipment_automatically: Optional[StrictBool] = None
    force_async: Optional[StrictBool] = None
    concat_paths: Optional[StrictBool] = None
    split_large_records: Optional[StrictBool] = None
    export_file_extension: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["separator", "target_class", "grouped_by", "grouped_path", "includes_header", "lines_as_package", "recreate_order_lines", "separate_order_line_mapping", "name", "example_input", "line_example_input", "rules", "shipment_export_format", "order_export_format", "create_shipment_automatically", "force_async", "concat_paths", "split_large_records", "export_file_extension"]

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
        """Create an instance of CsvMappings from a JSON string"""
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
        """Create an instance of CsvMappings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "separator": obj.get("separator"),
            "target_class": obj.get("target_class"),
            "grouped_by": obj.get("grouped_by"),
            "grouped_path": obj.get("grouped_path"),
            "includes_header": obj.get("includes_header"),
            "lines_as_package": obj.get("lines_as_package"),
            "recreate_order_lines": obj.get("recreate_order_lines"),
            "separate_order_line_mapping": obj.get("separate_order_line_mapping"),
            "name": obj.get("name"),
            "example_input": obj.get("example_input"),
            "line_example_input": obj.get("line_example_input"),
            "rules": obj.get("rules"),
            "shipment_export_format": obj.get("shipment_export_format"),
            "order_export_format": obj.get("order_export_format"),
            "create_shipment_automatically": obj.get("create_shipment_automatically"),
            "force_async": obj.get("force_async"),
            "concat_paths": obj.get("concat_paths"),
            "split_large_records": obj.get("split_large_records"),
            "export_file_extension": obj.get("export_file_extension")
        })
        return _obj


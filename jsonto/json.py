from __future__ import annotations
from typing import Union
from jsonto.settings import XML_CONFIG
import lxml.etree as ET
# import json


TJsonXMLConfig = dict[str, Union[dict[str, str], list[str], 'TJsonXMLConfig']]


def to_xml(json_config: TJsonXMLConfig, as_string=True) -> Union[str, ET._Element]:
    if len(json_config.keys()) != 1:
        raise Exception("Parameter `json_config` must be contained only one top tag (root)")
    top_tag = list(json_config.keys())[0]
    assert isinstance(top_tag, str)

    def to_xml_back(top_tag, json_config) -> ET._Element:
        result_xml = ET.Element(top_tag)
        result_xml.attrib.update(json_config.pop("ATTRIBUTE_KEY", {}))
        text = "\n".join(json_config.pop("TEXT_KEY", []))
        if text:
            result_xml.text = text
        tail = "\n".join(json_config.pop("TAIL_KEY", []))
        if tail:
            result_xml.tail = tail
        comment = "\n".join(json_config.pop("COMMENT_KEY", []))
        if comment:
            comment = ET.Comment(comment)
            result_xml.insert(0, comment)
        return result_xml
    
    result_xml = to_xml_back(top_tag, json_config[top_tag])
    if as_string:
        result_xml = ET.tostring(result_xml, pretty_print=True).decode()

    print(result_xml)

    return result_xml



def from_string(json_string: str) -> dict:
    ...


def from_file(filepath: str) -> dict:
    ...


def to_string(json_config: dict) -> str:
    ...


def to_file(json_config: dict, filepath: str) -> None:
    ...

from typing import Union
from jsonto.settings import XML_CONFIG

import lxml.etree as ET


def to_json(xml_config: Union[str, ET._Element]) -> dict:
    if isinstance(xml_config, str):
        xml_config = ET.fromstring(xml_config)
    assert isinstance(xml_config, ET._Element)

    def to_json_back(tag: ET._Element) -> dict:
        json_result = {
            XML_CONFIG.get("COMMENT_KEY"): [],
            XML_CONFIG.get("TEXT_KEY"): tag.text.split("\n") if tag.text else [],
            XML_CONFIG.get("TAIL_KEY"): tag.tail.split("\n") if tag.tail else [],
            XML_CONFIG.get("ATTRIBUTE_KEY"): tag.attrib,
        }
        for subtag in tag.iter():
            json_result[subtag.tag] = to_json_back(subtag)
        return json_result

    json_result = {xml_config.tag: to_json_back(xml_config)}
    return json_result


def to_file(xml_config: Union[str, ET._Element], filepath: str) -> None:
    ...


def from_file(filepath: str, as_string=True) -> Union[str, ET._Element]:
    ...

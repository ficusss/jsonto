from typing import Union
from lxml.etree import ElementBase
import lxml.etree as ET
# import json


def to_xml(json: dict, as_string=True) -> Union[str, ElementBase]:
    ...


def from_string(json_string: str) -> dict:
    ...


def from_file(filepath: str) -> dict:
    ...


def to_string(json_config: dict) -> str:
    ...


def to_file(json_config: dict, filepath: str) -> None:
    ...

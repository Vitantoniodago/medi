# coding: utf-8

"""
    MediHome-CloudServer

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOItemPrestazioni(BaseModel):
    """
    
    """ # noqa: E501
    id_item_prestazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier item prestazione.", alias="IDItemPrestazione")
    id_prestazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier prestazione.", alias="IDPrestazione")
    time_start: Optional[datetime] = Field(default=None, description="Richiedi o modifica time start.", alias="TimeStart")
    time_end: Optional[datetime] = Field(default=None, description="Richiedi o modifica time end.", alias="TimeEnd")
    lunedi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica lunedi.", alias="Lunedi")
    martedi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica martedi.", alias="Martedi")
    mercoledi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica mercoledi.", alias="Mercoledi")
    giovedi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica giovedi.", alias="Giovedi")
    venerdi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica venerdi.", alias="Venerdi")
    sabato: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica sabato.", alias="Sabato")
    domenica: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica domenica.", alias="Domenica")
    __properties: ClassVar[List[str]] = ["IDItemPrestazione", "IDPrestazione", "TimeStart", "TimeEnd", "Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato", "Domenica"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
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
        """Create an instance of DTOItemPrestazioni from a JSON string"""
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
        """Create an instance of DTOItemPrestazioni from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IDItemPrestazione": obj.get("IDItemPrestazione"),
            "IDPrestazione": obj.get("IDPrestazione"),
            "TimeStart": obj.get("TimeStart"),
            "TimeEnd": obj.get("TimeEnd"),
            "Lunedi": obj.get("Lunedi"),
            "Martedi": obj.get("Martedi"),
            "Mercoledi": obj.get("Mercoledi"),
            "Giovedi": obj.get("Giovedi"),
            "Venerdi": obj.get("Venerdi"),
            "Sabato": obj.get("Sabato"),
            "Domenica": obj.get("Domenica")
        })
        return _obj



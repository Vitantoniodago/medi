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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIPrestazione(BaseModel):
    """
    
    """ # noqa: E501
    id_prestazione_pai: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier prestazione pai.", alias="IDPrestazionePAI")
    id_prestazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier prestazione.", alias="IDPrestazione")
    prestazione: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica prestazione.", alias="Prestazione")
    descrizione: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica descrizione.", alias="Descrizione")
    durata: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Richiedi o modifica durata.", alias="Durata")
    __properties: ClassVar[List[str]] = ["IDPrestazionePAI", "IDPrestazione", "Prestazione", "Descrizione", "Durata"]

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
        """Create an instance of DTOAPIPrestazione from a JSON string"""
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
        """Create an instance of DTOAPIPrestazione from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IDPrestazionePAI": obj.get("IDPrestazionePAI"),
            "IDPrestazione": obj.get("IDPrestazione"),
            "Prestazione": obj.get("Prestazione"),
            "Descrizione": obj.get("Descrizione"),
            "Durata": obj.get("Durata")
        })
        return _obj



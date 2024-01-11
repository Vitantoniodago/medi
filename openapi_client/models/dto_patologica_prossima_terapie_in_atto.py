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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOPatologicaProssimaTerapieInAtto(BaseModel):
    """
    
    """ # noqa: E501
    nessun_farmaco: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [nessun farmaco].", alias="NessunFarmaco")
    id_farmaco: Optional[StrictInt] = Field(default=None, alias="IDFarmaco")
    quantita: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica quantita.", alias="Quantita")
    frequenza_assunzione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica frequenza assunzione.", alias="FrequenzaAssunzione")
    note: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica note.", alias="Note")
    id_patologica_prossima_terapie_in_atto: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier patologica prossima terapie in atto.", alias="IDPatologicaProssimaTerapieInAtto")
    id_assistito: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier assistito.", alias="IDAssistito")
    id_visita: Optional[StrictInt] = Field(default=None, alias="IDVisita")
    __properties: ClassVar[List[str]] = ["NessunFarmaco", "IDFarmaco", "Quantita", "FrequenzaAssunzione", "Note", "IDPatologicaProssimaTerapieInAtto", "IDAssistito", "IDVisita"]

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
        """Create an instance of DTOPatologicaProssimaTerapieInAtto from a JSON string"""
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
        """Create an instance of DTOPatologicaProssimaTerapieInAtto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NessunFarmaco": obj.get("NessunFarmaco"),
            "IDFarmaco": obj.get("IDFarmaco"),
            "Quantita": obj.get("Quantita"),
            "FrequenzaAssunzione": obj.get("FrequenzaAssunzione"),
            "Note": obj.get("Note"),
            "IDPatologicaProssimaTerapieInAtto": obj.get("IDPatologicaProssimaTerapieInAtto"),
            "IDAssistito": obj.get("IDAssistito"),
            "IDVisita": obj.get("IDVisita")
        })
        return _obj


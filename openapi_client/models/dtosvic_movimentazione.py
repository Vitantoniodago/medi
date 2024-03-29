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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOSVICMovimentazione(BaseModel):
    """
    DTOSVICMovimentazione
    """ # noqa: E501
    tipo_operazione: Optional[StrictStr] = Field(default=None, alias="TIPO_OPERAZIONE")
    data_operazione: Optional[datetime] = Field(default=None, alias="DATA_OPERAZIONE")
    numero_operazione: Optional[StrictInt] = Field(default=None, alias="NUMERO_OPERAZIONE")
    conto: Optional[StrictInt] = Field(default=None, alias="CONTO")
    sottoconto: Optional[StrictInt] = Field(default=None, alias="SOTTOCONTO")
    dare_avere: Optional[StrictStr] = Field(default=None, alias="DARE_AVERE")
    importo: Optional[StrictInt] = Field(default=None, alias="IMPORTO")
    missione: Optional[StrictInt] = Field(default=None, alias="MISSIONE")
    descrizione_missione: Optional[StrictStr] = Field(default=None, alias="DESCRIZIONE_MISSIONE")
    programma: Optional[StrictInt] = Field(default=None, alias="PROGRAMMA")
    descrizione_programma: Optional[StrictStr] = Field(default=None, alias="DESCRIZIONE_PROGRAMMA")
    titolo: Optional[StrictInt] = Field(default=None, alias="TITOLO")
    descrizione_titolo: Optional[StrictStr] = Field(default=None, alias="DESCRIZIONE_TITOLO")
    responsabile: Optional[StrictStr] = Field(default=None, alias="RESPONSABILE")
    contro_di_costo_ricavo: Optional[StrictStr] = Field(default=None, alias="CONTRO_DI_COSTO_RICAVO")
    __properties: ClassVar[List[str]] = ["TIPO_OPERAZIONE", "DATA_OPERAZIONE", "NUMERO_OPERAZIONE", "CONTO", "SOTTOCONTO", "DARE_AVERE", "IMPORTO", "MISSIONE", "DESCRIZIONE_MISSIONE", "PROGRAMMA", "DESCRIZIONE_PROGRAMMA", "TITOLO", "DESCRIZIONE_TITOLO", "RESPONSABILE", "CONTRO_DI_COSTO_RICAVO"]

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
        """Create an instance of DTOSVICMovimentazione from a JSON string"""
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
        """Create an instance of DTOSVICMovimentazione from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TIPO_OPERAZIONE": obj.get("TIPO_OPERAZIONE"),
            "DATA_OPERAZIONE": obj.get("DATA_OPERAZIONE"),
            "NUMERO_OPERAZIONE": obj.get("NUMERO_OPERAZIONE"),
            "CONTO": obj.get("CONTO"),
            "SOTTOCONTO": obj.get("SOTTOCONTO"),
            "DARE_AVERE": obj.get("DARE_AVERE"),
            "IMPORTO": obj.get("IMPORTO"),
            "MISSIONE": obj.get("MISSIONE"),
            "DESCRIZIONE_MISSIONE": obj.get("DESCRIZIONE_MISSIONE"),
            "PROGRAMMA": obj.get("PROGRAMMA"),
            "DESCRIZIONE_PROGRAMMA": obj.get("DESCRIZIONE_PROGRAMMA"),
            "TITOLO": obj.get("TITOLO"),
            "DESCRIZIONE_TITOLO": obj.get("DESCRIZIONE_TITOLO"),
            "RESPONSABILE": obj.get("RESPONSABILE"),
            "CONTRO_DI_COSTO_RICAVO": obj.get("CONTRO_DI_COSTO_RICAVO")
        })
        return _obj



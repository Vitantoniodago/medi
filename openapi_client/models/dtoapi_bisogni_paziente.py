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
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.dto_bisogni_paziente_alimentazione import DTOBisogniPazienteAlimentazione
from openapi_client.models.dto_bisogni_paziente_comunicazione import DTOBisogniPazienteComunicazione
from openapi_client.models.dto_bisogni_paziente_eliminazione import DTOBisogniPazienteEliminazione
from openapi_client.models.dto_bisogni_paziente_igiene import DTOBisogniPazienteIgiene
from openapi_client.models.dto_bisogni_paziente_mobilizzazione import DTOBisogniPazienteMobilizzazione
from openapi_client.models.dto_bisogni_paziente_sicurezza_sonno import DTOBisogniPazienteSicurezzaSonno
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIBisogniPaziente(BaseModel):
    """
    
    """ # noqa: E501
    bisogni_paziente_aliemntazione: Optional[List[DTOBisogniPazienteAlimentazione]] = Field(default=None, alias="BisogniPazienteAliemntazione")
    bisogni_paziente_comunicazione: Optional[List[DTOBisogniPazienteComunicazione]] = Field(default=None, alias="BisogniPazienteComunicazione")
    bisogni_paziente_eliminazione: Optional[List[DTOBisogniPazienteEliminazione]] = Field(default=None, alias="BisogniPazienteEliminazione")
    bisogni_paziente_igiene: Optional[List[DTOBisogniPazienteIgiene]] = Field(default=None, alias="BisogniPazienteIgiene")
    bisogni_paziente_mobilizzazione: Optional[List[DTOBisogniPazienteMobilizzazione]] = Field(default=None, alias="BisogniPazienteMobilizzazione")
    bisogni_paziente_sicurezza_sonno: Optional[List[DTOBisogniPazienteSicurezzaSonno]] = Field(default=None, alias="BisogniPazienteSicurezzaSonno")
    __properties: ClassVar[List[str]] = ["BisogniPazienteAliemntazione", "BisogniPazienteComunicazione", "BisogniPazienteEliminazione", "BisogniPazienteIgiene", "BisogniPazienteMobilizzazione", "BisogniPazienteSicurezzaSonno"]

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
        """Create an instance of DTOAPIBisogniPaziente from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_aliemntazione (list)
        _items = []
        if self.bisogni_paziente_aliemntazione:
            for _item in self.bisogni_paziente_aliemntazione:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteAliemntazione'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_comunicazione (list)
        _items = []
        if self.bisogni_paziente_comunicazione:
            for _item in self.bisogni_paziente_comunicazione:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteComunicazione'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_eliminazione (list)
        _items = []
        if self.bisogni_paziente_eliminazione:
            for _item in self.bisogni_paziente_eliminazione:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteEliminazione'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_igiene (list)
        _items = []
        if self.bisogni_paziente_igiene:
            for _item in self.bisogni_paziente_igiene:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteIgiene'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_mobilizzazione (list)
        _items = []
        if self.bisogni_paziente_mobilizzazione:
            for _item in self.bisogni_paziente_mobilizzazione:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteMobilizzazione'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bisogni_paziente_sicurezza_sonno (list)
        _items = []
        if self.bisogni_paziente_sicurezza_sonno:
            for _item in self.bisogni_paziente_sicurezza_sonno:
                if _item:
                    _items.append(_item.to_dict())
            _dict['BisogniPazienteSicurezzaSonno'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOAPIBisogniPaziente from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "BisogniPazienteAliemntazione": [DTOBisogniPazienteAlimentazione.from_dict(_item) for _item in obj.get("BisogniPazienteAliemntazione")] if obj.get("BisogniPazienteAliemntazione") is not None else None,
            "BisogniPazienteComunicazione": [DTOBisogniPazienteComunicazione.from_dict(_item) for _item in obj.get("BisogniPazienteComunicazione")] if obj.get("BisogniPazienteComunicazione") is not None else None,
            "BisogniPazienteEliminazione": [DTOBisogniPazienteEliminazione.from_dict(_item) for _item in obj.get("BisogniPazienteEliminazione")] if obj.get("BisogniPazienteEliminazione") is not None else None,
            "BisogniPazienteIgiene": [DTOBisogniPazienteIgiene.from_dict(_item) for _item in obj.get("BisogniPazienteIgiene")] if obj.get("BisogniPazienteIgiene") is not None else None,
            "BisogniPazienteMobilizzazione": [DTOBisogniPazienteMobilizzazione.from_dict(_item) for _item in obj.get("BisogniPazienteMobilizzazione")] if obj.get("BisogniPazienteMobilizzazione") is not None else None,
            "BisogniPazienteSicurezzaSonno": [DTOBisogniPazienteSicurezzaSonno.from_dict(_item) for _item in obj.get("BisogniPazienteSicurezzaSonno")] if obj.get("BisogniPazienteSicurezzaSonno") is not None else None
        })
        return _obj


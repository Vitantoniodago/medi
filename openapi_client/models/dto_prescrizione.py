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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.dto_item_prescrizione import DTOItemPrescrizione
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOPrescrizione(BaseModel):
    """
    
    """ # noqa: E501
    id_farmaco: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier farmaco.", alias="IDFarmaco")
    farmaco: Optional[StrictStr] = Field(default=None, alias="Farmaco")
    id_unita: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier unita.", alias="IDUnita")
    id_modalita_somministrazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier modalita somministrazione.", alias="IDModalitaSomministrazione")
    id_via_somministrazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier via somministrazione.", alias="IDViaSomministrazione")
    inizio_terapia: Optional[datetime] = Field(default=None, description="Richiedi o modifica inizio terapia.", alias="InizioTerapia")
    fine_terapia: Optional[datetime] = Field(default=None, description="Richiedi o modifica fine terapia.", alias="FineTerapia")
    durata_terapia: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica durata terapia.", alias="DurataTerapia")
    note: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica note.", alias="Note")
    id_assistito: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier assistito.", alias="IDAssistito")
    id_prescrizione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier prescrizione.", alias="IDPrescrizione")
    id_modalita_ora_somministrazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier modalita ora somministrazione.", alias="IDModalitaOraSomministrazione")
    modelli: Optional[List[DTOItemPrescrizione]] = Field(default=None, description="Richiedi o modifica modelli.", alias="Modelli")
    somministrazione_colazione: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica somministrazione colazione.", alias="SomministrazioneColazione")
    somministrato: Optional[StrictBool] = Field(default=None, alias="Somministrato")
    ora_colazione: Optional[datetime] = Field(default=None, description="Richiedi o modifica ora colazione.", alias="OraColazione")
    somministrazione_pranzo: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica somministrazione pranzo.", alias="SomministrazionePranzo")
    ora_pranzo: Optional[datetime] = Field(default=None, description="Richiedi o modifica ora pranzo.", alias="OraPranzo")
    somministrazione_cena: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica somministrazione cena.", alias="SomministrazioneCena")
    ora_cena: Optional[datetime] = Field(default=None, description="Richiedi o modifica ora cena.", alias="OraCena")
    ora_inizio: Optional[datetime] = Field(default=None, description="Richiedi o modifica ora inizio.", alias="OraInizio")
    ora_fine: Optional[datetime] = Field(default=None, description="Richiedi o modifica ora fine.", alias="OraFine")
    id_visita: Optional[StrictInt] = Field(default=None, alias="IDVisita")
    assistito: Optional[DTOAPIAssistito] = Field(default=None, alias="Assistito")
    __properties: ClassVar[List[str]] = ["IDFarmaco", "Farmaco", "IDUnita", "IDModalitaSomministrazione", "IDViaSomministrazione", "InizioTerapia", "FineTerapia", "DurataTerapia", "Note", "IDAssistito", "IDPrescrizione", "IDModalitaOraSomministrazione", "Modelli", "SomministrazioneColazione", "Somministrato", "OraColazione", "SomministrazionePranzo", "OraPranzo", "SomministrazioneCena", "OraCena", "OraInizio", "OraFine", "IDVisita", "Assistito"]

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
        """Create an instance of DTOPrescrizione from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in modelli (list)
        _items = []
        if self.modelli:
            for _item in self.modelli:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Modelli'] = _items
        # override the default output from pydantic by calling `to_dict()` of assistito
        if self.assistito:
            _dict['Assistito'] = self.assistito.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOPrescrizione from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IDFarmaco": obj.get("IDFarmaco"),
            "Farmaco": obj.get("Farmaco"),
            "IDUnita": obj.get("IDUnita"),
            "IDModalitaSomministrazione": obj.get("IDModalitaSomministrazione"),
            "IDViaSomministrazione": obj.get("IDViaSomministrazione"),
            "InizioTerapia": obj.get("InizioTerapia"),
            "FineTerapia": obj.get("FineTerapia"),
            "DurataTerapia": obj.get("DurataTerapia"),
            "Note": obj.get("Note"),
            "IDAssistito": obj.get("IDAssistito"),
            "IDPrescrizione": obj.get("IDPrescrizione"),
            "IDModalitaOraSomministrazione": obj.get("IDModalitaOraSomministrazione"),
            "Modelli": [DTOItemPrescrizione.from_dict(_item) for _item in obj.get("Modelli")] if obj.get("Modelli") is not None else None,
            "SomministrazioneColazione": obj.get("SomministrazioneColazione"),
            "Somministrato": obj.get("Somministrato"),
            "OraColazione": obj.get("OraColazione"),
            "SomministrazionePranzo": obj.get("SomministrazionePranzo"),
            "OraPranzo": obj.get("OraPranzo"),
            "SomministrazioneCena": obj.get("SomministrazioneCena"),
            "OraCena": obj.get("OraCena"),
            "OraInizio": obj.get("OraInizio"),
            "OraFine": obj.get("OraFine"),
            "IDVisita": obj.get("IDVisita"),
            "Assistito": DTOAPIAssistito.from_dict(obj.get("Assistito")) if obj.get("Assistito") is not None else None
        })
        return _obj

from openapi_client.models.dtoapi_assistito import DTOAPIAssistito
# TODO: Rewrite to not use raise_errors
DTOPrescrizione.model_rebuild(raise_errors=False)


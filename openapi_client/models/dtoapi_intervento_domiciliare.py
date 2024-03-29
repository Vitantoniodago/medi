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
from openapi_client.models.dtoapi_attivita_esterna import DTOAPIAttivitaEsterna
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIInterventoDomiciliare(BaseModel):
    """
    
    """ # noqa: E501
    codice_prestazione: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica codice prestazione.", alias="CodicePrestazione")
    id_ordine_lavoro: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier ordine lavoro.", alias="IDOrdineLavoro")
    data_inizio: Optional[datetime] = Field(default=None, description="Richiedi o modifica data inizio.", alias="DataInizio")
    data_fine: Optional[datetime] = Field(default=None, description="Richiedi o modifica data fine.", alias="DataFine")
    medi_box: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica medi box.", alias="MediBox")
    room: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica room.", alias="Room")
    id_operatore: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier operatore.", alias="IDOperatore")
    attivato: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOAPIInterventoDomiciliare} is attivato.", alias="Attivato")
    attivita_intervento: Optional[DTOAPIAttivitaEsterna] = Field(default=None, alias="AttivitaIntervento")
    guid_assistito: Optional[StrictStr] = Field(default=None, alias="GuidAssistito")
    __properties: ClassVar[List[str]] = ["CodicePrestazione", "IDOrdineLavoro", "DataInizio", "DataFine", "MediBox", "Room", "IDOperatore", "Attivato", "AttivitaIntervento", "GuidAssistito"]

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
        """Create an instance of DTOAPIInterventoDomiciliare from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attivita_intervento
        if self.attivita_intervento:
            _dict['AttivitaIntervento'] = self.attivita_intervento.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOAPIInterventoDomiciliare from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CodicePrestazione": obj.get("CodicePrestazione"),
            "IDOrdineLavoro": obj.get("IDOrdineLavoro"),
            "DataInizio": obj.get("DataInizio"),
            "DataFine": obj.get("DataFine"),
            "MediBox": obj.get("MediBox"),
            "Room": obj.get("Room"),
            "IDOperatore": obj.get("IDOperatore"),
            "Attivato": obj.get("Attivato"),
            "AttivitaIntervento": DTOAPIAttivitaEsterna.from_dict(obj.get("AttivitaIntervento")) if obj.get("AttivitaIntervento") is not None else None,
            "GuidAssistito": obj.get("GuidAssistito")
        })
        return _obj



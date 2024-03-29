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
from openapi_client.models.dtoapi_anamnesi import DTOAPIAnamnesi
from openapi_client.models.dtoapi_bisogni_paziente import DTOAPIBisogniPaziente
from openapi_client.models.dtoapi_consensi import DTOAPIConsensi
from openapi_client.models.dtoapi_diario_clinico import DTOAPIDiarioClinico
from openapi_client.models.dtoapi_esami_obiettivo import DTOAPIEsamiObiettivo
from openapi_client.models.dtoapi_esami_strumentale import DTOAPIEsamiStrumentale
from openapi_client.models.dtoapi_note import DTOAPINote
from openapi_client.models.dtoapi_prestazioni_fisioterapiche import DTOAPIPrestazioniFisioterapiche
from openapi_client.models.dtoapi_session import DTOAPISession
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIAssistito(BaseModel):
    """
    
    """ # noqa: E501
    guid_assistito: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica unique identifier assistito.", alias="GuidAssistito")
    id_assistito: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier assistito.", alias="IDAssistito")
    nome: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica nome.", alias="Nome")
    cognome: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica cognome.", alias="Cognome")
    codice_fiscale: Optional[StrictStr] = Field(default=None, alias="CodiceFiscale")
    data_nascita: Optional[datetime] = Field(default=None, alias="DataNascita")
    sesso: Optional[StrictInt] = Field(default=None, alias="Sesso")
    comune: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica comune.", alias="Comune")
    indirizzo: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica indirizzo.", alias="Indirizzo")
    cap: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica cap.", alias="CAP")
    anamnesi: Optional[DTOAPIAnamnesi] = Field(default=None, alias="Anamnesi")
    esami_obiettivo: Optional[DTOAPIEsamiObiettivo] = Field(default=None, alias="EsamiObiettivo")
    esami_strumentali: Optional[DTOAPIEsamiStrumentale] = Field(default=None, alias="EsamiStrumentali")
    prescrizioni: Optional[DTOAPIPrescrizioni] = Field(default=None, alias="Prescrizioni")
    somministrazioni: Optional[DTOAPISomministrazioni] = Field(default=None, alias="Somministrazioni")
    prestazioni_fisioterapiche: Optional[DTOAPIPrestazioniFisioterapiche] = Field(default=None, alias="PrestazioniFisioterapiche")
    diari_clinici: Optional[DTOAPIDiarioClinico] = Field(default=None, alias="DiariClinici")
    bisogni_paziente: Optional[DTOAPIBisogniPaziente] = Field(default=None, alias="BisogniPaziente")
    elenco_note: Optional[DTOAPINote] = Field(default=None, alias="ElencoNote")
    consensi: Optional[DTOAPIConsensi] = Field(default=None, alias="Consensi")
    sessione: Optional[DTOAPISession] = Field(default=None, alias="Sessione")
    __properties: ClassVar[List[str]] = ["GuidAssistito", "IDAssistito", "Nome", "Cognome", "CodiceFiscale", "DataNascita", "Sesso", "Comune", "Indirizzo", "CAP", "Anamnesi", "EsamiObiettivo", "EsamiStrumentali", "Prescrizioni", "Somministrazioni", "PrestazioniFisioterapiche", "DiariClinici", "BisogniPaziente", "ElencoNote", "Consensi", "Sessione"]

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
        """Create an instance of DTOAPIAssistito from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anamnesi
        if self.anamnesi:
            _dict['Anamnesi'] = self.anamnesi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of esami_obiettivo
        if self.esami_obiettivo:
            _dict['EsamiObiettivo'] = self.esami_obiettivo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of esami_strumentali
        if self.esami_strumentali:
            _dict['EsamiStrumentali'] = self.esami_strumentali.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prescrizioni
        if self.prescrizioni:
            _dict['Prescrizioni'] = self.prescrizioni.to_dict()
        # override the default output from pydantic by calling `to_dict()` of somministrazioni
        if self.somministrazioni:
            _dict['Somministrazioni'] = self.somministrazioni.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prestazioni_fisioterapiche
        if self.prestazioni_fisioterapiche:
            _dict['PrestazioniFisioterapiche'] = self.prestazioni_fisioterapiche.to_dict()
        # override the default output from pydantic by calling `to_dict()` of diari_clinici
        if self.diari_clinici:
            _dict['DiariClinici'] = self.diari_clinici.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bisogni_paziente
        if self.bisogni_paziente:
            _dict['BisogniPaziente'] = self.bisogni_paziente.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elenco_note
        if self.elenco_note:
            _dict['ElencoNote'] = self.elenco_note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consensi
        if self.consensi:
            _dict['Consensi'] = self.consensi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sessione
        if self.sessione:
            _dict['Sessione'] = self.sessione.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOAPIAssistito from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "GuidAssistito": obj.get("GuidAssistito"),
            "IDAssistito": obj.get("IDAssistito"),
            "Nome": obj.get("Nome"),
            "Cognome": obj.get("Cognome"),
            "CodiceFiscale": obj.get("CodiceFiscale"),
            "DataNascita": obj.get("DataNascita"),
            "Sesso": obj.get("Sesso"),
            "Comune": obj.get("Comune"),
            "Indirizzo": obj.get("Indirizzo"),
            "CAP": obj.get("CAP"),
            "Anamnesi": DTOAPIAnamnesi.from_dict(obj.get("Anamnesi")) if obj.get("Anamnesi") is not None else None,
            "EsamiObiettivo": DTOAPIEsamiObiettivo.from_dict(obj.get("EsamiObiettivo")) if obj.get("EsamiObiettivo") is not None else None,
            "EsamiStrumentali": DTOAPIEsamiStrumentale.from_dict(obj.get("EsamiStrumentali")) if obj.get("EsamiStrumentali") is not None else None,
            "Prescrizioni": DTOAPIPrescrizioni.from_dict(obj.get("Prescrizioni")) if obj.get("Prescrizioni") is not None else None,
            "Somministrazioni": DTOAPISomministrazioni.from_dict(obj.get("Somministrazioni")) if obj.get("Somministrazioni") is not None else None,
            "PrestazioniFisioterapiche": DTOAPIPrestazioniFisioterapiche.from_dict(obj.get("PrestazioniFisioterapiche")) if obj.get("PrestazioniFisioterapiche") is not None else None,
            "DiariClinici": DTOAPIDiarioClinico.from_dict(obj.get("DiariClinici")) if obj.get("DiariClinici") is not None else None,
            "BisogniPaziente": DTOAPIBisogniPaziente.from_dict(obj.get("BisogniPaziente")) if obj.get("BisogniPaziente") is not None else None,
            "ElencoNote": DTOAPINote.from_dict(obj.get("ElencoNote")) if obj.get("ElencoNote") is not None else None,
            "Consensi": DTOAPIConsensi.from_dict(obj.get("Consensi")) if obj.get("Consensi") is not None else None,
            "Sessione": DTOAPISession.from_dict(obj.get("Sessione")) if obj.get("Sessione") is not None else None
        })
        return _obj

from openapi_client.models.dtoapi_prescrizioni import DTOAPIPrescrizioni
from openapi_client.models.dtoapi_somministrazioni import DTOAPISomministrazioni
# TODO: Rewrite to not use raise_errors
DTOAPIAssistito.model_rebuild(raise_errors=False)


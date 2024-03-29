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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOSVICDebitorePOST(BaseModel):
    """
    DTOSVICDebitorePOST
    """ # noqa: E501
    codice_debitore: Optional[StrictStr] = Field(default=None, alias="CodiceDebitore")
    tipo_anagrafica: Optional[StrictStr] = Field(default=None, alias="TipoAnagrafica")
    ragione_sociale: Optional[StrictStr] = Field(default=None, alias="RagioneSociale")
    cognome: Optional[StrictStr] = Field(default=None, alias="Cognome")
    nome: Optional[StrictStr] = Field(default=None, alias="Nome")
    sesso: Optional[StrictStr] = Field(default=None, alias="Sesso")
    data_nascita: Optional[datetime] = Field(default=None, alias="DataNascita")
    localit_nascita: Optional[StrictStr] = Field(default=None, alias="LocalitàNascita")
    provincia_nascita: Optional[StrictStr] = Field(default=None, alias="ProvinciaNascita")
    partita_iva: Optional[StrictStr] = Field(default=None, alias="PartitaIVA")
    codice_fiscale: Optional[StrictStr] = Field(default=None, alias="CodiceFiscale")
    indirizzo: Optional[StrictStr] = Field(default=None, alias="Indirizzo")
    localit: Optional[StrictStr] = Field(default=None, alias="Località")
    cap: Optional[StrictStr] = Field(default=None, alias="CAP")
    provincia: Optional[StrictStr] = Field(default=None, alias="Provincia")
    email: Optional[StrictStr] = Field(default=None, alias="Email")
    telefono: Optional[StrictStr] = Field(default=None, alias="Telefono")
    __properties: ClassVar[List[str]] = ["CodiceDebitore", "TipoAnagrafica", "RagioneSociale", "Cognome", "Nome", "Sesso", "DataNascita", "LocalitàNascita", "ProvinciaNascita", "PartitaIVA", "CodiceFiscale", "Indirizzo", "Località", "CAP", "Provincia", "Email", "Telefono"]

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
        """Create an instance of DTOSVICDebitorePOST from a JSON string"""
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
        """Create an instance of DTOSVICDebitorePOST from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CodiceDebitore": obj.get("CodiceDebitore"),
            "TipoAnagrafica": obj.get("TipoAnagrafica"),
            "RagioneSociale": obj.get("RagioneSociale"),
            "Cognome": obj.get("Cognome"),
            "Nome": obj.get("Nome"),
            "Sesso": obj.get("Sesso"),
            "DataNascita": obj.get("DataNascita"),
            "LocalitàNascita": obj.get("LocalitàNascita"),
            "ProvinciaNascita": obj.get("ProvinciaNascita"),
            "PartitaIVA": obj.get("PartitaIVA"),
            "CodiceFiscale": obj.get("CodiceFiscale"),
            "Indirizzo": obj.get("Indirizzo"),
            "Località": obj.get("Località"),
            "CAP": obj.get("CAP"),
            "Provincia": obj.get("Provincia"),
            "Email": obj.get("Email"),
            "Telefono": obj.get("Telefono")
        })
        return _obj



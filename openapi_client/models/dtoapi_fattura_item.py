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
from openapi_client.models.dtoapi_categoria import DTOAPICategoria
from openapi_client.models.dtoapi_prodotto import DTOAPIProdotto
from openapi_client.models.dtoapi_unita_misura import DTOAPIUnitaMisura
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIFatturaItem(BaseModel):
    """
    DTOAPIFatturaItem
    """ # noqa: E501
    prodotto: Optional[DTOAPIProdotto] = Field(default=None, alias="Prodotto")
    quantit_singolo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="QuantitàSingolo")
    unita_qnt_singolo: Optional[DTOAPIUnitaMisura] = Field(default=None, alias="UnitaQntSingolo")
    tipologia_iva: Optional[DTOAPICategoria] = Field(default=None, alias="TipologiaIva")
    esenzione_iva: Optional[DTOAPICategoria] = Field(default=None, alias="EsenzioneIva")
    prezzo_singolo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PrezzoSingolo")
    prezzo_totale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PrezzoTotale")
    sconto: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Sconto")
    tipo_sconto: Optional[StrictInt] = Field(default=None, alias="TipoSconto")
    iva: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Iva")
    codice_commerciale: Optional[StrictStr] = Field(default=None, alias="CodiceCommerciale")
    nome_commerciale: Optional[StrictStr] = Field(default=None, alias="NomeCommerciale")
    tipo_retta_entita: Optional[DTOAPICategoria] = Field(default=None, alias="TipoRettaEntita")
    mese: Optional[StrictInt] = Field(default=None, alias="Mese")
    anno: Optional[StrictInt] = Field(default=None, alias="Anno")
    __properties: ClassVar[List[str]] = ["Prodotto", "QuantitàSingolo", "UnitaQntSingolo", "TipologiaIva", "EsenzioneIva", "PrezzoSingolo", "PrezzoTotale", "Sconto", "TipoSconto", "Iva", "CodiceCommerciale", "NomeCommerciale", "TipoRettaEntita", "Mese", "Anno"]

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
        """Create an instance of DTOAPIFatturaItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of prodotto
        if self.prodotto:
            _dict['Prodotto'] = self.prodotto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unita_qnt_singolo
        if self.unita_qnt_singolo:
            _dict['UnitaQntSingolo'] = self.unita_qnt_singolo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tipologia_iva
        if self.tipologia_iva:
            _dict['TipologiaIva'] = self.tipologia_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of esenzione_iva
        if self.esenzione_iva:
            _dict['EsenzioneIva'] = self.esenzione_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tipo_retta_entita
        if self.tipo_retta_entita:
            _dict['TipoRettaEntita'] = self.tipo_retta_entita.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOAPIFatturaItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Prodotto": DTOAPIProdotto.from_dict(obj.get("Prodotto")) if obj.get("Prodotto") is not None else None,
            "QuantitàSingolo": obj.get("QuantitàSingolo"),
            "UnitaQntSingolo": DTOAPIUnitaMisura.from_dict(obj.get("UnitaQntSingolo")) if obj.get("UnitaQntSingolo") is not None else None,
            "TipologiaIva": DTOAPICategoria.from_dict(obj.get("TipologiaIva")) if obj.get("TipologiaIva") is not None else None,
            "EsenzioneIva": DTOAPICategoria.from_dict(obj.get("EsenzioneIva")) if obj.get("EsenzioneIva") is not None else None,
            "PrezzoSingolo": obj.get("PrezzoSingolo"),
            "PrezzoTotale": obj.get("PrezzoTotale"),
            "Sconto": obj.get("Sconto"),
            "TipoSconto": obj.get("TipoSconto"),
            "Iva": obj.get("Iva"),
            "CodiceCommerciale": obj.get("CodiceCommerciale"),
            "NomeCommerciale": obj.get("NomeCommerciale"),
            "TipoRettaEntita": DTOAPICategoria.from_dict(obj.get("TipoRettaEntita")) if obj.get("TipoRettaEntita") is not None else None,
            "Mese": obj.get("Mese"),
            "Anno": obj.get("Anno")
        })
        return _obj



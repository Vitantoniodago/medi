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

class DTOBisogniPazienteAlimentazione(BaseModel):
    """
    
    """ # noqa: E501
    assenza_alimentazione: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [assenza alimentazione].", alias="AssenzaAlimentazione")
    alimentazione_orale: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [alimentazione orale].", alias="AlimentazioneOrale")
    ausili_alimentazione: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [ausili alimentazione].", alias="AusiliAlimentazione")
    imboccato: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is imboccato.", alias="Imboccato")
    dieta_specifica: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [dieta specifica].", alias="DietaSpecifica")
    dieta_sbilanciata: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [dieta sbilanciata].", alias="DietaSbilanciata")
    ematemesi: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is ematemesi.", alias="Ematemesi")
    meteorismo: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is meteorismo.", alias="Meteorismo")
    protesi_dentaria: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [protesi dentaria].", alias="ProtesiDentaria")
    nutrizione_parentale: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [nutrizione parentale].", alias="NutrizioneParentale")
    nutrizione_enterale: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [nutrizione enterale].", alias="NutrizioneEnterale")
    melena: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is melena.", alias="Melena")
    sondino: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica this {MediHomeCloudServer.Models.DTOBisogniPazienteAlimentazione} is sondino.", alias="Sondino")
    rifiuto_cibo: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [rifiuto cibo].", alias="RifiutoCibo")
    calo_ponderale: Optional[StrictBool] = Field(default=None, description="Richiedi o modifica un valore che indica [calo ponderale].", alias="CaloPonderale")
    id_gastrectomia: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier gastrectomia.", alias="IDGastrectomia")
    id_diabete: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier diabete.", alias="IDDiabete")
    intolleranze_alimentari: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica intolleranze alimentari.", alias="IntolleranzeAlimentari")
    impedimento_alimentazione: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica impedimento alimentazione.", alias="ImpedimentoAlimentazione")
    note: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica note.", alias="Note")
    id_analisi_bisogni_alimentazione: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier analisi bisogni alimentazione.", alias="IDAnalisiBisogniAlimentazione")
    id_assistito: Optional[StrictInt] = Field(default=None, description="Richiedi o modifica identifier assistito.", alias="IDAssistito")
    id_visita: Optional[StrictInt] = Field(default=None, alias="IDVisita")
    __properties: ClassVar[List[str]] = ["AssenzaAlimentazione", "AlimentazioneOrale", "AusiliAlimentazione", "Imboccato", "DietaSpecifica", "DietaSbilanciata", "Ematemesi", "Meteorismo", "ProtesiDentaria", "NutrizioneParentale", "NutrizioneEnterale", "Melena", "Sondino", "RifiutoCibo", "CaloPonderale", "IDGastrectomia", "IDDiabete", "IntolleranzeAlimentari", "ImpedimentoAlimentazione", "Note", "IDAnalisiBisogniAlimentazione", "IDAssistito", "IDVisita"]

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
        """Create an instance of DTOBisogniPazienteAlimentazione from a JSON string"""
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
        """Create an instance of DTOBisogniPazienteAlimentazione from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AssenzaAlimentazione": obj.get("AssenzaAlimentazione"),
            "AlimentazioneOrale": obj.get("AlimentazioneOrale"),
            "AusiliAlimentazione": obj.get("AusiliAlimentazione"),
            "Imboccato": obj.get("Imboccato"),
            "DietaSpecifica": obj.get("DietaSpecifica"),
            "DietaSbilanciata": obj.get("DietaSbilanciata"),
            "Ematemesi": obj.get("Ematemesi"),
            "Meteorismo": obj.get("Meteorismo"),
            "ProtesiDentaria": obj.get("ProtesiDentaria"),
            "NutrizioneParentale": obj.get("NutrizioneParentale"),
            "NutrizioneEnterale": obj.get("NutrizioneEnterale"),
            "Melena": obj.get("Melena"),
            "Sondino": obj.get("Sondino"),
            "RifiutoCibo": obj.get("RifiutoCibo"),
            "CaloPonderale": obj.get("CaloPonderale"),
            "IDGastrectomia": obj.get("IDGastrectomia"),
            "IDDiabete": obj.get("IDDiabete"),
            "IntolleranzeAlimentari": obj.get("IntolleranzeAlimentari"),
            "ImpedimentoAlimentazione": obj.get("ImpedimentoAlimentazione"),
            "Note": obj.get("Note"),
            "IDAnalisiBisogniAlimentazione": obj.get("IDAnalisiBisogniAlimentazione"),
            "IDAssistito": obj.get("IDAssistito"),
            "IDVisita": obj.get("IDVisita")
        })
        return _obj



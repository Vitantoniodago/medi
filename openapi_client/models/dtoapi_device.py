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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.dtoapi_licenza import DTOAPILicenza
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DTOAPIDevice(BaseModel):
    """
    DTOAPIDevice
    """ # noqa: E501
    guid_device: Optional[StrictStr] = Field(default=None, alias="GUID_Device")
    mac_address: Optional[StrictStr] = Field(default=None, alias="MAC_Address")
    api_key: Optional[StrictStr] = Field(default=None, alias="APIKey")
    messaggio: Optional[StrictStr] = Field(default=None, alias="Messaggio")
    stato: Optional[StrictInt] = Field(default=None, alias="Stato")
    licenza: Optional[DTOAPILicenza] = Field(default=None, alias="Licenza")
    __properties: ClassVar[List[str]] = ["GUID_Device", "MAC_Address", "APIKey", "Messaggio", "Stato", "Licenza"]

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
        """Create an instance of DTOAPIDevice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of licenza
        if self.licenza:
            _dict['Licenza'] = self.licenza.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DTOAPIDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "GUID_Device": obj.get("GUID_Device"),
            "MAC_Address": obj.get("MAC_Address"),
            "APIKey": obj.get("APIKey"),
            "Messaggio": obj.get("Messaggio"),
            "Stato": obj.get("Stato"),
            "Licenza": DTOAPILicenza.from_dict(obj.get("Licenza")) if obj.get("Licenza") is not None else None
        })
        return _obj



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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.external_login_view_model import ExternalLoginViewModel
from openapi_client.models.user_login_info_view_model import UserLoginInfoViewModel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ManageInfoViewModel(BaseModel):
    """
    
    """ # noqa: E501
    local_login_provider: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica local login provider.", alias="LocalLoginProvider")
    email: Optional[StrictStr] = Field(default=None, description="Richiedi o modifica email.", alias="Email")
    logins: Optional[List[UserLoginInfoViewModel]] = Field(default=None, description="Richiedi o modifica logins.", alias="Logins")
    external_login_providers: Optional[List[ExternalLoginViewModel]] = Field(default=None, description="Richiedi o modifica external login providers.", alias="ExternalLoginProviders")
    __properties: ClassVar[List[str]] = ["LocalLoginProvider", "Email", "Logins", "ExternalLoginProviders"]

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
        """Create an instance of ManageInfoViewModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in logins (list)
        _items = []
        if self.logins:
            for _item in self.logins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Logins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_login_providers (list)
        _items = []
        if self.external_login_providers:
            for _item in self.external_login_providers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ExternalLoginProviders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ManageInfoViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LocalLoginProvider": obj.get("LocalLoginProvider"),
            "Email": obj.get("Email"),
            "Logins": [UserLoginInfoViewModel.from_dict(_item) for _item in obj.get("Logins")] if obj.get("Logins") is not None else None,
            "ExternalLoginProviders": [ExternalLoginViewModel.from_dict(_item) for _item in obj.get("ExternalLoginProviders")] if obj.get("ExternalLoginProviders") is not None else None
        })
        return _obj



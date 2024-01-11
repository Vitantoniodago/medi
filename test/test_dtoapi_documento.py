# coding: utf-8

"""
    MediHome-CloudServer

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.dtoapi_documento import DTOAPIDocumento

class TestDTOAPIDocumento(unittest.TestCase):
    """DTOAPIDocumento unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DTOAPIDocumento:
        """Test DTOAPIDocumento
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DTOAPIDocumento`
        """
        model = DTOAPIDocumento()
        if include_optional:
            return DTOAPIDocumento(
                codice_documento = '',
                sessione = openapi_client.models.dtoapi_session.DTOAPISession(
                    guid_session = '00000000-0000-0000-0000-000000000000', 
                    utente = openapi_client.models.dtoapi_user.DTOAPIUser(
                        guid = '', 
                        user_name = '', 
                        email = '', 
                        password = '', 
                        tipologia = '', 
                        api_key = '00000000-0000-0000-0000-000000000000', 
                        nome = '', 
                        cognome = '', 
                        ruolo = '', 
                        id_tipologia = 56, 
                        codice_fiscale = '', 
                        guid_medibox = '', ), 
                    start_session = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expired = 56, )
            )
        else:
            return DTOAPIDocumento(
        )
        """

    def testDTOAPIDocumento(self):
        """Test DTOAPIDocumento"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

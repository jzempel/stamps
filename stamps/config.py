# -*- coding: utf-8 -*-
"""
    stamps.config
    ~~~~~~~~~~~~~

    Stamps.com configuration.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

import os


class StampsConfiguration(object):
    """Stamps service configuration.

    :param integration_id: Unique ID, provided by Stamps.com, that represents
        your application.
    :param username: Stamps.com account username.
    :param password: Stamps.com password.
    :param wsdl: Default `None`. WSDL URI. Use ``'testing'`` to use the test
        server WSDL.
    """

    def __init__(self, integration_id, username, password, wsdl=None):
        self.integration_id = integration_id,
        self.username = username
        self.password = password

        if wsdl is None or wsdl == "testing":
            file_path = os.path.abspath(__file__)
            directory_path = os.path.dirname(file_path)

            if wsdl == "testing":
                file_name = "stamps_v24.test.wsdl"
            else:
                file_name = "stamps_v24.wsdl"

            wsdl = os.path.join(directory_path, "wsdls", file_name)
            self.wsdl = "file://{0}".format(wsdl)
        else:
            self.wsdl = wsdl

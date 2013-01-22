# -*- coding: utf-8 -*-
"""
    stamps.config
    ~~~~~~~~~~~~~

    Stamps.com configuration.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from ConfigParser import NoOptionError, NoSectionError, SafeConfigParser
from logging import getLogger
import os


class StampsConfiguration(object):
    """Stamps service configuration. The service configuration may be provided
    directly via parameter values, or it can be read from a configuration file.
    If no parameters are given, the configuration will attempt to read from a
    ``'.stamps.cfg'`` file in the user's HOME directory. Alternately, a
    configuration filename can be passed to the constructor.

    Here is a sample configuration (by default the constructor reads from a
    ``'default'`` section)::

        [default]
        integration_id = XXXXXXXX-1111-2222-3333-YYYYYYYYYYYY
        username = stampy
        password = secret

    :param integration_id: Default `None`. Unique ID, provided by Stamps.com,
        that represents your application.
    :param username: Default `None`. Stamps.com account username.
    :param password: Default `None`. Stamps.com password.
    :param wsdl: Default `None`. WSDL URI.
    :param port: Default `None`. The name of the WSDL port to use.
    :param section: Default ``'default'``. The configuration section to use.
    :param file_name: Default `None`. Optional configuration file name.
    """

    def __init__(self, integration_id=None, username=None, password=None,
            wsdl=None, port=None, section="default", file_name=None):
        self.logger = getLogger("stamps")
        parser = SafeConfigParser()

        if file_name:
            parser.read([file_name])
        else:
            parser.read([os.path.expanduser("~/.stamps.cfg")])

        self.integration_id = self.__get(parser, section, "integration_id",
                integration_id)
        self.username = self.__get(parser, section, "username", username)
        self.password = self.__get(parser, section, "password", password)
        self.wsdl = self.__get(parser, section, "wsdl", wsdl)
        self.port = self.__get(parser, section, "port", port)

        if wsdl is None:
            file_path = os.path.abspath(__file__)
            directory_path = os.path.dirname(file_path)

            if section == "test":
                wsdl_name = "stamps_v25.test.wsdl"
            else:
                wsdl_name = "stamps_v25.wsdl"

            wsdl = os.path.join(directory_path, "wsdls", wsdl_name)
            self.wsdl = "file://{0}".format(wsdl)

            if port is None:
                self.port = "SwsimV25Soap12"

        assert self.integration_id
        assert self.username
        assert self.password
        assert self.wsdl
        assert self.port

    def __get(self, parser, section, name, default):
        """Get a configuration value for the named section.

        :param parser: The configuration parser.
        :param section: The section for the given name.
        :param name: The name of the value to retrieve.
        """
        if default:
            vars = {name: default}
        else:
            vars = None

        try:
            ret_val = parser.get(section, name, vars=vars)
        except (NoSectionError, NoOptionError) as error:
            self.logger.exception(error)
            ret_val = None

        return ret_val

#!/usr/bin/env python

from typing import Union
from splunklib.client import connect, Service


class Splunk:
    """SPLUNK Class"""

    def __init__(self, username: Union[str], password: Union[str],
                 host: Union[str] = 'localhost', port: Union[int] = 8089,
                 scheme: Union[str] = 'https', verify: Union[bool] = True,
                 owner: Union[str] = None, app: Union[str] = None,
                 sharing: Union[str] = 'user', token: Union[str] = None,
                 cookie: Union[str] = None, autologin: Union[bool] = None):
        """Initialization

        :param username: The Splunk account username,
                            which is used to authenticate the Splunk instance.
        :type username: str
        :param password: The password for the Splunk account.
        :type password: str
        :param host: The host name (the default is "localhost")
        :type host: str
        :param port: The port number (the default is 8089)
        :type port: int
        :param scheme: The scheme for accessing the service
                        (the default is "https")
        :type scheme: str
        :param verify: Enable (True) or disable (False) SSL verification for
                        https connections. (optional, the default is True)
        :type verify: bool
        :param owner: The owner context of the namespace (optional)
        :type owner: str
        :param app: The app context of the namespace (optional)
        :type app: str
        :param sharing: The sharing mode for the namespace
                        (the default is "user")
        :type sharing: str
        :param token: The current session token (optional).
                        Session tokens can be shared across multiple service instances.
        :type token: str
        :param cookie: A session cookie. When provided, you don't need to call :meth:`login`.
                        This parameter is only supported for Splunk 6.2+.
        :type cookie: str
        :param autologin: When ``True``, automatically tries to log in again
                            if the session terminates.
        :type autologin: bool

        :raise:
            ValueError: if `scheme`, `sharing` parameter values are incorrect
        """

        if scheme not in ['https', 'http']:
            raise ValueError
        if sharing not in ['user', 'global', 'system', 'app']:
            raise ValueError

        bind_dictionary = locals()
        # pop 'self', 'None' types
        for key, value in list(bind_dictionary.items()):
            if isinstance(value, type(self)):
                bind_dictionary.pop(key)
            if isinstance(value, type(None)):
                bind_dictionary.pop(key)
        self.kwargs = bind_dictionary

    def connect(self) -> Union[Service]:
        """This function connects and logs in to a Splunk instance.

        :return: An initialized Service connection.
        :rtype: Service

        :raise:
            ConnectionError: if server is down or fail authentication and etc
        """

        service = connect(**self.kwargs)
        if isinstance(service, Service):
            return service
        else:
            raise ConnectionError

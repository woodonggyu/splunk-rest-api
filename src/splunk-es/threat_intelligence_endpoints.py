#!/usr/bin/env python

import os
from base64 import b64encode
from typing import Union
from urllib.parse import urljoin
from src.bind import Splunk


class ThreatIntelligenceEndpoints(Splunk):
    """"""

    def __init__(self):
        """"""
        pass

    def upload_a_threat_intelligence(self, filename: str, threat_group: str,
                                     threat_category: str,
                                     weight: Union[int] = 1,
                                     overwrite: Union[bool] = False,
                                     sinkhole: Union[bool] = False) -> dict:
        """Upload a threat intelligence file in STIX, IOC, or CSV format.

        :param filename: The threat intelligence file name, with extension.
        :type filename: str
        :param weight: The relative weight assigned to this source of threat intelligence,
                        used for risk score calculations in notable events.
                        Most threat intelligence sources have a weight of 1.
        :type weight: int
        :param threat_group: The threat group to which this threat intelligence belongs.
                                Optional for IOC and STIX files because the parser can extract this value from the file itself.
                                Required for CSV files.
        :type threat_group: str
        :param threat_category: The threat group to which this threat intelligence belongs.
                                Optional for IOC and STIX files because the parser can extract this value from the file itself.
                                Required for CSV files.
        :type threat_category: str
        :param overwrite: If set to true and a file with this name already exists, the API overwrites the file and reports success.
                            If set to false and a file with this name already exists, the API returns an error.
        :param sinkhole: If set to true, deletes the file after processing.

        :return:

        :raise
            FileNotFoundError: If there is no file corresponding to `filename` value
        """

        if os.path.isfile(filename):
            with open(file=filename, mode='rb') as fp:
                content = fp.read()
            encoded_content = b64encode(content)
        else:
            raise FileNotFoundError

        # data = {'encoded_content': encoded_content, 'file_name': filename,
        #         'weight': weight, 'threat_group': threat_group,
        #         'threat_category': threat_category, 'overwrite': overwrite,
        #         'sinkhole': sinkhole}
        # url = urljoin(base=, url='/data/threat_intel/upload',
        #               allow_fragments=True)

    def create_colletion(self, collection_name: str,
                         item_key: Union[str] = None):
        """Create one or more rows in a collection."""
        pass

    def retrieve_collection(self, collection_name: str,
                            item_key: Union[str] = None):
        """List one or more rows from a collection."""
        pass

    def update_collection(self, collection_name: str,
                          item_key: Union[str] = None):
        """Update one or more rows in a collection."""
        pass

    def delete_collection(self, collection_name: str,
                          item_key: Union[str] = None):
        """Delete one or more rows from a collection."""
        pass

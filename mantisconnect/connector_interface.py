from mantisconnect.connector_v1 import *
from zeep import Client


def create_mantis_soap_connector(mantis_url):
    client = Client(mantis_url)
    version = client.service.mc_version()

    if version == "1.2.11":
        return MantisSoapConnectorV1_2_11(mantis_url)
    if version == "1.2.12":
        return MantisSoapConnectorV1_2_12(mantis_url)

    if version[0] != "1":
        raise NotImplementedError("Not yet support mantis soap api version "+version)

    return MantisSoapConnectorV1_2_12(mantis_url)

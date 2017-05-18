from zeep import Client


class MantisSoapConnector:
    """
    Mantis soap connector
     request filter, version, issue of filter, enum data using mantis soap api
    """
    def  __init__(self, mantis_soap_url = "https://www.mantisbt.org/bugs/api/soap/mantisconnect.php?wsdl"):
        self.mantis_soap_url = mantis_soap_url
        self.client = None
        self.version = None

    def set_user_passwd(self, name, passwd):
        self.user_name = name
        self.user_passwd = passwd

    def connect(self):
        self.client = Client(self.mantis_soap_url)
        self.version = self.request_version()

    def request_issue_get(self, issue_id):
        return self.client.service.mc_issue_get(self.user_name, self.user_passwd, issue_id)

    def request_enum_status(self):
        return self.client.service.mc_enum_status(self.user_name, self.user_passwd)

    def request_enum_priorities(self):
        return self.client.service.mc_enum_priorities(self.user_name, self.user_passwd)

    def request_enum_resolutions(self):
        return self.client.service.mc_enum_resolutions(self.user_name, self.user_passwd)

    def request_version(self):
        return self.client.service.mc_version()

    def request_project(self, project_name):
        return self.client.service.mc_project_get_id_from_name(self.user_name, self.user_passwd, project_name)

    def request_filter_get(self, project_id):
        return self.client.service.mc_filter_get(self.user_name, self.user_passwd, project_id)

    def request_filter_get_issue(self, project_id, filter_id, page_number=0, per_page=0):
        return self.client.service.mc_filter_get_issues(self.user_name, self.user_passwd,
                project_id, filter_id, page_number, per_page)

    def request_filter_get_issue_header(self, project_id, filter_id, page_number=0, per_page=0):
        return self.client.service.mc_filter_get_issue_headers(self.user_name, self.user_passwd,
                project_id, filter_id, page_number, per_page)

import sys

from mantisconnect.simple_project import Issue
from mantisconnect.simple_project import SimpleProject
from mantisconnect.connector_interface import create_mantis_soap_connector


if __name__ == "__main__":
    url = "https://your.mantis.com/api/soap/mantisconnect.php?wsdl"
    username = "user"
    password = "oooops"

    mc = create_mantis_soap_connector(url)
    mc.set_user_passwd(username, password)
    mc.connect()

    print("Connent %s" % url)
    print("Mantis SOAP MC Version:" + mc.version)

    # Must use project name in mantis
    p = SimpleProject(mc, "your project name")

    filter_name = "your filter name"

    # Get issue object list
    # see Issue class (mantisconnect/project.py)
    issue_list = p.request_filter_all_issues(filter_name, 10)

    # Write your code
    #
    for issue in issue_list:
        print("{0} {1}".format(issue.issue_id, issue.summary))

import sys

from mantisconnect.simple_project import Issue
from mantisconnect.simple_project import SimpleProject
from mantisconnect.connector import MantisSoapConnector


if __name__ == "__main__":
    url = "https://your.mantis.com/api/soap/mantisconnect.php?wsdl"
    username = "user"
    password = "oooops"

    mc = MantisSoapConnector(url)
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

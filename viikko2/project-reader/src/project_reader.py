from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        sisalto = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(f"{sisalto["tool"]["poetry"]["name"]}", f"{sisalto["tool"]["poetry"]["description"]}", [avain for avain in sisalto["tool"]["poetry"]["dependencies"]], [avain for avain in sisalto["tool"]["poetry"]["group"]["dev"]["dependencies"]])

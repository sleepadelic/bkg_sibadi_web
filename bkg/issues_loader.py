import yaml
import datetime
import bkg
from bkg.models import Issue as webIssue
from bkg.models import IssueType as webIssueType


def load_from_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as ff:
        return yaml.load(ff, Loader=yaml.UnsafeLoader)

def load_issues(filepath):

    issues = load_from_yaml(filepath)
    iss:Issue
    for iss in issues:
        web_iss: bkg.models.Issue()
        web_iss = bkg.models.Issue()
        web_iss.type = bkg.models.IssueType.objects.get(name=iss.type)
        web_iss.status = bkg.models.IssueStatus.objects.get(name='Премодерация')
        web_iss.description = iss.description
        web_iss.address = iss.address
        web_iss.creation_date = iss.send_time
        web_iss.image_path.name = iss.image
        web_iss.geo = iss.geo
        web_iss.save()

class Issue(yaml.YAMLObject):
    type = ''
    image = ''
    description = ''
    address = ''
    geo = ''
    send_time = None


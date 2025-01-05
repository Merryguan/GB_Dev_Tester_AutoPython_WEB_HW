import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_step1(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"]+"api/posts",
                       params={"owner": "notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres


def test_step2(login, testtext2):
    header = {"X-Auth-Token": login}
    requests.post(data["address"]+"api/posts",
                  params={"title": "AutoPythonWeb", "description": "Pytest_test1", "content": "Text"},
                  headers=header)
    res2 = requests.get(data["address"]+"api/posts", headers=header)
    listres2 = [i["description"] for i in res2.json()["data"]]
    assert testtext2 in listres2

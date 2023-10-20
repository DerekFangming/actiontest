#!/usr/bin/python3
import json
import os
import sys
import glob
import yaml
from yaml.loader import SafeLoader
from github import Github
from github import GithubException

def main():
    print("================================================")
    g = Github()
    print("================================================")
    repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
    
    with open(str(os.getenv('GITHUB_EVENT_PATH'))) as json_file:
        data = json.load(json_file)

    pr = repo.get_pull(data['pull_request']['number'])
    for file in pr.get_files():
        print(file.filename + " => " + file.status)

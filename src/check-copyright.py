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
    print("================================================ ")
    g = Github()
    repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
    
    with open(str(os.getenv('GITHUB_EVENT_PATH'))) as json_file:
        data = json.load(json_file)

    pr = repo.get_pull(data['pull_request']['number'])
    head = data['pull_request']['head']['ref']
    print(head)
#    print(json.dumps(data, indent = 4))
    print("================================================")
    for file in pr.get_files():
        print(file.filename + " => " + file.status)
        print("111111111111111111111111111111111111111111111111111")
#        contents = repo.get_contents(filename, ref=commit.sha).decoded_content
        print(repo.get_contents(file.filename, ref=head).decoded_content)
        print("222222222222222222222222222222222222222222222222222")


if __name__ == "__main__":
    main()

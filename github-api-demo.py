from urllib import response
import requests


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'  # base url
        self.api_token = '<your_token>'  # replace with your token

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()

    def getRepository(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.api_token, json={
            'name': name,
            'description': 'This is a repository created by github api',
            'private': False,
            'has_issues': True,
            'has_projects': True,
            'has_wiki': True
        })
        return response.json()


github = Github()

while True:
    choise = input(
        '1. Get user\n2. Get repository\n3. Create repository\n4. Exit\nEnter your choise: ')

    if choise == '4':
        break
    else:
        if choise == '1':
            username = input('Enter username: ')
            result = github.getUser(username)
            print(
                f'{result["name"]} has {result["public_repos"]} public repositories')

        elif choise == '2':
            username= input('Enter username: ')
            result = github.getRepository(username)

            for repo in result:
                print(f'{repo["name"]} - {repo["description"]}')

        elif choise == '3':
            name = input('Enter repository name: ')
            result = github.createRepository(name)
            print(f'{result["name"]} was created')
        
        else:
            print('Invalid choise')
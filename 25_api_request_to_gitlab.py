import requests

response = requests.get("https://gitlab.com/api/v4/users/priyabrata-devops/projects")


my_project = response.json()

print(my_project)
#for project in my_project:
#    print(f"Project Name: {project['name']},\nProject URL: {project['web_url']}\n")
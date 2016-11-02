from fabric.api import local

def prepare_deploy():
    #local("./manage.py test testAutomation")
    local("git add . && git commit -m 'random'")
    local("git push")
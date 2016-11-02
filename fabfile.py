from fabric.api import local

def prepare_deploy():
    #local("./manage.py test testAutomation")
    local("git add -p && git commit")
    local("git push")
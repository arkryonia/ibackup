# @Author: drxos
# @Date:   2016-08-13T02:09:00+01:00
# @Last modified by:   drxos
# @Last modified time: 2016-08-13T02:15:34+01:00


import random
import string

from fabric.api import run, local, hosts, cd


# Get global variables !!!!!!!! Important!!!!!!!
PROJECT = "irgibweb"
DOMAIN_NAME = "irgibafrica.university"

def hello(who="drxos"):
    print "\n......\n"
    print "Hello {who} ! ^_^".format(who=who)

def gen_secret_key():
    key = ''
    for i in range(100):
        key += random.SystemRandom().choice(string.digits + string.letters + string.punctuation)
    return key

def create_app(who="drxos"):
    # request the project name
    # project = raw_input("What's your project name ? \n")

    # Create dokku app for project
    run('dokku apps:create {0}'.format(PROJECT))
    print "dokku app created......ok"


def postgres():
    # Postgresql configuration
    # run('dokku postgres:create {0}'.format(PROJECT))
    run('dokku postgres:link {0} {1}'.format(PROJECT, PROJECT))
    print "dokku app linked to postgres database......ok"


def dj_secret_key():
    # Django environment variable
    run('dokku config:set {0} DJANGO_SECRET_KEY="{1}"'.format(PROJECT, gen_secret_key()))
    print "Django secret key configured!"


def set_domain():
    # Project domain name
    run('dokku domains:add {0} {1}'.format(PROJECT, DOMAIN_NAME))
    print "{0} added to {1} project".format(DOMAIN_NAME, PROJECT)


def media_persist(who='drxos'):
    # Make media files persistent
    run('dokku docker-options:add {0} deploy "-v /apps/{1}/mediafiles:/app/mediafiles"'.format(PROJECT, PROJECT))
    print "Media files persistent......ok"

    print "Super! It's done {who}.".format(who=who)

def deploy():
    hello()
    media_persist()
    # local('git push dokku master')

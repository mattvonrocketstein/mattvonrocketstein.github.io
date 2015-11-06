""" ghio.bin.ghio
"""
import os
import sys
import time
import threading
import webbrowser
#from optparse import OptionParser
from argparse import ArgumentParser

from fabric.api import local

from report import report
from goulash.python import dirname, opj, ope

COMMANDS = 'update build show init'.split()
COMMANDS = 'build'.split()
URL = 'http://localhost:8080/'
USAGE = '{0} subcommands are {1}'.format(
    os.path.split(sys.argv[0])[-1],
    COMMANDS)
USAGE += '\n\nas in: "ghio build project-name"'
ghio_root = dirname(dirname(dirname(__file__)))
src_root  = opj(ghio_root, 'src')

def _require_project_dir(fxn):
    def newf(*args, **kargs):
        project = args[0]
        proot = opj(src_root, project)
        assert ope(proot), "{0} does not exist".format(proot)
        return fxn(*args, **kargs)
    return newf

def build_parser():
    parser = ArgumentParser(usage=USAGE)
    parser.add_argument('command')
    parser.add_argument('project')
    return parser

def build(project):
    """ build project from source """
    proot = opj(src_root, 'conf')
    if project == 'all':
        for pdir in [x for x in os.listdir(proot) if x]:
            build(pdir)
        return
    else:
        proot=opj(proot,project)
        report("rebuilding " + proot)
        local("cd {0} && mkdocs build".format(proot))
        dest = os.path.dirname(src_root)
        rendered_site = os.path.join(dest, 'site')
        cmd = 'cp -rfv {0} "{1}"'.format(
            os.path.join(rendered_site, '*'),
            dest)
        local(cmd)
        #raise Exception,cmd

def init(project):
    """ initialize new project """
    local("cd {0} && poole --init --theme=foundation {1}".format(
        src_root, project))

@_require_project_dir
def show(project):
    build(project)
    proot = opj(src_root, project)
    report("serving "+proot)
    def f():
        webbrowser.open(URL)
    threading.Thread(target=f).start()
    local("cd {0} && poole --serve".format(proot))

def update(project):
    build(project)
    proot = opj(src_root, project)
    output = opj(proot, 'output')
    prod_dir = opj(src_root)
    assert ope(output)
    target = opj(ghio_root, project)
    if not ope(target):
        os.mkdir(target)
    cmd = "cp -rfv {0}/* {1}".format(output, target)
    local(cmd)
    local("git add -A {0}".format(target))
    local("cd {0} && git commit {1} -m \"{2}\"".format(
        ghio_root, project,'update '+project))
    local("git push")


def main():
    ns, extra = build_parser().parse_known_args()
    cmd, project = ns.command, ns.project
    try:
        cmd = eval(cmd)
    except NameError:
        err = 'no such command "{0}", choose one of {1}'
        err = err.format(cmd,COMMANDS)
        raise SystemExit(err)
    cmd(project)#, extra)

if __name__=='__main__':
    main()

""" ghio.bin.ghio
"""
import os
import sys
import time
import threading
import webbrowser
from optparse import OptionParser

from fabric.api import local

from report import report
from goulash.python import dirname, opj, ope
URL = 'http://localhost:8080/'
USAGE = '{0} subcommands are {1}'.format(
    os.path.split(sys.argv[0])[-1],
    'update build show init'.split())
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
    parser = OptionParser(usage=USAGE)
    return parser

@_require_project_dir
def build(project):
    """ build project from source """
    proot = opj(src_root, project)
    report("rebuilding "+proot)
    local("cd {0} && poole --build --base-url=project".format(proot))

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
    opts,args = build_parser().parse_args()
    print opts,args
    assert args
    cmd = args[0]
    project = args[1]
    try:
        cmd = eval(cmd)
    except NameError:
        raise SystemExit(USAGE)

    cmd(project)

if __name__=='__main__':
    main()

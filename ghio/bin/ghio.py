""" ghio.bin.ghio
"""
from optparse import OptionParser
import threading
import webbrowser
import time

from fabric.api import local

from report import report
from goulash.python import dirname, opj, ope

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
    parser = OptionParser()
    return parser

@_require_project_dir
def build(project):
    proot = opj(src_root, project)
    report("rebuilding "+proot)
    local("cd {0} && poole --build --base-url=project".format(proot))

@_require_project_dir
def show(project):
    proot = opj(src_root, project)
    report("serving "+proot)
    def f():

        webbrowser.open('http://localhost:8080/')
    threading.Thread(target=f).start()
    local("cd {0} && poole --serve".format(proot))

def update(project):
    build(project)
    proot = opj(src_root, project)
    output = opj(proot, 'output')
    prod_dir = opj(src_root)
    assert ope(output)
    cmd = "cp -rfv {0}/* {1}".format(output, opj(ghio_root,project))
    local(cmd)
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
        raise SystemExit('subcommands are {0}'.format('update build show'.split()))

    cmd(project)

if __name__=='__main__':
    main()

title: Intro
menu-position: 0
---

##What is it?

Smash is a smarter shell.  It offers features for project management, a flexible plugin architecture that is easy to use, and simple configuration files that try to be as sane as possible.  [Python developers](#smash-for-python-devs) will be particularly interested because it also happens to host a full-fledged python runtime via IPython, but non-python developers can safely ignore that feature.  Smash leverages existing system [tab completion](#tab-completion) setup, apart from variable/keyword completion in python namespaces.  Smash builds on, and offers very sophisticated support for python virtual environments.

<a id="quickstart"></a>
##Quickstart

The smash installation happens in a sandbox, does not require root, and will not interefere with existing versions of IPython.  The cost of this is that setup is a little bit nonstandard and `setup.py` should not be used directly unless you only want to develop against the support libraries (for that see: [dev installation](#dev-installation))


~~~~{.bash}
  $ sudo apt-get install git-core python-virtualenv python-dev
  $ bootstrap=https://raw.githubusercontent.com/mattvonrocketstein/smash/master/bootstrap.sh
  $ curl $bootstrap | bash
  $ ~/bin/smash
~~~~

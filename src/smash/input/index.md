title: Intro
menu-position: 0
---

##What is it?

Smash is a smarter shell.  [Python developers](python_use_cases.html) will be particularly interested because it also happens to host a full-fledged python runtime (via IPython) and offers sophisticated support for python virtual environments, but non-python developers can safely ignore these features.  Smash leverages existing system tab completion setup as well as allowing variable/keyword completion in python namespaces.  Additionally smash offers features for [project management](project_manager.html), a flexible [plugin architecture](plugins.html) that is easy to use, and simple [configuration files](configuration.html) that try to be as sane as possible.

<a id="requirements"></a>
##Requirements

You'll need git in order for the smash bootstrap to clone the smash repo.  Also virtualenv, and the usual python development prerequisites.  You need to be able to compile at least fairly simple C code (this is due to smash's reliance on fabric).  In debian-based linux, the following one-liner should do the trick and for OSX you can probably homebrew something similar.

~~~~{.bash}
  $ sudo apt-get install git-core python-virtualenv python-dev build-essential
~~~~

<a id="quickstart"></a>
##Quickstart

The smash installation happens in a sandbox, does not require root, and will not interefere with existing versions of IPython.  The cost of this is that setup is a little bit nonstandard and `setup.py` should not be used directly unless you only want to develop against the support libraries (for that see: [dev installation](#dev-installation))

~~~~{.bash}
  $ curl https://raw.githubusercontent.com/mattvonrocketstein/smash/master/bootstrap.sh | bash
  $ ~/bin/smash
~~~~

Don't like the idea of curling random instructions?  If the above installation method seems scary to you, here's more or less what the bootstrap.sh file is accomplishing:

~~~~{.bash}
  $ git clone https://github.com/mattvonrocketstein/smash.git
  $ mv smash ~/.smash
  $ cd ~/.smash
  $ virtualenv . --no-site-packages
  $ source bin/activate
  $ pip install -r install_requirements.txt
  $ python install.py
~~~~


<a id="dev-installation"></a>
##Installation for development

There are two parts to SmaSh: smashlib and the smash shell.  Smashlib by itself may be useful for writing other kinds of IPython extensions.  The instructions in the [quickstart section](#quickstart) will install both the shell and the support library.  Installing the shell is atypical for the reasons mentioned in that section, but **if you only want to develop against smashlib**, installation is  standard:

```shell
  $ git clone https://github.com/mattvonrocketstein/smashlib.git
  $ cd smashlib
  $ python setup.py develop
  $ pip install -r requirements.txt
```

Smash is in beta currently and has no major release versions apart from "master" and "experimental".  If you want to install a particular version of smash, the thing is to use the quickstart instructions, but specify a branch hash:

~~~~{.bash}
  $ SMASH_BRANCH=mainline curl https://raw.githubusercontent.com/mattvonrocketstein/smash/master/bootstrap.sh | bash
~~~~

<a id="dev-installation"></a>
##Philosophy

**But Why?**
So, *why build yet another shell?*  Put simply, shells still kind of suck.  The main problem is that classic shells are inflexible and difficult to extend.  If you do manage to extend them at all, then you probably had to do it with shell code and the result is something that's fragile and difficult to read and maintain.

Just for the sake of an examples, let's consider the problem of a "do what I mean" extension for your shell, where if you type something that looks like a url then the url is opened automatically for you.  To effect a pre-exec style hook in bash, you'll have to do [black magic](http://www.twistedmatrix.com/users/glyph/preexec.bash.txt) with the `DEBUG` trap (ugh).  Zsh is much better and has a built in pre-exec hook, but of course you'll still be writing (or at least invoking) your hooks in shell code.  This works at first, but things start to get messy when issues of code-reuse come up, or if you want to [invoke hooks conditionally](project_manager.html), etc.

If you still think the do-what-i-mean puzzle sounds easy to solve in your shell, how about colorizing random structured data (maybe json or server logs) sent to stdout, regardless of whether that data comes from "cat" or "echo"?   What about the possibility of cohosting arbitrary foreign REPLs alongside your shell?  At least in theory Smash could allow simultaneous and unambiguous usage of tools for sql, ruby, mongo, lisp, whatever.  Or, what if embedding your whole system shell into [an interactive webpage was trivial?](http://ipython.org/videos.html#the-ipython-notebook)

Eventually shells, like IDEs, get so complex they grow their own package managers, and why bother when a modern full-fledged programmingly language is bound to have package management options anyway?  Honestly there's a reason we don't usually write [socket code in shell script](http://www.lainoox.com/bash-socket-programming/), and a reason why system administration has moved so far away from it's roots in hacky shell scripts.  *But*, since you might have existing shell aliases or functions that you still depend on, smash tries to help you [access your legacy junk](configuration.html#inheritance-shell) until you can port it.

SmaSh's close integration with python itself is a huge plus, but it's also just a side effect of fixing the main problems around making a shell that is truly flexible and nontrivially extensible.

**Design goals**

0. Single-step idiot proof installation
1. The installation should always be inside a virtualenvironment, and never require root
2. Backwards compatability with existing setup for zsh and bash should always be maintained.
3. Everything is a plugin!  Core functionality is small as hell and everything is optional
4. Zero (initial) configuration and sane defaults. Only power users have to care about how configuration actually works
5. Python developers should be able to have a stable and persistent shell.  No kill/restart to clean namespaces, etc, regardless of how many projects they work on at once.
6. Backwards compatability with existing IPython configuration should always be maintained.
7. Always track with the bleeding edge of IPython, but never assume it's installed or used apart from smash
8. Eventually, non-python developers with an addiction to a particular REPL should be able co-host that REPL alongside their system shell.

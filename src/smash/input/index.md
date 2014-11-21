title: Intro
menu-position: 0
---

##What is it?

Smash is a smarter shell.  [Python developers](/python_use_cases.html) will be particularly interested because it also happens to host a full-fledged python runtime via IPython and offers sophisticated support for python virtual environments, but non-python developers can safely ignore these features.  Smash leverages existing system [tab completion](#tab-completion) setup, apart from variable/keyword completion in python namespaces.  Additionally smash offers features for project management, a flexible plugin architecture that is easy to use, and simple configuration files that try to be as sane as possible.

<a id="quickstart"></a>
##Quickstart

The smash installation happens in a sandbox, does not require root, and will not interefere with existing versions of IPython.  The cost of this is that setup is a little bit nonstandard and `setup.py` should not be used directly unless you only want to develop against the support libraries (for that see: [dev installation](#dev-installation))


~~~~{.bash}
  $ sudo apt-get install git-core python-virtualenv python-dev
  $ bootstrap=https://raw.githubusercontent.com/mattvonrocketstein/smash/master/bootstrap.sh
  $ curl $bootstrap | bash
  $ ~/bin/smash
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

<a id="dev-installation"></a>
##Philosophy

So, *why build yet another shell?*  Put simply, shells still kind of suck.  The main problem is that classic shells are inflexible and difficult to extend.  If you do manage to extend them at all, then you probably had to do it with shell code and the result is something that's fragile and difficult to read and maintain.

Just for the sake of an examples, let's consider the problem of a "do what I mean" extension for your shell, where if you type something that looks like a url then the url is opened automatically for you.  To effect a pre-exec style hook in bash, you'll have to do [black magic](http://www.twistedmatrix.com/users/glyph/preexec.bash.txt) with the `DEBUG` trap (ugh).  Zsh is much better and has a built in pre-exec hook, but of course you'll still be writing (or at least invoking) your hooks in shell code.  This works at first, but things start to get messy when issues of code-reuse come up, or if you want to [invoke hooks conditionally](#pm), etc.

If you still think the do-what-i-mean puzzle sounds easy to solve in your shell, how about colorizing random structured data (maybe json or server logs) sent to stdout, regardless of whether that data comes from "cat" or "echo"?   What about the possibility of cohosting arbitrary foreign REPLs alongside your shell?  At least in theory Smash could allow simultaneous and unambiguous usage of tools for sql, ruby, mongo, lisp, whatever.  Or, what if embedding your whole system [shell into an interactive webpage was trivial?](#)

Eventually shells, like IDEs, get so complex they grow their own package managers, and why bother when a modern full-fledged programmingly language is bound to have package management options anyway?  Honestly there's a reason we don't usually write [socket code in shell script](#), and a reason why system administration has moved so far away from it's roots in hacky shell scripts.  *But*, since you might have existing shell aliases or functions that you still depend on, smash tries to help you access your legacy junk until you can port it.

SmaSh's close integration with python itself is a huge plus, but it's also just a side effect of fixing the main problems around making a shell that is truly flexible and nontrivially extensible.

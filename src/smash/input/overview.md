title: overview
menu-position: 1
---

<a id="smash-for-shell-stuff"></a>
##SMASH FOR SHELL STUFF



####CD-hooks
Lorem Ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum

-------------------------------------------------------------------------------

<a id="dwim"></a>
####Do What I Mean
Lorem Ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum

-------------------------------------------------------------------------------

####Shell-related Problems <a id="shell-problems"></a>
Most shell stuff "just works", even when it looks like the grammar for shell vs. python might be ambiguous (for instance, try: `[ string ] && echo its true || echo its false`).  In the event of name collisions, the python namespace typically has preference over the system commands, but this is easy to fix by just deleting the python shadow:

~~~~{.bash}
    smash$ ls
    file1     file2     file3     file4
    file5     file6     file7     file8

    smash$ ls="python namespace shadow"
    smash$ ls
    Out[3]: "python namespace shadow"

    smash$ del ls
    smash$ ls
    file1     file2     file3     file4
    file5     file6     file7     file8
~~~~

If things aren't just working, file an issue or maybe try **IPython's various built-ins**:  The `%%bash` magic might be useful for pasting lots of lines.  The desperate or the paranoid can always prefix commands like `! ls` to ensure they go straight to shell and are not interpretted as python.    Out of the box IPython even supports some limited [mixed python/bash programming](#).


-------------------------------------------------------------------------------

<a id="smash-for-project-automation"></a> <a id="pm"></a>
##SMASH FOR PROJECT AUTOMATION

Projects are natural abstractions for lots of kinds of work, and will be familiar to anyone who has used an IDE.  In smash, project management features are essentially a plugin or extension, and because the "project" concept is flexible and powerful for all sorts of automation this is a pretty big topic.  Working with projects is [described in detail here](#), and what follows is just a summary.

*A project is defined by a nickname and associated with a directory.*  In the simplest case a project can function as merely a bookmark that can be jumped to, or for more involved projects you might want a set of command aliases and macros which other projects do not share.  Projects also have *types* and *operations*, which can either be specified or autodetected based on the contents of the project directory.  The default operations and some examples of what they might involve for your project are described below:

For each operation, here are some examples of the type of actions you might like to perform:

* *Add*: register new project nickname & directory with the Project Manager
* *Activate*: pull fresh code, start project-specific database services or system daemons.
* *Build*: maybe tox for a python project, ant for java or whatever
* *Check*: verify symlinks, start linters or other static analysis
* *Test*: set environment variables and then run unittests
* *Deactivate*: push finished code, stop project-specific database services or other system daemons.



<a id="dev-installation"></a>
##DEV INSTALLATION

There are two parts to SmaSh: smashlib and the smash shell.  The instructions in the [quickstart section](#quickstart) install *both*.  Installing the shell is atypical for the reasons mentioned in that section, but **if you only want to develop against smashlib**, installation is more typical:

```shell
  $ git clone https://github.com/mattvonrocketstein/smashlib.git
  $ cd smashlib
  $ python setup.py develop
  $ pip install -r requirements.txt
```

title: Features
menu-position: 1
---
####Standard System Shell + Python Support
SmaSh functions seamlessly as a normal system shell, but it also a full fledged python interpretter.  It does shell stuff in the shell places, and python stuff in the python places.

![screenshot1](/docs/screenshots/demo-python-bash.png?raw=true "screenshot1")

If you're a bash user or an ipython user, your existing configuration efforts can also be [inherited automatically](#TODO-config-inheritance).  If you don't care anything about python, you can ignore that aspect of the shell completely.  If you *are* a python programmer, you probably spend as much time in a python interpretter as you do in shell.  You can trade those two windows for one to reduce screen clutter, as well as enjoy all the [other python friendly features of smash](#smash-for-python-devs).

-------------------------------------------------------------------------------

<a id="prompts"></a>
####Prompt
By default smash ships with the wonderfully dynamic [liquidprompt tool](#https://github.com/nojhan/liquidprompt).  Liquidprompt has rich options for configuration and it's recommended that you [configure it in the normal way](https://github.com/nojhan/liquidprompt#features-configuration), but, some of these options can be overridden from `~/.smash/config.py`.  The default liquidprompt configuration features a prompt that shows activated python virtual environments, as well as VCS branch and commit/stash status, etc.  Other options include everything from cpu/battery status to write-permissions for the current directory.  Take a look at how it updates below based on the context:

![screenshot1](/docs/screenshots/demo-liquidprompt.png?raw=true "screenshot1")

-------------------------------------------------------------------------------

<a id="tab-completion"></a>
####Tab-completion system
Depending on the context, tab completion information is derived either from ipython (for python namespaces, ipython aliases, etc) or directly from bash (for system commands / paths, hostnames, VCS subcommands, debian packages, whatever your system supports).  Thus if you now use bash exclusively<sup>**</sup> then this means that no effort at all goes into porting old completers into smash shell.  For building new completion mechanisms, you have the option of writing them inside or outside of smash, based on your preference.

![screenshot1](/docs/screenshots/demo-completion.png?raw=true "screenshot3")

<sub>**: if you are a zsh wizard, please help fix [issue 11](https://github.com/mattvonrocketstein/smash/issues/11)!</sub>

-------------------------------------------------------------------------------

<a id="configuration"></a>
####Configuration
Lorem Ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum

-------------------------------------------------------------------------------

<a id="plugins"></a>
####Plugins / Extensions

Smash has lots of plugins that extend or modify the core behaviour.  Some plugins are turned on by default, some are complete but opt-in, and some are works in progress, demonstrations, or proof-of-concepts.  The smash core tries to be small and just includes the essential stuff, so it's safe to assume that most of the functionality described on this page is effected by plugins.

**Writing new plugins** is fairly easy, but may not be necessary for your application (see the [configuration section](#configuration)). If you do need to write a plugin, read on, but first a bit of background.  Smash is built on top of [IPython](http://ipython.org/) and is in fact itself an IPython extension.  *Smash plugins are essentially ipython extensions which require smash*, but it can be useful to differentiate the terminology.  Before going much further it's probably a good idea to check out the existing IPython docs on [writing extensions](http://ipython.org/ipython-doc/dev/config/extensions/).

If you want to do simple stuff like just writing new commands then a tutorials for [writing IPython magic](#http://catherinedevlin.blogspot.com/2013/07/ipython-helloworld-magic.html) will probably be all you need.

If you want to get your hooks into smash-specific events like "directory change" or "virtual environment deactived" then read [this documentation](#TODO) about the smash event system. For an example of writing new tab-completion stuff, check out [the code for the fabric completer](#TODO).  For an example of input preprocessing see the [currency converter code](#TODO).  Foran example of all-else-fails input processing (meaning input was neither bash nor python) see [the do-what-I-mean code](#TODO).

-------------------------------------------------------------------------------

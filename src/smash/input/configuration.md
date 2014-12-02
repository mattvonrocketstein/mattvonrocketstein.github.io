title: Configuration
menu-position: 6
---

Smash configuration, like smash libraries and executables, are stored in `~/.smash`.  The main configuration file is `~/.smash/etc/config.py`.  If your [editor is configured](#editor), you can open the main configuration file at any time from typing `ed_config` inside of smash.

<a id="inheritance-shell"></a><a id="inheritance"></a>
####Inheriting existing shell configuration
By default smash will try to honor existing bash aliases and functions.  If you do not want your bash aliases migrated into Smash, ensure the `load_bash_aliases` settings is False.

~~~~{.python}
    Smash.load_bash_aliases = False
~~~~

If you do not want to be able to run legacy bash functions from your shell, ensure the `load_bash_functions` setting is False.  Note that only bash functions mentioned in your profile, .bashrc, etc will be loaded.  (Loading bash functions from arbitrary files that you source is [issue #15](https://github.com/mattvonrocketstein/smash/issues))

~~~~{.python}
    Smash.load_bash_functions = False
~~~~


<a id="inheritance-ipython"></a>
####Inheriting existing IPython configuration
If you are already using IPython and want to load aspects of existing profile configuration, add something like this to `~/.smash/config.py`:

~~~~{.python}
    load_subconfig('ipython_config.py', profile='default')
~~~~


<a id="editor"></a>
####Editor configuration
There are several reasons that it can be useful to let smash know about your editor.  For example smash, like IPython, can help you quickly open and edit the correct source file for any given python object.  (To test this out you can try typing `import webbrowser; ed webbrowser`).
Also Zsh-style [paired openers / suffix aliases](plugins.html#dwim-suffix) are supported by the [DWIM plugin](plugins.html#dwim).

Editor settings are determined according to the following policy: **1** If `~/.smash/etc/editor.json` exists, it should have the form
~~~~{.json}
 {
   "console":"some_editor_invocation",
   "window_env":"some_editor_invocation"
 }
~~~~


Note that invocation lines may include flags, for instance *emacsclient -n* or  *nano --softwrap --quiet* is fine.  If there is no `editor.json` file or it is not formatted correctly, then the value of the $EDITOR environment variable will be used.  Finally, if no other options are found, a default editor will be assigned to you based on your operating system.  You can always type `ed_editor` inside of smash to open `~/.smash/etc/editor.json`.

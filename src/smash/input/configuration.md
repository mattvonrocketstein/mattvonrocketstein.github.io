title: Configuration
menu-position: 6
---

Smash configuration, like libraries and executables, are stored in ~/.smash.  The main configuration file is `~/.smash/config.py`.  If your [editor is configured](#editor), you can open the configuration file at any time from typing `ed_config` inside of smash.

<a id="editor"></a>
####Editor configuration
It helps to let smash know about your editor, because in some circumstances it's useful to let it open files for you.  (See for example the zsh-style [suffix aliases supported by the DWIM plugin](#suffix-aliases-and-openers), or try `import webbrowser; ed webbrowser`.)  You can setup your preferred editor using `~/.smash/etc/editor.json`.  Afterwards, regardless of what editor you use, your edit command will be `ed` or `edit`. This edit command can take input in the form of filenames, "file:row:column" syntax, or python objects.


<a id="inheritance"></a>

####Bash confguration inheritance

* set `_.Smash.load_bash_aliases=True` in ~/.smash/config.py

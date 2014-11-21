title: Plugins
menu-position: 4
---

Smash plugins are essentially IPython extensions which require smash.

<a id="list"></a>

[Liquidprompt](#liquidprompt) |
[Autojump](#autojump) |
[Do What I Mean](#dwim) |
[Change-dir Hooks](#cd-hooks) |
[Python Tools Completion](#ptc) |
[Python Virtual Environments](#virtualenv) |

<a id="ptc"></a>
####Python Tools Completion

This plugin provides completion options for common python tools like [Fabric](#), [IPython](#), [setup.py](#), [flake8](#)/[pyflakes](#) [tox](#), and other stuff you probably use on a daily basis.  Completion for each command is at least over command line options/flags, but in some cases there are other context clues that can be provided:

* fabric completion also works over task names.
* tox completion includes available environments according to tox.ini when using "tox -e"
* ipython completion includes available profiles when using --profile option

#####Configuration Options:
* _.PythonTools.verbose: set True to see debug messages

-------------------------------------------------------------------------------
<a id="autojump"></a>
####Autojump
Smash ships with an integrated version of the wonderful [autojump](https://github.com/joelthelion/autojump) command line tool, which uses information from change-dir to maintain a ranked list of flexible short cuts.  In other words after you've cd'd into /foo/bar/baz/qux at least once, you can use `j qux` or `jump qux` to take you there afterwards.  Tab completion over jump-destinations is automatically enabled so that `j qu<TAB>` does what you'd expect.

#####Configuration Options:
* _.AutoJump.verbose: set True to see debug messages

-------------------------------------------------------------------------------

<a id="liquidprompt"></a>
####Liquidprompt

This plugin provides prompt rendering via the wonderfully dynamic [liquidprompt tool](#https://github.com/nojhan/liquidprompt).  Liquidprompt has rich options for configuration and it's recommended that you [configure it in the normal way](https://github.com/nojhan/liquidprompt#features-configuration), but, some of these options can be overridden from `~/.smash/config.py` (see below).

#####Configuration Options:
* `_.LiquidPrompt.verbose`: set True to see debug messages
* `_.LiquidPrompt.float`: set True to insert more space around prompt
* `_.LiquidPrompt.prompt_append`: set a suffix on the prompt ('\n>' is a good one for legibility)

-------------------------------------------------------------------------------

<a id="cd-hooks"></a>
####Change directory hooks

Lorem Ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ip

#####Configuration Options:
* `_.ChangeDirHooks.verbose`: set True to see debug messages


-------------------------------------------------------------------------------

<a id="dwim"></a>
####Do What I mean

The DoWhatIMean plugin supports zsh-style alias suffixes, automatic directory changing, opening of urls, etc.  For a feature summary, see the input -> action list below.

| On Input             | Run test                          | If test is true Action is  |
| -------------------- |---------------------------------- | -------------------------- |
| http://foo/bar       | *(none)*                          | open with browser          |
| foo.bar              | is foo.bar executable?            | run as usual               |
| foo.bar              | is bar a defined suffix_alias?    | open with specified opener |
| foo/bar              | is bar a directory?               | change-dir to bar          |


#####Configuration Options:
* `DoWhatIMean.verbose`: set True to see debug messages
* `DoWhatIMean.suffix_aliases`: map of `{file_extension -> open_command}`

-------------------------------------------------------------------------------

<a id="virtualenv"></a>
####Virtual Environment

Smash has sophisticated virtualenv support which is useful particularly if you're working on multiple projects or working with multiple versions of the same requirements.  Activating/deactivating venvs is done with `venv_activate some_dir` and `venv_deactivate`, respectively.  This not only updates your $PATH, but updates the python runtime.  Modules from the new environment can now be imported directly, and side-effects from the old virtualenv are purged.  To activate and deactivate virtualenv's automatically, take a look at the [project manager documentation](/project_manager.html).

#####Commands:
* `venv_activate some_dir`: activate a specific virtual environment
* `venv_deactivate some_dir`: deactivates the current virtual environment

#####Configuration Options:
* VirtualEnv.verbose: set True to see debug messages

--------------------------------------------------------------------------------

<a id="writing-new"></a>
##Writing new plugins

Writing new plugins is fairly easy, but may not be necessary for your application (see the [configuration summary](#configuration) or the [main configuration documentation](/configuration.html)). If you do need to write a plugin, read on, but first a bit of background.  Smash is built on top of [IPython](http://ipython.org/) and is in fact itself an IPython extension.  *Smash plugins are essentially ipython extensions which require smash*, but it can be useful to differentiate the terminology.  Before going much further it's probably a good idea to check out the existing IPython docs on [writing extensions](http://ipython.org/ipython-doc/dev/config/extensions/).

If you want to do simple stuff like just writing new commands then a tutorials for [writing IPython magic](#http://catherinedevlin.blogspot.com/2013/07/ipython-helloworld-magic.html) will probably be all you need.

If you want to get your hooks into smash-specific events like "directory change" or "virtual environment deactived" then read [this documentation](#TODO) about the smash event system. For an example of writing new tab-completion stuff, check out [the code for the fabric completer](#TODO).  For an example of input preprocessing see the [currency converter code](#TODO).  Foran example of all-else-fails input processing (meaning input was neither bash nor python) see [the do-what-I-mean code](#TODO).

-------------------------------------------------------------------------------

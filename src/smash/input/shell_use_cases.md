title: Use Cases: Shell
menu-position: 2
---

This section is just an overview.  You could also jump directly to the plugin documentation for the relevant plugins: [Liquidprompt](#liquidprompt), [Autojump](#autojump), [Do What I Mean](#dwim), or [Change-dir Hooks](#cd-hooks).


-------------------------------------------------------------------------------

####Considerations <a id="considerations"></a>

To avoid conflicting with python namespaces, commands that involve period (`.`) will be translated to use an underscore (`_`) instead.  Any command invocations that use a hyphen (`-`) should work normally.

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

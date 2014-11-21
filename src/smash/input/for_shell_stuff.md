title: Use Cases: Shell
menu-position: 2
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
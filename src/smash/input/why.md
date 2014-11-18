title: But.. why?
menu-position: 3
---

So, *why build yet another shell?*  Put simply, shells still kind of suck.  The main problem is that classic shells are inflexible and not easy to extend.  If you do manage to extend them, you probably had to do it with shell code, and so the result is something that's fragile and difficult to maintain.  Just for the sake of an example, let's consider the problem of a "do what I mean" extension for your shell, where if you type something that looks like a url then the url is opened automatically for you.  To effect a pre-exec style hook in bash, you'll have to do [black magic](http://www.twistedmatrix.com/users/glyph/preexec.bash.txt) with the `DEBUG` trap (ugh).  Zsh is better, but of course you'll still be writing (or at least invoking) your hooks in shell code.  This works at first, but things start to get messy when issues of code-reuse come up, or if you want to [invoke hooks conditionally](#pm), etc.  If you still think the do-what-i-mean puzzle sounds easy to solve in your shell, consider the problem of colorizing random structured data (maybe json or server logs) sent to stdout!

SmaSh's close integration with python itself is a huge plus, but it's also just a side effect of fixing the main problems around making a shell that is truly flexible and nontrivially extensible.

# pydoer
A threaded modular python job scheduler/worker.

## Purpose
This was just an experiement to make a modular, threaded, and scheduled python function runner.

It starts as a plugin framework that loads all plugins, a plugin manager that can execute all
or one plugin by name. Each plugin has an interval in minutes, each plugin is run in a thread
that waits for a scheduler to fun.

## Warnings
I put this together on a Saturday, on the couch, while binge watching television; it isn't for
production use, I'm not sure I'll even use this.

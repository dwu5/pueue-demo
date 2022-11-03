#!/bin/bash

cd pyfile
pueue group add 0123
pueue group add 4567
pueue clean
pueue add -g 0123 failure
pueue add -g 0123 -l A python taskA.py
pueue add -g 4567 -l BB python taskB.py
pueue add -g 0123 -l CCC python taskC.py
pueue add -g 4567 -l sleep sleep 10
#!/bin/sh

tmux new-session -d "vis"
tmux split-window -v "mpsyt"
tmux -2 attach-session -d

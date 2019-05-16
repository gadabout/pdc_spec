#!/bin/bash
# Set up ansd install the environment to run peek.com test cases
if [ ! $(which ruby) ]; then
    echo "Error: Ruby not found. Pleae install ruby"
    exit 1
fi

gem install rspec
rspec --init


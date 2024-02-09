#! /usr/bin/bash

curl "$1" -s -L -I -o /dev/null -w '%{url_effective}'
# -o output to /dev/null
# -I don't actually download, just discover the final URL
# -s silent mode, no progressbars
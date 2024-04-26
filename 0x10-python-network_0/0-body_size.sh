#!/bin/bash
# get content-size of body
curl -sI $1 | grep "Content-Length" | cut -d " " -f2

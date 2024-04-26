#!/bin/bash
# http_code
curl -o /dev/null -sw "%{http_code}" $1

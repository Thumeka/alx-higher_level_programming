#!/bin/bash
# Take in URL, add header variable, displays X-School-User-Id
curl -s -H "X-School-User-Id":98 "$1"

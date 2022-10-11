#!/bin/bash

PROJFILE='proj1.py'
TESTFOLDER='public_instances'

if [[ $# != 2 ]] ; then
	echo "Usage: ${0} <project> <test_folder>"
	echo "Example: ${0} ${PROJFILE} ${TESTFOLDER}"
	exit 1
fi

SOLUTION="$1"
TESTSFOLDER="$2"

./run.sh ${SOLUTION} ${TESTSFOLDER}/*.hsp

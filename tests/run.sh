#!/bin/bash

SOLUTION='proj1.py'
TESTEG=FIXME

if [ $# -lt 2 ] ; then
	echo "Usage: ${0} <solution> <test1> <test2> ..."
	echo "Example: ${0} ${SOLUTION} ${TESTEG}"
	exit 1
fi

RED='\033[0;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SOLUTION=${1}
HYP='.hyp'
OUT='.out'
DIFF='.diff'
CHECK='.check'

DIFFDIR='diff/'
HYPDIR='hyp/'
OUTDIR='out/'
CHECKDIR='check/'

CHECKER='hsp-checker'

RUN='python3'

shift
failures=0

for test in "$@"
do
	testname=$(basename -as .hsp "${test}")
	testhyp=${HYPDIR}${testname}${HYP}
	testout=${OUTDIR}${testname}${OUT}
	testdiff=${DIFFDIR}${testname}${DIFF}
	testcheck=${CHECKDIR}${testname}${CHECK}
	
	echo "Testing ${test}..."
	${RUN} ${SOLUTION} < ${test} > ${testhyp}
	diff -q ${testout} ${testhyp} > ${testdiff}
	rv_diff=$?

	if [ ${rv_diff} == 0 ] ; then
		echo "Test ${testname} PASSSED. :)"
	else
		echo "Test ${testname} FAILED. :("
		echo "Checking with ${CHECKER} what is wrong..."
		./${CHECKER} ${test} ${testhyp} > ${testcheck}

		let failures="1+${failures}"
	fi
done

echo -e "Failures: ${failures}"


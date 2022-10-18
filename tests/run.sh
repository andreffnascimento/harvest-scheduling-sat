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
CHECK='.check'

HYPDIR='hyp/'
OUTDIR='out/'
CHECKDIR='check/'

CHECKER='hsp-checker'

RUN='python3'

shift
rm overall.txt

for test in "$@"
do
	testname=$(basename -as .hsp "${test}")
	testhyp=${HYPDIR}${testname}${HYP}
	testout=${OUTDIR}${testname}${OUT}
	testcheck=${CHECKDIR}${testname}${CHECK}
	
	echo "Testing ${test}..."
	ts=$(date +%s%N)
	${RUN} ${SOLUTION} < ${test} > ${testhyp}
	tt=$((($(date +%s%N) - $ts)/1000000)) 
	echo -e "${testname}\t|\t${tt} ms" >> overall.txt

	./${CHECKER} ${test} ${testhyp} > ${testcheck}
	
done

#!/bin/bash
cd U:/Experiments/sleepHSP_followup/sleepHSPfollowup/
BASE=$2
echo ${BASE}
git checkout --orphan $BASE
git fetch origin master
cp -a $1/$2 U:/Experiments/sleepHSP_followup/sleepHSPfollowup/
cd U:/Experiments/sleepHSP_followup/sleepHSPfollowup/
git add .
git commit -m "$1 created"
git push origin $BASE
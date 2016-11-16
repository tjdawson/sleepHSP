#!/bin/bash
home=`pwd`
for d in */ ; do
    dir=${d%/}
    cd U:/Experiments/sleepHSP\ followup/sleepHSPfollowup/
    git checkout -b $dir
    cd home
    cp -a $d. U:/Experiments/sleepHSP\ followup/sleepHSPfollowup/
    cd U:/Experiments/sleepHSP\ followup/sleepHSPfollowup/
    git add .
    git commit -m "$dir created"
    git push origin $dir
    cd home
done

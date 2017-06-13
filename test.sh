#!/usr/bin/env bash

timestamp() {
	date +"%d-%T"
}

while true; do
        thestamp=$(timestamp)
        printf "${thestamp}\n" >> results.log
	python speedtest-cli &> results/${thestamp}.log
        cat results/${thestamp}.log |  grep " ms\|Download: \|Upload: " >> results.log
        sleep 10m
done

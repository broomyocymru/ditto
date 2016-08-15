#!/usr/bin/env bash
printf "getting ditto-cli dependencies \n"
pip install -r requirements.txt --upgrade

printf "installing ditto-cli \n"
pip install -e .
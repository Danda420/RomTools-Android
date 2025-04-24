#!/system/bin/sh

### IMPORT FUNCTIONS AND VARIABLES FROM TOOLS ###
script_dir=$(dirname "$(realpath "$0")")
MAIN="${script_dir%%/tool/*}"
source $MAIN/tool/functions
#################################################
clear
#################################################

### write script here ###

echo $PWD
echo Hello

#################################################
restart_tool
exit
#################################################

#!/bin/bash
# University of Victoria - Auto VM Shelving System - Setup Script
# By Rahim Khoja (rahim@khoja.ca)
# https://www.linkedin.com/in/rahim-khoja-879944139/

echo
echo -e "\033[0;31m░░░░░░░░▀▀▀██████▄▄▄"
echo "░░░░░░▄▄▄▄▄░░█████████▄ "
echo "░░░░░▀▀▀▀█████▌░▀▐▄░▀▐█ "
echo "░░░▀▀█████▄▄░▀██████▄██ "
echo "░░░▀▄▄▄▄▄░░▀▀█▄▀█════█▀"
echo "░░░░░░░░▀▀▀▄░░▀▀███░▀░░░░░░▄▄"
echo "░░░░░▄███▀▀██▄████████▄░▄▀▀▀██▌"
echo "░░░██▀▄▄▄██▀▄███▀▀▀▀████░░░░░▀█▄"
echo "▄▀▀▀▄██▄▀▀▌█████████████░░░░▌▄▄▀"
echo "▌░░░░▐▀████▐███████████▌"
echo "▀▄░░▄▀░░░▀▀██████████▀"
echo "░░▀▀░░░░░░▀▀█████████▀"
echo "░░░░░░░░▄▄██▀██████▀█"
echo "░░░░░░▄██▀░░░░░▀▀▀░░█"
echo "░░░░░▄█░░░░░░░░░░░░░▐▌"
echo "░▄▄▄▄█▌░░░░░░░░░░░░░░▀█▄▄▄▄▀▀▄"
echo -e "▌░░░░░▐░░░░░░░░░░░░░░░░▀▀▄▄▄▀\033[0m"
echo "---University of Victoria - Auto VM Shelving System - Setup Script---"
echo "---By: Rahim Khoja (rahim@khoja.ca)---"
echo

# Requirements: Redhat Linux 9 Base Intsall
#               IPV4 Public IP, (or at least a public IP's Port 443 routed)
#               Internet Access
#               Access to Run OpenStack CLI Commands
#               Ability to connect to Request Tracker API

# Stop on Error
set -eE  # same as: `set -o errexit -o errtrace`

# Dump Vars Function
function dump_vars {
    if ! ${STATUS+false};then echo "STATUS = ${STATUS}";fi
    if ! ${LOGFILE+false};then echo "LOGFILE = ${LOGFILE}";fi
    if ! ${SCRIPTDIR+false};then echo "SCRIPTDIR = ${SCRIPTDIR}";fi
    if ! ${DEBUG+false};then echo "DEBUG = ${DEBUG}";fi
    if ! ${PUBLICIP+false};then echo "PUBLICIP = ${PUBLICIP}";fi
    if ! ${TIMESTAMP+false};then echo "TIMESTAMP = ${TIMESTAMP}";fi
    if ! ${finish+false};then echo "finish = ${finish}";fi
    if ! ${nginx+false};then echo "nginx = ${nginx}";fi
}

# Failure Function
function failure() {
    local lineno=$1
    local msg=$2
    echo ""
    echo -e "\033[0;31mError at Line Number $lineno: '$msg'\033[0m"
    echo ""
    if [[ $DEBUG -eq 1 ]]; then
      dump_vars
    fi
}

# Failure Function Trap
trap 'failure ${LINENO} "$BASH_COMMAND"' ERR

# Default Variriable Declaration
LOGFILE=/var/log/uvic_auto_shelve_system_setup.log
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DEBUG=1
STATUS="Initializing"
TIMESTAMP="$( date +%s )"
#PUBLICIP="$(dig @resolver1.opendns.com ANY myip.opendns.com +short)"
finish="-1"
nginx="0"

# Check the bash shell script is being run by root
STATUS="Check - Script Run as Root user"
if [[ $EUID -ne 0 ]];
then
    echo "This script must be run as root" 1>&2
    exit 1
fi

STATUS="Starting Installation"
echo "$(date \"+%FT%T\") $STATUS" >> "${LOGFILE}"

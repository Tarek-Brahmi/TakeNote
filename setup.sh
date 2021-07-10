#!/bin/bash

readonly DB_NAME="TAKENOTE"
readonly NOTES_TABLE="NOTES"
readonly USERS_TABLE="USERS"
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'

check_root() {
    printf "\e[1;31m[\e[0m+\e[1;31m] \e[5mCheck the root previlages :\e[25m${NC}\n"
    if [[ $EUID -ne 0 ]]; then
        printf "${RED}This script must be run with root previlages ${NC}\n"
        exit 1
    fi
}
check_requirement() {
    printf "\e[1;31m[\e[0m+\e[1;31m] \e[5mCheck and Install requirements :\e[25m${NC}\n"
    ## for python===3.*
    for_python3=$(type -P python3 >/dev/null 2>&1 && echo "1")

    if [[ $for_python3 != "1" ]]; then
        printf "${RED}python3 is not installed !${NC}\n"
        sudo apt install python3

    fi

    ## for pip===3.*
    for_pip3=$(type -P pip3 >/dev/null 2>&1 && echo "1")
    if [[ $for_pip3 != "1" ]]; then
        printf "${RED}pip3 is not installed !${NC}\n"
        sudo apt install python3-pip

    fi
    ## for my sql server
    sudo apt install mysql-client-core-8.0
    sudo apt install mariadb-client-core-10.3
    ## for pyQT5 and mysql-connector
    pip3 install mysql-connector-python==8.0.25
    pip3 install PyQt5==5.14.1


}

createDBandTables() {
    printf "\e[1;31m[\e[0m+\e[1;31m] \e[5mCreating Database and Tables:\e[25m${NC}\n"
    printf "${GREEN}Enter the root password ${NC}\n"

    printf "\e[1;31m[\e[0m+\e[1;31m]${NC} trying to create a database for your notes named ${RED}${NOTES_TABLE}${NC} with two tables ${GREEN}${NOTES_TABLE}${NC} and ${GREEN}${USERS_TABLE}${NC} :\n"
    mysql -uroot -p <"db.sql"
    printf "${GREEN}Done ! ${NC}\n"

    ## get the username and password for login details
    printf "Enter a ${GREEN}username${NC} and ${GREEN}password${NC} to make your notes private .. it is well used to log in later:\n"
    read -p "Username: " username
    read -sp "Password: " password

    printf "\n\e[5m${GREEN}username${NC}:${username} and ${GREEN}password${NC}:${password}\e[25m\n"

    python3 CrateDbTables.py $username $password
    printf "${GREEN}All Done ! You can Log in now with \n\t\t${BLUE}username${NC}:${username} \n\t\t${BLUE}password${NC}:${password}${NC}\n\t run python3 main.py to getStarted \n"
}

check_root
check_requirement
createDBandTables

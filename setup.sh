#!/bin/bash
readonly DB_NAME="TAKENOTE"
readonly NOTES_TABLE="NOTES"
readonly USERS_TABLE="USERS"
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m' 
BLUE='\033[0;34m'
printf "trying to create a database for your notes named ${RED}${NOTES_TABLE}${NC}  with two tables ${GREEN}${NOTES_TABLE}${NC} and ${GREEN}${USERS_TABLE}${NC} :\n"
read -p "Username: " username
read -sp "Password: " password
echo
echo Thankyou $uservar we now have your login details

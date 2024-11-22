#!/bin/bash

echo "Enter the password to get the flag:"
read -s password

if [ "$password" == "secret123" ]; then
    echo "Correct! Here is the flag: CTF_{password_success}"
else
    echo "Incorrect password. Try again!"
fi

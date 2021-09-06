#!/bin/bash


echo """
 _   _      _ _______       _   
| | | |    | | | ___ \     | |  
| |_| | ___| | | |_/ / ___ | |_ 
|  _  |/ _ \ | | ___ \/ _ \| __|
| | | |  __/ | | |_/ / (_) | |_ 
\_| |_/\___|_|_\____/ \___/ \__|
                                
"""
rm -rf Perry-Userbot
git clone https://github.com/Perry-xD/Perry-Userbot
cd Perry-Userbot
python3 -m userbot

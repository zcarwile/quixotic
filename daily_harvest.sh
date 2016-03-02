#!/bin/bash
cd /Users/zcarwile/Documents/quixotic
./harvest_email.py
./harvest_calendar.py
./harvest_rescue_time.py
./qetl.py
./sanitize.py
cd ~

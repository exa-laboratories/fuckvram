#!/bin/bash  

SCREEN_NAME=vram
WORK_DIR=/tmp/exalabsiscool
REPO=https://github.com/exa-laboratories/fuckvram.git

# Print cool banner
echo "
     ##########      ######          #######       ##########         #          ##
  ################    #######       ######      ################      #          ##
 #######      ####     #######     ######      ######     #######     #   ####   ######   #####
######                   ######  ######                    ######     #      ##  ##    #  ##
 ######                   ############                      ######    #  ##  ##  ##    #     ##
   ############             #########                 ############    #  ## ###  ### ##  ##  ##
  #############            ##########           ##################
#######                   ############        #######       ######
######                   ######  #######      #####         ######
#######       ####     #######    #######    #######      ########
  ################    ######        #######   ####################
     ##########     #######          #######    #########    #####

               Copyright 2024, Exa Laboratories, Inc.
                    https://exalaboratories.com
"

# Validate the webhook url 
if [ -z "$WEBHOOK_URL" ]; then
  echo "You need to specify the webhook url env var: WEBHOOK_URL=$WEBHOOK_URL"
  echo "e.g.: \$ export WEBHOOK_URL=https://example.com/webhook && curl -s ... | bash"
  exit 1
fi

# Clone the repo and cd into it
if [ -d $WORK_DIR ]; then
  cd $WORK_DIR && git pull
else 
  git clone $REPO $WORK_DIR && cd $WORK_DIR
fi

# Install deps
pip install -r requirements.txt

# Run the daemon
echo "Running the daemon using GNU screen with the name \"$SCREEN_NAME\"."
screen -dmS $SCREEN_NAME $SHELL -c "WEBHOOK_URL=$WEBHOOK_URL python watchdog.py 2>>/tmp/fuckvram.log"

cd -

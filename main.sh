#!/bin/sh

#  main.sh
#  
#
#  Created by Mutasem Dmour on 11/4/14.
# to run, open terminal, sh main.sh

/usr/local/homebrew/bin/mysql.server start
/usr/local/homebrew/bin/mysql -u root -e "use classes; truncate table section"
cd ~/dropbox/isiscrawler
# to edit which terms, and which focus areas to update, edit updateDB.py
python updateDB.py
# to edit which pages to update, edit buildHTML.py
python buildHTML.py
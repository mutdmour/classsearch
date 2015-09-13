## to start server 
## /usr/local/homebrew/bin/mysql.server start
## if error is _mysql_exceptions.OperationalError: (2002, "Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)")

## to clear mysql database
## /usr/local/homebrew/bin/mysql -u root
## use classes;
## truncate table section

from scrap import scrap;
from models import section;

def updateDB():
    ## this function updates the database with the latest from isis.jhu.edu for each term and each focus area
    for term in ["Fall 2015"]:
        print("");
        print(term);
        for focusA in ["instrumentation","celltissue","systems","imaging","computational"]:
            print("");
            print(focusA);
            file = open("input/"+focusA+".txt");
            for classNumber in file:
                sec = section(classNumber.strip(),term,focusA);
            ##    print(classNumber.strip());
                scrap(sec);
                ## this function scraps isis for data and updates the database
            file.close();

if __name__ == "__main__":
    updateDB();

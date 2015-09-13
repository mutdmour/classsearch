from post_request import post_request
from mine_data import mine_data

def scrap(sec):
    print(sec.term + " " + sec.classNumber);
    htmlPage = post_request(sec.term, sec.classNumber);
    ##this function returns the html page of the results of the isis search expanded
    print(sec.classNumber + "?")
    mine_data(htmlPage, sec);
    ##this function mines the html page for the needed data and saves it to the database

if __name__ == "__main__":
    print scrap("Fall 2014","510.311","instrumentation");

from bs4 import BeautifulSoup
##http://www.crummy.com/software/BeautifulSoup/bs4/doc/#

def mine_data(htmlPage, sec):
    class_details = []
    soup = BeautifulSoup(htmlPage,"lxml") ##this puts it in Soup form, making it easier to mine
    soup = soup.find(id="results") ##finds the table of results, if this fails, then there are no results
    if soup != None:
        for tr in soup.find_all('tr'):
            if tr.get('class') == [u'even']:
                det = []
                for td in tr.find_all('td'):
                    det.append(td.get_text().strip().encode('latin_1','ignore')) ##adds the name, class number, day-times, instructor and status
                sec.update1(det[0],det[1],det[3],det[4],det[5],det[6])
            elif tr.find(id="classdetailstext") != None:
                div = tr.find(id="classdetailstext")
                tr = div.table.extract().tr.extract()
                det = []
                for td in tr.find_all("td"):
                    det.append(td.span.get_text().encode('latin_1','ignore')) ##adds the level, credits, area, and other details
                if len(det) == 5:
                    sec.update2(det[0],det[1],det[2],det[3],det[4])
                elif len(det) == 4:
                    sec.update2(det[0],"",det[1],det[2],det[3])
                    print("yo, pay attention, check that it does not have area field")
                sec.update_description(div.span.extract().get_text().encode('latin_1','ignore'))
#                print(div)
                div = BeautifulSoup(str(div).replace("<br/>"," \n ").replace("<strong>","\n"));
                rest = div.get_text().replace("Description","").replace("Textbook Info [+]","").strip().encode('latin_1','ignore')
                sec.update_rest(rest) ##adds the rest of the details, including schedule and preReqs
                sec.save()
                print(sec)
    else:
        sec.update_status("unavailable");
        sec.save()
        print("nop")
if __name__ == "__main__":
    from post_request import post_request
    from models import section
    term = "Spring 2014"
    FA = "instrumentation"
    CN = "520.448"
    mine_data(post_request(term,CN),section(CN,term,FA))
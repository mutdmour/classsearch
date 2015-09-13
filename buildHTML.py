from chameleon import PageTemplate, PageTemplateFile
from models import section,find
import time

def build(term,focusA):
    data = find(term, focusA, True)
    template = PageTemplateFile("template.txt","")
    #    h = "///Users/mutdmour/Dropbox/IsisCrawler/public_html/"
    h = "http://classsearch.bme.jhu.edu/"
    t = template(Term=term,FocusArea=focusA,all=data, host=h, time=time.strftime("%c"))
    file = open("./public_html/{0}/{1}.html".format(term,focusA),'w')
    file.writelines(t)
    file.close()
if __name__ == "__main__":
    for term in ["Fall 2015"]:
        for focusA in ["instrumentation","celltissue","computational","imaging","systems"]:
            build(term,focusA)

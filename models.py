import _mysql
##https://github.com/farcepest/MySQLdb1/blob/master/doc/user_guide.rst
db = _mysql.connect(host="localhost",user="root",db="classes")

def find(term, focusArea,status):
    if status == True:
        q = """select * from section where term = "{0}" and focusArea = "{1}" and status != "unavailable" order by classNumber;""".format(term,focusArea)
    else:
        q = """select * from section where term = "{0}" and focusArea = "{1}" and status = "unavailable" order by classNumber;""".format(term,focusArea)
    db.query(q)
    result = db.store_result()
    all = []
    for i in range(result.num_rows()):
        val = result.fetch_row()[0]
        sec = section("","","")
        sec.update_all(val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10],val[11],val[12].replace('\n\n','\n').replace('\n','<br>'),val[13],val[14])
        all.append(sec)
    return all
class section():
    def __init__(self, CN, term, FA):
        self.classNumber = CN
        self.term = term
        self.focusArea = FA
        self.name=""
        self.status=""
        self.enrollmentLimit=""
        self.rest=""
        self.description=""
        self.instructor=""
        self.area=""
        self.level=""
        self.credits=""
        self.department=""
        self.location=""
        self.times=""
    def update_all(self, CN, FA, name, term, times, description, status, instructor, level, area,credits,enrollmentLimit,rest,department,location):
        self.classNumber = CN
        self.focusArea=FA
        self.term = term
        self.name = name
        self.location = location
        self.times = times
        self.instructor = instructor
        self.status = status
        self.description = description
        self.level = level
        self.area = area
        self.credits = credits
        self.enrollmentLimit = enrollmentLimit
        self.department = department
        self.rest = rest
    def update_status(self, status):
        self.status = status
    def update1(self, classNumber, name, location, times, instructor,status):
        self.classNumber = classNumber
        self.name = name
        self.location = location
        self.times = times
        self.instructor = instructor
        self.status = status
    def update_description(self, description):
        self.description = description.replace("\"","'")
    def update2(self, level,area,credits,department,enrollmentLimit):
        self.level = level
        self.area = area
        self.credits = credits
        self.enrollmentLimit = enrollmentLimit
        self.department = department
    def update_rest(self, rest):
        self.rest = rest.replace("\"","'")
    def save(self):
        q = """insert into section values('{0}','{1}',\"{2}\",'{3}','{4}',\"{5}\",'{6}','{7}','{8}','{9}','{10}','{11}',\"{12}\",'{13}','{14}')""".format(self.classNumber, self.focusArea, self.name,self.term,self.times,self.description,self.status,self.instructor,self.level,self.area,self.credits,self.enrollmentLimit,self.rest,self.department,self.location);
        #   print(q)
        db.query(q)
    #    print(self)
    def __str__(self):
        return self.focusArea + ": " + self.classNumber + " " + self.name

if __name__ == '__main__':
    #   var = section('En.520.345','Fall 2014','systems')
    #   var.save()
    print(find("Fall 2014","celltissue",True));

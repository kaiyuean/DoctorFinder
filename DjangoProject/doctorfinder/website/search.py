from .sort import RatingSort, AvailabilitySort
from .models import Doctor, Insurance

class Search():
    def __init__(self, speciality, city, state, zip, insurance):
        self.speciality = speciality
        self.city = city
        self.state = state
        self.zip = zip
        self.insurance=insurance

    def doSearch(self):
        docResults = Doctor.objects.filter(speciality=self.speciality, city=self.city, state=self.state, zip=self.zip)
        insResults = Insurance.objects.filter(name=self.insurance)
        docList=[doc.username_id for doc in docResults]
        insList=[doc.doctor_id for doc in insResults]
        inters_list= list(set(docList).intersection(insList))

        doctors=[]
        for doc in inters_list: 
            doctors.append(Doctor.objects.get(username=doc))
               
        self.results = self.sortType.sort(doctors)

    def setSort(self, sortType):
        self.sortType = sortType

    def reSort(self, type):
        if type == 'Rating':
            self.setSort(RatingSort())
        elif type == 'Availability':
            self.setSort(AvailabilitySort())
        self.results = self.sortType.sort(self.results)





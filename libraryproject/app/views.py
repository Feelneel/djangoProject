from django.shortcuts import render
from . models import Book
# Create your views here.

# 
# 
# 
# 



from datetime import datetime


def index(req):
    allbooks = Book.objects.all()    #ORM
    print(allbooks)
    # context={"myname":"ITV"}
    # return render(req,'index.html',context)

    myname = "Neel"
    # return render(req,'index.html',{"myname" : myname})
    
    print(datetime.now())
    curdate = (datetime.now())
    hour = datetime.now().hour
    print(hour)
    context = {"myname" : myname, "curdate": curdate, "hour": hour, "allbooks": allbooks}
    
    return render(req,'index.html', context)
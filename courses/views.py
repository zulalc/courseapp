from datetime import date, datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title": "javascript course",
            "description": "javascript course desc",
            "imageUrl": "1.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "python course",
            "description": "python course desc",
            "imageUrl": "2.png",
            "slug": "python-kursu",
            "date": date(2024,9,10),
            "isActive": True,
            "isUpdated": True

            
        },
        {
            "title": "web geliştirme course",
            "description": "web geliştirme course desc",
            "imageUrl": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2024,8,10),
            "isActive": True,
            "isUpdated": True
        }
    ],

    "categories": [
        {"id":1, "name":"programlama", "slug": "programlama"},
        {"id":2, "name":"web geliştirme", "slug": "web-gelistirme"},
        {"id":3, "name":"mobil uygulamalar", "slug": "mobil-uygulamalar"}, 
    ]
}

def index(request):
    # list comphension
    kurslar = [course for course in db["courses"] if course["isActive"] == True]
    kategoriler = db["categories"]

    # for kurs in db["courses"]:
    #    if kurs["isActive"] == True:
    #        kurslar.append(kurs)

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar
    })

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")


def getCoursesByCategory(request, category_name):
    try:
        category_text=data[category_name]  
        return render(request,'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text,
        })
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")
    

#dinamik olan gelir, kurs kategori bilgisini önce alman gerekiyor kurs/category kurs/1 kurstan sonraki herhangi değer
def getCoursesByCategoryId(request, category_id):

    category_list = list(data.keys()) #1-2-3 => progr - web - mobil

    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1] # user 1 2 3 göndersin liste 0 1 2 başlar 

    redirect_url = reverse('courses_by_category', args=[category_name]) #parametre de args ,.,ne

    return redirect(redirect_url)



#return HttpResponse(f'{category} kategorisindeki göre kurs list')
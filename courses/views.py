from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

def index(request):
    return render(request, 'courses/index.html') ##kendi uygulaması altında arar bulamazsa diğerlerine bakar


def kurslar(request):
    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirect_url = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi</h1> <br> <ul>{list_items}</ul>"

    return HttpResponse(html)

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
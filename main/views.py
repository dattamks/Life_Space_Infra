from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render

# Views for each page
def aboutus(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')
def work(request):
    gallery_images = [
        {"image": "assets/img/gallery/gallery1.jpg", "cols": 6},
        {"image": "assets/img/gallery/gallery2.jpg", "cols": 3},
        {"image": "assets/img/gallery/gallery3.jpg", "cols": 3},
        {"image": "assets/img/gallery/gallery4.jpg", "cols": 3},
        {"image": "assets/img/gallery/gallery5.jpg", "cols": 3},
        {"image": "assets/img/gallery/gallery6.jpg", "cols": 6},
        # {"image": "assets/img/gallery/gallery7.jpg", "cols": 6},
        # {"image": "assets/img/gallery/gallery8.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery9.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery10.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery11.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery12.jpg", "cols": 6},
        # {"image": "assets/img/gallery/gallery13.jpg", "cols": 6},
        # {"image": "assets/img/gallery/gallery14.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery15.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery16.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery17.jpg", "cols": 3},
        # {"image": "assets/img/gallery/gallery18.jpg", "cols": 6},
    ]

    return render(request, 'work.html', {
        'gallery_images': gallery_images
    })




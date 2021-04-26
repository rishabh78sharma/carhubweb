from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
  cr = Car.objects.order_by('-created_date')
  paginator = Paginator(cr, 4)
  page = request.GET.get('page')
  paged_car = paginator.get_page(page)
  data = {
    'cr': paged_car,
  }

  return render(request, 'cars/cars.html',data)


def car_detail(request, id):
  single_car = get_object_or_404(Car, pk=id)
  data = {
    'single_car': single_car,
  }
  return render(request, 'cars/car_details.html', data)  



def search(request):
  all_cars = Car.objects.order_by('-created_date')
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      all_cars = all_cars.filter(description__icontains= keyword)

  if 'model' in request.GET:
    model = request.GET['model']
    if model:
      all_cars = all_cars.filter(model__iexact= model)

  if 'body_style' in request.GET:
    body_style = request.GET['body_style']
    if body_style:
      all_cars = all_cars.filter(body_style__iexact= body_style)

  if 'year' in request.GET:
    year = request.GET['year']
    if year:
      all_cars = all_cars.filter(year__iexact= year)

  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      all_cars = all_cars.filter(city__iexact= city) 

  if 'min_price' in request.GET:
    min_price = request.GET['min_price'] 
    max_price = request.GET['max_price'] 
    if max_price:
      all_cars = all_cars.filter(price__gte=min_price, price__lte=max_price)      

  data = {
      'all_cars': all_cars,
   }
  return render(request, 'cars/search.html', data)  
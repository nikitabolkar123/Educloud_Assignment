from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from math import sqrt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from logconfig.logger import get_logger
from .models import School
from .serializers import SchoolSerializer
logger = get_logger()


@api_view(['POST'])
def create_school(request):
    """Create a new school record."""
    try:
        serializer = SchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # if valid then deserialization
        serializer.save()
        return Response({"message": "School data created Successfully", "status": 201, "data": serializer.data},
                        status=201)
    except Exception as e:
        logger.exception(e)
        return Response({"message": str(e), "status": 400, "data": {}}, status=400)


def landing_page(request):
    """Render the landing page."""
    return render(request, 'landing.html')


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate the Euclidean distance between two points."""
    dx = lon2 - lon1
    dy = lat2 - lat1
    distance = sqrt(dx * dx + dy * dy)
    return distance


def calculate_optimized_route(schools):
    """Calculate the optimized route for visiting schools using a nearest neighbor algorithm."""
    num_schools = len(schools)
    if num_schools < 2:
        return [], []

    visited = [False] * num_schools
    optimized_route = [schools[0]]  # it will Start with the first school
    visited[0] = True

    for i in range(1, num_schools):
        current_school = optimized_route[i - 1]
        min_distance = float('inf')  # min_distance variable is set to positive infinity to find the minimum distances.
        nearest_school = None

        for j, school in enumerate(schools):
            if not visited[j]:
                distance = calculate_distance(
                    current_school.latitude, current_school.longitude,
                    school.latitude, school.longitude
                )
                if distance < min_distance:
                    min_distance = distance
                    nearest_school = school

        optimized_route.append(nearest_school)
        visited[schools.index(nearest_school)] = True

    distances = [calculate_distance(
        optimized_route[i].latitude, optimized_route[i].longitude,
        optimized_route[i + 1].latitude, optimized_route[i + 1].longitude
    ) for i in range(num_schools - 1)]  # for loop for to find  distances between consecutive schools.
    return optimized_route, distances


def school_listing(request):
    """Render the school listing page based on the provided pincode."""
    if request.method == 'POST':
        pincode = request.POST.get('pincode')
        schools = School.objects.filter(pincode=pincode)

        if not schools:
            return render(request, 'school_listing.html',
                          {'error_message': 'No schools found for the provided pincode.'})

        optimized_route, distances = calculate_optimized_route(list(schools))

        paginator = Paginator(list(schools), 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'schools': page_obj,
            'optimized_route': optimized_route,
            'distances': distances,
        }
        return render(request, 'school_listing.html', context)

    return render(request, 'landing.html')

from django.shortcuts import render, HttpResponse, redirect
from .forms import MyForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import FileResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method =='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        # for storing hashed password.
        plain_password = request.POST.get('password')
        hashed_password = make_password(plain_password)
        # password stored.
        resi_add = request.POST.get('resi_add')
        office_add = request.POST.get('office_add')
        office_contact = request.POST.get('office_contact')
        area = request.POST.get('area')
        pincode = request.POST.get('pincode')
        user=User(firstname=firstname, lastname=lastname, email=email, password=hashed_password, resi_add=resi_add,office_add=office_add,office_contact=office_contact,area=area,pincode=pincode)
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        home_user = authenticate(request, email=email, password=password)
        if home_user is not None:
            login(request, home_user)
            return redirect('dashboard')
        else:
            # Add error message for invalid credentials
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

# to delete all users
# def delete_users(request):
#     if request.method == 'POST':
        # Delete all User objects
    #     User.objects.all().delete()
    #     return redirect('index')
    # else:
    #     return render(request, 'delete_users.html')
#ends

def profile(request):
    return render(request, "profile.html")

def history(request):
    return render(request, "history.html")

def slot(request):
    form=MyForm()
    return render(request, "slot.html", {'form':form})

def slot_details(request):
    return render(request, "slot_details.html")

def receipt(request):
    return render(request, "receipt.html")

def download_receipt(request):
    # Render the HTML template with context data
    html_string = render_to_string('receipt.html', {'context': 'data'})

    # Create a BytesIO object to write PDF data to
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Use ReportLab to generate the PDF from the HTML string
    p.drawString(100, 100, html_string)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')



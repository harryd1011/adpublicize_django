from django.shortcuts import render, HttpResponse, redirect
from .forms import MyForm
from django.http import FileResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

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
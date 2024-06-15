from django.http import Http404
import datetime
from . import renderers

def pdf_view(request, *args, **kwargs):
  data = {
    'pdf_title': "Factura Rovistar",
    'today': datetime.date.today(), 
    'amount': 39.99,
    'customer_name': 'Jorge Luis Mamani Huarsaya',
    'invoice_number': 1233434,
  }
  return renderers.render_to_pdf('pdf/invoice.html', data)

import os

from pdfjinja import PdfJinja

dirname = os.path.dirname(__file__)
template_pdf_file = os.path.join(dirname, 'input.pdf')

template_pdf = PdfJinja(template_pdf_file)

rendered_pdf = template_pdf({
    "Name": "Vijay",
    "Age": 26,
    "Gender": "Male",
})

output_file = os.path.join(dirname, 'output.pdf')
rendered_pdf.write(open(output_file, 'wb'))
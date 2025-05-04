from pypdf import PdfWriter, PdfReader
import os

path = input("Absolute URL to directory: ")
n = int(input("How many files to merge? "))
pdfs = []
for _ in range(n):
    pdf_name = input("Pdf name (without .pdf extension): ")
    pdfs.append(pdf_name)

pdfs = [os.path.join(path, f"{x}.pdf") for x in pdfs]

writer = PdfWriter()
for pdf in pdfs:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

output_path = os.path.join(path, "merged.pdf")
with open(output_path, "wb") as output_file:
    writer.write(output_file)

print(f"PDFs merged successfully! Merged file saved at: {output_path}")

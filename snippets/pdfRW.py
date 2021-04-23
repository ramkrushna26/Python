
import PyPDF2

pdfFile = open("file.pdf", 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

#get no. of pages
print(reader.numPages)
#top get page
page = reader.getPage(0)
print(page.extractText())

#adding two pdfs
p1f = open("f1.pdf", 'rb')
p2f = open("f2.pdf", 'rb')
r1 = PyPDF2.PdfFileReader(p1f)
r2 = PyPDF2.PdfFileReader(p2f)

wr = PyPDF2.PdfFileWriter()

for pn in range(r1.numPages):
    p = r1.getPage(pn)
    wr.addpage(p)

for pn in range(r2.numPages):
    p = r2.getPage(pn)
    wr.addpage(p)

of = open("f3.pdf", 'wb')
wr.write(of)
of.close()
p1f.close()
p2f.close()

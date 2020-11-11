import PyPDF2
PDFFile = open("CPPO+PartnerList+ISVs.pdf",'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'
isv_aws=open('isv_aws.csv',mode='a')
for page in range(pages):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                isv_aws.write(u[ank][uri]+'\n')
                print(u[ank][uri])

isv_aws.close()
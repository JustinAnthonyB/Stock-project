import tabula

df = tabula.read_pdf(r'C:\Users\Jazz\Desktop\test\test.pdf', pages='all')
tabula.convert_into(r'C:\Users\Jazz\Desktop\test\test.pdf', r'C:\Users\Jazz\Desktop\test\test.csv' , output_format="csv",pages='all', stream=True)

# coding: utf-8

import os, fitz, pytesseract, PyPDF2
from PIL import Image

# change it with your own username and pdf filename
filepath = "c:/users/administrator/desktop/1.pdf"  

with fitz.open(filepath) as doc:
    for i in range(doc.page_count):
        page = doc[i]
        mat = fitz.Matrix(2, 2)
        '''
        This rectangle consist with lefttop 
        and rightbottom coordinates 
        which refer to current PC monitor resolution
        '''
        clip = fitz.Rect(1162, 1125, 1408, 1142) # an example
        pix = page.get_pixmap(matrix=mat, clip=clip)
        imgpath = "c:/users/administrator/desktop/Page/page-%s.png" % page.number
        pix.save(imgpath)
        img = Image.open(imgpath).convert("L")
        threshold = 200
        table = []
        for j in range(256):
            if j < threshold:
                table.append(0)
            else:
                table.append(1)
        newImg = img.point(table, "1")
        newImg.save(imgpath, dpi=(300.0,300.0))
        text = pytesseract.image_to_string(Image.open(imgpath), lang="chi_sim")
        
        # split pdf
        pdf_writer = PyPDF2.PDF2.PdFileWriter()
        with open(filepath, "rb") as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            page_obj = pdf_reader.getPage(i)
            pdf_writer.addPage(page_obj)
            newname = "%s-%s.pdf" % (i, text.strip("\n\t")) # Or change to name style needed
            with open("c:/users/administrator/desktop/SplitPDF/%s" % newname, "wb") as f:
                pdf_writer.write(f)
            pdf_writer.__init__()
            
        print(text)
        
        
# coding=utf-8

import os,re,sys
import codecs
import io
import subprocess

# import bookmark_class
import PyPDF2
from PyPDF2.pdf import PdfFileReader,PdfFileWriter
# from PdfBookmark import PdfBookmark
# from wand.image import Image

def getPdffileBookmark(filename,bookmark_file_savepath):
    pdf = PdfFileReader(open(filename, "rb"))

    pagecount=pdf.getNumPages()
    print('pagecount:',pagecount)

    pageLabels = {}#真实页码的索引 indirectRef  “{'/Type': '/Fit', '/Page': IndirectObject(7871, 0), '/Title': '封面'}”
    for i in range(pagecount):
        page=pdf.getPage(i)
        pageLabels[page.indirectRef.idnum]=i+1
        # print(page.indirectRef.idnum,i+1)

    bookmark_file= codecs.open(bookmark_file_savepath,'w',encoding='utf-8')
    title=[]
    pagedir=[]
    bookmark_jibie=[]
    outlines= pdf.getOutlines()
    print(outlines)
    index=0
    jibie=0
    for outline in outlines:
        index+=1
        jibie=0
        print(len(outline),outline)
        if type(outline)==PyPDF2.generic.Destination:
            # print('dict--------')
            # print(list(outline.keys()))
            # for x,j in enumerate(list(outline.keys())):
            #     print(str(outline[j]))
            # print(outline['/Title'])
            # print(outline['/Type'])
            # print(outline.page.idnum)
            bookmark_file.write(outline['/Title']+'\t'+str(pageLabels[outline.page.idnum])+'\r\n')
        if type(outline)==list:
            # print('list')
            jibie=1
            for i,outline in enumerate(outline):
                if type(outline)==PyPDF2.generic.Destination:
                    bookmark_file.write('\t'*jibie+outline['/Title'] + '\t' + str(pageLabels[outline.page.idnum]) + '\r\n')
                elif type(outline)==list:
                    jibie = 2
                    for i, o in enumerate(outline):
                        if type(outline) == PyPDF2.generic.Destination:
                            bookmark_file.write('\t'*jibie+outline['/Title'] + '\t' + str(pageLabels[outline.page.idnum]) + '\r\n')

        # print('\n')
        # if index>=3:
        #     break
    bookmark_file.close()

def getTitlePDFfromBookmarkfile(pdf_filepath, bookmark_filepath, pdf_filepath_output):

    bookmark_file=codecs.open(bookmark_filepath,'r',encoding='utf-8')
    lines=bookmark_file.readlines()
    page_start=0
    for i,line in enumerate(lines):
        # print(line)
        if line.find(u'目录')>=0:
            line=line.strip()
            print(line)
            print(line.split('\t'))
            page_start=int(line.split('\t')[1])
    page_start-=1
    print(page_start)
    page_end=0
    page_list=[]
    for i,line in enumerate(lines):
        line=line.strip()
        # print(line)
        if line.find('\t')>=0:
            # print(int(line.rsplit('\t',1)[1]))
            page_list.append(int(line.rsplit('\t',1)[1]))
    # page_list=page_list.sort()
    # print(page_list)
    for i in range(0,len(page_list)):
        if page_list[i]>page_start:
            page_end=page_list[i]
            break
        page_end-=1
    print(page_end)
    if page_end<=page_start and page_start>=0 and page_end>0:
        print('not find title page')
        return
    pdf = PdfFileReader(open(pdf_filepath, "rb"))

    output=PdfFileWriter()
    for i in range(page_start,page_end+1):
        output.addPage(pdf.getPage(i))

        # dst_pdf.addPage(pdf.getPage(i))

        # pdf_bytes = io.BytesIO()
        # output.write(pdf_bytes)
        # pdf_bytes.seek(0)
        # img = Image(file=pdf_bytes, resolution=300)
        # img.convert("png")
        # img.save(pdf_filepath_output+'_out.tif')
    stream=open(pdf_filepath_output,'wb')
    output.write(stream)



if __name__ == '__main__':

    # os.system('./xpdf/testXpdfToImg.exe -f 1 -l 1 -mono -r 300 -img 0 60662197.pdf 016')
    # os.system('testXpdfToImg.exe -f 1 -l 1 -mono -r 300 -img 0 60662197.pdf 016')
    # subprocess.Popen('cmd')
    # os.system(u'notepad')
    # exit()

    # if len(sys.argv) < 2:
    #     print (globals()['__doc__'] % locals())
    #     sys.exit(1)
    # dir_pro=sys.argv[1]
    # print(dir_pro)
    # if not os.path.exists(dir_pro):
    #     print('path not exist')
    #     sys.exit(1)

    dir_pro=r'E:\\pdfTest'
    if not os.path.exists(dir_pro+r'\out'):
        os.makedirs(dir_pro+r'\out')
    print(dir_pro)
    filepathvec = []
    # for rt, dirs, files in os.walk(dir_pro):  # =pathDir
    #     for filename in files:
    #         # print filename
    #         if filename.find('.') >= 0:
    #             (shotname, extension) = os.path.splitext(filename)
    #             # print shotname,extension
    #             if extension == '.pdf':
    #                 filepathvec.append(os.path.join('%s\\%s' % (rt, filename)))
    #                 # print filename
    for i in os.listdir(dir_pro):
        print(i)
        (shotname, extension) = os.path.splitext(i)
        if extension == '.pdf':
            filepathvec.append(os.path.join('%s\\%s' % (dir_pro, i)))
    for i, filepath in enumerate(filepathvec):
        print(filepath, i + 1, len(filepathvec))
        # print(os.path.splitext(filepath))
        bookmark_filepath=os.path.splitext(filepath)[0]+'_bookmark.txt'
        try:
            getPdffileBookmark(filepath, bookmark_filepath)
        except:
            print('error')
        #
        # #通过bookmark.txt得到目录的页码，存出只有目录面的pdf
        try:
            pdfout_filepath=os.path.splitext(filepath)[0]+'_toc'+os.path.splitext(filepath)[1]
            getTitlePDFfromBookmarkfile(filepath, bookmark_filepath, pdfout_filepath)
        except:
            print('error')




    # getPdffileBookmark('60662197.pdf','bookmark.txt')
    #
    # #通过bookmark.txt得到目录的页码，存出只有目录面的pdf
    # getTitlePDFfromBookmarkfile('60662197.pdf','bookmark.txt','60662197_out.pdf')


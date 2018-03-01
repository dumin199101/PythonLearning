# encoding:utf-8
from PyPDF2 import PdfFileReader, PdfFileWriter


def add_blank_page():
    readFile = 'E:/pdfTest/9787504962980H.pdf'
    outFile = 'E:/pdfTest/9787504962980H_copy.pdf'
    pdfFileWriter = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    numPages = pdfFileReader.getNumPages()

    for index in range(0, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
    pdfFileWriter.write(open(outFile, 'wb'))

    # pdfFileWriter.addBlankPage()   # 在文件的最后一页写入一个空白页,保存至文件中
    # pdfFileWriter.write(open(outFile,'wb'))

if __name__ == '__main__':
    add_blank_page()
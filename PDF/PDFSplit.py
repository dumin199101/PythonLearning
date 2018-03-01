from PyPDF2 import PdfFileReader, PdfFileWriter


def splitPdf():
    readFile = 'E:/pdfTest/中国科学技术协会  正文.pdf'
    outFile = 'E:/pdfTest/中国科学技术协会  正文_split.pdf'
    pdfFileWriter = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    # 文档总页数
    numPages = pdfFileReader.getNumPages()

    if numPages > 600:
        # 从第五页之后的页面，输出到一个新的文件中，即分割文档
        for index in range(600, numPages):
            pageObj = pdfFileReader.getPage(index)
            pdfFileWriter.addPage(pageObj)
        # 添加完每页，再一起保存至文件中
        pdfFileWriter.write(open(outFile, 'wb'))

if __name__ == '__main__':
    splitPdf()
from PyPDF2 import PdfFileReader, PdfFileWriter

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    for inFile in inFileList:
        # 依次循环打开要合并文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)

        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))

if __name__ == '__main__':
    inFileList = ["E:/pdfTest/9787504962980H.pdf","E:/pdfTest/9787504962980H_split.pdf"]
    outFile = "E:/pdfTest/9787504962980H_merge.pdf"
    mergePdf(inFileList,outFile)
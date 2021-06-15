import docx
# import io
from io import StringIO

fileName = './downloads/2018D56368-test.docx'
fileName2 = './downloads/2018D56368.doc'

def getFullText(fileName):
    doc = docx.Document(fileName)
    fullText = []
    for par in doc.paragraphs:
        fullText.append(par.text)
    return '\n'.join(fullText)

def getFullTextFromDoc(fileName):
    # f = open(fileName,'rb')
    with open(fileName, 'rb') as f:
        source_stream = StringIO(f.read())
    result = getFullText(source_stream)
    f.close()
    return result

# test = getFullText(fileName)
test = getFullTextFromDoc(fileName2)
print(test)


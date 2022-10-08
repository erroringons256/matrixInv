import numpy

a = numpy.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]], dtype = "float")
aTranspose = a.T

cIdx = 0
nCol = a.shape[0]
print(nCol)

while cIdx < nCol - 1:
    pIdx = numpy.argmax(numpy.abs(aTranspose[cIdx]))
    if a[pIdx,cIdx] == 0:
        cIdx += 1
    else:
        a[[pIdx,cIdx]] = a[[cIdx,pIdx]]
        pIdx = cIdx
        cIdx += 1
        a[cIdx:,pIdx] /= a[pIdx,pIdx]
        print(a[cIdx:, cIdx:], a[cIdx:, pIdx], a[pIdx, cIdx: nCol + 1])
        a[cIdx:,cIdx:] -= numpy.outer(a[cIdx:,pIdx],(a[pIdx,cIdx:nCol + 1]))
        a[cIdx:,pIdx] = 0

print(a)
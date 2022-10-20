import lista5bib

#Testando função testaMultiplo4 usando o print
print(lista5bib.testaMultiplo4(4))
print(lista5bib.testaMultiplo4(7))
print(lista5bib.testaMultiplo4(-16))
print(lista5bib.testaMultiplo4(-7))

#Testando função testaDivisor usando o assert
assert lista5bib.testaDivisor(3, 1)
assert not lista5bib.testaDivisor(6, 18)
assert lista5bib.testaDivisor(18, 6)
assert not lista5bib.testaDivisor(14, 4)
##
## Imprima la cantidad de registros por cada letra
## de la columna _c1 de la tabla tbl0
##
from readtsv import readAll

tbl0, _, _ = readAll()

print(tbl0['_c1'].value_counts().sort_index())

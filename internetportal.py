from googlesearch import search
import wikipedia
print("The . . . . . . . . .")
print(". . .I n t e r n e t")
print(". . . . . .P o r t a l")
term = input("[Que desea buscar ahora?] ")
print("Resultados en Wikipedia--------")
print(wikipedia.search(term))
print("------------------------------------")
print()
print("URLS de resultados en Google---")
for i in search(term, lang='es'):
   print("- - - - - - - - - - - - - - - - - - - - -")
   print(i)

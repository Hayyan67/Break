st1=input('Enter any string')
ch=input('Enter a charater to search')
for c in st1:
    if c==ch:
        print(ch,"Found")
        break
    else:
        print(ch,"ch not found")

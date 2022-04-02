
flattened = []
def flatten_list(x):
    for item in x:
        if type(item) in [list]:
            yield from flatten_list(item)
        else :
            yield(item)

nested =  [ [ 1 , 'a' , [ 'cat' ] , 2 ] , [ [ [ 3 ] ] , 'dog' ] , 4 , 5]
flattened = (list(flatten_list(nested))) 
print("#Task 1 ")
print(flattened)
print("****************************")
list_2 = [ [ 1 , 2 ] , [ 3 , 4 ] , [ 5 , 6 , 7 ] ]
list_2.reverse()
print("#Task 2 Aşama 1")
print(list_2)
for l in list_2:
    l.reverse() 
print("#Task 2 Aşama 2 (Sonuç)")
print(list_2)

              
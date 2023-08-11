d={
    "name":"arya",
    "age":20,
    "rollno":21,
    "place":"kasaragod"
}
print(d)



#add
d.update({"father":"suku"})
print(d)

#replace
d["name"]="abhi"
print(d)

#delete
d.pop("place")
print(d)


#keys
c=d.keys()
print(c)
#values
b=d.values()
print(b)
#items()
e=d.items()
print(e)
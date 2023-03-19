list_of_cloud=["AWS","GCP","AZure"]
list_of_env = ["dev","stage","test"]

#list iteration
for cl in list_of_cloud:
    if cl == "AWS":
        print(cl, "is best cloud")
    
#dictionary  are used to store data values in key:value pairs.
dict_of_cloud = {
    "AWS":"Amazon web service",
    "Azure":"Microsoft cloud",
    "GCP":"Google cloud"
}
print(dict_of_cloud["AWS"]) #get value from dictionary
print(dict_of_cloud.get("Azure","Not found")) #get value from dictionary
dict_of_cloud.update({"linode":"This in linode"}) #update dictionary
dict_of_cloud.update({
    "Newitem":"This is new item"
})
dict_of_cloud.pop("linode") #delete dictionary
dict_of_cloud.popitem() #removes the last inserted item
print(dict_of_cloud)

#dict_of_cloud.clear()  #empties the dictionary
#del dict_of_cloud  #The del keyword can also delete the dictionary
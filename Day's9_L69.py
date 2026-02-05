#dictionary

capitals = {
     "Arizona": "Arizona",
     "Ashley": "Ashley",
}

#Nested List in dictionary

# Travel_log = {
#     "Arizona": ['rome','new'],
#     "Ashley": ['city','uk'],
# }
#
# print(Travel_log["Arizona"])#['rome','new']
# print(Travel_log["Arizona"][1])#'new'

#Nested List

N_L = ['A','B',['c','d']]
print(N_L[2][1])#d

#Nested dictionary


travel_bog = {
    "India": {
        "vist_states": 7,
        "states":['Delhi','Madhya Pradesh'],
    },
    "UAE":{
        "buy_items":['car','watch'],
        "adventure":['sky','swin','fly'],
        "Price":{
            "buy_items":20000,
            "adventure":10000,
            "Rest":5000,
        },

    }
}

print(travel_bog["UAE"]["Price"]["Rest"])

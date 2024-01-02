
from pymongo.mongo_client import MongoClient
from pprint import pprint
from bson import ObjectId

uri = "mongodb+srv://shiva35143:NrAyzSo57PzOFQGk@admindb.tczhftu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    db = client['AdminDB']
    collection = db['Users']
    # mgs=db['message']
    data={
        "name":'shiva'
    }
    # collection.insert_one(data)
    result=collection.insert_one({"name":"hello"}).inserted_id
    print(result)
    # collection.find_one_and_update({"_id":"6572b670483d45e47f7c943a"},{"$set":{"Username":"naveen123"}},return_document=True)
    # result=collection.find_one({"_id":"6572b670483d45e47f7c943a"})
    
    # for i in result:
    #    pprint(i)
    # pprint(result)
    # document_to_update = collection.find_one({"_id": "6572b670483d45e47f7c943a"})

# Update the Username field in the found document
    # if document_to_update:
        # collection.update_one({"_id": "6572b670483d45e47f7c943a"},{"$set": {"Username": "naveen123"}})
        # print("Update successful")
    # else:
    #   print("Document not found")

# Print the updated document
    # id=ObjectId("6572a7a8ad4e3c048e7307c7")
    # existing_entry = collection.find_one({"_id":id, "Chat.naveen123": {'$exists': True}})
    # existing_entry=existing_entry['Chat'] 
    # string_keys = [next(iter(dictionary.keys())) for dictionary in existing_entry if dictionary]
    # id=existing_entry[string_keys.index('naveen123')]['naveen123']
    # id=ObjectId(id)
    # # mgs.update_one({"_id":id},{'$push':{'chats':{"naveen123":"hello"}}})
    # mgs.update_one({"_id":id},{'$set':{'chats':[]}})
    # updated_document = collection.find_one({"_id":id})
    # if existing_entry:
    #     print("yes")
    # else:
    #     print("no")
    # pprint(existing_entry)
    # # print("Updated Document:")
    # for i in updated_document:
    #    pprint(i)




except Exception as e:
    print(e)


   #/ collection_mgs=db['message']
    # # data={
    # #     "chats":[]
    # # }
    # # mgs_id=collection_mgs.insert_one(data).inserted_id
    # # mgs_id=collection_mgs.find_one({"_id":"6572aac5395982eac25b04e5"})
    # # collection2=db['message']
    # # document_id = ObjectId("6571994c261e92c400056eee")
    # collection.update_one({"_id":"6572a7a8ad4e3c048e7307c7"},{'$push':{'Chat':{"naveen123":"6572aac5395982eac25b04e5"}}})
    
    # 
    # collection.update_one({"Username":"naveen123"},{"$set":{"Username":"admin143"}})
    # 

    # collection.find_one_and_update({"_id":"6572b670483d45e47f7c943a"},{"$set":{"Username":"naveen123"}},return_document=True)
    # result=collection.find()
    # for i in result:
    #    pprint(i)
    # # result=collection_mgs.find()
    # for i in result:
    #   pprint(i)
#     db = client['AdminDB']
#     collection = db['Users']

# # Corrected update query
#     collection.update_one({"_id": ObjectId("6572a7a8ad4e3c048e7307c7")},
#                       {'$push': {'Chat': {"naveen123": "6572aac5395982eac25b04e5"}}})

# # Corrected find query
#     result = collection.find()
#     db = client['AdminDB']
#     collection = db['Users']

# # Specify the document's ObjectId
#     document_id = ObjectId("6572a7a8ad4e3c048e7307c7")

# # Retrieve the Chat array for the specified document
#     document = collection.find_one({"_id": document_id})
#     chat_array = document.get("Chat", [])

# # Extract the desired value from the Chat array
#     # desired_value = None
#     # for chat_item in chat_array:
#     #     desired_value = chat_item.get("naveen123")
#     #     if desired_value:
#     #        document = collection_mgs.find_one({"_id":desired_value})

#     pprint(chat_array[0]['naveen123'])



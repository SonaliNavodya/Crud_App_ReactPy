# Import necessary libraries
from pymongo import MongoClient

# Replace <uri> with your MongoDB Atlas connection string
uri = "mongodb+srv://Sonali:Sonali123@cluster1.qkgptuq.mongodb.net/"
client = MongoClient(uri)

# Replace <database-name> with the name of your database
db = client["firstApp"]

# Replace <collection-name> with the name of your collection
collection = db["Collection1"]

# Check the connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

document = {"name": "Danial", "age": 36}

# Install the document into the collection
insert_result = collection.insert_one(document)

# Print the ID of the inserted document
print("Inserted Document ID:", insert_result.inserted_id)

client.close()

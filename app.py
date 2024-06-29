from pymongo import MongoClient
import hashlib

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["auth-diet"]
users_collection = db["auth-diet"]

# Provided user data
user_data = [
    
  {"username": "user1", "password": "P@ssw0rd1!", "role": "admin"},
  {"username": "user2", "password": "P@ssw0rd2!", "role": "user"},
  {"username": "user3", "password": "P@ssw0rd3!", "role": "user"},
  {"username": "user4", "password": "P@ssw0rd4!", "role": "user"},
  {"username": "user5", "password": "P@ssw0rd5!", "role": "user"},
  {"username": "user6", "password": "P@ssw0rd6!", "role": "user"},
  {"username": "user7", "password": "P@ssw0rd7!", "role": "user"},
  {"username": "user8", "password": "P@ssw0rd8!", "role": "user"},
  {"username": "user9", "password": "P@ssw0rd9!", "role": "user"},
  {"username": "user10", "password": "P@ssw0rd10!", "role": "user"},
  {"username": "user11", "password": "P@ssw0rd11!", "role": "user"},
  {"username": "user12", "password": "P@ssw0rd12!", "role": "user"},
  {"username": "user13", "password": "P@ssw0rd13!", "role": "user"},
  {"username": "user14", "password": "P@ssw0rd14!", "role": "user"},
  {"username": "user15", "password": "P@ssw0rd15!", "role": "user"},
  {"username": "user16", "password": "P@ssw0rd16!", "role": "user"},
  {"username": "user17", "password": "P@ssw0rd17!", "role": "user"},
  {"username": "user18", "password": "P@ssw0rd18!", "role": "user"},
  {"username": "user19", "password": "P@ssw0rd19!", "role": "user"},
  {"username": "user20", "password": "P@ssw0rd20!", "role": "user"},
  {"username": "user21", "password": "P@ssw0rd21!", "role": "user"},
  {"username": "user22", "password": "P@ssw0rd22!", "role": "user"},
  {"username": "user23", "password": "P@ssw0rd23!", "role": "user"},
  {"username": "user24", "password": "P@ssw0rd24!", "role": "user"},
  {"username": "user25", "password": "P@ssw0rd25!", "role": "user"},
  {"username": "user26", "password": "P@ssw0rd26!", "role": "user"},
  {"username": "user27", "password": "P@ssw0rd27!", "role": "user"},
  {"username": "user28", "password": "P@ssw0rd28!", "role": "user"},
  {"username": "user29", "password": "P@ssw0rd29!", "role": "user"},
  {"username": "user30", "password": "P@ssw0rd30!", "role": "user"},
  {"username": "user31", "password": "P@ssw0rd31!", "role": "user"},
  {"username": "user32", "password": "P@ssw0rd32!", "role": "user"},
  {"username": "user33", "password": "P@ssw0rd33!", "role": "user"},
  {"username": "user34", "password": "P@ssw0rd34!", "role": "user"},
  {"username": "user35", "password": "P@ssw0rd35!", "role": "user"},
  {"username": "user36", "password": "P@ssw0rd36!", "role": "user"},
  {"username": "user37", "password": "P@ssw0rd37!", "role": "user"},
  {"username": "user38", "password": "P@ssw0rd38!", "role": "user"},
  {"username": "user39", "password": "P@ssw0rd39!", "role": "user"},
  {"username": "user40", "password": "P@ssw0rd40!", "role": "user"},
  {"username": "user41", "password": "P@ssw0rd41!", "role": "user"},
  {"username": "user42", "password": "P@ssw0rd42!", "role": "user"},
  {"username": "user43", "password": "P@ssw0rd43!", "role": "user"},
  {"username": "user44", "password": "P@ssw0rd44!", "role": "user"},
  {"username": "user45", "password": "P@ssw0rd45!", "role": "user"},
  {"username": "user46", "password": "P@ssw0rd46!", "role": "user"},
  {"username": "user47", "password": "P@ssw0rd47!", "role": "user"},
  {"username": "user48", "password": "P@ssw0rd48!", "role": "user"},
  {"username": "user49", "password": "P@ssw0rd49!", "role": "user"},
  {"username": "user50", "password": "P@ssw0rd50!", "role": "user"}
]



# Hash passwords and insert into the database
for user in user_data:
    user["password"] = hashlib.sha256(user["password"].encode()).hexdigest()
    users_collection.insert_one(user)

print("Data inserted successfully")

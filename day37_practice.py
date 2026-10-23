import pickle

# Your object (can be a dict, list, custom class instance, etc.)
obj = {"key": "value"}

# Open the file in 'wb' (write binary) mode
with open("data.pkl", "wb") as f:
    pickle.dump(obj, f)
  

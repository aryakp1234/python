# import pandas 

# mydataset = {
#   'students': ["arya", "archu", "anu"],
#   'marks': [38, 37, 32]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)




# import pandas as pd

# mydataset = {
# 'students': ["arya", "archu", "anu"],
# 'marks': [38, 37, 32]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# # check versaion
# import pandas as pd

# print(pd.__version__)

# ------------------------------------------------------------------

# Pandas Series
#-------------------
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)
# print(myvar[0])
# print(myvar[2])
# print(myvar[1])


# Create Labels
# ---------------
# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)
# print(myvar["y"])



# Key/Value Objects as Series
# ----------------------------
import pandas as pd

calories = {"day1k": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)


# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.
# Example

# Create a DataFrame from two Series:
# -----------------------------------------------------------------

# DataFrames

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.
# Example

# # Create a DataFrame from two Series:
# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)


















# import pandas as pd

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)

# print(df)
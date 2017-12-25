"""
sets are collection of unique objects
"""
fileSet = {2015,2016, 2017}
print(fileSet)

"""
Dictonaries are collection of key value pairs, similar to hashes in ruby
"""
fileDict = {"last year": 2016, "current year": 2017, "next year": 2018}
print(fileDict)
print(fileDict["last year"])

"""
A list can be converted to set by using set()
"""
fileList = [2015,2016,2016]
fileSet = set(fileList)
print(type(fileSet))
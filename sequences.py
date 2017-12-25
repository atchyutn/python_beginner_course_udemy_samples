fileList = list(range(2000,2018,2))
print(fileList)

print(fileList[0])
print(fileList[0:3])
print(fileList[2:5])
print(fileList[:2])
print(fileList[2:])
print(fileList[-1])
print(fileList[-2:])
print(fileList[:-2])

"""
Output:

[2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016]
2000
[2000, 2002, 2004]
[2004, 2006, 2008]
[2000, 2002]
[2004, 2006, 2008, 2010, 2012, 2014, 2016]
2016
[2014, 2016]
[2000, 2002, 2004, 2006, 2008, 2010, 2012]

"""
import os
import re
import math

'''
from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


'''
this function only works with the common format of the data sets. it also assumes all the data sets contain doubles in each column and it will only read the first data set from a file even if the file has more than one data set
'''
def ParseFile(fn):
    with open(fn, 'rb') as f:
        lines = f.readlines()
        '''
        0 = looking through the individual qualities of the file like the star id
        1 = skipping past the column labels for data set
        2 = reading in the columns of the data set
        '''
        mode = 0
        
        numCols = 3 # days, rad vel, rad vel uncert
        data = {
            "dataPoints" : [],
            "colLabels" : -1
        }
        
        for l in lines:
            lp = l.decode('ISO-8859-1')
            if(mode == 0):
                if(lp[0] != '\\'):
                    mode += 1
                else:
                    lp = lp[1:]
                    qName = ""
                    for i in range(len(lp)):
                        if(lp[i].isspace()):
                            qName = lp[:i]
                            lp = lp[i:]
                            break
                    try:
                        qVal = (re.search('\"(.*)\"', lp)).group(1)
                        data[qName] = qVal
                    except:
                        lp = lp.strip()
                        data[qName] = lp[1:len(lp)-1]
                            
            if(mode == 1):
                if(lp[0] != '|'):
                    mode += 1
                else:
                    if(data["colLabels"] == -1):
                        data["colLabels"] = lp.split('|')
                        data["colLabels"].pop(0)
                        data["colLabels"].pop()
                        for i in range(len(data["colLabels"])):
                            data["colLabels"][i] = data["colLabels"][i].strip()
            if(mode == 2):
                if(not lp[0].isspace()):
                    break
                else:
                    lp = lp.strip()
                    d = []
                    for c in range(numCols-1):
                        for end in range(len(lp)):
                            if((end) >= len(lp) or lp[end].isspace()): #check if the number has ended or the end has been reached
                                d.append(lp[:end])
                                lp = (lp[end:]).strip()
                                break
                    d.append(lp)
                    
                    isValidData = True
                    for i in range(len(d)):
                        if(is_number(d[i])):
                            d[i] = float(d[i])
                            if(math.isnan(d[i])):
                                isValidData = False
                                break
                        else:
                            isValidData = False
                            break
                    if(len(d) != 3):
                        isValidData = False
                    
                    if(isValidData):
                        data["dataPoints"].append(d)
                    
        return data

#list of file names to be ignored
excludedFiles = ['RADIAL.log', 'UID_0300073_RVC_002.tbl']
'''
takes a directory to read files from as input
returns a list of dictionaries based on the files in the input directory
'''
def ParseData(dataLocation):
    filesToLoad = os.listdir(dataLocation)
    
    dataList = []
    failedList = []
    
    i = 0
    for fileName in filesToLoad:
        if(fileName not in excludedFiles):
            try:
                print(fileName)
                p = ParseFile(dataLocation+fileName)
                print(p)
                dataList.append(p)
            except:
                failedList.append(fileName)
    '''
    print("failed count: " + str(len(failedList)))
    print("failed on: " + str(failedList))
    '''
    return dataList


if __name__ == "__main__":
    dir = "exo_data/"
    print(ParseData(dir))
    #print(ParseFile(dir + "UID_0007981_RVC_004.tbl"))

with open("otherRaw.txt","r") as inputFile, open("AODATA00.txt","r") as matchFile, open("uniqueOTHER.txt","a") as outputFile:
    errors = 0
    matches = 0
    total = 0
    for line in inputFile:
        total += 1
        suspectLine = line
        unique = True
        matchLine = "derp"
        for line in matchFile:
            matchLine = line

            match = True
            
            for x in range(len(matchLine)):
                #print(matchLine[x])
                if suspectLine[x] == matchLine[x]:
                    match = match and True
                else:
                    match = match and False
                    break
            if match:
                #print(len(suspectLine))
                unique = False
                matches += 1
                break

        if unique == True:
            outputFile.write(suspectLine)
            #print(total)
    inputFile.close()
    matchFile.close()
    outputFile.close()
    print("errors = ",errors)
    print("matches = ", matches)
    print("total cases = ",total)
    raise SystemExit

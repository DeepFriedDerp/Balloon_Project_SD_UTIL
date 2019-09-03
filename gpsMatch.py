with open("gpsRaw.txt","r") as inputFile, open("GPSLOG00.txt","r") as matchFile, open("uniqueGPS.txt","a") as outputFile:
    errors = 0
    matches = 0
    total = 0
    for line in inputFile:
        total += 1
        suspectLine = line
        startIndex_suspect = suspectLine.find("$")
        stopIndex = suspectLine.find("*") + 2
        unique = True
        matchLine = "derp"
        for line in matchFile:
            matchLine = line
            startIndex_match = matchLine.find("$")

            if startIndex_suspect < 0:
                #print(suspectLine)
                errors += 1
                break
            elif startIndex_match < 0:
                #print(matchLine)
                errors += 1
                break

            match = True
            
            for x in range(startIndex_suspect,stopIndex):
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

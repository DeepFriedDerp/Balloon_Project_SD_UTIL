max_bytes = 4000000000 # 4GB

with open("image.dd","r") as inputFile, open("otherRaw.txt","a") as outputFile:
    #
    #inputFile.seek(17884811,0)
    #
    total_bytes = 0
    megaBytes = 0
    totalReadBytes = 0
    totalReadMB = 0
    while True:
        totalReadBytes += 1
        if (totalReadBytes / 1000000) >= 1:
            totalReadMB += 1
            totalReadBytes = 0
            print("SCANNED : ",totalReadMB,"MB")
        workingChar = inputFile.read(1)
        lastRead = inputFile.tell()
        if workingChar == "":
            if inputFile.tell() > max_bytes:
                inputFile.close()
                outputFile.close()
                sys.exit("end of file reached, terminating program")
        elif workingChar == "+":
            #print(lastRead)
            inputFile.seek(-22,1)

            beginFound = False
            for x in range(22):
                c = inputFile.read(1)
                if c == "%":
                    if inputFile.read(2) == "%\n":
                        beginFound = True
                        break

            if beginFound:
                otherBegin = inputFile.tell()
                endFound = False
                index = 0
                for x in range(175):
                    index = index + 1
                    if inputFile.read(1) == "%":
                        endFound = True
                        break;
                if endFound:
                    index = index + 1
                    inputFile.seek(-index,1)
                    otherSentence = inputFile.read(index)
                    #print(otherSentence)
                    outputFile.write(otherSentence)
                    outputFile.write("\n")
                    total_bytes += len(otherSentence)
                    totalReadBytes += len(otherSentence)
                    if (total_bytes / 1000000) >= 1:
                        megaBytes += 1
                        total_bytes = 0
                        print("FOUND : ",megaBytes,"MB")
                else:
                    inputFile.seek(lastRead + 1,0)
            else:
                inputFile.seek(lastRead + 1,0)
                

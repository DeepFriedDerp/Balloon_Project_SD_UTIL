max_bytes = 4000000000 # 4GB

with open("image.dd","r") as inputFile, open("gpsRaw.txt","a") as outputFile:
    total_bytes = 0;
    megaBytes = 0;
    totalReadBytes = 0
    totalReadMB = 0
    while True:
        totalReadBytes += 1
        if (totalReadBytes / 1000000) >= 1:
            totalReadMB += 1
            totalReadBytes = 0
            print("SCANNED : ",totalReadMB,"MB")
        workingChar = inputFile.read(1)
        #print(inputFile.tell())
        if workingChar == "":
            if inputFile.tell() > max_bytes:
                inputFile.close()
                outputFile.close()
                sys.exit("end of file reached, terminating program")
        elif workingChar == "$":
            beginGPS = inputFile.tell()
            nextChars = inputFile.read(5)
            sentenceDetected = False
            
            if nextChars == "GPRMC":
                sentenceDetected = True
            elif nextChars == "GPGGA":
                sentenceDetected = True
                
            if sentenceDetected:
                index = 0
                endFound = True
                inputFile.seek(-6,1)
                while True:
                    index = index + 1
                    if index > 100:
                        endFound = False
                        break;
                    derp = inputFile.read(1)
                    if derp == "*":
                        break;
                    
                if endFound:
                    index = index + 2
                    inputFile.seek(beginGPS-1,0)
                    gpsSentence = inputFile.read(index)
                    outputFile.write(gpsSentence)
                    outputFile.write("\n")
                    total_bytes += len(gpsSentence)
                    totalReadBytes += len(gpsSentence)
                    if total_bytes / 1000000 >= 1:
                        megaBytes += 1
                        total_bytes = 0
                        print("FOUND : ",megaBytes,"MB")
                    #print(gpsSentence)
                else:
                    beginGPS = beginGPS + 1
                    inputFile.seek(beginGPS,0);
                    #print(inputFile.tell())

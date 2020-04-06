# read file from unicode standard and create a json array of all emojis in a .txt document

# file containing all standard unicode emojis
# downloaded from: https://unicode.org/Public/emoji/
inputFileName = 'emoji-test.txt'

outputFileName = 'emojis.txt'

# only select emojis up to a certain version
# (iOS doesnt currently support version 13.0)
maxEmojiVersion = '12.1'

# Methods for converting emojis
def codepointToUnicode(codepoint): 
    zerosToPrepend = 8 - len(codepoint)
    unicodeString = '\U' + ('0' * zerosToPrepend) + codepoint
    return unicodeString

def unicodeToEmoji(unicodeString):
    emoji = unicodeString.decode('unicode-escape')
    return emoji.encode('UTF-8')

def unicodeToComboEmoji(unicodeArray):
    emojiString = ""
    for unicodeString in unicodeArray:
        emojiString = emojiString + unicodeString.decode('unicode-escape')
    return emojiString.encode('UTF-8')

#check version of emoji against max supported version
def emojiVersionIsValid(version):
    if float(version) <= float(maxEmojiVersion):
        return True
    else:
        return False

emojiList = []

emojiStandardFile = open(inputFileName, 'r') 
lines = emojiStandardFile.readlines() 

for line in lines:
    if line[0] != '#':
        splitLine = line.split()
        if len(splitLine) > 0 and 'fully-qualified' in splitLine :

            emojiVersion = splitLine[splitLine.index(';') + 4][1:]
            if emojiVersionIsValid(emojiVersion):

                # standard method

                emoji = splitLine[splitLine.index(';') + 3]
                emojiList.append(emoji)

                # backup method
                # if for some reason emojis cannot be read directly from file this method can read unicode values from file and convert them to emojis

                # unicodeValues = []
                # for subString in splitLine:
                #     if subString == ';':
                #         break
                #     else:
                #         unicodeValues.append(codepointToUnicode(subString))
                # if len(unicodeValues) > 1:
                #     emoji = unicodeToComboEmoji(unicodeValues)
                #     emojiList.append(emoji)
                # elif len(unicodeValues) == 1:
                #     emoji = unicodeToEmoji(unicodeValues[0])
                #     emojiList.append(emoji)


outputFile = open(outputFileName, "w")
outputFile.write("[\n")

for emojiIndex in range(len(emojiList)):
    emoji = emojiList[emojiIndex]
    outputString = str(emojiIndex) + ":\"" + emoji + "\",\n"
    outputFile.write(outputString)

outputFile.write("]")
outputFile.close()



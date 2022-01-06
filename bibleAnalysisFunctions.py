def GetVerseReferences(verseReferenceListing):
    '''Given a book, chapter, verse listing, return three lists that contain those elements broken out in that order.'''
    
    verseReferenceListing = [ele[::-1] for ele in verseReferenceListing]
    
    verses = []
    chapters = []
    books = []

    for ele in verseReferenceListing:
        temp_list_1 = ele.split(':')
        verses.append(temp_list_1[0][::-1])
        temp_list_2 = temp_list_1[1].split(' ',1)
        chapters.append(temp_list_2[0][::-1])
        books.append(temp_list_2[1][::-1])

    return books, chapters, verses

def GetMaxVerseLength(verseListing):
    '''Given a list of verse texts, return the maximum verse length in terms of word count along with a dictionary of verse references and their lengths'''
    lenDict = {}
    counter = 0
    for ele in verseListing:
        temp_list = ele.split(' ') 
        lenDict[counter] = len(temp_list)
        counter = counter + 1
    maxLen = max(lenDict.values())
    return maxLen
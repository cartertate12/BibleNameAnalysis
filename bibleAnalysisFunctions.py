def GetVerseReferences(verseReferenceListing):
    '''Given a book, chapter, verse listing, return three lists that contain those elements broken out in that order.'''
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
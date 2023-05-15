from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def about(reauest):
    return render(reauest, 'about.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            #increase the count
            worddict[word] += 1
        else:
            #decrease the count
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
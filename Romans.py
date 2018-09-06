#Romans
#Use all dicts for 1 Corinthians
import random


def pickRandFavoriteVerse(favoriteVerse):
    verse = random.choice(favoriteVerse)
    return verse

def chapter1():
    mainHeadings = ['Greetings','Desire to visit Rome','The Just live by faith',
    "God's Wrath on Unrighteousness"]
    boldVerse = ["First, I thank my God through Jesus Christ for you all, that \
your faith is spoken of throughout the whole world", "For I am not ashamed of the \
gospel of Christ, for it is the power of God to salvation for everyone who believes \
for the Jew first and also for the Greek","For the wrath of God is revealed from \
heaven against all ungodliness and unrighteousness,"]
    keyLinks = {'1:16':'NU- Text omits of Christ','1:17':'Habakkuk 2:14',
 '1:29':'NU-Text omits sexual immorality.', '1:31': 'NU-text omits unforgiving'}
    favoriteVerse = ["To all who are in Rome, beloved of God, called to be saints: \
Grace to you and peace from God out Father and the Lord Jesus Christ.", "For \
I long to see you, that I may impart to you some spiritual gift, so that you may be \
established--That is, that I may be encouraged together with you by the mutual faith \
both of you and me", "Professing to be wise, they became fools, and changed the glory \
of the incorruptible God into an image made like corruptible man-- and birds and \
four-footed animals and creeping things."]
    return mainHeadings, boldVerse, keyLinks, favoriteVerse

def chapter2():
    mainHeadings = ["God's Righteous Judgment","The Jews Guilty as the Gentiles"," \
Circumcision of No Avail"]
    boldVerse = ['Indeed you are called a Jew, and rest on the law, and make your \
boast in God', 'For circumcision is indeed profitable if you keep the law; but if you \
are a breaker of the law, your circumcision has become uncircumcision']
    keyLinks = {'2:6':'Psalm 62:12; Proverbs 24:12', '2:17': 'NU-Text reads But if',
    '2:24': 'Isaiah 52:5 ; Ezekiel 36:22'}
    favoriteVerse = ['Therefore you are inexcusable, O man, whoever you are who judge, \
for in whatever you judge another you condemn yourself; for you who judge practice the \
same things.', 'You who make your boast in the law, do you dishonor God through breaking \
the law? For "The name of God is blasphemed among the Gentiles because of you," as it is \
written.','but he is a Jew who is one inwardly; and circumcision is that of the heart, \
in the Spirit, not in the letter; whose praise is not from men but from God.']
    return mainHeadings, boldVerse, keyLinks, favoriteVerse

def chapter3():
    mainHeadings = ["God's Judgment Defended", "All Have Sinned", "God's Right\
eousness through Faith","Boasting Excluded"]
    favoriteVerse = ['Certainly not! For then how will God judge the world?','There\
fore by deed of law no flesh will be justified in His sight, for by the law is \
the knowledge of sin ','to demonstrate at the present time His righteousness, t\
hat He might be just and the justifier of the one who has faith in Jesus']
    keyLinks = {'3:4':'Psalm 51:4', '3:12':
    'Psalms 14:1-3; 53:1-3; Ecclesiastes 7:20',
    '3:13':'Psalm 5:9 Psalm 140:3','3:14':'Psalms 10:7', '3.17':'Isaiah 59:7,8',
 '3:18':'Psalm 36:1', '3:22':'NU- Text omits of Christ'}
    boldVerse = ['What then? Are we better than they? Not at all. For we have p\
reviously charged both Jews and Greeks that they are all under sin.','But now \
the righteousness of God apart from the law is revealed, being witnessed by th\
e Law and the Prophets','Where is boasting then? It is excluded. By what law? O\
f works? No, but by the law of faith.']
    return mainHeadings, keyLinks, favoriteVerse, boldVerse

def chapter4():
    mainHeadings = ['Abraham Justified by Faith', 'David Celebrates the Same Tr\
uth', 'Abraham Justified Before Circumcision', 'The Promise Granted Through Fai\
th']
    boldVerse = ['But to him who does not work but believes on Him who justifie\
s the ungodly, his faith is accounted for righteousness.','Does this blessednes\
s then come upon the uncircumcised also? For we say that faith was accounted to\
Abraham for righteousness','For the promise that he would be the heir of the wo\
rld was not to Abraham or to his seed though the law, but through the righteous\
ness of faith']
    keyLinks = {'4:1':"""Or Abraham our fore father according to the flesh has f
ound?""", '4:3': 'Genesis 15:6', '4:8':'Psalm 32:1,2','4.17':'Genesis 17.5',
'4:18':'Genesis 15:5', '4:22':'Genesis 15:6'}
    favoriteVerse = ['For what does the Scripture say? "Abraham believed God, \
and it was accounted to him for righteousness."', 'Just as David also describes\
the blessedness of the man to whom God imputes righteousness apart from works:',
'And the father of circumcision to those who not only are of the circumcision, \
but who also walk in the steps of the faith which our father Abraham had while \
still uncircumcised.','who, contrary to hope, in hope believed. so that he beca\
me the father of many nations, according to what was spoken,"So shall your desc\
endants be."'
]
    return mainHeadings, boldVerse, keyLinks, favoriteVerse



def main():
    print("The Epistle of Paul the Apostle to Romans")
    mH = []
    bV =[]
    kL = {}
    fV = []
    verse = ""
    mH,bV,kL,fV = chapter1()
    print("Chapter 1:")
    print(mH[0])
    print(bV[1])
    print(kL['1:16'])
    tuplePairs= list(kL.items())
    print(tuplePairs[1])
    print("One of my favorite verses is", fV[1])
    print("Chapter 2:")
    mH,bV,kL,fV = chapter2()
    print(mH[0])
    print(bV[1])
    print(kL['2:24'])
    print("One of my favorite verses is", fV[2])
    print("Chapter 3:")
    mH,kL,fV,bV = chapter3()
    print(mH[2])
    print(kL['3:18'])
    print(fV[0])
    print(bV[1])
    mH,bV,kL,fV = chapter4()
    print("Chapter 4:")
    print(bV[2])
    print(kL['4:18'])
    print("One of my favorite verses is", fV[3])
    verse = pickRandFavoriteVerse(fV)
    print(verse)




if __name__ == '__main__':
    main()

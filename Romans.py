#Romans
#Use all dicts for 1 Corinthians
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


def main():
    print("The Epistle of Paul the Apostle to Romans")
    mH = []
    bV =[]
    kL = {}
    fV = []
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
    pass

if __name__ == '__main__':
    main()

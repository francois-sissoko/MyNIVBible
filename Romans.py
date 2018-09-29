#Romans
#Use all dicts for 1 Corinthians
import random
from datetime import *


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

def chapter5():
    mainHeadings = ['Faith Triumphs in Trouble', 'Christ in Our Place', 'Death \
in Adam, Life in Christ']
    boldVerse = ['For when we were still without strength, in due time Christ d\
ied for the ungodly.','Therefore, just as through one man sin entered the world\
, and death through sin, and thus death spread to all men, because all sinned--']
    keyLinks = {'5:1':'Another ancient reading is, let us have peace.' }
    favoriteVerse = ['Now hope does not disappoint, because the love has been p\
oured out in our hearts by the Holy Spirit who was given to us.', 'Therefore, a\
s through one man\'s offense judgment came to all men, resulting in condemnatio\
n,even so through one Man\'s righteous act the free gift came to all men, resul\
ting in justification of life.']
    return mainHeadings, boldVerse, keyLinks, favoriteVerse

def chapter6():
    mainHeadings =['Dead to Sin, Alive to God', 'From Slaves of Sin to Slaves o\
f God']
    boldVerse = ['What then? Shall we sin because we are not under law but unde\
r grace? Certainly not!']
    keyLinks = {'':None}
    favoriteVerse = ['And do not present your members as instruments of unright\
eousness to sin, but present yourselves to God as being alive from the dead, an\
d your members as instruments of righteousness to God','I speak in human terms \
because of the weakness of your flesh. For just as you presented your members a\
s slaves of uncleanness, and of lawlessness leading to more lawlessness, so now\
 present your members as slaves of righteousness for holiness.']
    return mainHeadings, boldVerse, keyLinks, favoriteVerse

def chapter7():
    mainHeadings =['Freed from the Law', 'Sin\'s Advantage in the Law','Law Can\
not Save from Sin']
    boldVerse = ['What shall we say then? Is the law sin? Certainly not! On the\
contrary, I would not have know sin except the law. For I would not have known \
covetousness unless the law had said, "You shall not covet','Has then what is g\
ood become death to me? Certainly not! But sin, that it might appear sin, was p\
roducing death in me through what is good, so that sin through the commandment \
might become exceedingly sinful']
    keyLinks = {'7:7':'Exodus 20:17; Deuteronomy 5:21'}
    favoriteVerse = ['So then if, while her husband lives, she marries another \
man, she will be called an adulteress; but if her husband dies, she is free fro\
m that law, so that she is no adulteress, though she has married another man.',
'Therefore the law is holy, and the commandment holy and just and good','If, th\
en, I do what I will not to do. I agree with the law that it is good.','For I d\
elight in the law of God according to the inward man.']
    return mainHeadings, boldVerse, keyLinks, favoriteVerse

def chapter8():
    mainHeadings =['Free from Indwelling Sin','Sonship Through the Spirit', 'Fr\
om Suffering to Glory','God\'s Everlasting Love']
    boldVerse = ['Therefore, brethren, we are debtors- not to the flesh, to liv\
e according to the flesh.','For I consider that the sufferings of this present \
time are not worthy to be compared with the glory which shall be revealed in us'
,'What then shall we say to these things? If God is for us, who can be against \
us?']
    keyLinks = {'8:1':'NU-Text omits the rest of this verse',
    '8:26':'NU-text omits for us','8:36':'Psalm 44:22'}
    favoriteVerse = ['For to be carnally minded is death, but to be spiritually\
minded is life and peace','The Spirit Himself bears witness with our spirit tha\
t we are children of God', ' Now He who searches the hearts knows what the mind\
 of the Spirit is, because He makes intercession for the saints according to th\
e will of God','Yet in all these things we are more than conquerors through Him\
who loved us.']
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
    mH,bV,kL,fV = chapter5()
    print("Chapter 5:")
    print(bV[0])
    print(kL['5:1'])
    print("One of my favorite verses is", fV[1])
    verse = pickRandFavoriteVerse(fV)
    print(verse)
    mH,bV,kL,fV = chapter6()
    print("Chapter 6:")
    print(mH[1])
    print(bV[0])
    print("One of my favorite verses is", fV[1])
    verse = pickRandFavoriteVerse(fV)
    print(verse)
    print('9/10/18')
	#print(date(2018,9,10).weekday()) # day of the week function
    print('9/12/18')
    print("High 93 L 63 UV Index 7 of 10")
    mH,bV,kL,fV = chapter7()
    print(mH[0])
    print(bV[0])
    print(kL['7:7'])
    print("One of my favorite verses is", fV[1])
    verse = pickRandFavoriteVerse(fV)
    print(verse)
    mH,bV,kL,fV = chapter8()
    print(mH[3])
    print(bV[2])
    print(kL['8:36'])
    print("One of my favorite verses is", fV[3])
    verse = pickRandFavoriteVerse(fV)
    print(verse)
    print(date(2018,9,27))
    print(date(2018,9,27).weekday())
    print("Thursday")
    print("Satuday 9/29/2018")
    print(date(2018,9,29))
    print(date(2018,9,29).weekday())
    print("DET 24:16")







if __name__ == '__main__':
    main()

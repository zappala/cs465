from flask import render_template

from config import app
from .schedule import *
import os

static = '/static/lectures/f20/'
pubs = '/static/pubs/'
term = '/fall-2020/'

@app.route('/fall-2020/lectures')
def fall2020lectures():
    lecs = os.listdir(static[1:])
    return render_template(term + 'lectures.html', files=lecs, base=static )


@app.route('/fall-2020/schedule')
def fall2020schedule():
    s = Schedule()

    #week 1
    s.week()

    d = s.day("Sept 1")

    d.lecture("Cryptography")
    d.slide("Introduction",static + 'Introduction.pdf')
    d.slide("Terminology",static + 'Terminology.pdf')
    d.assignment("Homework #1",term + 'homework/homework1')
    
    d = s.day("Sept 3")
    d.assignment("Homework #0",term + 'homework/homework0')
    d.slide("Cryptography",static + 'Cryptography.pdf')
    d.slide("AES",static + 'AES.pdf')
    d.lecture("Cryptography")

    #week 2
    s.week()

    d = s.day("Sept 8")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')
    d = s.day("Sept 9")
    d.assignment("Homework #2",term + 'homework/homework2')    

    d = s.day("Sept 10")
    d.lecture("Block Cipher Modes, Authenticated Encryption Modes, and Padding")
    d.slide("Block Cipher Modes",static + 'BlockCipherModes.pdf')
    d.reading("How to Choose an Authenticated Encryption Mode (optional)", "https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/")
    d.reading("The Galois/Counter Mode of Operation (GCM) (optional)","http://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/gcm-spec.pdf")

    d = s.day("Sept 14")
    d.assignment("Project #1: AES",term + 'projects/project1')

    #week 3
    s.week()

    d = s.day("Sept 15")
    d.assignment("Homework #3",term + 'homework/homework3')
    d.lecture("Cryptographic Hash Functions")
    d.slide("Cryptographic Hash Functions",static + 'CryptographicHashFunctions.pdf')
    d.reading('NIST Hash Project (optional)','http://csrc.nist.gov/groups/ST/hash/index.html')
    d.reading('Chinese researchers find first SHA-1 collision 2005','https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html')
    d.reading("Google announces practical collision SHA-1, Feb 2017","https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html")
    d.slide("Class Slides for Hash Attack Discussion","https://docs.google.com/presentation/d/1i2TvaLXZjWtZubOm-7sNVrbmnNg3ji1fQ9XmaWzE_n8/edit?usp=sharing")



    d = s.day("Sept 17")
    d.lecture("Message Authentication Codes - MAC")
    d.reading("SHA-1 spec",pubs + 'fips180-3_final.pdf')
    d.reading("Why I hate CBC-MAC (Optional)","https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/")
    d.slide("MAC",static + "MAC.pdf")


    d = s.day("Sept 18")
    d.assignment("Project #2: Hash Attack", term + 'projects/project2')

    #week 4
    s.week()

    d = s.day("Sept 22")
    d.lecture("Public-Key Crypto Intro + Math overview  (discuss Hash Attack)")
    d.slide("Class Slides for MAC Attack Discussion","https://docs.google.com/presentation/d/19HfSDfiPJxaC-snRp-C2gw466UzeYlOtPEpeh2679CE/edit?usp=sharing")
    d.slide("Publick-key Intro / Math Intro / Diffie-Hellman",static + "Diffie-Hellman.pdf")
    d.assignment("Homework #4",term + 'homework/homework4')

    d = s.day("Sept 24")
    d.lecture("Diffie-Hellman")
    d.slide("Diffie-Hellman",static + "Diffie-Hellman.pdf")
    
    d = s.day("Sept 25")
    d.assignment("Project #3: MAC Attack", term + 'projects/project3')

    #week 5
    s.week()
    
    d = s.day("Sept 29")
    d.lecture("RSA Part 1")
    d.slide("RSA",static + "RSA.pdf")
    d.assignment("Homework #5",term + 'homework/homework5')

    d = s.day("Oct 1")
    d.lecture("RSA Part 2")
    d.slide("RSA",static + "RSA.pdf")

    d = s.day("Oct 2")
    d.assignment("Project #4: Diffie-Hellman", term + 'projects/project4')

    #week 6
    s.week()

    d = s.day("Oct 6")
    d.lecture("Digital Certificates and Signatures")
    d.slide("PKI",static + "PKI.pdf")
    d.assignment("Homework #6",term + 'homework/homework6')
    
    d = s.day("Oct 8")
    d.lecture("Public Key Infrastructure ")
    d.slide("PKI",static + "PKI.pdf")
    

    d = s.day("Oct 9")
    d.assignment("Project #5: RSA", term + 'projects/project5')
    
    s.week()

    d = s.day("Oct 13")
    d.assignment("None", None)
    d.lecture("In Class Review for Midterm Exam 1.") 
    d.slide("Midterm Exam 1 study guide","https://docs.google.com/document/d/1tUISx0gQz1OkKihHag4WBzRKlo5hgIB_-ApwGypFmJg/edit?usp=sharing")

    d = s.day("Oct 15")
    d.lecture("Test will be live  Oct 15 through Oct 17 on LearningSuite")
    d.assignment("No Class. Take your Midterm Exam.")

    s.week()

    d = s.day("Oct 20")
    d.assignment("Homework #7",term + 'homework/homework7')
    d.lecture("TLS Part 1")
    d.slide("TLS",static + "TLS-2020.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")

    d = s.day("Oct 22")
    d.lecture("TLS part 2")    
    d.slide("TLS",static + "TLS-2020.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")

    d = s.day("Oct 23")
    d.assignment("Project #6: TLS", term + 'projects/project6')


    s.week()
    d = s.day("Oct 27")

    d.assignment("Homework #8", term + 'homework/homework8')
    d.lecture("Passwords (+ Midterm Exam #1 handback)")
    d.slide("Passwords", static + "Passwords.pdf")
    d.reading("Easy Ways to Build a Better P@$5w0rd (NIST)", "https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd")
    d.reading("How to Devise Passwords That Drive Hackers Away","https://www.nytimes.com/2012/11/08/technology/personaltech/how-to-devise-passwords-that-drive-hackers-away.html")


    d=s.day("Oct 29")
    d.lecture("Passwords Continued/Multi-factor Authentication and Password Managers")
    d.slide("Passwords", static + "Passwords.pdf")
    d.slide("Multi-factor authentication and password vaults", "https://docs.google.com/presentation/d/1eqFB1IklngE5x2iEVxkU2q9cV-eFH7JJPF7TK9AE0BM/edit?usp=sharing")


    d=s.day("Oct 30")
    d.assignment("Project #7: Password Cracking", term + 'projects/project7')


    s.week()

    d=s.day("Nov 3")
    d.assignment("Homework #9",term + 'homework/homework9')
    d.lecture("Binary Layout/Exploitation and Buffer Overflows")
    d.slide("Stack Frame Layout Simplified", "https://docs.google.com/presentation/d/1FnqqExqirZTQYsI3kN_74OfyiQKBoIsNShXk2ApcNrI/edit#slide=id.p")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    d.reading("Smashing the Stack For Fun and Profit","http://www.phrack.org/issues/49/14.html#article")
    d.reading("Smashing the Stack For Fun and Profit (Today)","https://travisf.net/smashing-the-stack-today")
    d.reading("Smashing the Stack in 2011","https://paulmakowski.wordpress.com/2011/01/25/smashing-the-stack-in-2011/")
    d.reading("Smashing the Modern Stack for Fun and Profit","https://www.ethicalhacker.net/columns/heffner/smashing-the-modern-stack-for-fun-and-profit/")

    d = s.day("Nov 5")
    d.lecture("Binary Layout/Exploitation and Buffer Overflows Part 2")

    d = s.day("Nov 6")
    d.assignment("Project #8: Extracting Secrets", term + 'projects/project8')


    s.week()
    d = s.day("Nov 10")
    d.assignment("Homework #10", term + 'homework/homework10')
    d.lecture("Binary Layout/Exploitation and Buffer Overflows Part 3")
    d.slide("Stack Frame Layout Simplified", "https://docs.google.com/presentation/d/1FnqqExqirZTQYsI3kN_74OfyiQKBoIsNShXk2ApcNrI/edit#slide=id.p")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")

    d = s.day("Nov 12")
    d.lecture("TBD - check back later")
    #d.slide("Secure Email",static + "SecureEmail.pdf")

    d = s.day("Nov 13")
    d.assignment("Project #9: Buffer Overflow", term + 'projects/project9')


    s.week()


    d = s.day("Nov 17")
    d.lecture("In Class Review for Midterm Exam 2")
    d.reading("Midterm Exam 2 study guide","https://docs.google.com/document/d/1tUISx0gQz1OkKihHag4WBzRKlo5hgIB_-ApwGypFmJg/edit?usp=sharing")



    
    d = s.day("Nov 19")
    d.lecture("Midterm Exam 2 Live on LearningSuite Nov 19 through Nov 21")
    d.assignment("No Class. Take your Midterm.")


    s.week()
    d = s.day("Nov 24")
    d.lecture("No Class Tuesday (Friday Instruction)")
    d = s.day("Nov 26")
    d.lecture("No Class Thursday (Holiday)")


    s.week()
    d = s.day("Dec 1")
    d.lecture("Secure Email (Midterm Exam 2 handback)")
    d.slide("Secure Email",static + "SecureEmail.pdf")
    d.assignment("Homework #11", term + 'homework/homework11')


    d = s.day("Dec 3")
    d.lecture("Secure Email part 2")
    d.slide("Secure Email",static + "SecureEmail.pdf")

    d = s.day("Dec 4")
    d.assignment("Project #10: Secure Email", term + 'projects/project10')

    s.week()

    d = s.day("Dec 8")
    d.lecture("Integer Manipulation Vulnerabilities / Social Engineering")
    d.slide("Microsoft Whitepaper", "https://bit.ly/2I9nKPW")
    d.slide("Social Engineering", static + "social_engineering.pdf")

    d = s.day("Dec 9")
    d.assignment("Homework #12: Extra Credit",term + 'homework/homework12')

    d = s.day("Dec 10")
    d.lecture("Course Review and Final Exam review")
    d.slide("Exam Review", "https://docs.google.com/document/d/1suND4Z-r1uDvHMj8fSCWAyScR_1gjavcNu8SFtjPcCQ/edit?usp=sharing")
    d.assignment("Project #11: Extra Credit - last day for submission", term + 'projects/project11')



    return render_template('fall-2020/schedule.html',active='schedule', weeks=s.weeks)

from flask import render_template

from config import app
from .schedule import *
import os

static = '/static/lectures/w20/'
pubs = '/static/pubs/'
term = '/winter-2020/'

@app.route('/winter-2020/lectures')
def winter2020lectures():
    lecs = os.listdir(static[1:])
    return render_template(term + 'lectures.html', files=lecs, base=static )


@app.route('/winter-2020/schedule')
def winter2020schedule():
    s = Schedule()

    s.week()

    d = s.day("January 7")

    d.lecture("Cryptography")
    d.slide("Introduction",static + 'Introduction.pdf')
    d.slide("Terminology",static + 'Terminology.pdf')
    d.lecture("Cryptography")
    d.assignment("Homework #1",term + 'homework/homework1')
    
    d = s.day("January 09")
    d.slide("Cryptography",static + 'Cryptography.pdf')
    d.slide("AES",static + 'AES.pdf')
    d.lecture("Cryptography")

    s.week()

    d = s.day("January 14")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')

    d = s.day("January 15")
    d.assignment("Homework #2",term + 'homework/homework2')    

    d = s.day("January 16")
    d.lecture("Block Cipher Modes, Authenticated Encryption Modes, and Padding")
    d.slide("Block Cipher Modes",static + 'BlockCipherModes.pdf')
    d.reading("How to Choose an Authenticated Encryption Mode (optional)", "https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/")
    d.reading("The Galois/Counter Mode of Operation (GCM) (optional)","http://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/gcm-spec.pdf")

    d = s.day("January 17")
    d.assignment("Project #1: AES",term + 'projects/project1')

    s.week()

    d = s.day("January 21")
    d.assignment("Homework #3",term + 'homework/homework3')
    d.lecture("Cryptographic Hash Functions")
    d.slide("Cryptographic Hash Functions",static + 'CryptographicHashFunctions.pdf')
    d.reading('NIST Hash Project (optional)','http://csrc.nist.gov/groups/ST/hash/index.html')
    d.reading('Chinese researchers find first SHA-1 collision 2005','https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html')
    d.reading("Google announces practical collision SHA-1, Feb 2017","https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html")




    d = s.day("January 23")
    d.lecture("Message Authentication Codes - MAC")
    d.reading("SHA-1 spec",pubs + 'fips180-3_final.pdf')
    d.reading("Why I hate CBC-MAC","https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/")
    d.slide("MAC",static + "MAC.pdf")


    d = s.day("January 24")
    d.assignment("Project #2: Hash Attack", term + 'projects/project2')
    s.week()


    d = s.day("January 28")
    d.lecture("Public-Key Crypto Intro + Math overview  (discuss Hash Attack)")
#    d.slide("Class Slides for Hash Attack Discussion","https://docs.google.com/presentation/d/1i2TvaLXZjWtZubOm-7sNVrbmnNg3ji1fQ9XmaWzE_n8/edit?usp=sharing")
    d.slide("Class Slides for MAC Attack Discussion","https://docs.google.com/presentation/d/19HfSDfiPJxaC-snRp-C2gw466UzeYlOtPEpeh2679CE/edit?usp=sharing")
    d.slide("Publick-key Intro / Math Intro / Diffie-Hellman",static + "Diffie-Hellman.pdf")
    d.assignment("Homework #4",term + 'homework/homework4')

    d = s.day("January 30")
    d.lecture("Diffie-Hellman")
    d.slide("Diffie-Hellman",static + "Diffie-Hellman.pdf")
    
    d = s.day("January 31")
    d.assignment("Project #3: MAC Attack", term + 'projects/project3')

    s.week()
    
    d = s.day("February 4")
    d.lecture("RSA Part 1")
    d.slide("RSA",static + "RSA.pdf")
    d.assignment("Homework #5",term + 'homework/homework5')

    d = s.day("February 6")
    d.lecture("RSA Part 2")
    d.slide("RSA",static + "RSA.pdf")

    d = s.day("February 7")
    d.assignment("Project #4: Diffie-Hellman", term + 'projects/project4')

    s.week()

    d = s.day("February 11")
    d.lecture("Digital Certificates and Signatures")
    d.slide("PKI",static + "PKI.pdf")
    d.assignment("Homework #6",term + 'homework/homework6')
    
    d = s.day("February 13")
    d.lecture("Public Key Infrastructure ")
    d.slide("PKI",static + "PKI.pdf")
    

    d = s.day("February 14")
    d.assignment("Project #5: RSA", term + 'projects/project5')
    
    s.week()

    d = s.day("Febrary 18")
    d.assignment("None", None)
    d.lecture("Monday Class on this day - No Lecture")

    d = s.day("Febrary 19")
    d.assignment("Homework #7",term + 'homework/homework7')


    d = s.day("February 20")
    d.lecture("TLS Part 1")
    d.slide("TLS",static + "TLS.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")
    d.assignment("None", None)

    s.week()

    d = s.day("February 25")
    d.assignment("None", None)
    d.lecture("In Class Review for Exam 1")
    d.reading("Midterm 1 study guide","https://docs.google.com/document/d/1tUISx0gQz1OkKihHag4WBzRKlo5hgIB_-ApwGypFmJg/edit?usp=sharing")
    d.lecture("Midterm 1 Feb 27 - Mar 2. No office hours (out of town) through the 2nd of March")

    d = s.day("February 27")
    d.assignment("No Class. Take your Midterm.")

    d = s.day("Feb 28")
    d.assignment("Read March 3 Readings over the weekend")

    s.week()

    d = s.day("March 3")
    d.lecture("TLS part 1.5/2")    
    d.slide("TLS",static + "TLS.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")
    d.assignment("Homework #8", term + 'homework/homework8')


    d = s.day("March 5")
    d.lecture("TLS continued")
    d.lecture("Passwords")
    d.slide("Passwords", static + "Passwords.pdf")
    d.reading("Easy Ways to Build a Better P@$5w0rd (NIST)", "https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd")
    d.reading("How to Devise Passwords That Drive Hackers Away","https://www.nytimes.com/2012/11/08/technology/personaltech/how-to-devise-passwords-that-drive-hackers-away.html")


    d = s.day("March 6")
    d.assignment("Project #6: TLS", term + 'projects/project6')

    s.week()
    d=s.day("March 10")
    d.lecture("Passwords Continued")
    d.slide("Passwords", static + "Passwords.pdf")
    d.assignment("Homework #9",term + 'homework/homework9')

    d=s.day("March 12")


    d = s.day("March 13")
    d.lecture("Beyond Passwords and Authentication")
    d.slide("Multi-factor authentication and password vaults", "https://docs.google.com/presentation/d/1eqFB1IklngE5x2iEVxkU2q9cV-eFH7JJPF7TK9AE0BM/edit?usp=sharing")
    d.assignment("Project #7: Password Cracking", term + 'projects/project7')

    s.week()
    d = s.day("March 17")
    d.lecture("Buffer Overflow")
    d.reading("Smashing the Stack For Fun and Profit","http://www.phrack.org/issues/49/14.html#article")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    d.reading("Smashing the Stack For Fun and Profit (Today)","https://travisf.net/smashing-the-stack-today")
    d.reading("Smashing the Stack in 2011","https://paulmakowski.wordpress.com/2011/01/25/smashing-the-stack-in-2011/")
    d.reading("Smashing the Modern Stack for Fun and Profit","https://www.ethicalhacker.net/columns/heffner/smashing-the-modern-stack-for-fun-and-profit/")
    
    d.assignment("Homework #10", term + 'homework/homework10')

    d = s.day("March 19")
    d.lecture("Buffer Overflow")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")

    d = s.day("March 20")
    d.assignment("Project #9: Extracting Secrets", term + 'projects/project9')
    s.week()



    d = s.day("March 24")
    d.assignment("Homework #11",term + 'homework/homework11')
    d.lecture("Buffer Overflow")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    
    d = s.day("March 26")
    d.lecture("Secure Email")
    d.slide("Secure Email",static + "SecureEmail.pdf")

    d = s.day("March 27")
    d.assignment("Project #8: Buffer Overflow", term + 'projects/project8')

    s.week()
    d = s.day("March 31")
    d.lecture("Secure Email part 2")
    d.slide("Secure Email",static + "SecureEmail.pdf")
    d.assignment("Homework #12", term + 'homework/homework12')


    d = s.day("April 2")
    d.lecture("Integer Manipulation Vulnerabilities")
    d.slide("Microsoft Whitepaper", "https://bit.ly/2I9nKPW")
    d.slide("Exam Review", "https://docs.google.com/document/d/1suND4Z-r1uDvHMj8fSCWAyScR_1gjavcNu8SFtjPcCQ/edit?usp=sharing")

    d = s.day("April 3")
    d.assignment("Project #10: Secure Email", term + 'projects/project10')

    s.week()


    d = s.day("April 9")
    d.lecture("TENNATIVE - schedule for rest of semester not yet arranged = possibly - In class Mid-Term Test (#2)")
#    
#    d = s.day("April 11")
#    d.lecture("Social Engineering")
#    d.slide("Social Engineering", static + "social_engineering.pdf")
#    
#
#    s.week()
#
#    d = s.day("April 16")
#    d.lecture("Exam Return (MT2) and Exam Review (Final), and if we have time, Signal")
#    d.slide("Signal",static + "Signal.pdf")
#
#    d = s.day("April 17")
#    d.assignment("Project #11: Extra Credit", term + 'projects/project11')
#    d.assignment("Homework #13: Extra Credit", term + 'homework/homework13')
#
#    
    return render_template('winter-2020/schedule.html',active='schedule', weeks=s.weeks)

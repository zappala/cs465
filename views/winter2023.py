from flask import render_template

from config import app
from .schedule import *

@app.route('/winter-2023/schedule')
def winter2023schedule():
    static = '/static/lectures/v1/'
    v2 = '/static/lectures/v2/'
    pubs = '/static/pubs/'
    term = '/winter-2023/'
    s = Schedule()

    s.week()

    d = s.day("January 9")

    d.lecture("Cryptography")
    d.slide("Introduction",static + 'Introduction.pdf')
    d.slide("Terminology",static + 'Terminology.pdf')
    d.assignment("Homework #1",term + 'homework/homework1')

    d = s.day("January 11")
    d.lecture("Cryptography")
    d.slide("Cryptography",static + 'Cryptography.pdf')
    
    d = s.day("January 13")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')

    s.week()
    
    d = s.day("January 16")
    d.lecture("HOLIDAY -- MLK Jr Day")

    d = s.day("January 17")
    d.assignment("Homework #2",term + 'homework/homework2')

    d = s.day("January 18")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')

    d = s.day("January 20")
    d.lecture("Block Cipher Modes, Authenticated Encryption Modes, and Padding")
    d.reading("How to Choose an Authenticated Encryption Mode (optional)", "https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/")
    d.reading("The Galois/Counter Mode of Operation (GCM) (optional)","http://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/gcm-spec.pdf")
    d.slide("Block Cipher Modes",static + 'BlockCipherModes.pdf')

    d.assignment("Project #1: AES",term + 'projects/project1')

    s.week()


    d = s.day("January 23")
    d.lecture("Cryptographic Hash Functions")
    d.reading('NIST Hash Project (optional)','http://csrc.nist.gov/groups/ST/hash/index.html')
    d.reading('Chinese researchers find first SHA-1 collision 2005','https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html')
    d.reading("Google announces practical collision SHA-1, Feb 2017","https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html")
    d.slide("Cryptographic Hash Functions",static + 'CryptographicHashFunctions.pdf')
    d.assignment("Homework #3",term + 'homework/homework3')

    d = s.day("January 25")
    d.lecture("Hash Attack")

    d = s.day("January 27")
    d.lecture("MAC")
    d.reading("SHA-1 spec",pubs + 'fips180-3_final.pdf')
    d.reading("Why I hate CBC-MAC","https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/")
    d.slide("MAC",v2 + "MAC.pdf")
    
    d.assignment("Project #2: Hash Attack", term + 'projects/project2')

    s.week()

    d = s.day("January 30")
    d.lecture("Diffie-Hellman")
    d.slide("Diffie-Hellman",static + "Diffie-Hellman.pdf")
    d.assignment("Homework #4",term + 'homework/homework4')
    
    d = s.day("February 1")
    d.lecture("Diffie-Hellman")

    d = s.day("February 3")
    d.lecture("Project discussion")

    d.assignment("Project #3: MAC Attack", term + 'projects/project3')

    s.week()

    d = s.day("February 6")
    d.lecture("RSA")
    d.slide("RSA",static + "RSA.pdf")
    
    d.assignment("Homework #5",term + 'homework/homework5')

    d = s.day("February 8")
    d.lecture("RSA")


    d = s.day("February 10")
    d.lecture("Project discussion")
    d.assignment("Project #4: Diffie-Hellman", term + 'projects/project4')

    s.week()

    d = s.day("February 13")
    d.lecture("Public Key Infrastructure and Certificates")
    d.slide("PKI",static + "PKI.pdf")
    d.assignment("Homework #6",term + 'homework/homework6')

    d = s.day("February 15")
    d.lecture("Public Key Infrastructure and Certificates")

    d = s.day("February 17")
    d.lecture("Project discussion")

    d.assignment("Project #5: RSA", term + 'projects/project5')


    s.week()

    d = s.day("February 20")
    d.lecture("HOLIDAY -- Presidents Day")

    d = s.day("February 21")
    d.lecture("No Class")

    d = s.day("February 22")
    d.lecture("Midterm Review")
    d.reading("Midterm 1 Study Guide","help/study-guide-midterm1")
    d.assignment("Homework #7",term + 'homework/homework7')

    d = s.day("February 24")
    d.lecture("No class -- take the midterm")
    d.assignment("Midterm will be live February 23 and February 24 on Learning Suite")    


    s.week()

    d = s.day("February 27")
    d.lecture("TLS")
    d.slide("TLS",static + "TLS.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")
    
    d = s.day("March 1")
    d.lecture("TLS")

    d = s.day("March 3")
    d.lecture("Project discussion")

    d.assignment("Project #6: TLS", term + 'projects/project6')

    s.week()

    d = s.day("March 6")
    d.lecture("Passwords")
    d.slide("Passwords",static + "Passwords.pdf")
    d.reading("Easy Ways to Build a Better P@$5w0rd (NIST)", "https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd")
    d.reading("How to Devise Passwords That Drive Hackers Away","https://www.nytimes.com/2012/11/08/technology/personaltech/how-to-devise-passwords-that-drive-hackers-away.html")
    
    d.assignment("Homework #9", term + 'homework/homework9')

    d = s.day("March 8")
    d.lecture("Passwords")
    d.reading("An Administrator's Guide to Password Research","https://www.microsoft.com/en-us/research/publication/an-administrators-guide-to-internet-password-research/")

    d = s.day("March 10")
    d.lecture("Passwords")
    d.reading("The Quest to Replace Passwords: A Framework for Comparative Evaluation of Web Authentication Schemes","https://ieeexplore.ieee.org/document/6234436")
    
    d.assignment("Project #7: Password Cracking", term + 'projects/project7')
    
    s.week()

    d = s.day("March 13")
    d.lecture("Buffer Overflow")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    d.reading("Smashing the Stack For Fun and Profit","http://www.phrack.org/issues/49/14.html#article")
    d.reading("Smashing the Stack For Fun and Profit (Today)","https://travisf.net/smashing-the-stack-today")
    d.reading("Smashing the Stack in 2011","https://paulmakowski.wordpress.com/2011/01/25/smashing-the-stack-in-2011/")
    d.reading("Smashing the Modern Stack for Fun and Profit","https://www.ethicalhacker.net/columns/heffner/smashing-the-modern-stack-for-fun-and-profit/")

    d = s.day("March 15")
    d.lecture("Buffer Overflow")
    d.assignment("Homework #10", term + 'homework/homework10')

    d = s.day("March 17")
    d.lecture("Spring Break -- No class")

    s.week()

    d = s.day("March 20")
    d.lecture("Signal")
    d.slide("Signal",static + "Signal.pdf")
    d.assignment("Homework #11",term + 'homework/homework11')

    d = s.day("March 22")
    d.lecture("Signal")

    d = s.day("March 24")
    d.lecture("Encryption Backdoor Debate -- Read in advance and come to class with 3 to 5 points in favor or against government surveillance of encrypted traffic that you found compelling")
    d.reading("Paper: Keys under doormats: Mandating insecurity by requiring government access to all data and communications","Https://academic.oup.com/cybersecurity/article/1/1/69/2367066")
    d.reading("Perspectives on Encryption and Surveillance","https://www.lawfareblog.com/perspectives-encryption-and-surveillance")

    s.week()

    d = s.day("March 27")
    d.lecture("Secure Email")
    d.slide("Secure Email",static + "SecureEmail.pdf")

    d = s.day("March 29")
    d.lecture("TBD")

    d = s.day("March 31")
    d.lecture("TBD")
   
    d.assignment("Project #10: PGP and S/MIME", term + 'projects/project10')

    s.week()

    d = s.day("April  3")
    d.lecture("TBD")

    d = s.day("April 5")
    d.lecture('TBD')

    d = s.day("April 7")
    d.lecture("TBD")
    d.assignment("Homework #12", term + 'homework/homework12')


    s.week()

    d = s.day("April 10")
    d.lecture("Trust")

    d = s.day("April 12")
    d.lecture("TBD")

    d = s.day("April 14")
    d.lecture("TBD")


    d.assignment("Project #11: Extra Credit", term + 'projects/project11')

    s.week()

    d = s.day("April 17")
    d.lecture("TBD")


    d = s.day("April 19")
    d.lecture("TBD")


    return render_template('winter-2023/schedule.html',active='schedule', weeks=s.weeks)

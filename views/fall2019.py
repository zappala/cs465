from flask import render_template

from config import app
from .schedule import *

@app.route('/fall-2019/schedule')
def fall2019schedule():
    static = '/static/lectures/v1/'
    v2 = '/static/lectures/v2/'
    pubs = '/static/pubs/'
    term = '/fall-2019/'
    s = Schedule()

    s.week()

    d = s.day("September 4")

    d.lecture("Introduction")
    d.slide("Introduction",static + 'Introduction.pdf')
    d.assignment("Homework #1",term + 'homework/homework1')

    d = s.day("September 6")
    d.lecture("Introduction")
    d.slide("Terminology",static + 'Terminology.pdf')


    s.week()
    d = s.day("September 9")
    d.lecture("Cryptography")
    d.slide("Cryptography",static + 'Cryptography.pdf')

    
    d = s.day("September 11")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')

    d = s.day("September 13")
    d.lecture("AES")
    d.slide("AES",static + 'AES.pdf')
    d.assignment("Homework #2",term + 'homework/homework2')

    s.week()


    d = s.day("September 16")
    d.lecture("Block Cipher Modes, Authenticated Encryption Modes, and Padding")
    d.reading("How to Choose an Authenticated Encryption Mode (optional)", "https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/")
    d.reading("The Galois/Counter Mode of Operation (GCM) (optional)","http://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/gcm-spec.pdf")
    d.slide("Block Cipher Modes",static + 'BlockCipherModes.pdf')

    d = s.day("September 18")
    d.lecture("Cryptographic Hash Functions")
    d.reading('NIST Hash Project (optional)','http://csrc.nist.gov/groups/ST/hash/index.html')
    d.reading('Chinese researchers find first SHA-1 collision 2005','https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html')
    d.reading("Google announces practical collision SHA-1, Feb 2017","https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html")
    d.slide("Cryptographic Hash Functions",static + 'CryptographicHashFunctions.pdf')

    d = s.day("September 20")
    d.lecture("MAC")
    d.reading("SHA-1 spec",pubs + 'fips180-3_final.pdf')
    d.reading("Why I hate CBC-MAC","https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/")
    d.slide("MAC",v2 + "MAC.pdf")
    d.assignment("Homework #3",term + 'homework/homework3')

    d = s.day("September 21")
    d.assignment("Project #1: AES",term + 'projects/project1')

    s.week()

    d = s.day("September 23")
    d.lecture("Hash Attack")
    d.assignment("Homework #4",term + 'homework/homework4')

    d = s.day("September 25")
    d.lecture("Diffie-Hellman")
    d.slide("Diffie-Hellman",static + "Diffie-Hellman.pdf")

    d = s.day("September 27")
    d.lecture("Diffie-Hellman")
    d.assignment("Project #2: Hash Attack", term + 'projects/project2')

    s.week()

    d = s.day("September 30")
    d.lecture("Discuss Homework #5 and Modular Exponentiation")
    d.assignment("Homework #5",term + 'homework/homework5')

    d = s.day("October 2")
    d.lecture("RSA")
    d.slide("RSA",static + "RSA.pdf")

    d = s.day("October 4")
    d.lecture("RSA")
    d.assignment("Project #3: MAC Attack", term + 'projects/project3')

    s.week()

    d = s.day("October 7")
    d.lecture("No class -- office hours")

    d = s.day("October 9")
    d.lecture("Public Key Infrastructure and Certificates")
    d.slide("PKI",static + "PKI.pdf")
    d.assignment("Homework #6",term + 'homework/homework6')

    d = s.day("October 11")
    d.lecture("Public Key Infrastructure and Certificates")
    d.assignment("Project #4: Diffie-Hellman", term + 'projects/project4')

    s.week()

    d = s.day("October 14")
    d.lecture("Exam Review")
    d.reading("Midterm 1 Study Guide","help/study-guide-midterm1")
    d.assignment("Homework #7",term + 'homework/homework7')

    d = s.day("October 15")
    d.assignment("Exam #1 first day in the testing center")

    d = s.day("October 16")
    d.lecture("No Class")
    d.assignment("Exam #1 last day in the testing center")


    d = s.day("October 18")
    d.lecture("TLS")
    d.slide("TLS",static + "TLS.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")


    s.week()

    d = s.day("October 21")
    d.lecture("TLS, Project #5 Discussion")

    d = s.day("October 23")
    d.lecture("Exam Recap")

    d = s.day("October 25")
    d.lecture("Exam Recap and RSA project")
    d.assignment("Project #5: RSA", term + 'projects/project5')

    s.week()

    d = s.day("October 28")
    d.lecture("No class -- Dr. Zappala at NSF PI Meeting")

    d = s.day("October 30")
    d.lecture("Logjam TLS Attack")
    d.reading("Weak Diffie-Hellman and the Logjam Attack","https://weakdh.org/")
    d.assignment("Homework #8",term + 'homework/homework8')

    d = s.day("November 1")
    d.lecture("TBD")
    d.assignment("Project #6: TLS", term + 'projects/project6')

    s.week()

    d = s.day("November 4")
    d.lecture("Passwords")
    d.slide("Passwords",static + "Passwords.pdf")
    d.reading("Easy Ways to Build a Better P@$5w0rd (NIST)", "https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd")
    d.reading("How to Devise Passwords That Drive Hackers Away","https://www.nytimes.com/2012/11/08/technology/personaltech/how-to-devise-passwords-that-drive-hackers-away.html")

    d = s.day("November 6")
    d.assignment("Homework #9", term + 'homework/homework9')
    d.lecture("Passwords")
    d.reading("An Administrator's Guide to Password Research","https://www.microsoft.com/en-us/research/publication/an-administrators-guide-to-internet-password-research/")

    d = s.day("November 8")
    d.lecture("Passwords")
    d.reading("The Quest to Replace Passwords: A Framework for Comparative Evaluation of Web Authentication Schemes","https://ieeexplore.ieee.org/document/6234436")
    d.assignment("Project #7: Password Cracking", term + 'projects/project7')

    s.week()

    d = s.day("November 11")
    d.lecture("Buffer Overflow")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    d.reading("Smashing the Stack For Fun and Profit","http://www.phrack.org/issues/49/14.html#article")
    d.reading("Smashing the Stack For Fun and Profit (Today)","https://travisf.net/smashing-the-stack-today")
    d.reading("Smashing the Stack in 2011","https://paulmakowski.wordpress.com/2011/01/25/smashing-the-stack-in-2011/")
    d.reading("Smashing the Modern Stack for Fun and Profit","https://www.ethicalhacker.net/columns/heffner/smashing-the-modern-stack-for-fun-and-profit/")

    d = s.day("November 13")
    d.lecture("Buffer Overflow")
    d.assignment("Homework #10", term + 'homework/homework10')

    d = s.day("November 15")
    d.lecture("Buffer Overflow")

    s.week()

    d = s.day("November 18")
    d.lecture("Signal")
    d.slide("Signal",static + "Signal.pdf")
    d.assignment("Homework #11",term + 'homework/homework11')

    d = s.day("November 20")
    d.lecture("Signal")

    d = s.day("November 22")
    d.lecture("Encryption Backdoor Debate -- Read in advance and come to class with 3 to 5 points in favor or against government surveillance of encrypted traffic that you found compelling")
    d.assignment("Project #8: Buffer Overflow", term + 'projects/project8')
    d.reading("Paper: Keys under doormats: Mandating insecurity by requiring government access to all data and communications","Https://academic.oup.com/cybersecurity/article/1/1/69/2367066")
    d.reading("Perspectives on Encryption and Surveillance","https://www.lawfareblog.com/perspectives-encryption-and-surveillance")
    

    s.week()

    d = s.day("November 25")
    d.lecture("Secure Email")
    d.slide("Secure Email",static + "SecureEmail.pdf")

    d = s.day("November 26")
    d.lecture("No Class -- Thanksgiving Holiday")
    d.assignment("Project #9: Extracting Secrets", term + 'projects/project9')

    d = s.day("November 27")
    d.lecture("No Class -- Thanksgiving Holiday")

    d = s.day("November 29")
    d.lecture("No Class -- Thanksgiving Holiday")

    s.week()

    d = s.day("December 2")
    d.lecture("Exam Review")

    d = s.day("December 3")
    d.assignment("Exam #2 first day in testing center")

    d = s.day("December 4")
    d.lecture("No class")
    d.assignment("Exam #2 last day in testing center (ends at 3pm)")

    d = s.day("December 6")
    d.lecture("Encryption Back Door Debate")
    d.assignment("Homework #12", term + 'homework/homework12')


    s.week()

    d = s.day("December 9")
    d.lecture("Trust")
    d.assignment("Project #10: PGP and S/MIME", term + 'projects/project10')

#    d.slide("Demystifying the Secure Enclave Processor","https://www.youtube.com/watch?v=7UNeUT_sRos")

    d = s.day("December 11")
    d.lecture("Exam Recap")


    d.assignment("Project #11: Extra Credit", term + 'projects/project11')

    s.week()

    d = s.day("December 16")
    d.assignment("Last day to take optional final exam")


    return render_template('fall-2019/schedule.html',active='schedule', weeks=s.weeks)

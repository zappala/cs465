from flask import render_template

from config import app
from .schedule import *

@app.route('/fall-2018/schedule')
def fall2018schedule():
    static = '/static/lectures/v1/'
    term = '/fall-2018/'
    s = Schedule()

    s.week()

    d = s.day("September 4")

    d.lecture("Cryptography")
    d.reading("Chapter 1")
    d.assignment("Homework #1")
    
    d = s.day("September 6")
    d.reading("Chapter 2")
    d.lecture("Cryptography")

    s.week()

    d = s.day("September 11")
    d.lecture("AES")
    d.reading("Chapter 3.1 - 3.3.4")
    d.assignment("Homework #2")
    
    d = s.day("September 13")
    d.lecture("Block Cipher Modes")
    d.reading("Chapter 3.1 - 3.3.7")

    s.week()

    d = s.day("September 18")
    d.lecture("Cryptographic Hash Functions")
    d.reading("Chapter 5")
    d.assignment("Homework #3")

    d = s.day("September 19")
    d.assignment("Project #1: AES")

    d = s.day("September 20")
    d.lecture("MAC")

    s.week()

    d = s.day("September 25")
    d.lecture("Public Key Cryptography")
    d.assignment("Homework #4")
    
    d = s.day("September 27")
    d.lecture("Diffie-Hellman")

    d = s.day("September 29")
    d.assignment("Project #2: Hash Attack")
    
    s.week()

    d = s.day("October 2")
    d.lecture("Diffie-Hellman")
    d.assignment("Homework #5")
    
    d = s.day("October 4")
    d.lecture("RSA")

    d = s.day("October 5")
    d.assignment("Project #3: MAC Attack")
    
    s.week()

    d = s.day("October 9")
    d.lecture("RSA")    
    d.assignment("Homework #6")

    
    d = s.day("October 11")
    d.lecture("Certificates")

    s.week()

    d = s.day("October 15")
    d.assignment("Project #4: Diffie-Hellman")
    d.assignment("Project #5: RSA")

    d = s.day("October 16")
    d.lecture("Exam Review")
    d.assignment("Homework #7")
    
    d = s.day("October 18")
    d.lecture("No Class")
    d.assignment("Exam #1")

    s.week()

    d = s.day("October 23")
    d.lecture("TLS")

    d = s.day("October 25")
    d.lecture("TLS")

    d = s.day("October 26")
    d.assignment("Project #6: TLS")

    s.week()

    d = s.day("October 30")
    d.lecture("TLS")
    d.assignment("Homework #8")
    
    d = s.day("November 1")
    d.lecture("Exam Review")

    s.week()

    d = s.day("November 6")
    d.lecture("Passwords")
    d.assignment("Homework #9")
    
    d = s.day("November 8")
    d.lecture("Authentication")

    d = s.day("November 9")
    d.assignment("Project #7: Password Cracking")

    s.week()

    d = s.day("November 13")
    d.lecture("Software Exploits")
    d.assignment("Homework #10")
    
    d = s.day("November 15")
    d.lecture("Stack Smashing")

    s.week()
    
    d = s.day("November 20")
    d.lecture("No Class -- Friday Instruction")
    d.assignment("Project #8: Buffer Overflow")
    
    d = s.day("November 22")
    d.lecture("Thanksgiving Holiday")

    s.week()

    d = s.day("November 27")
    d.lecture("Software Expoits")
    d.assignment("Homework #11")
    
    d = s.day("November 29")
    d.lecture("Software Expoits")

    d = s.day("November 30")
    d.assignment("Project #9: Extracting Secrets")

    s.week()

    d = s.day("December 4")
    d.lecture("Secure Email")
    d.assignment("Homework #12")
    
    d = s.day("December 6")
    d.assignment("Exam #2")    

    s.week()

    d = s.day("December 11")
    d.lecture("Social Engineering")
    d.assignment("Project #10: PGP and S/MIME")
    
    d = s.day("December 13")
    d.lecture("TBD")
    d.assignment("Project #11: Extra Credit")

    
    return render_template('fall-2018/schedule.html',active='schedule', weeks=s.weeks)

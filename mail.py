import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("sharmanirupam2016@gmail.com","ropnjpnbuvjasrhx")
subject="Testing send Email from Python"
body="laal hei laal hei , uncle jee mujhe pyaas lagi hei paani pila do"
message="subject:{}\n\n{}".format(subject,body)
listadd=['sj1025176601@gmail.com']
ob.sendmail('sharmanirupam2016@gmail.com',listadd,message)
ob.quit()


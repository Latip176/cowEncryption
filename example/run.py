from cowEncryption import savior

#your name / path file project
file = "setup.py"

#Encryption
Encrypt = savior.Encryption(file, jenis="file").encPrem()

#check status
print(Encrypt)

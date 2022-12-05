from cowEncryption import savior

#your name / path file project
file = "example.py"

#Encryption
Encrypt = savior.Encryption(file, jenis="file").encPrem()

#check status
print(Encrypt)

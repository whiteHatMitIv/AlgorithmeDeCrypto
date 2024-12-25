import numpy as np

liste = [[5,8],[17,3]]
key = np.matrix(liste)

inverse = np.linalg.inv(key)
det = np.linalg.det(key)
print(det)
print(inverse/(-1/det))

"""if det < 0 :
    det = -det

matrice = inverse / (1/det)

det = int(det)
modulo = det % 26

i=0
while True:
    if (i*modulo)%26 == 1:
        modulo = i
        break
    else:
        i = i+1

print(modulo)"""
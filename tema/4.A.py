import numpy as np

np.random.seed(42)
A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))
print("A = ", A)
print("B = ", B)

C = A @ B
print("C = ", C)

suma = np.sum(C)
print("Suma: ", suma)

col_avg = np.mean(C, axis=0)
print("Col avg: ", col_avg)

maxim = np.max(C)
print("Max: ", maxim)

M = np.random.randint(1, 11, size=(3,3))

print("M = ", M)

det_M = np.linalg.det(M)
print("Det_M: ", det_M)

if det_M != 0:
    inv_M = np.linalg.inv(M)
    print("Inversa lui M: ", inv_M)

    iden_M = M @ inv_M
    print("iden_M: ", iden_M)

    print("Arpoape iden: ", np.allclose(iden_M, np.eye(3)))
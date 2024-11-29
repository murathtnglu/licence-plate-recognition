import cv2 as cv  # Import cv2 but alias it as cv

# Letters
A = cv.imread('alphanumeric/A.bmp', cv.IMREAD_GRAYSCALE)
B = cv.imread('alphanumeric/B.bmp', cv.IMREAD_GRAYSCALE)
C = cv.imread('alphanumeric/C.bmp', cv.IMREAD_GRAYSCALE)
D = cv.imread('alphanumeric/D.bmp', cv.IMREAD_GRAYSCALE)
E = cv.imread('alphanumeric/E.bmp', cv.IMREAD_GRAYSCALE)
F = cv.imread('alphanumeric/F.bmp', cv.IMREAD_GRAYSCALE)
G = cv.imread('alphanumeric/G.bmp', cv.IMREAD_GRAYSCALE)
H = cv.imread('alphanumeric/H.bmp', cv.IMREAD_GRAYSCALE)
I = cv.imread('alphanumeric/I.bmp', cv.IMREAD_GRAYSCALE)
J = cv.imread('alphanumeric/J.bmp', cv.IMREAD_GRAYSCALE)
K = cv.imread('alphanumeric/K.bmp', cv.IMREAD_GRAYSCALE)
L = cv.imread('alphanumeric/L.bmp', cv.IMREAD_GRAYSCALE)
M = cv.imread('alphanumeric/M.bmp', cv.IMREAD_GRAYSCALE)
N = cv.imread('alphanumeric/N.bmp', cv.IMREAD_GRAYSCALE)
O = cv.imread('alphanumeric/O.bmp', cv.IMREAD_GRAYSCALE)
P = cv.imread('alphanumeric/P.bmp', cv.IMREAD_GRAYSCALE)
Q = cv.imread('alphanumeric/Q.bmp', cv.IMREAD_GRAYSCALE)
R = cv.imread('alphanumeric/R.bmp', cv.IMREAD_GRAYSCALE)
S = cv.imread('alphanumeric/S.bmp', cv.IMREAD_GRAYSCALE)
T = cv.imread('alphanumeric/T.bmp', cv.IMREAD_GRAYSCALE)
U = cv.imread('alphanumeric/U.bmp', cv.IMREAD_GRAYSCALE)
V = cv.imread('alphanumeric/V.bmp', cv.IMREAD_GRAYSCALE)
W = cv.imread('alphanumeric/W.bmp', cv.IMREAD_GRAYSCALE)
X = cv.imread('alphanumeric/X.bmp', cv.IMREAD_GRAYSCALE)
Y = cv.imread('alphanumeric/Y.bmp', cv.IMREAD_GRAYSCALE)
Z = cv.imread('alphanumeric/Z.bmp', cv.IMREAD_GRAYSCALE)

# Numbers
one = cv.imread('alphanumeric/1.bmp', cv.IMREAD_GRAYSCALE)
two = cv.imread('alphanumeric/2.bmp', cv.IMREAD_GRAYSCALE)
three = cv.imread('alphanumeric/3.bmp', cv.IMREAD_GRAYSCALE)
four = cv.imread('alphanumeric/4.bmp', cv.IMREAD_GRAYSCALE)
five = cv.imread('alphanumeric/5.bmp', cv.IMREAD_GRAYSCALE)
six = cv.imread('alphanumeric/6.bmp', cv.IMREAD_GRAYSCALE)
seven = cv.imread('alphanumeric/7.bmp', cv.IMREAD_GRAYSCALE)
eight = cv.imread('alphanumeric/8.bmp', cv.IMREAD_GRAYSCALE)
nine = cv.imread('alphanumeric/9.bmp', cv.IMREAD_GRAYSCALE)
zero = cv.imread('alphanumeric/0.bmp', cv.IMREAD_GRAYSCALE)

# Create Template Dictionary
TEMPLATES = {
    'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
    'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
    'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z,
    '1': one, '2': two, '3': three, '4': four, '5': five, '6': six,
    '7': seven, '8': eight, '9': nine, '0': zero
}

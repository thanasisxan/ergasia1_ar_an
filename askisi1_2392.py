import math
import matplotlib.pyplot as plt

e = math.e
sin = math.sin
cos = math.cos
AKRIBEIA = 5


# Η συνάρτηση e^sin^3(x) + x^6 - 2 x^4 - x^3 - 1
def f1(x):
    return e ** ((sin(x)) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1


# πρώτη παράγωγος: (6 x^3 - 8 x - 3) x^2 + 3 e^sin^3(x) sin^2(x) cos(x)
def f1_par1(x):
    return (6*x**3 - 8*x - 3) * x**2 + 3 * e**((sin(x))**3) * ((sin(x))**2) * cos(x)


# δεύτερη παράγωγος: 30 x^4 - 24 x^2 - 6 x - 3 e^sin^3(x) sin^3(x) + 6 e^sin^3(x) sin(x) cos^2(x)
# + 9 e^sin^3(x) sin^4(x) cos^2(x)
def f1_par2(x):
    return 30 * x**4 - 24 * x**2 - 6 * x - 3 * e ** ((sin(x))**4) * (sin(x)**3) + 6 * e ** (sin(x)**3) * sin(x) * (cos(x)**2) \
           + 9 * e ** (sin(x)**3) * (sin(x)**4) * (cos(x)**2)


# Η γραφική παράσταση της f1 στο δίαστημα [-2,2]
points = int(1e4)    # Σύνολο των σημέιων για την γραφική παράσταση
xmin, xmax = -2, 2
xlist = list(map(lambda x: float(xmax - xmin)*x/points, range(int(-points/2),int(points/2+1))))
ylist = list(map(lambda y: f1(y), xlist))
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(xlist, ylist)
plt.show()


# Η συνάρτηση επιστρέφει το αποτέλεσμα της μεθόδου διχοτόμησης με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα a: Το ένα από τα δύο άκρα
# τρίτο ορισμα b: Το δεύτερο απο τα δύο άκρα
# τέταρτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def bisection(f, a, b, n):
    tol = 10 ** (-n)
    i = 0
    m = (a + b) / 2
    while abs((b - a)/2.0) >= tol:
        i += 1
        m = (a + b) / 2
        if f(m) == 0:
            break
        if (f(m) * f(a)) < 0:
            b = m
        else:
            a = m
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format((a+b)/2)
    return apotelesma, i


# Η συνάρτηση επιστρέφει το αποτέλεσμα της μεθόδου Newton-Raphson με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα f_par: Η παράγωγος της συνάρτησης f
# τρίτο ορισμα x0: Σημείο που επιλέγουμε (πρεπει να ικανοποιεί την συνθήκη f(x0)*f''(x0)>0
# τέταρτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def newtonraphson(f, f_par, x0, n):
    if not f1(x0) * f1_par2(x0) > 0:
        return 'σφάλμα', 'σφάλμα\nΤο σημείο που επιλέχθηκε δεν ικανοποιεί την συνθήκη f(x0)*f''(x0)>0'
    x = x0
    h = f(x) / f_par(x)
    tol = 10 ** (-n)
    i = 0
    while abs(h) >= tol:
        if f(x) == 0:
            break
        i += 1
        h = f(x) / f_par(x)
        x = x - h
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format(x)
    return apotelesma, i


# Η συνάρτηση επιστρέφει το αποτέλεσμα της μεθόδου τέμνουσας με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα x0: Το πρώτο από τα δύο σημεία
# τρίτο ορισμα x1: Το δεύτερο απο τα δύο σημεία
# τέταρτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def temnousa(f, x0, x1, n):
    tol = 10 ** (-n)
    i = 0
    while abs(f(x1) - f(x0)) >= tol:
        if f(x0) == 0:
            break
        i += 1
        x_temp = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x_temp
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format(x1)
    return apotelesma, i


(apotelesma1, epanalipseis1) = bisection(f1, -2, 1.5, AKRIBEIA)
(apotelesma2, epanalipseis2) = bisection(f1, 0, 2, AKRIBEIA)
(apotelesma3, epanalipseis3) = bisection(f1, -2, 2, AKRIBEIA)

(apotelesma4, epanalipseis4) = newtonraphson(f1, f1_par1, -2, AKRIBEIA)
(apotelesma5, epanalipseis5) = newtonraphson(f1, f1_par1, 2, AKRIBEIA)
(apotelesma6, epanalipseis6) = newtonraphson(f1, f1_par1, 0.5, AKRIBEIA)

(apotelesma7, epanalipseis7) = temnousa(f1, -2, 0, AKRIBEIA)
(apotelesma8, epanalipseis8) = temnousa(f1, -2, -1, AKRIBEIA)
(apotelesma9, epanalipseis9) = temnousa(f1, -2, 2, AKRIBEIA)

print('\n---Μέθοδος Διχοτόμησης---')
print('Προσσέγγιση ρίζας:', apotelesma1, '\tΕπαναλήψεις:', epanalipseis1)
print('Προσσέγγιση ρίζας:', apotelesma2, '\tΕπαναλήψεις:', epanalipseis2)
print('Προσσέγγιση ρίζας:', apotelesma3, '\tΕπαναλήψεις:', epanalipseis3)

print('\n---Μέθοδος Newton Raphson---')
print('Προσσέγγιση ρίζας:', apotelesma4, '\tΕπαναλήψεις:', epanalipseis4)
print('Προσσέγγιση ρίζας:', apotelesma5, '\tΕπαναλήψεις:', epanalipseis5)
print('Προσσέγγιση ρίζας:', apotelesma6, '\tΕπαναλήψεις:', epanalipseis6)

print('\n---Μέθοδος Τέμνουσας---')
print('Προσσέγγιση ρίζας:', apotelesma7, '\tΕπαναλήψεις:', epanalipseis7)
print('Προσσέγγιση ρίζας:', apotelesma8, '\tΕπαναλήψεις:', epanalipseis8)
print('Προσσέγγιση ρίζας:', apotelesma9, '\tΕπαναλήψεις:', epanalipseis9)

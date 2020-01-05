import math
import random
from datetime import datetime

e = math.e
cos = math.cos
sin = math.sin
AKRIBEIA = 5


random.seed(datetime.now())


def g1(x):
    return 54*x**6 + 45*x**5 - 102*x**4 - 69*x**3 + 35*x**2 + 16*x - 4


def g1_par1(x):
    return 324*x**5 + 225*x**4 - 408*x**3 - 207*x**2 + 70*x + 16


def g1_par2(x):
    return 2*(810*x**4 + 450*x**3 - 612*x**2 - 207*x + 35)


# Η συνάρτηση επιστρέφει το αποτέλεσμα της τροποποιημένης μεθόδου Newton-Raphson με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα f_par1: Η πρώτη παράγωγος της συνάρτησης f
# τρίτο όρισμα f_par2: Η δεύτερη παράγωγος της συνάρτησης f
# τέταρτο ορισμα x0: Σημείο που επιλέγουμε (πρεπει να ικανοποιεί την συνθήκη f(x0)*f''(x0)>0
# πέμπτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def newtonraphson_mod(f, f_par1, f_par2, x0, n):
    if not f(x0) * f_par2(x0) > 0:
        return 'σφάλμα', 'σφάλμα\nΤο σημείο που επιλέχθηκε (' + str(x0) + ') δεν ικανοποιεί την συνθήκη f(' + str(
            x0) + ') * f\'\'(' + str(x0) + ') > 0'
    x = x0
    h = 1 / ((f_par1(x)/f(x)) - 1/2*f_par2(x)/f_par1(x))
    tol = 10 ** (-n)
    i = 0
    while abs(h) >= tol:
        if f(x) == 0:
            break
        i += 1
        h = 1 / ((f_par1(x) / f(x)) - 1 / 2 * f_par2(x) / f_par1(x))
        x = x - h
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format(x)
    return apotelesma, i


# Η συνάρτηση επιστρέφει το αποτέλεσμα της τροποποιημένης μεθόδου διχοτόμησης με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα a: Το ένα από τα δύο άκρα
# τρίτο ορισμα b: Το δεύτερο απο τα δύο άκρα
# τέταρτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def bisection_mod(f, a, b, n):
    tol = 10 ** (-n)
    i = 0
    while abs((b - a)/2.0) >= tol:
        i += 1
        r = random.uniform(a, b)
        if f(r) == 0:
            break
        if (f(r) * f(a)) < 0:
            b = r
        else:
            a = r
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format((a+b)/2.0)
    return apotelesma, i


# Η συνάρτηση επιστρέφει το αποτέλεσμα της τροποποιημένης μεθόδου τέμνουσας με την ακριβεια που ορίζουμε
# πρωτο όρισμα f: Η συνάρτηση
# δεύτερο όρισμα x0: Το πρώτο από τα τρία σημεία
# τρίτο ορισμα x1: Το δεύτερο απο τα τρία σημεία
# τέταρτο όρισμα x2: Το τρίτο απο τα τρία σημεία
# πέμπτο όρισμα n: Η ακρίβεια δεκαδικού ψηφίου που θέλουμε
def temnousa_mod(f, x0, x1, x2, n):
    tol = 10 ** (-n)
    i = 0
    while abs(f(x1) - f(x0)) >= tol:
        if f(x0) == 0:
            break
        q = f(x0) / f(x1)
        r = f(x2) / f(x1)
        s = f(x2) / f(x0)
        i += 1
        x_temp = x2 - (r * (r - q) * (x2 - x1) + (1 - r) * s * (x2 - x0)) / ((q - 1) * (r - 1) * (s - 1))
        x0 = x1
        x1 = x2
        x2 = x_temp
    akrivia_psifiou = "{:." + str(n) + "f}"
    apotelesma = akrivia_psifiou.format(x1)
    return apotelesma, i


(apotelesma1_new, epanalipseis1_new) = newtonraphson_mod(g1, g1_par1, g1_par2, -2, AKRIBEIA)
(apotelesma2_new, epanalipseis2_new) = newtonraphson_mod(g1, g1_par1, g1_par2, -1, AKRIBEIA)
(apotelesma3_new, epanalipseis3_new) = newtonraphson_mod(g1, g1_par1, g1_par2, 3/4, AKRIBEIA)
(apotelesma4_new, epanalipseis4_new) = newtonraphson_mod(g1, g1_par1, g1_par2, 1.5, AKRIBEIA)
(apotelesma5_new, epanalipseis5_new) = newtonraphson_mod(g1, g1_par1, g1_par2, 3/20, AKRIBEIA)

(apotelesma1_dix, epanalipseis1_dix) = bisection_mod(g1, -2, -1, AKRIBEIA)
(apotelesma2_dix, epanalipseis2_dix) = bisection_mod(g1, -1, 0.5, AKRIBEIA)
(apotelesma3_dix, epanalipseis3_dix) = bisection_mod(g1, 1, 2, AKRIBEIA)
(apotelesma4_dix, epanalipseis4_dix) = bisection_mod(g1, 0.3, 1, AKRIBEIA)
(apotelesma5_dix, epanalipseis5_dix) = bisection_mod(g1, -0.69, -0.66, AKRIBEIA)

(apotelesma1_tem, epanalipseis1_tem) = temnousa_mod(g1, -2, 0, 2, AKRIBEIA)
(apotelesma2_tem, epanalipseis2_tem) = temnousa_mod(g1, 0, 1, 2, AKRIBEIA)
(apotelesma3_tem, epanalipseis3_tem) = temnousa_mod(g1, 1, 0, 1.5, AKRIBEIA)
(apotelesma4_tem, epanalipseis4_tem) = temnousa_mod(g1, 2, 1, 1.5, AKRIBEIA)
(apotelesma5_tem, epanalipseis5_tem) = temnousa_mod(g1, -1, -1.5, -1.4, AKRIBEIA)


print('\n---Τροποποιημένη Μέθοδος Newton Raphson---')
print('Προσσέγγιση ρίζας:', apotelesma1_new, '\tΕπαναλήψεις:', epanalipseis1_new)
print('Προσσέγγιση ρίζας:', apotelesma2_new, '\tΕπαναλήψεις:', epanalipseis2_new)
print('Προσσέγγιση ρίζας:', apotelesma3_new, '\tΕπαναλήψεις:', epanalipseis3_new)
print('Προσσέγγιση ρίζας:', apotelesma4_new, '\tΕπαναλήψεις:', epanalipseis4_new)
print('Προσσέγγιση ρίζας:', apotelesma5_new, '\tΕπαναλήψεις:', epanalipseis5_new)

print('\n---Τροποποιημένη Μέθοδος Διχοτόμησης---')
print('Προσσέγγιση ρίζας:', apotelesma1_dix, '\tΕπαναλήψεις:', epanalipseis1_dix)
print('Προσσέγγιση ρίζας:', apotelesma2_dix, '\tΕπαναλήψεις:', epanalipseis2_dix)
print('Προσσέγγιση ρίζας:', apotelesma3_dix, '\tΕπαναλήψεις:', epanalipseis3_dix)
print('Προσσέγγιση ρίζας:', apotelesma4_dix, '\tΕπαναλήψεις:', epanalipseis4_dix)
print('Προσσέγγιση ρίζας:', apotelesma5_dix, '\tΕπαναλήψεις:', epanalipseis5_dix)

print('\n---Τροποποιημένη Μέθοδος Τέμνουσας---')
print('Προσσέγγιση ρίζας:', apotelesma1_tem, '\tΕπαναλήψεις:', epanalipseis1_tem)
print('Προσσέγγιση ρίζας:', apotelesma2_tem, '\tΕπαναλήψεις:', epanalipseis2_tem)
print('Προσσέγγιση ρίζας:', apotelesma3_tem, '\tΕπαναλήψεις:', epanalipseis3_tem)
print('Προσσέγγιση ρίζας:', apotelesma4_tem, '\tΕπαναλήψεις:', epanalipseis4_tem)
print('Προσσέγγιση ρίζας:', apotelesma5_tem, '\tΕπαναλήψεις:', epanalipseis5_tem)

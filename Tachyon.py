#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Features of matter to optimize thermonuclear fusion \n
and understand the possibilities of time travel and rejuvenation""" 
# Program ver 5.2 part one
import pandas as pd
import numpy as np
from numpy import *
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.pyplot import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.optimize import curve_fit
from scipy.interpolate import PchipInterpolator
from scipy.signal import savgol_filter
from prettytable import PrettyTable
from collections import namedtuple
import csv
# Uncomment the line below if you plan to view 3D graphics from different angles.
# %matplotlib notebook
# Error elimination, since it does not affect the values obtained
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 

"""A table with the initial knowledge with which the calculation begins"""

Initial_conditions = [[1, 'Project implemented in Python', 'ver. 3.7.6 \n'],
                      [2, 'ID - Anaconda', 'ver. 2020 02 \n'],
                      [3, 'All data presented in the SI system', 'nist.gov/\n'],
                      [4, 'All constants are taken from the\n'
                       'data the US NIST.\n', 'nist.gov/ \n'],
                      [5, 'Particle structure -\n'                       
                       'published works of Nobel laureates.\n', 'published scientific works \n'],
                      [6, 'Protons, neutrons\n'
                       'have a core and two shells.\n', 'Robert Hofstadter \n'],
                      [7, 'Speed of light in a vacuum, c = 299792458\n', 'nist.gov/ \n'],
                      [8, 'Electrical constant, ε0 = 8.8541878128E−12\n', 'nist.gov/ \n'],
                      [9, 'Gravitational constant, G = 6.67430E-11\n', 'nist.gov/ \n'],
                      [10, 'Electric charge of an electron\n'
                       '-1.602176634e-19 \n', 'nist.gov/ \n'],
                      [11, 'π = 3.14159265358979', "Scientific American\n"],
                      [12, "Planck's constant, h = 6.62607015E−34", 'nist.gov/\n'],
                      [13, 'Electron diameter 10e−22,\n', 'Hans D. Dehmelt Experiments\n'],
                      [14, 'The proton consists of two quarks \n', 'Murray Gell-Mann\n'],
                      [15, 'The newneutron consists of two quarks \n', 'Murray Gell-Mann \n'],
                      [16, 'Quark radius − (0.47 · 10E−16 cm)E2\n'
                       '< RE2 < (0.43 · 10E−16 cm)E2 \n', 'arxiv.org/pdf/1604.01280.pdf \n'],
                      [17, 'Additional information\n', 'Data from available sources. \n'],
                     [18, "Quark condensate provides about 9\n"
                      "percent of the proton's mass\n", 'Physical Review Letters, 2018\n,'
                      ' website arXiv.org\n'],
                     [19, 'Electron diameter: 10e−22 \n', 'Nobel lecture, December, 8, 1989,\n'
                      ' Hans D. Dehmelt Experiments with \n'
                      'an isolated subatomic particle at rest\n'],
                     [20, 'proton mass: 1.67262192369E-27\n', 'nist.gov/\n'],
                     [21, 'neutron mass: 1.67492749804E-27\n', 'nist.gov/\n'],
                     [22, 'The magnitude of the charge\n'
                      'of the core, shells in the proton\n'
                     'respectively: 0.35; 0.5; 0.15\n', 'Robert Hofstadter the\n'
                      'Nobel laureate\n'], 
                     [23, 'The magnitude of the charge of the core,\n'
                      ' shells in the neutron\n'
                     'respectively: 0.35; - 0.5; 0.15\n', 'Robert Hofstadter the\n'],
                     [24, 'The proton radius: 0.84 fm\n', 'aps.org/publications/apsnews/201806/proton.cfm\n'],
                     [25, 'The neutron radius: 0.8e−15\n', 'Povh, B.; Rith, K.(2002).\n'],
                     [26, 'Rradius of the proton core: 0.23 ± 0.03 F\n', 'https://doi.org/10.1103/PhysRevD.18.2484\n'],
                     [27, 'Rradius of the neutron core:\n'
                      ' from 0.3 to 0.36 fm\n', 'arxiv.org/pdf/1810.00486.pdf\n'],
                     [28, 'The radius of the inner shell of the neutron\n'
                      'is approximately 0.6 fm.\n', 'actaphys.uj.edu.pl/fulltext?series=Reg&vol=30&page=119\n'],
                     [29, 'Proton, neutron consists of a nucleus and two\n'
                      'shells, or three quarks, ... \n', 'https://cerncourier.com/a/the-proton-laid-bare/ \n'
                     'https://www.nature.com/articles/s41586-019-0925-9'],
                     [30, 'This calculation starts with the fact that \n'
                      'a quark consists of a nucleus and two shells \n', 'This is a conditional division']] 
table1 = PrettyTable(['#', 'Description', 'Link to source/ comments'])
for rec in Initial_conditions:
    table1.add_row(rec)
    
"""Program class for obtaining data for analysis"""

class Algorithm():
# Assigning values to constants.
# Constants with more characters than constants according to US NIST data are index two.

    constantε0 = 8.8541878128e-12
    constantε02 = 8.85418781762039e-12
    
    constantc = 299792458
        
    constantg = 6.67430E-11
    constantg2 = 6.67448478E-11
    
    constanth = 6.62607015e-34     

# Data from different research groups may differ from each other.

    π = 3.14159265358979
    
# electron mass
    me = 9.1093837015e-31
    
# electron diameter
    de = 10e-22
    
# Electric charge of an electron
    qe = 1.602176634e-19
    qe2 = 1.602176620898e-19
    
# proton mass  
    mp = 1.67262192369E-27
# radius of a proton estimated by electric charge
    rp = 0.84e-15
# Rradius of the proton core
    rpc = 0.23e-15
# The radius of the inner layer (assumption).
    rpi = 0.6e-15 
# neutron mass
    mn = 1.67492749804E-27
# radius of a neutron
    rn = 0.8e-15
# Radius of the neutron core, 
# following from the hadronic and nuclear matter properties
    rnc = 0.33e-15
# The radius of the inner layer.
    rni = 0.6e-15
    
# quark radius
# The third sign "n" - for negative radius
# The third sign "p" - for positive radius
    qrn = - 0.47 * 10e-18
    qrp = 0.43 * 10e-18
    
# The magnitude of the charge of the core, shells respectively

# proton
    SHELLP0 = 0.35
    SHELLP1 = 0.5
    SHELLP2 = 0.15
    
# neutron
    SHELLN0 = 0.35
    SHELLN1 = -0.5
    SHELLN2 = 0.15
    
    def __init__ (self, xq02, xq13, xv02, xv13, xm02, xm13):
        
        
# The first symbol is the name of the quark, the second symbol is:
# 0 - core, 1 - inner shell, 2 - outer shell.

# RULE 1:
# The calculation takes into account that the quarks of the nucleus
# can not fall on a single line, as it will mean the synthesis of quarks
# and the loss of their identity.

# RULE 2:
# Quarks are connected if there is their intersection is at least one shell.

# RULE 3:
# The combination of quarks is obliged to provide the densest arrangement.

        self.xq02 = xq02
        self.xq13 = xq13
                
        self.xv02 = xv02
        self.xv13 = xv13
                
        self.xm02 = xm02
        self.xm13 = xm13
                
# The combination of "u" and "d" quarks makes it possible to obtain several 
# variants of matrices for the proton, neutron.

# The matrixes for the proton.
a000 = ['u0', 0,   0,   0,  0]
a001 = [ 0,  'u1', 0,   0,  0]
a002 = [ 0,   0,  'u2', 0,  0]

a003 = [0, 'u0',  0,   0,   0]
a004 = [0,  0,   'u1', 0,   0]
a005 = [0,  0,    0,  'u2', 0]

a006 = [0,  0, 'd0', 0,    0]
a007 = [0,  0,  0,  'd1',  0]
a008 = [0,  0,  0,   0,   'd2']

#a0 = list(zip(a000, a001, a002, a003, a004, a005, a006, a007, a008))

"""The result is a matrix.
a0 = [('u0', 0,   0,   0,   0,   0,   0,   0,   0), 
      (0,   'u1', 0,  'u0', 0,   0,   0,   0,   0), 
      (0,    0,  'u2', 0,  'u1', 0,  'd0', 0,   0),
      (0,    0,   0,   0,   0,  'u2', 0,  'd1', 0), 
      (0,    0,   0,   0,   0,   0,   0,   0,  'd2')]"""

      
# The matrixes for the neutron.
a020 = ['d0', 0,   0,   0,   0]
a021 = [ 0,  'd1', 0,   0,   0]
a022 = [ 0,   0,  'd2', 0,   0]

a023 = [0, 'd0',  0,   0,   0]
a024 = [0,  0,   'd1', 0,   0]
a025 = [0,  0,    0,  'd2', 0]

a026 = [0,  0, 'u0', 0,   0]
a027 = [0,  0,  0,  'u1', 0]
a028 = [0,  0,  0,   0,  'u2']

#a2 = list(zip(a020, a021, a022, a023, a024, a025, a026, a027, a028))

"""The result is a matrix.
a2 = [['d0',  0,  0,   0,   0,   0,   0,   0,   0], 
      [0,   'd1', 0,  'd0', 0,   0,   0,   0,   0], 
      [0,    0,  'd2', 0,  'd1', 0,  'u0', 0,   0],
      [0,    0,   0,   0,   0,  'd2', 0,  'u1', 0], 
      [0,    0,   0,   0,   0,   0,   0,   0,  'u2']]"""

# Since we know the values for the nuclei and shells of the proton, neutron, 
# for the calculation we use the matrices a0 with a2.

"""It looks visually.
[['u0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' 'u1' '0' 'u0' '0' '0' '0' '0' '0']
 ['0' '0' 'u2' '0' 'u1' '0' 'd0' '0' '0']
 ['0' '0' '0' '0' '0' 'u2' '0' 'd1' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' 'd2']]
[['d0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' 'd1' '0' 'd0' '0' '0' '0' '0' '0']
 ['0' '0' 'd2' '0' 'd1' '0' 'u0' '0' '0']
 ['0' '0' '0' '0' '0' 'd2' '0' 'u1' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' 'u2']]"""

# All lines with 0 in the second character form a core.
# The remaining two lines form the inner and outer shell.

# Matrices are converted into an array, taking into account the available
# data for the calculation. 
# The array represents the equations for the proton and neutron.
      
# The top three lines of the array are proton (coefficients for the array)
# (u0+u0 = 2; u1+u1 = 2; u2 = 1; d0 = 1) - core for a0; (d1 = 1; u2 = 1) - 
# inner shell for a0; d2 = 1 - outer shell for a0

# The bottom three lines of the array are a neutron (coefficients for the array)
# (d0+d0 = 2; d1+d1 = 2; d2 = 1; u0 = 1) - core for a2; (d2 = 1; u1 = 1) - 
# inner shell for a2; u2 = 1 - outer shell for a2

x00 = (a000.count('u0') + a001.count('u0') + a002.count('u0') +
       a003.count('u0') + a004.count('u0') + a006.count('u0')) 

x01 = (a000.count('u1') + a001.count('u1') + a002.count('u1') +
       a003.count('u1') + a004.count('u1') + a006.count('u1'))

x02 = (a000.count('u2') + a001.count('u2') + a002.count('u2') +
       a003.count('u2') + a004.count('u2') + a006.count('u2'))

x03 = (a000.count('d0') + a001.count('d0') + a002.count('d0') +
       a003.count('d0') + a004.count('d0') + a006.count('d0'))

x04 = (a000.count('d1') + a001.count('d1') + a002.count('d1') +
       a003.count('d1') + a004.count('d1') + a006.count('d1'))

x05 = (a000.count('d2') + a001.count('d2') + a002.count('d2') +
       a003.count('d2') + a004.count('d2') + a006.count('d2'))

an20 = [0]
an20.insert(0, x00)
an20.insert(1, x01)
an20.insert(2, x02)
an20.insert(3, x03)
an20.insert(4, x04)
an20.insert(5, x05)
an20.pop(6)

x10 = (a005.count('u0') + a007.count('u0')) 
x11 = (a005.count('u1') + a007.count('u1'))
x12 = (a005.count('u2') + a007.count('u2'))
x13 = (a005.count('d0') + a007.count('d0'))
x14 = (a005.count('d1') + a007.count('d1'))
x15 = (a005.count('d2') + a007.count('d2'))

an21 = [0]
an21.insert(0, x10)
an21.insert(1, x11)
an21.insert(2, x12)
an21.insert(3, x13)
an21.insert(4, x14)
an21.insert(5, x15)
an21.pop(6)

x20 = a008.count('u0') 
x21 = a008.count('u1')
x22 = a008.count('u2')
x23 = a008.count('d0')
x24 = a008.count('d1')
x25 = a008.count('d2')

an22 = [0]
an22.insert(0, x20)
an22.insert(1, x21)
an22.insert(2, x22)
an22.insert(3, x23)
an22.insert(4, x24)
an22.insert(5, x25)
an22.pop(6)

x30 = (a020.count('u0') + a021.count('u0') + a022.count('u0') +
       a023.count('u0') + a024.count('u0') + a026.count('u0')) 

x31 = (a020.count('u1') + a021.count('u1') + a022.count('u1') +
       a023.count('u1') + a024.count('u1') + a026.count('u1'))

x32 = (a020.count('u2') + a021.count('u2') + a022.count('u2') +
       a023.count('u2') + a024.count('u2') + a026.count('u2'))

x33 = (a020.count('d0') + a021.count('d0') + a022.count('d0') +
       a023.count('d0') + a024.count('d0') + a026.count('d0'))

x34 = (a020.count('d1') + a021.count('d1') + a022.count('d1') +
       a023.count('d1') + a024.count('d1') + a026.count('d1'))

x35 = (a020.count('d2') + a021.count('d2') + a022.count('d2') +
       a023.count('d2') + a024.count('d2') + a026.count('d2'))

a120 = [0]
a120.insert(0, x30)
a120.insert(1, x31)
a120.insert(2, x32)
a120.insert(3, x33)
a120.insert(4, x34)
a120.insert(5, x35)
a120.pop(6)

x40 = (a025.count('u0') + a027.count('u0')) 
x41 = (a025.count('u1') + a027.count('u1'))
x42 = (a025.count('u2') + a027.count('u2'))
x43 = (a025.count('d0') + a027.count('d0'))
x44 = (a025.count('d1') + a027.count('d1'))
x45 = (a025.count('d2') + a027.count('d2'))

a121 = [0]
a121.insert(0, x40)
a121.insert(1, x41)
a121.insert(2, x42)
a121.insert(3, x43)
a121.insert(4, x44)
a121.insert(5, x45)
a121.pop(6)

x50 = a028.count('u0') 
x51 = a028.count('u1')
x52 = a028.count('u2')
x53 = a028.count('d0')
x54 = a028.count('d1')
x55 = a028.count('d2')

a122 = [0]
a122.insert(0, x50)
a122.insert(1, x51)
a122.insert(2, x52)
a122.insert(3, x53)
a122.insert(4, x54)
a122.insert(5, x55)
a122.pop(6)

a02 = [an20, an21, an22, a120, a121, a122]
a02 = array(a02)

"""It looks visually.
a02 = array([[2.0 , 2.0, 1.0, 1.0, 0.0, 0.0],
             [0.0, 0.0, 1.0, 0.0, 1.0, 0.0], 
             [0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 
             [1.0, 0.0, 0.0, 2.0, 2.0, 1.0], 
             [0.0, 1.0, 0.0, 0.0, 0.0, 1.0], 
             [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]])"""

a010 = ['u0', 0,   0,   0,   0]
a011 = [ 0,  'u1', 0,   0,   0]
a012 = [ 0,   0,  'u2', 0,   0]

a013 = [0, 'd0',  0,   0,   0]
a014 = [0,  0,   'd1', 0,   0]
a015 = [0,  0,    0,  'd2', 0]

a016 = [0,  0, 'u0', 0,   0]
a017 = [0,  0,  0,  'u1', 0]
a018 = [0,  0,  0,   0,  'u2']

#a1 = list(zip(a010, a011, a012, a013, a014, a015, a016, a017, a018))

"""The result is a matrix.
a1 = [('u0',  0,  0,   0,   0,   0,   0,   0,   0), 
      (0,   'u1', 0,  'd0', 0,   0,   0,   0,   0), 
      (0,    0,  'u2', 0,  'd1', 0,  'u0', 0,   0),
      (0,    0,   0,   0,   0,  'd2', 0,  'u1', 0), 
      (0,    0,   0,   0,   0,   0,   0,   0,  'u2')]"""

a030 = ['d0', 0,   0,   0,   0]
a031 = [ 0,  'd1', 0,   0,   0]
a032 = [ 0,   0,  'd2', 0,   0]

a033 = [0, 'u0',  0,   0,   0]
a034 = [0,  0,   'u1', 0,   0]
a035 = [0,  0,    0,  'u2', 0]

a036 = [0,  0, 'd0', 0,   0]
a037 = [0,  0,  0,  'd1', 0]
a038 = [0,  0,  0,   0,  'd2']

#a3 = list(zip(a030, a031, a032, a033, a034, a035, a036, a037, a038))

"""The result is a matrix.
a3 = [('d0', 0,   0,   0,   0,   0,   0,   0,   0), 
      (0,   'd1', 0,  'u0', 0,   0,   0,   0,   0), 
      (0,    0,  'd2', 0,  'u1', 0,  'd0', 0,   0),
      (0,    0,   0,   0,   0,  'u2', 0,  'd1', 0), 
      (0,    0,   0,   0,   0,   0,   0,   0,  'd2')]"""

# Since we know the values for the nuclei and shells of the proton, neutron, 
# for the calculation we use the matrices a1 with a3.
"""It looks visually.
[['u0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' 'u1' '0' 'd0' '0' '0' '0' '0' '0']
 ['0' '0' 'u2' '0' 'd1' '0' 'u0' '0' '0']
 ['0' '0' '0' '0' '0' 'd2' '0' 'u1' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' 'u2']]
[['d0' '0' '0' '0' '0' '0' '0' '0' '0']
 ['0' 'd1' '0' 'd0' '0' '0' '0' '0' '0']
 ['0' '0' 'd2' '0' 'd1' '0' 'u0' '0' '0']
 ['0' '0' '0' '0' '0' 'd2' '0' 'u1' '0']
 ['0' '0' '0' '0' '0' '0' '0' '0' 'u2']]"""

# The top three lines of the array are a proton (coefficients for the array)
# (u0+u0 = 2; u1 = 1; u2 = 1; d0 = 1; d1 = 1) - core for a1; (d2 = 1; u1 = 1) - 
# inner shell for a1; u2 = 1 - outer shell for a1

# The bottom three lines of the array are neutron (coefficients for the array)
# (d0+d0 = 2; d1 = 1; d2 = 1; u0 = 1; u1 = 1) - core for a3; (u2 = 1; d1 = 1) - 
# inner shell for a3; d2 = 1 - outer shell for a3

x60 = (a010.count('u0') + a011.count('u0') + a012.count('u0') +
       a013.count('u0') + a014.count('u0') + a016.count('u0')) 

x61 = (a010.count('u1') + a011.count('u1') + a012.count('u1') +
       a013.count('u1') + a014.count('u1') + a016.count('u1'))

x62 = (a010.count('u2') + a011.count('u2') + a012.count('u2') +
       a013.count('u2') + a014.count('u2') + a016.count('u2'))

x63 = (a010.count('d0') + a011.count('d0') + a012.count('d0') +
       a013.count('d0') + a014.count('d0') + a016.count('d0'))

x64 = (a010.count('d1') + a011.count('d1') + a012.count('d1') +
       a013.count('d1') + a014.count('d1') + a016.count('d1'))

x65 = (a010.count('d2') + a011.count('d2') + a012.count('d2') +
       a013.count('d2') + a014.count('d2') + a016.count('d2'))

a123 = [0]
a123.insert(0, x60)
a123.insert(1, x61)
a123.insert(2, x62)
a123.insert(3, x63)
a123.insert(4, x64)
a123.insert(5, x65)
a123.pop(6)

x70 = (a015.count('u0') + a017.count('u0')) 
x71 = (a015.count('u1') + a017.count('u1'))
x72 = (a015.count('u2') + a017.count('u2'))
x73 = (a015.count('d0') + a017.count('d0'))
x74 = (a015.count('d1') + a017.count('d1'))
x75 = (a015.count('d2') + a017.count('d2'))

a124 = [0]
a124.insert(0, x70)
a124.insert(1, x71)
a124.insert(2, x72)
a124.insert(3, x73)
a124.insert(4, x74)
a124.insert(5, x75)
a124.pop(6)


x80 = a018.count('u0') 
x81 = a018.count('u1')
x82 = a018.count('u2')
x83 = a018.count('d0')
x84 = a018.count('d1')
x85 = a018.count('d2')

a125 = [0]
a125.insert(0, x80)
a125.insert(1, x81)
a125.insert(2, x82)
a125.insert(3, x83)
a125.insert(4, x84)
a125.insert(5, x85)
a125.pop(6)

x90 = (a030.count('u0') + a031.count('u0') + a032.count('u0') +
       a033.count('u0') + a034.count('u0') + a036.count('u0')) 

x91 = (a030.count('u1') + a031.count('u1') + a032.count('u1') +
       a033.count('u1') + a034.count('u1') + a036.count('u1'))

x92 = (a030.count('u2') + a031.count('u2') + a032.count('u2') +
       a033.count('u2') + a034.count('u2') + a036.count('u2'))

x93 = (a030.count('d0') + a031.count('d0') + a032.count('d0') +
       a033.count('d0') + a034.count('d0') + a036.count('d0'))

x94 = (a030.count('d1') + a031.count('d1') + a032.count('d1') +
       a033.count('d1') + a034.count('d1') + a036.count('d1'))

x95 = (a030.count('d2') + a031.count('d2') + a032.count('d2') +
       a033.count('d2') + a034.count('d2') + a036.count('d2'))

a126 = [0]
a126.insert(0, x90)
a126.insert(1, x91)
a126.insert(2, x92)
a126.insert(3, x93)
a126.insert(4, x94)
a126.insert(5, x95)
a126.pop(6)

x100 = (a035.count('u0') + a037.count('u0')) 
x101 = (a035.count('u1') + a037.count('u1'))
x102 = (a035.count('u2') + a037.count('u2'))
x103 = (a035.count('d0') + a037.count('d0'))
x104 = (a035.count('d1') + a037.count('d1'))
x105 = (a035.count('d2') + a037.count('d2'))

a127 = [0]
a127.insert(0, x100)
a127.insert(1, x101)
a127.insert(2, x102)
a127.insert(3, x103)
a127.insert(4, x104)
a127.insert(5, x105)
a127.pop(6)

x110 = a038.count('u0') 
x111 = a038.count('u1')
x112 = a038.count('u2')
x113 = a038.count('d0')
x114 = a038.count('d1')
x115 = a038.count('d2')

a128 = [0]
a128.insert(0, x110)
a128.insert(1, x111)
a128.insert(2, x112)
a128.insert(3, x113)
a128.insert(4, x114)
a128.insert(5, x115)
a128.pop(6)

a13 = [a123, a124, a125, a126, a127, a128]
a13 = array(a13)

"""It looks visually.
a13 = array( [[2.0, 1.0, 1.0, 1.0, 1.0, 0.0], 
              [0.0, 1.0, 0.0, 0.0, 0.0, 1.0], 
              [0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
              [1.0, 1.0, 0.0, 2.0, 1.0, 1.0], 
              [0.0, 0.0, 1.0, 0.0, 1.0, 0.0], 
              [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])"""

# This formula is used at the initial stage of calculations.
# The results obtained allow the interested person to obtain an 
#accurate volumetric model.
# V = 4/3πR**3
# In accordance with the existing representation
# v - volume; u - quark "u"; d - quark "d"; n - neutron; p - proton
# i - inner; o - outer
    
vu = 4/3 * Algorithm.π * (abs(Algorithm.qrn)**3 + Algorithm.qrp**3)/2
vd = vu
vn = 4/3 * Algorithm.π * Algorithm.rn**3
vp = 4/3 * Algorithm.π * Algorithm.rp**3
vrpc = 4/3 * Algorithm.π * Algorithm.rpc**3
vrnc = 4/3 * Algorithm.π * Algorithm.rnc**3
vrpi = 4/3 * Algorithm.π * Algorithm.rpi**3 - vrpc
vrpo = vp - vrpc - vrpi
vrni = 4/3 * Algorithm.π * Algorithm.rni**3 - vrnc
vrno = vn - vrnc - vrni
ve = 4/3 * Algorithm.π * (Algorithm.de/2)**3
mpc = Algorithm.mp * 0.91
mnc = Algorithm.mn * 0.91
mpi = Algorithm.mp * 0.09 * (vrpi/vrpo)
mni = Algorithm.mn * 0.09 * (vrni/vrno)
mpo = Algorithm.mp - mpc - mpi
mno = Algorithm.mn - mnc - mni
    
bq = array ([Algorithm.SHELLP0, Algorithm.SHELLP1, Algorithm.SHELLP2, 
             Algorithm.SHELLN0, Algorithm.SHELLN1, Algorithm.SHELLN2])
    
bv = array ([vrpc, vrpi, vrpo, vrnc, vrni, vrno])
    
bm = array ([mpc, mpi, mpo, mnc, mni, mno])

# Calculation of the charge in the electric charges of an electron for the
# core and shells of the "u" and "d" quarks.
# The numbers from [0] to [2] refer to the "u" quark.
# The numbers from [3] to [5] refer to the "d" quark.
xq02 = linalg.solve(a02, bq)
xq13 = linalg.solve(a13, bq)

# Calculation of volume for core and shells of the "u" and "d" quarks.
# The numbers from [0] to [2] refer to the "u" quark.
# The numbers from [3] to [5] refer to the "d" quark.
xv02 = linalg.solve(a02, bv)
xv13 = linalg.solve(a13, bv)

# Calculation of mass for core and shells of the "u" and "d" quarks.
# The numbers from [0] to [2] refer to the "u" quark.
# The numbers from [3] to [5] refer to the "d" quark.
xm02 = linalg.solve(a02, bm)
xm13 = linalg.solve(a13, bm)

# Calculation of the charge for the core and shells of the "u" and "d" 
#quarks.
# The numbers from [0] to [2] refer to the "u" quark.
# The numbers from [3] to [5] refer to the "d" quark.
for i, item in enumerate(xq02):
    xq02[i] *= Algorithm.qe
    
for i, item in enumerate(xq13):
    xq13[i] *= Algorithm.qe

unit = Algorithm(xq02, xq13, xv02, xv13, xm02, xm13)

"""Preparation of a data set for a protons, and neutrons"""
"""Calculating tachyon values"""

class Particles():
    def __init__ (self, proton0, proton1, neutron0, neutron1, tachyon_charge,
                 tachyon_mass, tachyon_volume):
        self.proton0 = proton0
        self.proton1 = proton1
        self.neutron0 = neutron0
        self.neutron1 = neutron1
        self.tachyon_charge = tachyon_charge
        self.tachyon_mass = tachyon_mass
        self.tachyon_volume = tachyon_volume        
        
# Matrices from a0 to a3 from the Algorithm class are used to form a data set
# for protons, and neutrons. 
# The x...02 values are used for the matrices a0 and a2.
# The x...13 values are used for the matrices a1 and a3.
Proton2 = namedtuple('Proton2', 'name1 charge name2 mass name3 volume')

proton0 = [[1, 'pq1', unit.xq02[0], 'pm1', unit.xm02[0], 'pv1', unit.xv02[0]],
           [2, 'pq2', unit.xq02[1], 'pm2', unit.xm02[1], 'pv2', unit.xv02[1]],
           [3, 'pq3', unit.xq02[0], 'pm3', unit.xm02[0], 'pv3', unit.xv02[0]],
           [4, 'pq4', unit.xq02[2], 'pm4', unit.xm02[2], 'pv4', unit.xv02[2]],
           [5, 'pq5', unit.xq02[1], 'pm5', unit.xm02[1], 'pv5', unit.xv02[1]],           
           [6, 'pq6', unit.xq02[3], 'pm6', unit.xm02[3], 'pv6', unit.xv02[3]],           
           [7, 'pq7', unit.xq02[2], 'pm7', unit.xm02[2], 'pv7', unit.xv02[2]],           
           [8, 'pq8', unit.xq02[4], 'pm8', unit.xm02[4], 'pv8', unit.xv02[4]],
           [9, 'pq9', unit.xq02[5], 'pm9', unit.xm02[5], 'pv9', unit.xv02[5]]] 

table3 = PrettyTable(['#', 'Charge sym.', 'Charge in Cl', 'Mass sym.',
                      'Mass in kg.', 'Volume sym.', 'Volume in cbm'])

for rec in proton0:
    table3.add_row(rec) 

Proton = namedtuple('Proton', 'name1 charge name2 mass name3 volume')
proton1 = [[1, 'pq1', unit.xq13[0], 'pm1', unit.xm13[0], 'pv1', unit.xv13[0]], 
           [2, 'pq2', unit.xq13[1], 'pm2', unit.xm13[1], 'pv2', unit.xv13[1]], 
           [3, 'pq3', unit.xq13[3], 'pm3', unit.xm13[3], 'pv3', unit.xv13[3]],
           [4, 'pq4', unit.xq13[2], 'pm4', unit.xm13[2], 'pv4', unit.xv13[2]],
           [5, 'pq5', unit.xq13[4], 'pm5', unit.xm13[4], 'pv5', unit.xv13[4]],           
           [6, 'pq6', unit.xq13[0], 'pm6', unit.xm13[0], 'pv6', unit.xv13[0]],
           [7, 'pq7', unit.xq13[5], 'pm7', unit.xm13[5], 'pv7', unit.xv13[5]],           
           [8, 'pq8', unit.xq13[1], 'pm8', unit.xm13[1], 'pv8', unit.xv13[1]],
           [9, 'pq9', unit.xq13[2], 'pm9', unit.xm13[2], 'pv9', unit.xv13[2]]] 

table4 = PrettyTable(['#', 'Charge sym.', 'Charge in Cl', 'Mass sym.',
                      'Mass in kg.', 'Volume sym.', 'Volume in cbm'])
for rec in proton1:
    table4.add_row(rec)

Neutron2 = namedtuple('Neutron2', 'name1 charge name2 mass name3 volume')
neutron0 = [[1, 'nq1', unit.xq02[3], 'nm1', unit.xm02[3], 'nv1', unit.xv02[3]], 
            [2, 'nq2', unit.xq02[4], 'nm2', unit.xm02[4], 'nv2', unit.xv02[4]],
            [3, 'nq3', unit.xq02[3], 'nm3', unit.xm02[3], 'nv3', unit.xv02[3]],
            [4, 'nq4', unit.xq02[5], 'nm4', unit.xm02[5], 'nv4', unit.xv02[5]],
            [5, 'nq5', unit.xq02[4], 'nm5', unit.xm02[4], 'nv5', unit.xv02[4]],            
            [6, 'nq6', unit.xq02[0], 'nm6', unit.xm02[0], 'nv6', unit.xv02[0]],
            [7, 'nq7', unit.xq02[4], 'nm7', unit.xm02[4], 'nv7', unit.xv02[4]],            
            [8, 'nq8', unit.xq02[1], 'nm8', unit.xm02[1], 'nv8', unit.xv02[1]],
            [9, 'nq9', unit.xq02[2], 'nm9', unit.xm02[2], 'nv9', unit.xv02[2]]]

table5 = PrettyTable(['#', 'Charge sym.', 'Charge in Cl', 'Mass sym.',
                      'Mass in kg.', 'Volume sym.', 'Volume in cbm'])
for rec in neutron0:
    table5.add_row(rec)

Neutron = namedtuple('Neutron', 'name1 charge name2 mass name3 volume')    
neutron1 = [[1, 'nq1', unit.xq13[3], 'nm1', unit.xm13[3], 'nv1', unit.xv13[3]], 
            [2, 'nq2', unit.xq13[4], 'nm2', unit.xm13[4], 'nv2', unit.xv13[4]], 
            [3, 'nq3', unit.xq13[0], 'nm3', unit.xm13[0], 'nv3', unit.xv13[0]],
            [4, 'nq4', unit.xq13[5], 'nm4', unit.xm13[5], 'nv4', unit.xv13[5]],
            [5, 'nq5', unit.xq13[1], 'nm5', unit.xm13[1], 'nv5', unit.xv13[1]],
            [6, 'nq6', unit.xq13[3], 'nm6', unit.xm13[3], 'nv6', unit.xv13[3]],            
            [7, 'nq7', unit.xq13[2], 'nm7', unit.xm13[2], 'nv7', unit.xv13[2]],
            [8, 'nq8', unit.xq13[4], 'nm8', unit.xm13[4], 'nv8', unit.xv13[4]],
            [9, 'nq9', unit.xq13[5], 'nm9', unit.xm13[5], 'nv9', unit.xv13[5]]]

table6 = PrettyTable(['#', 'Charge sym.', 'Charge in Cl', 'Mass sym.',
                      'Mass in kg.', 'Volume sym.', 'Volume in cbm'])
for rec in neutron1:
    table6.add_row(rec)

proton0 = list(zip(* proton0))
proton1 = list(zip(* proton1))
neutron0 = list(zip(* neutron0))
neutron1 = list(zip(* neutron1))

"""Algorithm for finding tachyon""" 

proton0_min_charge = min((proton0)[2], key=abs)
proton1_min_charge = min((proton1)[2], key=abs)
neutron0_min_charge = min((neutron0)[2], key=abs)
neutron1_min_charge = min((neutron1)[2], key=abs)

# Let's compare the minimum values of charges in protons, and neutrons, 
# and find the value of a tachyon

if (proton0_min_charge == neutron0_min_charge and  
    proton1_min_charge == neutron1_min_charge and 
    proton0_min_charge == proton1_min_charge):    

# ATTENTION! THE CYCLE DOES NOT CONTAIN A FORCED INTERRUPTION.
   
    a = proton0_min_charge
    b = unit.qe2
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

# Electric charge of the tachyon.
tachyon_charge = a
        
# Find the mass of a tachyon.
tachyon_mass = unit.me/(unit.qe2/tachyon_charge)
 
# Minimum_volume tachyon. 
tachyon_volume = ve/(unit.qe2/tachyon_charge)

# Let's define protons, and neutrons, through the definition
# of electric charge.

if (sum(neutron0[2]) > sum(neutron1[2]) and sum(proton0[2]) == sum(proton1[2])): 
    neutron = neutron1 
    new_neutron = neutron0 
    proton = proton1 
    new_proton = proton0
else:
    print('Algorithm requires verification.')     

unit1 = Particles(proton0, proton1, neutron0, neutron1, tachyon_charge,
                 tachyon_mass, tachyon_volume)

tachyon_electrical_charge = [[1, 'Electric charge \n', unit1.tachyon_charge],
                              [2, 'Mass \n', unit1.tachyon_mass],
                              [3, 'Volume', unit1.tachyon_volume]]
table7 = PrettyTable(['#', 'Description', 'Design data'])

for rec in tachyon_electrical_charge:
                              table7.add_row(rec)       
        
"""Analysis of the data obtained for protons, neutrons, tachyon."""

# Histograms for protons, neutrons
# The histogram of the volume of shells of protons, neutrons
np_par = [f"P{i}" for i in range(9)]
width = 0.2
x = np.arange(len(np_par))
fig, ax = plt.subplots(figsize=(14,5))
rects1 = ax.bar(x - width/4 -0.2, ([unit.xv02[0], unit.xv02[1], unit.xv02[0], unit.xv02[2], 
                                    unit.xv02[1], unit.xv02[3], unit.xv02[2], unit.xv02[4], 
                                    unit.xv02[5]]), width, label='proton2')
rects2 = ax.bar(x + width/4 -0.2, ([unit.xv13[0], unit.xv13[1], unit.xv13[3], unit.xv13[2], 
                                    unit.xv13[4], unit.xv13[0], unit.xv13[5], unit.xv13[1],
                                    unit.xv13[2]]), width, label='proton')
rects3 = ax.bar(x - width/4 +0.2, ([unit.xv02[3], unit.xv02[4], unit.xv02[3], unit.xv02[5], 
                                    unit.xv02[4], unit.xv02[0], unit.xv02[4], unit.xv02[1],
                                    unit.xv02[2]]), width, label='neutron2')
rects4 = ax.bar(x + width/4 +0.2, ([unit.xv13[3], unit.xv13[4], unit.xv13[0], unit.xv13[5], 
                                    unit.xv13[1], unit.xv13[3], unit.xv13[2], unit.xv13[4], 
                                    unit.xv13[5]]), width, label='neutron')
ax.set_title('The histogram of the volume of shells of protons, neutrons\n'
             'Graph#1', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(np_par, fontsize = 14)
ax.legend(fontsize = 14)

# The histogram of the distribution of electric charge over the shells\n' 
# for protons, neutrons.
np_par = [f"P{i}" for i in range(9)]
width = 0.2
x = np.arange(len(np_par))
fig, ax = plt.subplots(figsize=(14,5))
rects1 = ax.bar(x - width/4 -0.2, ([unit.xq02[0], unit.xq02[1], unit.xq02[0], unit.xq02[2], 
                                    unit.xq02[1], unit.xq02[3], unit.xq02[2], unit.xq02[4], 
                                    unit.xq02[5]]), width, label='proton2')
rects2 = ax.bar(x + width/4 -0.2, ([unit.xq13[0], unit.xq13[1], unit.xq13[3], unit.xq13[2], 
                                    unit.xq13[4], unit.xq13[0], unit.xq13[5], unit.xq13[1],
                                    unit.xq13[2]]), width, label='proton')
rects3 = ax.bar(x - width/4 +0.2, ([unit.xq02[3], unit.xq02[4], unit.xq02[3], unit.xq02[5], 
                                    unit.xq02[4], unit.xq02[0], unit.xq02[4], unit.xq02[1],
                                    unit.xq02[2]]), width, label='neutron2')
rects4 = ax.bar(x + width/4 +0.2, ([unit.xq13[3], unit.xq13[4], unit.xq13[0], unit.xq13[5], 
                                    unit.xq13[1], unit.xq13[3], unit.xq13[2], unit.xq13[4], 
                                    unit.xq13[5]]), width, label='neutron')
ax.set_title('The histogram of the distribution of electric charge over the shells\n' 
             'for protons, neutrons. Graph#2\n', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(np_par, fontsize = 14)
ax.legend(fontsize = 14)

# The histogram of the mass distribution over the shells\n'
# for protons, neutrons.
np_par = [f"P{i}" for i in range(9)]
width = 0.2
x = np.arange(len(np_par))
fig, ax = plt.subplots(figsize=(14,5))
rects1 = ax.bar(x - width/4 -0.2, ([unit.xm02[0], unit.xm02[1], unit.xm02[0], unit.xm02[2], 
                                    unit.xm02[1], unit.xm02[3], unit.xm02[2], unit.xm02[4], 
                                    unit.xm02[5]]), width, label='proton2')
rects2 = ax.bar(x + width/4 -0.2, ([unit.xm13[0], unit.xm13[1], unit.xm13[3], unit.xm13[2], 
                                    unit.xm13[4], unit.xm13[0], unit.xm13[5], unit.xm13[1],
                                    unit.xm13[2]]), width, label='proton')
rects3 = ax.bar(x - width/4 +0.2, ([unit.xm02[3], unit.xm02[4], unit.xm02[3], unit.xm02[5], 
                                    unit.xm02[4], unit.xm02[0], unit.xm02[4], unit.xm02[1],
                                    unit.xm02[2]]), width, label='neutron2')
rects4 = ax.bar(x + width/4 +0.2, ([unit.xm13[3], unit.xm13[4], unit.xm13[0], unit.xm13[5], 
                                    unit.xm13[1], unit.xm13[3], unit.xm13[2], unit.xm13[4], 
                                    unit.xm13[5]]), width, label='neutron')
ax.set_title('The histogram of the mass distribution over the shells\n'
             'for protons, neutrons. Graph#3\n', fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(np_par, fontsize = 14)
ax.legend(fontsize = 14)

plt.show()

# We will build pie charts based on the obtained data visualized using histograms.
# The values of the protons, neutrons are the positive and negative volume.

data_names = ['In the 3D space \n', 
              'In the invariant space \n']
data_names2 = ['In the 3D space, Electric charge is positive \n', 
               'In the invariant space, Electric charge is negative \n']
data_names3 = ['In the 3D space, Electric charge is positive \n', 
               'In the invariant space, Electric charge is positive \n']
dpi = 80

data_values = [(unit.xv02[0] + unit.xv02[0] + unit.xv02[2] + unit.xv02[2] + 
                unit.xv02[5]) * 10e45, 
               -(unit.xv02[1] + unit.xv02[1] + unit.xv02[3] + 
                 unit.xv02[4]) * 10e45]
data_values2 = [(unit.xq02[0] + unit.xq02[0] + unit.xq02[2] + unit.xq02[2] + 
                 unit.xq02[5]) * 10e19, 
                -(unit.xq02[1] + unit.xq02[1] + unit.xq02[3] + 
                  unit.xq02[4]) * 10e19]
data_values3 = [(unit.xm02[0] + unit.xm02[0] + unit.xm02[2] + unit.xm02[2] + 
                 unit.xm02[5]) * 10e28, 
                (unit.xm02[1] + unit.xm02[1] + unit.xm02[3] + 
                 unit.xm02[4]) * 10e28]
data_values4 = [(unit.xv13[3] + unit.xv13[2] + unit.xv13[5] + unit.xv13[2]) * 10e45, 
                -(unit.xv13[0] + unit.xv13[1] + unit.xv13[4] + unit.xv13[0] + 
                  unit.xv13[1]) * 10e45]
data_values5 = [(unit.xq13[3] + unit.xq13[2] + unit.xq13[5] + unit.xq13[2]) * 10e19, 
                (unit.xq13[0] + unit.xq13[1] + unit.xq13[4] + unit.xq13[0] + 
                 unit.xq13[1]) * 10e19]
data_values6 = [(unit.xm13[3] + unit.xm13[2] + unit.xm13[5] + unit.xm13[2]) * 10e28, 
                (unit.xm13[0] + unit.xm13[1] + unit.xm13[4] + unit.xm13[0] + 
                 unit.xm13[1]) * 10e28]
data_values7 = [(unit.xv02[5] + unit.xv02[0] + unit.xv02[2]) * 10e45, 
                -(unit.xv02[3] + unit.xv02[4] + unit.xv02[3] + unit.xv02[4] + 
                  unit.xv02[4] + unit.xv02[1]) * 10e45]
data_values8 = [(unit.xq02[5] + unit.xq02[0] + unit.xq02[2]) * 10e19, 
                -(unit.xq02[3] + unit.xq02[4] + unit.xq02[3] + unit.xq02[4] + 
                 unit.xq02[4] + unit.xq02[1]) * 10e19]
data_values9 = [(unit.xm02[5] + unit.xm02[0] + unit.xm02[2]) * 10e28, 
                (unit.xm02[3] + unit.xm02[4] + unit.xm02[3] + unit.xm02[4] + 
                 unit.xm02[4] + unit.xm02[1]) * 10e28]
data_values10 = [(unit.xv13[3] + unit.xv13[5] + unit.xv13[3] + unit.xv13[2] + 
                  unit.xv13[5]) * 10e45, 
                 -(unit.xv13[4] + unit.xv13[0] + unit.xv13[1] + unit.xv13[4]) * 10e45]
data_values11 = [(unit.xq13[3] + unit.xq13[5] + unit.xq13[3] + unit.xq13[2] + 
                  unit.xq13[5]) * 10e19, 
                 -(unit.xq13[4] + unit.xq13[0] + unit.xq13[1] + unit.xq13[4]) * 10e19]
data_values12 = [(unit.xm13[3] + unit.xm13[5] + unit.xm13[3] + unit.xm13[2] + 
                  unit.xm13[5]) * 10e28, 
                 (unit.xm13[4] + unit.xm13[0] + unit.xm13[1] + unit.xm13[4]) * 10e28]

fig = plt.figure(1, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton for volume \n Graph#4")

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names)


fig = plt.figure(2, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton for electric charge \n Graph#5")

xs = range(len(data_names))

plt.pie(data_values2, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names2) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names2)

fig = plt.figure(3, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton for mass \n Graph#6")

xs = range(len(data_names))

plt.pie(data_values3, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

fig = plt.figure(4, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton 2 for volume \n Graph#7")

xs = range(len(data_names))

plt.pie(data_values4, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.25, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

fig = plt.figure(5, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton 2 for electric charge \n Graph#8")

xs = range(len(data_names3))

plt.pie(data_values5, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names3) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names3)

fig = plt.figure(6, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for proton 2 for mass \n Graph#9")

xs = range(len(data_names))

plt.pie(data_values6, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

fig = plt.figure(7, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron for volume \n Graph#10")

xs = range(len(data_names))

plt.pie(data_values7, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.25, 0.25, 0.25),
           loc = 'lower left', labels = data_names)


fig = plt.figure(8, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron for electric charge \n Graph#11")

xs = range(len(data_names2))

plt.pie(data_values8, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names2) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names2)

fig = plt.figure(9, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron for mass \n Graph#12")

xs = range(len(data_names))

plt.pie(data_values9, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

fig = plt.figure(10, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron 2 for volume \n Graph#13")

xs = range(len(data_names))

plt.pie(data_values10, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.25, 0.25, 0.25),
           loc = 'lower left', labels = data_names)


fig = plt.figure(11, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron 2 for electric charge \n Graph#14")

xs = range(len(data_names2))

plt.pie(data_values11, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names2) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names2)

fig = plt.figure(12, dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title("Distribution to placement in spaces in (%) \n"
              "for neutron 2 for mass \n Graph#15")

xs = range(len(data_names))

plt.pie(data_values12, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.31, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton, neutron

# Time distribution of proton1 volume in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xv02[0] + unit.xv02[0] + unit.xv02[2] + unit.xv02[2] + 
                unit.xv02[5]) * 10e46,
               -(unit.xv02[1] + unit.xv02[1] + unit.xv02[3]) * 10e46, 
               -(unit.xv02[4]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton volume in (%)\n Graph#16')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton1 electric charge in (%)

data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xq02[0] + unit.xq02[0] + unit.xq02[2] + unit.xq02[2] + 
                unit.xq02[5]) * 10e46,
               -(unit.xq02[1] + unit.xq02[1] + unit.xq02[3]) * 10e46, 
               (unit.xq02[4]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/ dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton electric charge in (%)\n Graph#17')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton1 mass in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xm02[0] + unit.xm02[0] + unit.xm02[2] + unit.xm02[2] + 
                unit.xm02[5]) * 10e46,
               (unit.xm02[1] + unit.xm02[1] + unit.xm02[3]) * 10e46, 
               (unit.xm02[4]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton mass in (%)\n Graph#18')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton2 volume in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xv13[3] + unit.xv13[2] + unit.xv13[5] + unit.xv13[2]) * 10e46,
               -(unit.xv13[4]) * 10e46, 
               -(unit.xv13[0] + unit.xv13[1] + unit.xv13[0] + unit.xv13[1]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton2 volume in (%)\n Graph#19')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton2 electric charge in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xq13[3] + unit.xq13[2] + unit.xq13[5] + unit.xq13[2]) * 10e20,
               -(unit.xq13[4]) * 10e20, 
               (unit.xq13[0] + unit.xq13[1] + unit.xq13[0] + unit.xq13[1]) * 10e20]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton2 electric charge in (%)\n Graph#20')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of proton2 mass in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xm13[3] + unit.xm13[2] + unit.xm13[5] + unit.xm13[2]) * 10e29,
               (unit.xm13[4]) * 10e29, 
               (unit.xm13[0] + unit.xm13[1] + unit.xm13[0] + unit.xm13[1]) * 10e29]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of proton2 mass in (%)\n Graph#21')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron1 volume in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xv02[5] + unit.xv02[0] + unit.xv02[2]) * 10e46,
               -(unit.xv02[3] + unit.xv02[3] + unit.xv02[1]) * 10e46, 
               -(unit.xv02[4] + unit.xv02[4] + unit.xv02[4]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron volume in (%)\n Graph#22')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron1 electric charge in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xq02[5] + unit.xq02[0] + unit.xq02[2]) * 10e20,
               -(unit.xq02[3] + unit.xq02[3] + unit.xq02[1]) * 10e20, 
               (unit.xq02[4] + unit.xq02[4] + unit.xq02[4]) * 10e20]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron electric charge in (%)\n Graph#23')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.50, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron1 mass in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xm02[5] + unit.xm02[0] + unit.xm02[2]) * 10e29,
               (unit.xm02[3] + unit.xm02[3] + unit.xm02[1]) * 10e29, 
               (unit.xm02[4] + unit.xm02[4] + unit.xm02[4]) * 10e29]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron mass in (%)\n Graph#24')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)])
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron2 volume in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xv13[3] + unit.xv13[5] + unit.xv13[3] + unit.xv13[2] + 
                unit.xv13[5]) * 10e46,
               -(unit.xv13[4] + unit.xv13[4]) * 10e46, 
               -(unit.xv13[0] + unit.xv13[1]) * 10e46]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron2 volume in (%)\n Graph#25')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron2 electric charge in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xq13[3] + unit.xq13[5] + unit.xq13[3] + unit.xq13[2] + 
                unit.xq13[5]) * 10e20,
               -(unit.xq13[4] + unit.xq13[4]) * 10e20, 
               (unit.xq13[0] + unit.xq13[1]) * 10e20]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron2 electric charge in (%)\n Graph#26')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Time distribution of neutron2 mass in (%)
data_names = ['Present time \n', 
              'Past time: \n',
              'Future']
data_values = [(unit.xm13[3] + unit.xm13[5] + unit.xm13[3] + unit.xm13[2] + 
                unit.xm13[5]) * 10e29,
               (unit.xm13[4] + unit.xm13[4]) * 10e29, 
               (unit.xm13[0] + unit.xm13[1]) * 10e29]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512/dpi, 500/dpi))
mpl.rcParams.update({'font.size': 14})

plt.title('Time distribution of neutron2 mass in (%)\n Graph#27')

xs = range(len(data_names))

plt.pie(data_values, autopct='%.1f', radius = 1.1,
        explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(bbox_to_anchor = (-0.16, 0.28, 0.25, 0.25),
           loc = 'lower left', labels = data_names)

# Demo graph comparing charge and mass from tachyon to neutron
x = np.array([tachyon_mass, unit.me, unit.xm02[3] + unit.xm02[4] + 
              unit.xm02[3] + unit.xm02[5] + unit.xm02[4] + 
              unit.xm02[0] + unit.xm02[4] + unit.xm02[1] + 
              unit.xm02[2], unit.xm02[0] + unit.xm02[1] + 
              unit.xm02[0] + unit.xm02[2] + unit.xm02[1] + 
              unit.xm02[3] + unit.xm02[2] + unit.xm02[4] + 
              unit.xm02[5], unit.xm13[0] + unit.xm13[1] + 
              unit.xm13[3] + unit.xm13[2] + unit.xm13[4] + 
              unit.xm13[0] + unit.xm13[5] + unit.xm13[1] + 
              unit.xm13[2], unit.xm13[3] + unit.xm13[4] + 
              unit.xm13[0] + unit.xm13[5] + unit.xm13[1] + 
              unit.xm13[3] + unit.xm13[2] + unit.xm13[4] + 
              unit.xm13[5]])

znp = np.array([tachyon_charge, -unit.qe, unit.xq02[3] + 
                unit.xq02[4] + unit.xq02[3] + unit.xq02[5] + 
                unit.xq02[4] + unit.xq02[0] + unit.xq02[4] + 
                unit.xq02[1] + unit.xq02[2] , unit.xq02[0] + 
                unit.xq02[1] + unit.xq02[0] + unit.xq02[2] + 
                unit.xq02[1] + unit.xq02[3] + unit.xq02[2] + 
                unit.xq02[4] + unit.xq02[5], unit.xq13[0] + 
                unit.xq13[1] + unit.xq13[3] + unit.xq13[2] + 
                unit.xq13[4] + unit.xq13[0] + unit.xq13[5] +
                unit.xq13[1] + unit.xq13[2], unit.xq13[3] + 
                unit.xq13[4] + unit.xq13[0] + unit.xq13[5] + 
                unit.xq13[1] + unit.xq13[3] + unit.xq13[2] + 
                unit.xq13[4] + unit.xq13[5]])  

fig, axs = plt.subplots(1, 1, figsize=(14, 11))

axs.plot(x, znp, 'bs', label= 'Weight in kg and charge \n in coulombs, respectively')

plt.ylabel('The amount of charge \n \n in Cl х Е-19', fontsize=15)
plt.xlabel('The amount of mass', fontsize=15)

plt.text(0, 0.01e-18, "Tachyon")
plt.text(0.02e-27, 0, tachyon_mass)
plt.text(0.02e-27, -0.01e-18, tachyon_charge)

plt.text(0.05e-27, -unit.qe + 0.015e-18, "Electron")
plt.text(0.05e-27, -unit.qe + 0.005e-18, unit.me)
plt.text(0.05e-27, -unit.qe - 0.025e-19, -unit.qe)

plt.text(1.5e-27 - 0.05e-27, unit.qe + 0.05e-19, "Proton&Proton2")

plt.text(1.5e-27 - 0.5e-27, unit.qe, unit.xm02[0] + unit.xm02[1] + 
         unit.xm02[0] + unit.xm02[2] + unit.xm02[1] + 
         unit.xm02[3] + unit.xm02[2] + unit.xm02[4] + 
         unit.xm02[5])

plt.text(1.5e-27 - 0.5e-27, unit.qe - 0.1e-19, unit.xq02[0] + unit.xq02[1] + 
         unit.xq02[0] + unit.xq02[2] + unit.xq02[1] + 
         unit.xq02[3] + unit.xq02[2] + unit.xq02[4] + 
         unit.xq02[5])


plt.text(1.5e-27 - 0.2e-27, unit.qe - 0.2e-19, unit.xm13[0] + unit.xm13[1] + 
         unit.xm13[3] + unit.xm13[2] + unit.xm13[4] + 
         unit.xm13[0] + unit.xm13[5] + 
         unit.xm13[1] + unit.xm13[2])

plt.text(1.5e-27 - 0.2e-27, unit.qe - 0.3e-19, unit.xq13[0] + unit.xq13[1] + 
         unit.xq13[3] + unit.xq13[2] + unit.xq13[4] + 
         unit.xq13[0] + unit.xq13[5] +
         unit.xq13[1] + unit.xq13[2])

plt.text(1.55e-27, 0.4e-19, "Neutron2")

plt.text(1.15e-27, 0.25e-19, unit.xm02[3] + unit.xm02[4] + 
         unit.xm02[3] + unit.xm02[5] + unit.xm02[4] + 
         unit.xm02[0] + unit.xm02[4] + unit.xm02[1] + 
         unit.xm02[2])

plt.text(1.15e-27, 0.15e-19, unit.xq02[3] + unit.xq02[4] + 
         unit.xq02[3] + unit.xq02[5] + unit.xq02[4] + 
         unit.xq02[0] + unit.xq02[4] + 
         unit.xq02[1] + unit.xq02[2])

plt.text(1.5e-27, 0 -0.05e-19, "Neutron")
plt.text(1.3e-27, 0 -0.15e-19, unit.xm13[3] + unit.xm13[4] + 
              unit.xm13[0] + unit.xm13[5] + unit.xm13[1] + 
              unit.xm13[3] + unit.xm13[2] + unit.xm13[4] + 
              unit.xm13[5])

plt.text(1.3e-27, 0-0.25e-19, unit.xq13[3] + 
                unit.xq13[4] + unit.xq13[0] + unit.xq13[5] + 
                unit.xq13[1] + unit.xq13[3] + unit.xq13[2] + 
                unit.xq13[4] + unit.xq13[5])


yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=18)
grid()         
plt.title('Mass and charge from tachyon to neutron\n' 
          'Graph#28\n', fontsize=20)


# THE DISTRIBUTION ELECTRIC CHARGE FOR NEUTRON2
# FOR SEGMENT AT PRESENT`S TIME

x = np.array([0, 1, 2, 3, 4])

# neutronv2 free state
znp = np.array([unit.xq13[3], unit.xq13[5], unit.xq13[3], unit.xq13[2], unit.xq13[5]])  

xx = np.linspace(x.min(),x.max(), 1000)
fig, axs = plt.subplots(1, 1, figsize=(14, 11))

itp2 = PchipInterpolator(x,znp)
window_size, poly_order = 3, 1

znpznp_sg = savgol_filter(itp2(xx), window_size, poly_order)

axs.plot(x, znp, 'bs', label= 'The neutronv2')
axs.plot(xx, znpznp_sg, 'b', label= "Smoothed curve")

# or fit to a global function for neutron2 
def func(x, A, B, x0, sigma):
    return A+B*np.tanh((x-x0)/sigma)
    
fit, _ = curve_fit(func, x, znp)
znpznp_fit = func(xx, *fit)

axs.plot(xx, znpznp_fit, 'b--', 
         label=r"$f(xnn) = |A| + B \tanh\left(\frac{x-x_0}{\sigma}\right)$")

plt.ylabel('The amount of charge \n \n in Cl х Е-20', fontsize=15)
plt.xlabel('Shells & present time', fontsize=15)

yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=16)
grid()         
plt.title('THE DISTRIBUTION ELECTRIC CHARGE FOR NEUTRON2 \n' 
          'FOR SEGMENT AT PRESENT`S TIME\n Graph#29.\n', fontsize=17)

# Interrelation of electric charge, volume and mass,
# segment for the present time, 3D graf

fig = plt.figure(figsize=plt.figaspect(0.3))

ax = fig.add_subplot(1, 2, 1, projection='3d')

Xnn = ([unit.xq02[0], unit.xq02[0], unit.xq02[2], unit.xq02[2], unit.xq02[5]])
Ynn = ([unit.xm02[0], unit.xm02[0], unit.xm02[2], unit.xm02[2], unit.xm02[5]])
Znn = ([unit.xv02[0], unit.xv02[0], unit.xv02[2], unit.xv02[2], unit.xv02[5]])

ax.plot(Xnn,Ynn,Znn)

ax.set_xlabel('\n \n \n Electric charge \n ', fontsize = 15)
ax.set_zlabel('\n \n \n \n \n Volume \n ', fontsize = 15)
ax.set_ylabel('\n \n \n \n Mass\n ', fontsize = 15)

ax.text2D(0.2, 0.95,         
          "Proton1 segment & present time \n" 
          "Graph # 30", 
          transform=ax.transAxes, fontsize = 16)

# Interrelation of Q, M and V in neytron2, 3D graf

ax = fig.add_subplot(1, 2, 2, projection='3d')

Xnn = ([unit.xq13[3], unit.xq13[5], unit.xq13[3], unit.xq13[2], unit.xq13[5]])
Ynn = ([unit.xm13[3], unit.xm13[5], unit.xm13[3], unit.xm13[2], unit.xm13[5]])
Znn = ([unit.xv13[3], unit.xv13[5], unit.xv13[3], unit.xv13[2], unit.xv13[5]])

ax.plot(Xnn,Ynn,Znn)

ax.set_xlabel('\n \n \n Electric charge \n ', 
              fontsize = 15)
ax.set_zlabel('\n \n \n \n \n Mass \n ', fontsize = 15)
ax.set_ylabel('\n \n \n \n Volume\n ', fontsize = 15)

ax.text2D(0.2, 0.95, 
          
          "Neytron2 segment & present time \n"
          "Graph # 31", 
          transform=ax.transAxes, fontsize = 16)

print('\n Initial conditions. Table 1.\n')
print(table1)

# table2 Reserved for quarks

print('\nValues of electric charge, mass, volume by shells for the proton2.\n'
     'Table 3.')
print(table3)

print('\nValues of electric charge, mass, volume by shells for the proton.\n'
     'Table 4.')
print(table4)

print('\nValues of electric charge, mass, volume by shells for the neutron2.\n'
     'Table 5.')
print(table5)

print('\nValues of electric charge, mass, volume by shells for the neutron.\n'
     'Table 6.')
print(table6)

print('\n Mass, electric charge and volume of the tachyon.\n'
      'Table 7.')
print(table7)


# In[ ]:





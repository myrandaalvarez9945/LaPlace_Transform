Laplace Transfer Function Tool

A Python tool for symbolically deriving Laplace-domain equations and transfer functions directly from time-domain equations of motion.

Supports:

1-DOF (single mass–spring–damper) systems

2-DOF (two coupled masses) systems

Direct time-domain ODE input (e.g. m*diff(x(t),t,2) + B*diff(x(t),t) + k*x(t) - F(t) = 0)

Built with SymPy

Features

Enter system parameters (m, b, k) as symbols or numbers.

Auto-converts time-domain ODEs into Laplace-domain equations.

Solves for transfer functions 
𝑋(𝑠)/𝐹(𝑠)

Diagnostic checks:

Denominator matches determinant of system matrix

Degrees of numerator/denominator for sanity-checks

Getting Started
Requirements

Python 3.8+

SymPy

Install SymPy with:

pip install sympy

Usage

Clone this repo:

git clone https://github.com/yourusername/laplace-tf-tool.git
cd laplace-tf-tool


Run:

python laplace_tf.py

💡 Examples
1-DOF System

Input:

How many masses (DOF)? 1
m1 [Enter = symbolic]: m
b1 [Enter = symbolic]: B
k1 [Enter = symbolic]: k


Output:

Equation of motion (Laplace):
(m*s**2 + B*s + k)*X1 = F

Transfer Function G(s) = X1/F(s):
        1
-----------------
m*s**2 + B*s + k

2-DOF System

Input:

How many masses (DOF)? 2
m1: m1
m2: m2
k1: k1
k2: k2
b1: b1


Output:

Equations of motion (Laplace):
(m1*s**2 + b1*s + k1 + k2)*X1 - (b1*s + k2)*X2 = 0
-(b1*s + k2)*X1 + (m2*s**2 + b1*s + k2)*X2 = F

G1(s) = X1/F(s):
(b1*s + k2) / D(s)

G2(s) = X2/F(s):
(m1*s**2 + b1*s + k1 + k2) / D(s)


Where:

D(s) = (m1*s**2 + b1*s + k1 + k2)*(m2*s**2 + b1*s + k2) - (b1*s + k2)**2

Direct ODE Input

Input:

m*diff(x(t),t,2) + B*diff(x(t),t) + k*x(t) - F(t) = 0


Output:

Laplace-domain equation:
(m*s**2 + B*s + k)*X - F = 0

Transfer Function X(s)/F(s):
1 / (m*s**2 + B*s + k)

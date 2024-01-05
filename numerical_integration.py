# Numerical Integration
import math

def left_endpoint(a, b, n):
    ''' (int, int, int) -> (float)
        Calculates left endpoint Rienman sum for the interval indicated'''
    sum = 0
    delta_x = (b - a)/n
    x = a
    while x < b:
        sum = sum + (function(x)*delta_x)
        x  = x + delta_x
    return sum
              
def right_endpoint(a,b,n):
    ''' (int, int, int) -> (float)
        Calculates right endpoint Rienman sum for the interval indicated'''
    sum = 0
    delta_x = (b - a)/n
    x = a + delta_x
    while x <= b:
        sum = sum + (function(x)*delta_x)
        x = x + delta_x
    return sum

def trapezoid_rule(a,b,n):
    ''' (int, int, int) -> (float)
        Approximates the area under the function using the trapezoid rule
        2Tn = Ln + Rn'''
    sum = (left_endpoint(a,b,n) + right_endpoint(a,b,n))/2
    return sum

def midpoint_rule(a,b,n):
    ''' (int, int, int) -> (float)
        Approximates the area under the function using the midpoint rule'''
    sum = 0
    delta_x = (b - a)/n
    x = a + delta_x/2
    while x < b:
        sum = sum + (function(x)*delta_x)
        x = x + delta_x
    return sum

def derive(value):
    '''(float) -> (float)
       Calculates the derivate of the function at the x given from first principles, not always very accurate'''
    h = 0.000000000001
    top = function(value+h) - function(value)
    first_derivative = top / h
    
    return float(first_derivative)

def max_derivative(a, b):
    '''(int, int) -> (float)
       Finds the approximate maximum derivative in the interval [a,b]'''
    interval = 0.0001
    x = a
    max_value = 0
    while x <= b:
        temp = abs(derive(x))
        if temp > max_value:
            max_value = temp
        x = x + interval
    return max_value

def function(x):
    ''' (float) -> (float)
        Returns the y value of the function at x.
        The function can be edited by the user'''
    return 3*x**2-2*x

lower_bound = int(input("Enter the lower bound of the integral: "))
upper_bound = int(input("Enter the upper bound of the integral: "))
intervals = int(input("How many sub intervals will there be? "))

L = left_endpoint(lower_bound, upper_bound, intervals)
R = right_endpoint(lower_bound, upper_bound, intervals)
T = trapezoid_rule(lower_bound, upper_bound, intervals)
M = midpoint_rule(lower_bound, upper_bound, intervals)

L_error = (max_derivative(lower_bound, upper_bound)*(upper_bound-lower_bound)**2)/(2*intervals)
R_error = (max_derivative(lower_bound, upper_bound)*(upper_bound-lower_bound)**2)/(2*intervals)

print()
print("L" + str(intervals) + " = " + str(L) + " \n with an error bound of %0.4f" %L_error)
print()
print("R" + str(intervals) + " = " + str(R) + " \n with an error bound of %0.4f" %R_error)
print()
print("T" + str(intervals) + " = " + str(T))
print()
print("M" + str(intervals) + " = " + str(M))

# Now we expand on the partial derivative calculus to:

# Calculate the gradient of mean squared error on a batch of data
# Visualize gradient descent in action

import torch
import matplotlib.pyplot as plt


print("Defining xs")
xs = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print(xs)
print("")



print("Defining ys sample vector")
ys = torch.tensor([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37]) # E.g.: Patient's "forgetfulness score"
print(ys)
print("")

print("Defining method for calculating the slope")
def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b
  
m = torch.tensor([0.9]).requires_grad_()
b = torch.tensor([0.1]).requires_grad_()
print("")

#-----------------------------------------------------------------------
# Step 1: Forward pass

print("Resulting yhat is:")
yhats = regression(xs, m, b)
print(yhats)
print("")

#-----------------------------------------------------------------------
# Step 2: Compare y^ with true y to calculate cost C
#let's use mean squared error, which averages quadratic cost across multiple data points:
# C= 1/n n∑i=1 (yi^−yi)**2


def mse(my_yhat, my_y):
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)

print("C (cost) for the given inputs in relation to yhat")  
C = mse(yhats, ys)
print(C)
print("")

#-----------------------------------------------------------------------
# Step 3: Use autodiff to calculate gradient of C w.r.t. parameters
C.backward()

# --  Define the partial derivative of  C with respect to b  ( ∂C/∂m )
print("Gradient of m: ",m.grad)
print(m.grad)
print("")

# --  Define the partial derivative of  C with respect to b  ( ∂C/∂b )
print("Gradient of b: ",b.grad)
print(b.grad)
print("")

#After manually calculating the gradient descent of cost we
#arrive to the following formula ∂C/∂m= 2x(y^−y) and ∂C/∂b=2(y^−y)

#This is means is that if we want to do the autodiff manually
#we must apply this formla to the given context and we should get
#the same results

print("∂C/∂m= 2x(y^−y): ",2*x*(yhat.item()-y))

print("∂C/∂b=2(y^−y): ",2*(yhat.item()-y))
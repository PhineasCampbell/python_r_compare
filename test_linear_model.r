# An r script to test the the linear model
# Load the data
data<-read.csv('data.csv')
# Fit the model
lin_res<-lm(y~x_1 + x_2, data)
# Print the intercept
print("Intercept:")
print(lin_res$coefficients[1])
# Print the parameter on x_1
print("Parameter on x_1:")
print(lin_res$coefficients[2])
# Print the parameter on x_2
print("Parameter on x_2:")
print(lin_res$coefficients[3])




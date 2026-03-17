# This is a basic r script to test the estimate o the linear model
# It loads data from data.csv, loops though the data, fits the linear
# model stores the parameter estimates in a dataframe then saves the
# dataframe as a csv.
# Read the data
data<-read.csv('data.csv')
# Initialize the loop
i<-1
# Create a dataframe for the results
results <- data.frame(matrix(ncol = 3, nrow = 0))
# Loop through the data
while(i <= 30000) {
    y<-data.frame(data[i])
    x1<-data.frame(data[i+1])
    x2<-data.frame(data[i+2])
    temp<-data.frame(y, x1, x2) 
    colnames(temp)<-c("y", "x_1", "x_2")
    # Fit the linear model 
    lin_res<-lm(y~x_1 + x_2, temp)
    # Add the results to the dataframe
    results <- rbind(results, list(lin_res$coefficients[1], lin_res$coefficients[2], lin_res$coefficients[3]))
    i<-i + 3
}
colnames(results) <- c("intercept_hat", "b_1_hat", "b_2_hat")
# Save results to csv file
write.csv(results, "r_results.csv", row.names=FALSE)

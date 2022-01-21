

for (i in 1:5){
     print(1+i)
}


prueba <- 1:1000 


View(prueba)


for (i in prueba) {
        print(i)%"este numero"
}

nombre <- c("Richard","Douglas")
nombre

x <- c(rnorm(10), runif(10), rnorm(10, 1))
f <- gl(3, 10)
split(x, f)

getwd()

data <- read.csv("hw1_data.csv" , header = T)

print(data)


class(data)

nrow(data)

names(data)

data[c(1,2)]

tail(data)


mean(x=data$Ozone,na.rm =TRUE)

sub = subset(data, Month == 6, select = Temp)
apply(sub, 2, mean)

head(data)

library(datasets)
datasets::airquality
airquality
s <- split(airquality, airquality$Month)
lapply(s, function(x) colMeans(x[, c("Ozone", "Solar.R", "Wind")]))


sapply(s, function(x) colMeans(x[, c("Ozone", "Solar.R", "Wind")]))
sapply(s, function(x) colMeans(x[, c("Ozone", "Solar.R", "Wind")],
                               na.rm = TRUE))

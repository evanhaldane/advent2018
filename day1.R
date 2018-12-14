require(tidyverse)

frequencies = read_csv("~/Desktop/advent2018/input1.csv", "freq")
sum(frequencies$freq)

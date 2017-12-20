# Problem 8 Solution

This solution searches the number in windows of 13 digits at a time, keeping a
running product of all the digits. If at any point there is a zero, we know the
product will be 0, so shift the window 13 digits forward past the zero and begin
checking again. Otherwise, shift the window forward by 1 digit. Other string
searching algorithms may be more efficient, but the string is short enough that
the performance is relatively the same.

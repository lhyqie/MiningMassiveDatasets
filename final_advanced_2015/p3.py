# the number of items = 10^8
# the number of baskets = 10^8
# each basket with 10 items
# the number pairs = 10^8 * C(10, 2) = 4.5 * 10^9
# total memory 10^9 bytes

# total size of memory for holding the buckets = 10^9 Bytes - 4 * 10^8 Bytes = 6 * 10^8 bytes
# each bucket is 4 bytes, we could at most have 6 * 10^8 / 4 = 1.5* 10^8 buckets

# average count of buckets is =  (4.5 * 10^9)  / (1.5* 10^8) = 30 
# since only if the average count of a bucket is at most half the support value, PCY is effective
# the smallest support value is 2 * 30 = 60

# B

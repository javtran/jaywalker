
# 1 -> (-17, 44) 
# 2 -> (-21, 44)
# 3 -> (12, 13) 
# 4 -> (12, 16) 
# 5 -> (-49, 12)
# 6 -> (-49, 16) 
# 7 -> (-17, 30)



#   A
# 
# |   |
# |3 4|
# |   |
# |   L________________
# |      7    1          # B
# |    _______2________
# |   |
# |   |
# |5 6|
# 
#   C


# (-17, 44) -> (12, 16), (-49, 12)
# (12, 13)  -> (-49, 12), (-21, 44)
# (-49, 16) -> (-21, 44), (12, 16)


trajectory_follower_settings = {
    
    'trajectory1': [ ((-49, 16), 0),
                    ((-40, 12), 2),
                    ((-31, 12), 4),
                    ((-22, 12), 6),
                    ((-13, 12), 8),
                    ((-4, 12), 10),
                    ((5, 12),  12),
                    ((12, 16), 14)],
    
    
}
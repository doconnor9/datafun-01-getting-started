"""
Assessing length of gymnasts beam routines.

Determines the shortest, longest and average times.

Uses if statements to determine if the routines are within the allowed time limit.

"""

print()
print('Hello')
print()
print('Enter the length of your gymnasts beam routines for further review')
print()


# get length of gymnasts beam routines from user
gymnast1_time = input('Enter the number of seconds of the first gymnasts beam routine: ' )
print()
gymnast2_time = input('Enter the number of seconds of the second gymnasts beam routine: ' )
print()
gymnast3_time = input('Enter the number of seconds of the third gymnasts beam routine: ' )
print()

type(gymnast1_time)

# change gymnast variables to float
gymnast1_time = float(gymnast1_time)
gymnast2_time = float(gymnast2_time)
gymnast3_time = float(gymnast3_time)

# finding the shortest routine
shortest_beam_routine = min(gymnast1_time, gymnast2_time, gymnast3_time)

print()
print('The shortest routine was', shortest_beam_routine, 'seconds')
print()


# finding the longest routine
longest_beam_routine = max(gymnast1_time, gymnast2_time, gymnast3_time)

print('The longest routine was', longest_beam_routine, 'seconds')
print()

# finding the average length of routines
gymnast_average_beamtime = ((gymnast1_time + gymnast2_time + gymnast3_time) / 3)

gymnast_average_beamtime = round(gymnast_average_beamtime, 1)

print('The average beam routine was', gymnast_average_beamtime, 'seconds')
print()

# defining max allowed time (time in seconds)
max_time = ('90')

# change max allowed time to integer
max_time = int(max_time)

# maximum allowed time is 90 seconds or less

print()

# assess the first gymnast beam time
if gymnast1_time < max_time:
    print('The first gymnast beam routine was within the time limit')

if gymnast1_time == max_time:
    print('The first gymnast beam routine was within the time limit')

if gymnast1_time > max_time:
    print('The first gymnast beam routine was over the time limit')

print()

# assess the second gymnast beam time
if gymnast2_time < max_time:
    print('The second gymnast beam routine was within the time limit')

if gymnast2_time == max_time:
    print('The second gymnast beam routine was within the time limit')

if gymnast2_time > max_time:
    print('The second gymnast beam routine was over the time limit')

print()

# asses the third gymnast beam time
if gymnast3_time <= max_time:
    print('The third gymnast beam routine was within the time limie')

if gymnast3_time > max_time:
    print('The third gymnast beam routine was over the time limit')


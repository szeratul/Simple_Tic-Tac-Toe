user_input = int(input())

if user_input < 1:
    print('no army')
elif user_input <= 9:
    print('few')
elif user_input <= 49:
    print('pack')
elif user_input <= 499:
    print('horde')
elif user_input <= 999:
    print('swarm')
else:
    print('legion')

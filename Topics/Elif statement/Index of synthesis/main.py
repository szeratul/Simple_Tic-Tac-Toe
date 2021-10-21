user_input = float(input())

if user_input < 2:
    print('Analytic')
elif 2 <= user_input <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')

# coding: utf-8


def calculerSalaire(prof, exp):
    if prof == 'architecte' and exp == 4:
        return '4000€'
    elif prof == 'médecin' and exp == 8:
        return '7000€'
    elif prof == 'consultant' and exp == 5:
        return '5000€'
    else:
        return 'une somme'


print('Un {} ayant une expérience de {} doit gagner environ {}'.format('architecte', 4, calculerSalaire('architecte', 4)))
print('Un {} ayant une expérience de {} doit gagner environ {}'.format('architecte', 8, calculerSalaire('architecte', 8)))
print('Un {} ayant une expérience de {} doit gagner environ {}'.format('médecin', 8, calculerSalaire('médecin', 8)))
print('Un {} ayant une expérience de {} doit gagner environ {}'.format('consultant', 5, calculerSalaire('consultant', 5)))

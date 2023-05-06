# relação de dias da semana que cada médico atende
cardiologista = {'terca', 'quarta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quarta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}
# Calcula quais os dias possíveis para dois médicos


def disp_dois_especialistas(medico01, medico02):
    intxn = medico01 & medico02
    return intxn if len(intxn) > 0 else 'Não há datas disponíveis'


# Calcula quais os dias possíveis para três médicos


def disp_tres_especialistas(medico01, medico02, medico03):
    intxn = medico01 & medico02 & medico03
    return intxn if len(intxn) > 0 else 'Não há datas disponíveis'

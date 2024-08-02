import pandas as pd

df = pd.read_excel('ganhos.ods')

data = {
    ('Semana', ''): df['week'],
    ('Dia', ''): df['day'],
    ('Data', ''): df['date'],
    ('Ifood', 'Qtd'): df['ifood_qtd'],
    ('Ifood', 'Ganho'): df['ifood_ganho'],
    ('Rappi', 'Qtd'): df['rappi_qtd'],
    ('Rappi', 'Ganho'): df['rappi_ganho'],
    ('Mottu', 'Qtd'): df['mottu_qtd'],
    ('Mottu', 'Ganho'): df['mottu_ganho'],
    ('Gastos', 'Gasolina'): df['gasolina'],
    ('Gastos', 'Parcela Mottu'): df['parcela moto'],
    ('Total', 'Entregas'): df['entregas'],
    ('Total', 'Diária'): df['total dia'],
}

df = pd.DataFrame(data)

#sumary
cdesc = df['Total'].sum()['Diária'] - (df['Gastos'].sum()['Gasolina']+df['Gastos'].sum()['Parcela Mottu'])

#df.add('Com Desconto', fill_value=cdesc)

#for index, row in df.iterrows():
#   print('dbg: '+row[index])

print('dbg '+str(cdesc))
print(df)


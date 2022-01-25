per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите планируемую сумму для инвестиции:"))
dep_bank = 0
max_dep = 0
max_name_bank = ''
deposit = []
for bank in per_cent:
    dep_bank = money / 100 * per_cent.get(bank)
    if max_dep < dep_bank:
        max_dep = dep_bank
        max_name_bank = bank
    print(bank, per_cent.get(bank),'% ', dep_bank)
    deposit.append(dep_bank)
print('Инвестируя на год:', money, '\ndeposit =', deposit,
      '\nМаксимальная сумма, которую вы можете заработать --', max_dep,
      "в банке:", max_name_bank)



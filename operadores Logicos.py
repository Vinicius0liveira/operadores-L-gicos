# AND =  Para ser true tudo tem que ser True
# OR = Para ser True apenas um tem que ser True

print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)

Saldo = 1000
Saque = 250
Limite = 200
Conta_especial = True


exp = Saldo >= Saque and Saque <= Limite or Conta_especial and Saldo >= Saque
print (exp)

exp_2 = (Saldo >= Saque and Saque <= Limite) or (Conta_especial and Saldo >= Saque)
print (exp_2)

conta_normal_com_saldo_suficiente = Saldo >= Saque and Saque <= Limite
Conta_especial_com_saldo_suficiente = Conta_especial and Saldo >= Saque

exp_3 = Conta_especial_com_saldo_suficiente or Conta_especial_com_saldo_suficiente
print (exp_3)

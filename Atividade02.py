salario_base = float(input("digite o salario base funcionario: r$ "))
total_vendas = float(input("digite o valor de suas vendas: r$ "))





bonus = 0.0
if total_vendas >= 1000.00:
    bonus= 150.00
    print("\ndesempenho execelente! bonus de r$ 150.00 aplicado.")
elif total_vendas >=500.00:
    bonus = 75.00
    print("\sbom desempenho! bonus de r$75.00 aplicado.")
else:
    print("vendas inferiores a r$ 500: sem bonus.")
    salario_total = salario_base + bonus

    print(f"\salario base: r$  {salario_base:.2f}")
    print(f"valor do bonus: r$ {bonus:.2f}")
    print(f"valor total a receber: r$ {salario_total:.2f}")



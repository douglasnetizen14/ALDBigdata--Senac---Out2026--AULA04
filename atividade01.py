
valor_original =float(input("digite o valor da compra: r$ "))
if valor_original >250.00:
    valor_com_desconto = valor_original * (1 - 0.16)

    print(f"\ndesconto de 16% aplicado !")
    print(f"valor original: r$ {valor_original:.2f}")
    print(f"valor final com desconto: r$ {valor_com_desconto:.2f}")
else:
    print(f"\nnhehum desconto aplicavel.")
    print(f"valor total da compra: r${valor_original:.2f}")

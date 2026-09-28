import sys

def mdc(a, b):
    
    if b == 0:
        return a
    return mdc(b, a % b)

def soma_digitos(n):
   
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

   
    lines = [line.strip() for line in input_data if line.strip()]
    if not lines:
        return

    try:
        q = int(lines[0])
    except ValueError:
        return

    for i in range(1, q + 1):
        if i >= len(lines):
            break

        parts = lines[i].split()
        if not parts:
            continue

        op = parts[0]

        if op == 'M':
            
            if len(parts) != 3:
                print("ERRO: EntradaInvalida")
                continue
            try:
                a = int(parts[1])
                b = int(parts[2])
               
                if a < 1 or b < 1:
                    print("ERRO: EntradaInvalida")
                else:
                    res = mdc(a, b)
                    print(f"MDC = {res}")
            except ValueError:
                print("ERRO: EntradaInvalida")

        elif op == 'S':
            
            if len(parts) != 2:
                print("ERRO: EntradaInvalida")
                continue
            try:
                n = int(parts[1])
               
                if n < 0:
                    print("ERRO: EntradaInvalida")
                else:
                    res = soma_digitos(n)
                    print(f"SOMA = {res}")
            except ValueError:
                print("ERRO: EntradaInvalida")

        else:
            # Operação diferente de M ou S
            print("ERRO: OperacaoInvalida")

if __name__ == '__main__':
    main()
# FIAP - Thiago Sales - Graduação Inteligência Artificial - Farm Tech Solutions - 17/09/2025
# Importa o módulo 'csv' para trabalhar com arquivos CSV
import csv

# Listas para armazenar os dados. Cada lista representa um vetor.
culturas = []
areas = []
insumos_necessarios = []


def salvar_dados_csv():
    """Salva os dados das listas em um arquivo CSV."""
    if not culturas:
        print("Nenhum dado para salvar em arquivo.")
        return

    try:
        with open('dados_culturas.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            # Escreve o cabeçalho
            writer.writerow(['cultura', 'area', 'insumos_necessarios'])
            # Escreve os dados linha por linha
            for i in range(len(culturas)):
                writer.writerow([culturas[i], areas[i], insumos_necessarios[i]])
        print("\nDados salvos em 'dados_culturas.csv' com sucesso!")
    except IOError:
        print("\nErro ao salvar o arquivo. Verifique as permissões de escrita.")


# Variável de controle para o loop principal do programa.
continuar = True

while continuar:
    print("----- Menu da FarmTech Solutions -----")
    print("1. Entrada de dados")
    print("2. Saída de dados (Exibir todos)")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Salvar dados em CSV")
    print("6. Sair do programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n--- Entrada de Dados de Cultura ---")
        cultura = input("Digite o tipo de cultura (soja/milho): ").lower()

        if cultura == 'soja':
            comprimento = float(input("Digite o comprimento da área (metros): "))
            largura = float(input("Digite a largura da área (metros): "))
            area = comprimento * largura
            print(f"Área calculada para a soja: {area:.2f} m²")

        elif cultura == 'milho':
            base_maior = float(input("Digite a base maior do trapézio (metros): "))
            base_menor = float(input("Digite a base menor do trapézio (metros): "))
            altura = float(input("Digite a altura do trapézio (metros): "))
            area = ((base_maior + base_menor) * altura) / 2
            print(f"Área calculada para o milho: {area:.2f} m²")

        else:
            print("Cultura inválida. Por favor, escolha 'soja' ou 'milho'.")
            area = 0.0

        if area > 0:
            litros_por_metro = float(input("Digite a quantidade de insumo por metro quadrado (litros/m²): "))
            insumos = area * litros_por_metro

            culturas.append(cultura)
            areas.append(area)
            insumos_necessarios.append(insumos)

            print("\nDados adicionados com sucesso!")

    elif opcao == 2:
        print("\n--- Dados de Culturas Registrados ---")
        if not culturas:
            print("Nenhum dado de cultura encontrado.")
        else:
            for i in range(len(culturas)):
                print(f"ID: {i}")
                print(f"Cultura: {culturas[i].capitalize()}")
                print(f"Área: {areas[i]:.2f} m²")
                print(f"Insumos: {insumos_necessarios[i]:.2f} litros")
                print("-" * 30)

    elif opcao == 3:
        print("\n--- Atualizar Dados ---")
        if not culturas:
            print("Nenhum dado para atualizar.")
        else:
            id_atualizar = int(input("Digite o ID do registro que deseja atualizar: "))

            if id_atualizar >= 0 and id_atualizar < len(culturas):
                print(f"Atualizando registro para {culturas[id_atualizar].capitalize()}...")
                nova_area = float(input("Digite a nova área (m²): "))
                novos_insumos = float(input("Digite a nova quantidade de insumos (litros): "))

                areas[id_atualizar] = nova_area
                insumos_necessarios[id_atualizar] = novos_insumos
                print("Dados atualizados com sucesso!")
            else:
                print("ID inválido.")

    elif opcao == 4:
        print("\n--- Deletar Dados ---")
        if not culturas:
            print("Nenhum dado para deletar.")
        else:
            id_deletar = int(input("Digite o ID do registro que deseja deletar: "))

            if id_deletar >= 0 and id_deletar < len(culturas):
                culturas.pop(id_deletar)
                areas.pop(id_deletar)
                insumos_necessarios.pop(id_deletar)
                print("Registro deletado com sucesso!")
            else:
                print("ID inválido.")

    elif opcao == 5:
        salvar_dados_csv()

    elif opcao == 6:
        print("Saindo do programa. Até mais!")
        continuar = False

    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 6.")

    if continuar:
        input("\nPressione Enter para voltar ao menu...")
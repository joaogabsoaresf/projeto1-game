from Score import Score
from Operation import Operation

def main():
    difficulty = set_difficulty()
    start_game(0, difficulty)


def set_difficulty():
    try:
        difficulty = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: "))
        
    except ValueError:
        print("Tipo digitado não é válido, digite apenas um dos niveis informados.")
        set_difficulty()

    if difficulty > 4:
        print("Nivel digitado não é válido, digite apenas um dos niveis informados.")
        set_difficulty()

    return difficulty
    

def start_game(initial_score, difficulty):
    score = Score(initial_score)

    operation = Operation(difficulty)

    new_operation = operation.operation_manager()

    print(f"{new_operation} = ?")

    try_again = True

    while try_again:
        try:
            asw = round(float(input('Digite a sua resposta: ')), 2)
        except ValueError:
            print("Tipo digitado não é válido, digite apenas números.")
            pass
        if type(asw) == float: try_again = False

        else: try_again = True

    if asw == operation.result:
        print('BLIM BLIM BLIM!!! Resposta Correta!!')
        score.update_score()
        print(f'Sua pontuação atual é {score.current_score}')
    
    else:
        print(f'PEEEEEEH!!! Resposta Incorreta...\nA resposta correta é {operation.result}')
        print(f'Sua pontuação atual é {score.current_score}')

    try_again = True

    while try_again:
        next_round = input("Deseja continuar o jogo? [S/N]: ")
        if next_round.lower() == 's':
            try_again = False
        elif next_round.lower() == 'n':
            try_again = False
            print(f'Sua pontuação total foi de {score.return_score()}!')
            return
        else:
            print('Opção inválida, tente novamente')
            return
    
    return start_game(score.return_score(), difficulty)

    
main()
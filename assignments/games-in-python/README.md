
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Pratique strings, listas, seleção aleatória, loops e condicionais ao criar um jogo da Forca em que o jogador tenta descobrir uma palavra antes de esgotar as tentativas.

## 📝 Tasks

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição
Use a lista `words` do código inicial para escolher uma palavra secreta aleatoriamente e inicialize as variáveis que controlarão os palpites e as tentativas incorretas.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra de `words` usando o módulo `random`.
- Inicializar uma coleção vazia para armazenar as letras já tentadas.
- Definir o número de tentativas incorretas e o limite máximo permitido.

### 🛠️ Implementar as Rodadas e o Resultado

#### Descrição
Crie o loop principal do jogo. Em cada rodada, mostre as letras adivinhadas e peça ao jogador que informe uma letra, atualizando o estado do jogo até que ele vença ou fique sem tentativas.

#### Requisitos
O programa concluído deve:

- Mostrar a palavra oculta com `_` nas posições ainda não adivinhadas e revelar as letras corretas. Por exemplo, para `python`, um progresso possível é `p _ _ h _ n`.
- Comparar cada palpite com a palavra secreta e aumentar o contador de erros somente quando a letra não estiver na palavra.
- Encerrar o jogo quando todas as letras da palavra forem adivinhadas ou o limite de erros for atingido.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.
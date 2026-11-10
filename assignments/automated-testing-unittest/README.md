# 📘 Assignment: Testes Automatizados com unittest

## 🎯 Objective

Aprenda a escrever e executar testes automatizados para verificar funções em Python usando `unittest`, que faz parte da biblioteca padrão e não exige dependências externas.

## 📝 Tasks

### 🛠️ Testar Operações Básicas

#### Descrição
Execute o código inicial e complete os testes para as funções de soma e subtração. Use o teste de soma já implementado como exemplo e confirme que os testes detectam os resultados esperados.

#### Requisitos
O programa concluído deve:

- Executar o arquivo com `python starter-code.py`.
- Manter o teste de exemplo para `add(2, 3)` e confirmar que o resultado é `5`.
- Implementar um teste para `subtract(8, 3)` que confirme o resultado `5`.
- Substituir o marcador `self.fail()` do teste de subtração por uma asserção de `unittest`.

### 🛠️ Testar Diferentes Resultados

#### Descrição
Amplie a suíte com mais casos para as operações aritméticas. Use métodos de asserção apropriados para comparar resultados inteiros e decimais.

#### Requisitos
O programa concluído deve:

- Verificar a soma com números negativos e com zero.
- Verificar a divisão de `7` por `2` usando `assertAlmostEqual` para o resultado `3.5`.
- Organizar cada cenário em um método de teste cujo nome comece com `test_`.
- Executar a suíte e confirmar que todos os testes implementados passam.

### 🛠️ Verificar Casos de Erro

#### Descrição
Teste como a função `divide` se comporta quando recebe um divisor igual a zero. Use a asserção de exceção do `unittest` para garantir que o erro esperado seja tratado.

#### Requisitos
O programa concluído deve:

- Confirmar que `divide(7, 0)` levanta `ValueError` usando `assertRaises`.
- Substituir o marcador `self.fail()` do teste de divisão por zero por uma asserção.
- Executar novamente a suíte e confirmar que todos os testes passam.

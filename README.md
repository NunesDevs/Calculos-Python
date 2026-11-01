# Calculos-Python

Calculadora de console para áreas geométricas e circunferência com entrada de medidas e formatação decimal.

## Funcionalidades verificadas

- Triângulo, quadrado e trapézio.
- Círculo por raio ou diâmetro.
- Circunferência por raio ou diâmetro.
- Seleção de unidade cm ou m.

## Operação e arquitetura verificadas

program.py contém menu e cálculos; const.py armazena PI e caracteres usados pelo filtro de entrada.

Arquivos principais: `program.py`, `const.py`.

### Requisitos e execução

Python 3; biblioteca padrão.

```text
python program.py
python -m unittest discover -s tests -v
```



### Testes e estado

A suíte unittest cobre a execução no Windows e o cálculo de círculo por diâmetro.

Estado: projeto de estudo/experimental. Deploy ativo não foi confirmado nesta revisão.

### Limitações conhecidas

- As opções de retângulo e losango exibidas no menu ainda não calculam os valores.
- A validação de entradas numéricas e unidades precisa ser ampliada.

### Licença e manutenção

Nenhum arquivo de licença foi identificado nesta revisão; não foi adicionada uma nova licença. Atualize comandos e limitações quando houver mudança de comportamento.

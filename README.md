# Calculadora geométrica de console

Calcula áreas de triângulo, quadrado, trapézio, círculo, retângulo e losango, além de circunferência. Círculo e circunferência aceitam raio ou diâmetro. A versão atual completa retângulo/losango e mantém as sete opções originais do menu.

```sh
python program.py
python -m unittest discover -s tests -v
```

Requer Python 3 e somente biblioteca padrão. Escolha cm ou m; todas as medidas da operação devem usar essa unidade. Aceita ponto ou vírgula decimal e sufixo opcional igual à unidade escolhida (`2,5cm`). Valores vazios, negativos, zero, não finitos e textos malformados são rejeitados com nova tentativa. O menu permite sair com 0 e EOF/interrupção encerram sem traceback.

`geometry.py` separa fórmulas puras, validação de dimensões e limites numéricos do menu em `program.py`. `const.PI` permanece como compatibilidade, agora com o valor de `math.pi`. O parser não remove letras arbitrárias nem converte silenciosamente unidades diferentes. Áreas são exibidas em cm² ou m²; circunferência em cm ou m. Resultados usam ponto flutuante com apresentação de até 12 dígitos significativos, sem promessa de aritmética decimal exata.

Oito testes verificam todas as fórmulas, equivalência entre raio/diâmetro, entradas inválidas, unidades, limites numéricos, importação sem interação e execução real de todas as opções. A correção anterior do import de curses no Windows continua preservada.

Licença MIT em `LICENSE`. Não há serviço externo ou banco de dados. Distribuição em pacote de scripts Python com checksum. Memória técnica: `docs/ai-context/QUALITY_REFRESH.md`.

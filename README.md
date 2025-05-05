# Controle Clássico para o Pusher (Gymnasium)

Este projeto implementa um controlador clássico para o ambiente Pusher do Gymnasium (anteriormente OpenAI Gym).

## Estrutura do Projeto

```
.
├── requirements.txt    # Dependências do projeto
├── src/
│   ├── env.py         # Configuração do ambiente
│   ├── controller.py  # Funções de controle
│   ├── utils.py       # Funções auxiliares
│   └── main.py        # Script principal
└── README.md          # Este arquivo
```

## Instalação

1. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OU
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal:
```bash
python src/main.py
```

## Descrição dos Módulos

- `env.py`: Configuração e interação com o ambiente Pusher
- `controller.py`: Implementação das funções de controle clássico
- `utils.py`: Funções auxiliares para visualização e processamento
- `main.py`: Script principal que integra todos os módulos

## Ambiente Pusher

O ambiente Pusher consiste em um braço robótico que deve empurrar um objeto até uma posição alvo.

### Espaço de Ações
- 7 juntas controladas por torque
- Intervalo de ação: [-2.0, 2.0]

### Espaço de Observação
- 23 dimensões incluindo:
  - Posições das juntas (7)
  - Velocidades das juntas (7)
  - Posição do efetuador final (3)
  - Posição do objeto (3)
  - Posição do alvo (3) 
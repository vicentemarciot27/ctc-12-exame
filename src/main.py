import numpy as np
from env import criar_ambiente, reset_ambiente, executar_acao
from controller import calcular_acao_controle, extrair_estados
from utils import plotar_trajetoria, salvar_dados, calcular_metricas

def executar_episodio(env, max_steps=100, render=False):
    """
    Executa um episódio completo.
    
    Args:
        env: Ambiente Pusher
        max_steps: Número máximo de passos
        render: Flag para renderização
    
    Returns:
        historico: Dicionário com histórico do episódio
    """
    observation, _ = reset_ambiente(env)
    
    # Inicializar históricos
    historico = {
        'pos_efetuador': [],
        'pos_objeto': [],
        'pos_alvo': [],
        'recompensas': [],
        'erros': []
    }
    
    for _ in range(max_steps):
        # Extrair estados atuais
        estados = extrair_estados(observation)
        
        # Calcular e executar ação de controle
        acao = calcular_acao_controle(observation)
        observation, reward, terminated, truncated, info = executar_acao(env, acao)
        
        # Atualizar históricos
        historico['pos_efetuador'].append(estados['pos_efetuador'])
        historico['pos_objeto'].append(estados['pos_objeto'])
        historico['pos_alvo'].append(estados['pos_alvo'])
        historico['recompensas'].append(reward)
        historico['erros'].append(np.linalg.norm(estados['pos_objeto'] - estados['pos_alvo']))
        
        if render:
            env.render()
        
        if terminated or truncated:
            break
    
    return historico

def main():
    """
    Função principal do programa.
    """
    # Criar e configurar ambiente
    env = criar_ambiente(render_mode='human')
    
    try:
        # Executar episódio
        historico = executar_episodio(env, render=True)
        
        # Calcular métricas
        metricas = calcular_metricas(
            historico['recompensas'],
            historico['erros']
        )
        
        # Plotar resultados
        plotar_trajetoria(
            historico['pos_efetuador'],
            historico['pos_objeto'],
            historico['pos_alvo']
        )
        
        # Salvar dados
        salvar_dados('resultados_experimento.npy', {
            'historico': historico,
            'metricas': metricas
        })
        
        # Imprimir métricas
        print("\nMétricas do experimento:")
        for nome, valor in metricas.items():
            print(f"{nome}: {valor:.4f}")
            
    finally:
        env.close()

if __name__ == "__main__":
    main() 
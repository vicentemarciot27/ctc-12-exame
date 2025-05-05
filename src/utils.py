import numpy as np
import matplotlib.pyplot as plt

def plotar_trajetoria(historico_pos_efetuador, historico_pos_objeto, historico_pos_alvo):
    """
    Plota a trajetória do efetuador final, objeto e alvo.
    
    Args:
        historico_pos_efetuador: Lista de posições do efetuador final
        historico_pos_objeto: Lista de posições do objeto
        historico_pos_alvo: Lista de posições do alvo
    """
    historico_pos_efetuador = np.array(historico_pos_efetuador)
    historico_pos_objeto = np.array(historico_pos_objeto)
    historico_pos_alvo = np.array(historico_pos_alvo)
    
    plt.figure(figsize=(10, 6))
    
    # Plotar trajetórias
    plt.plot(historico_pos_efetuador[:, 0], historico_pos_efetuador[:, 1], 'b-', label='Efetuador')
    plt.plot(historico_pos_objeto[:, 0], historico_pos_objeto[:, 1], 'r-', label='Objeto')
    plt.plot(historico_pos_alvo[:, 0], historico_pos_alvo[:, 1], 'g*', label='Alvo')
    
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Trajetória do Sistema')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def salvar_dados(nome_arquivo, dados):
    """
    Salva dados do experimento em arquivo numpy.
    
    Args:
        nome_arquivo: Nome do arquivo para salvar
        dados: Dicionário com os dados a serem salvos
    """
    np.save(nome_arquivo, dados)

def carregar_dados(nome_arquivo):
    """
    Carrega dados de experimento salvos.
    
    Args:
        nome_arquivo: Nome do arquivo para carregar
    
    Returns:
        dados: Dicionário com os dados carregados
    """
    return np.load(nome_arquivo, allow_pickle=True).item()

def calcular_metricas(historico_recompensas, historico_erros):
    """
    Calcula métricas de desempenho do controlador.
    
    Args:
        historico_recompensas: Lista de recompensas
        historico_erros: Lista de erros
    
    Returns:
        dict: Dicionário com as métricas calculadas
    """
    return {
        'recompensa_media': np.mean(historico_recompensas),
        'recompensa_std': np.std(historico_recompensas),
        'erro_medio': np.mean(historico_erros),
        'erro_std': np.std(historico_erros)
    } 
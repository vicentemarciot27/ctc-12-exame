import gymnasium as gym

def criar_ambiente(render_mode=None, width=1024, height=768):
    """
    Cria e configura o ambiente Pusher.
    
    Args:
        render_mode (str, opcional): Modo de renderização ('human' ou None)
        width (int, opcional): Largura da janela de renderização em pixels
        height (int, opcional): Altura da janela de renderização em pixels
    
    Returns:
        env: Ambiente Pusher configurado
    """
    return gym.make('Pusher-v5', 
                   render_mode=render_mode,
                   width=width,
                   height=height)

def reset_ambiente(env):
    """
    Reinicia o ambiente e retorna o estado inicial.
    
    Args:
        env: Ambiente Pusher
    
    Returns:
        observation: Estado inicial
        info: Informações adicionais
    """
    observation, info = env.reset()
    return observation, info

def executar_acao(env, acao):
    """
    Executa uma ação no ambiente e retorna o resultado.
    
    Args:
        env: Ambiente Pusher
        acao: Array com 7 valores de torque para as juntas
    
    Returns:
        observation: Novo estado
        reward: Recompensa
        terminated: Flag de término
        truncated: Flag de truncamento
        info: Informações adicionais
    """
    return env.step(acao) 
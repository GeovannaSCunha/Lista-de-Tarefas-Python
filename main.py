import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

SUPPORTS_256 = "256color" in os.environ.get("TERM", "")

def fg256(code: int) -> str:
    return f"\033[38;5;{code}m" if SUPPORTS_256 else ""

def pastel(text: str, code: int, fallback=Fore.MAGENTA) -> str:
    return f"{fg256(code)}{text}{Style.RESET_ALL}" if SUPPORTS_256 else f"{fallback}{text}{Style.RESET_ALL}"

PINK      = 218  
ROSE      = 217  
BLUSH     = 224  
LILAC     = 183  
SOFTGRAY  = 245  

def soft(text: str) -> str:
    return pastel(text, SOFTGRAY, Fore.WHITE)

def title(text: str) -> str:
    return Style.BRIGHT + pastel(text, PINK)

def accent(text: str) -> str:
    return pastel(text, ROSE)

def badge(text: str) -> str:
    return Style.BRIGHT + pastel(text, LILAC)

# --- App ---
tarefas = []            
tarefas_concluidas = [] 

FMT = "%d/%m/%Y %H:%M"

def agora():
    return datetime.now().strftime(FMT)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def listar():
    if not tarefas:
        print(soft("Nenhuma tarefa pendente."))
    else:
        print(badge("Pendentes:"))
        for i, t in enumerate(tarefas, 1):
            linha = f"{i}. ✿ {t['texto']} " + soft(f"(criada em {t['criada_em']})")
            print(linha)

    if tarefas_concluidas:
        print()
        print(badge("Concluídas:"))
        for i, t in enumerate(tarefas_concluidas, 1):
            linha = f"  - ✅ {pastel(t['texto'], BLUSH)} " + soft(f"(criada em {t['criada_em']}, concluída em {t['concluida_em']})")
            print(linha)

def add():
    texto = input(accent("Digite a nova tarefa: ")).strip()
    if texto:
        tarefas.append({"texto": texto, "criada_em": agora()})
        print(pastel("Adicionada! ₊˚⊹♡", PINK))
    else:
        print(soft("Nada foi adicionado."))

def finish():
    if not tarefas:
        print(soft("Não há tarefas para concluir."))
        return
    listar()
    try:
        idx = int(input(accent("\nNúmero da tarefa para concluir: ")))
        if 1 <= idx <= len(tarefas):
            t = tarefas.pop(idx - 1)
            t["concluida_em"] = agora()
            tarefas_concluidas.append(t)
            print(pastel(f"-`♡´- Concluída: {t['texto']}", ROSE))
        else:
            print(soft("Índice inválido."))
    except ValueError:
        print(soft("Digite um número válido."))

def remove():
    if not tarefas:
        print(soft("Não há tarefas para remover."))
        return
    listar()
    try:
        idx = int(input(accent("\nNúmero da tarefa para remover: ")))
        if 1 <= idx <= len(tarefas):
            t = tarefas.pop(idx - 1)
            print(pastel(f"🗑️  Removida: {t['texto']}", LILAC))
        else:
            print(soft("Índice inválido."))
    except ValueError:
        print(soft("Digite um número válido."))

def menu():
    while True:
        limpar()
        print(title("To-do list ♡\n"))
        print(pastel("1 - Adicionar nova tarefa", PINK))
        print(pastel("2 - Concluir tarefa", PINK))
        print(pastel("3 - Remover tarefa", PINK))
        print(pastel("4 - Listar tarefas", PINK))
        print(pastel("5 - Sair", PINK))
        print("\n" + soft(". ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.\n"))

        opcao = input(accent("Escolha uma opção: ")).strip()
        limpar()

        if opcao == "1":
            add()
        elif opcao == "2":
            finish()
        elif opcao == "3":
            remove()
        elif opcao == "4":
            listar()
        elif opcao == "5":
            print(pastel("Até mais! (ෆ˙ᵕ˙ෆ)♡\n", BLUSH))
            break
        else:
            print(soft("Opção inválida."))

        input(soft("\nPressione Enter para continuar..."))

if __name__ == "__main__":
    menu()

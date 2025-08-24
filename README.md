# To-do List ₊˚⊹ᰔ

Um projetinho simples em **Python** para organizar tarefas do dia a dia.  
Agora com **datas de criação/conclusão (`datetime`)** e **cores rosa** no terminal usando **`colorama`**.  

Você pode **adicionar, concluir, remover e listar** tarefas!

---

## ❀ Funcionalidades
- ➕ Adicionar novas tarefas (**registra data de criação**).
- ✅ Concluir tarefas (**registra data de conclusão**).
- 🗑️ Remover tarefas indesejadas.
- 📋 Listar pendentes e concluídas.

---

## ❤︎ Como rodar

### 1) Pré‑requisitos
- **Python 3.x** instalado.
- (Opcional) **Windows Terminal** ou **VS Code Terminal** para melhor visual das cores.

### 2) Clonar o repositório
```bash
git clone https://github.com/seu-usuario/todo-list-fofinho.git
cd todo-list-fofinho
```

### 3) Instalar dependências
```bash
# Garanta que instala no MESMO Python que você usa para executar
python -m pip install colorama

# Alternativas
py -m pip install colorama          # Windows com 'py'
# ou (Conda)
conda install colorama
```

### 4) Executar
```bash
python main.py
```

---

## ᯓ★ Exemplo no terminal
```
To-do list ♡

1 - Adicionar nova tarefa
2 - Concluir tarefa
3 - Remover tarefa
4 - Listar tarefas
5 - Sair

. ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.
```

---

## ୨ৎ Tecnologias
- [Python 3](https://www.python.org/) 🐍
- [`datetime`](https://docs.python.org/3/library/datetime.html) para registrar datas ✨
- [`colorama`](https://pypi.org/project/colorama/) para cores em rosa 💗
- `os` para limpar o console

---

## 🧰 Dicas & Solução de problemas

### `ModuleNotFoundError: No module named 'colorama'`
Instale o pacote no **mesmo Python** usado para rodar o script:
```bash
python -m pip install colorama
# ou
py -m pip install colorama
# ou (Conda)
conda install colorama
```
Verifique qual Python está sendo usado:
```bash
python -c "import sys; print(sys.executable)"
```

### As cores não aparecem no PowerShell
- Prefira **Windows Terminal** ou o **terminal do VS Code**.  
- O script usa `colorama.just_fix_windows_console()` para habilitar ANSI no Windows 10+.  
- Em terminais sem 256 cores, o tema cai para um **magenta** seguro.  
- Se quiser forçar 256 cores, rode no Windows Terminal ou adicione `FORCE_256 = True` no script (se seu terminal suportar).


---

## ✨ Créditos
Feito por [Geovanna Cunha](https://github.com/GeovannaSCunha).  

# 🔍 Identificador de Bandeiras de Cartão de Crédito

Um script Python para identificar a bandeira de cartões de crédito/débito com base no número do cartão.

## 🚀 Funcionalidades

- ✅ Identificação de 11 bandeiras diferentes
- 🧹 Limpeza automática de espaços e caracteres especiais
- 🛡️ Suporte para bandeiras nacionais e internacionais
- 🔄 Processamento rápido via expressões regulares

## 📋 Bandeiras Suportadas

| Bandeira          | Comprimento | Prefixos/IINs                     |
|-------------------|------------|-----------------------------------|
| Visa              | 13-16-19   | 4                                 |
| Mastercard        | 16         | 51-55, 2221-2720                  |
| American Express  | 15         | 34, 37                            |
| Discover         | 16         | 6011, 644-649, 65                 |
| Diners Club      | 14         | 300-305, 36, 38-39                |
| JCB              | 16         | 35                                |
| Hipercard        | 16         | 3841, 606282                      |
| EnRoute          | 15         | 2014, 2149                        |
| Voyager          | 15         | 8699                              |
| Aura             | 19         | 50                                |

## 💻 Como Usar

### Instalação
Nenhuma instalação necessária além do Python 3.6+.

### Uso Básico
```python
from identificador_bandeiras import identificar_bandeira

# Exemplo simples
print(identificar_bandeira("5599 2000 7936 2457"))  # Mastercard
print(identificar_bandeira("4024007121693831"))     # Visa


## ⚠️ Limitações

- **Não valida a existência real do cartão**: Apenas identifica o padrão do número, não verifica se o cartão realmente existe.
  
- **Bandeiras históricas**: Algumas bandeiras como EnRoute e Voyager podem não ser mais emitidas atualmente.

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos para contribuir:

1. **Faça um fork** do repositório
2. **Crie sua branch**:  
   ```bash
   git checkout -b feature/improvement

# Engenharia de Software – Rede de Cinemas - João Vitor Franco Moraes - RA: 25001068
## PARTE 1: Atividade 

---

## 1. Levantamento de Requisitos e Regras de Negócio

### 1.1 Requisitos Funcionais

| ID | Requisito |
|----|-----------|
| RF01 | O sistema deve permitir o cadastro de cinemas com nome, endereço e capacidade |
| RF02 | O sistema deve permitir o cadastro de filmes com título, duração, gênero, diretor e elenco |
| RF03 | O sistema deve permitir a criação de sessões vinculando filme, cinema, data e horário |
| RF04 | O sistema deve permitir o registro diário de público por sessão |
| RF05 | O sistema deve calcular o total de público por sessão |
| RF06 | O sistema deve calcular o total de público por filme (somando todas as sessões) |
| RF07 | O sistema deve calcular o total de público por cinema |
| RF08 | O sistema deve listar todos os filmes em cartaz em um determinado cinema |
| RF09 | O sistema deve listar as sessões de um filme em um determinado dia |
| RF10 | O sistema deve permitir consultar informações de elenco, diretores e gêneros |

### 1.2 Regras de Negócio

| ID | Regra |
|----|-------|
| RN01 | Um cinema pode exibir múltiplos filmes simultaneamente em salas diferentes |
| RN02 | Uma sessão deve respeitar a duração do filme mais um intervalo mínimo de 30 minutos entre sessões na mesma sala |
| RN03 | O público registrado por sessão não pode ser maior que a capacidade do cinema |
| RN04 | Um filme deve ter pelo menos um gênero, um diretor e um ator cadastrado |
| RN05 | A data/hora de início de uma sessão deve ser sempre futura no momento do cadastro |
| RN06 | Um filme deve ter duração mínima de 60 minutos |
| RN07 | Cada sessão pertence a exatamente um cinema e exibe exatamente um filme |

---

## 2. Diagrama de Casos de Uso

<img width="400" height="570" alt="image" src="https://github.com/user-attachments/assets/86f855ff-f27c-4572-bc67-c0116337e785" />

---

## 3. Diagrama de Classes do Domínio

<img width="279" height="398" alt="image" src="https://github.com/user-attachments/assets/42c88f0a-3025-470f-8978-c274fb45d6d9" />

---

## 4. Diagramas de Atividade

<img width="765" height="985" alt="image" src="https://github.com/user-attachments/assets/4df6d727-e804-4d0a-bbee-58d250a7a06d" />

---

## 5. Diagramas de Sequência

<img width="1102" height="1128" alt="image" src="https://github.com/user-attachments/assets/4cfee768-75fc-4c06-a61a-80891128161a" />

---

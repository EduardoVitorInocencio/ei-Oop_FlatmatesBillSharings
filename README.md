# 🏠 Flatmates Bill Sharing App

Este é um projeto em Python que calcula e divide automaticamente uma conta (como luz, água, aluguel, etc.) entre dois moradores com base nos dias em que cada um permaneceu na casa. O programa também gera um **relatório em PDF** com as informações detalhadas e permite o **compartilhamento online** via API do Filestack.

## 💡 Objetivo

Demonstrar o uso de **Programação Orientada a Objetos (OOP)** na prática com Python para resolver um problema real: dividir contas de forma justa entre colegas de quarto.

---

## 📦 Funcionalidades

- Entrada interativa dos dados via terminal
- Cálculo proporcional com base nos dias que cada morador ficou na casa
- Geração de relatório em PDF com os valores e período
- Compartilhamento do relatório via link (Filestack API)

---

## 🧠 Conceitos de OOP Aplicados

Este projeto foi construído usando **OOP** para manter o código organizado, modular e reutilizável.

### ✔️ Classes Utilizadas:

- **`Bill`**
  - Representa a conta (valor total + período).
- **`Flatmate`**
  - Representa um morador, incluindo os dias em que ficou na casa e sua participação no pagamento.
- **`PdfReport`**
  - Gera um relatório em PDF com os dados dos flatmates e a conta.
- **`FileSharer`**
  - Compartilha o PDF gerado usando a API do [Filestack](https://www.filestack.com/).

### 🧱 Princípios OOP Demonstrados:

| Princípio     | Exemplo                                                                 |
|---------------|-------------------------------------------------------------------------|
| **Encapsulamento** | Cada classe tem seus próprios dados e comportamentos (`Flatmate.pays()`)    |
| **Abstração**      | O usuário final não precisa saber como o PDF é gerado ou compartilhado       |
| **Modularidade**   | Separação clara entre lógica de negócio, apresentação e infraestrutura       |
| **Reusabilidade**  | As classes podem ser reaproveitadas em outros projetos semelhantes           |

---

## ▶️ Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/flatmates-bill-sharing.git
   cd flatmates-bill-sharing
````

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Coloque um ícone `house.png` dentro da pasta `files/`**

5. **Rode o programa**:

   ```bash
   python main.py
   ```

6. **(Opcional)** Configure sua chave da API Filestack no `main.py` para compartilhar o PDF online.

---

## 📄 Exemplo de Saída

```
Hey user, enter the bill amount: 120
What is the bill period? E.g. December 2020: June 2024
What is your name? Alice
How many days did Alice stay in the house during the bill period? 20
What is the name of the other flatmate? Bob
How many days did Bob stay in the house during the bill period? 10
Alice pays: 80.0
Bob pays: 40.0
```

---

## 🔧 Requisitos

* Python 3.8+
* Bibliotecas:

  * `fpdf`
  * `filestack`
  * `requests`
  * `urllib3==1.26.x`
  * `six`

---

## 📚 Créditos

Este projeto foi inspirado por exercícios de OOP e projetos educacionais sobre Python. Ideal para quem está aprendendo **Programação Orientada a Objetos** com aplicações práticas.

---

## 🧪 Sugestão de Expansões

* Suporte a mais de dois moradores
* Interface gráfica (GUI)
* Armazenamento em banco de dados (SQLite)
* Envio automático por e-mail

---

## 📝 Licença

Este projeto é livre para uso educacional e pessoal. Sinta-se à vontade para modificar e reutilizar.

```

---

Se quiser, posso criar a versão real desse `README.md` como arquivo para você baixar. Deseja isso?
```

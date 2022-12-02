# Desafio-SW-Embarcado

* ARQUITETURA

  Simulação de aquisição e envio de dados de sensores utilizando uma criptografia.

![Arquitetura drawio (2)](https://user-images.githubusercontent.com/119670639/205284129-2026d361-ddbb-456c-8889-6407c2682494.png)

  Arquivo contendo os dados simulados no formato JSON: `data.json`
  
  Criptografia: `encryption.py`.
  Os caracteres são representados conforme a seguir:
  * Letra: Caracter 5 posições a frente no alfabeto
  * Número: Soma 5 ao valor do número
  
  Exemplo:
  - "cozinha": {"temperatura": 30, "potencia": 30} --> {"htensmf": {"yjrujwfyzwf": "85", "utyjshnf": "85"}
  
* MAIN

  Simulação de envio de dados por meio de escrita de arquivos
  - `encrypted_data.json`
  - `decrypted_data.json`

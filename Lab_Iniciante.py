{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "446611e2",
   "metadata": {},
   "source": [
    "### Lista de Compras\n",
    "\n",
    "Exercício 1.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "76f7aa71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['leite', 'pão', 'queijo']\n"
     ]
    }
   ],
   "source": [
    "lista_compras = [\"leite\", \"pão\", \"queijo\"]\n",
    "\n",
    "print(lista_compras)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f92bdbe2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['leite', 'pão', 'queijo', 'ovos']\n"
     ]
    }
   ],
   "source": [
    "lista_compras.append(\"ovos\")\n",
    "\n",
    "print(lista_compras)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2568196d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "leite\n",
      "queijo\n",
      "ovos\n"
     ]
    }
   ],
   "source": [
    "for item in lista_compras:\n",
    "    print (item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1e18dee8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['leite', 'queijo', 'ovos']\n"
     ]
    }
   ],
   "source": [
    "lista_compras.remove(\"pão\")\n",
    "\n",
    "print(lista_compras)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50f37590",
   "metadata": {},
   "source": [
    "Exercício 1.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4f216250",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "leite\n"
     ]
    }
   ],
   "source": [
    "print(lista_compras[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "69ee54c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ovos\n"
     ]
    }
   ],
   "source": [
    "##-1 é para mostrar o último da lista, independente da posição\n",
    "\n",
    "print(lista_compras[-1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d1a6b4e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "queijo\n"
     ]
    }
   ],
   "source": [
    "print(lista_compras[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9493b521",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ovos\n"
     ]
    }
   ],
   "source": [
    "print(lista_compras[2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f3ed2eb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "print(len(lista_compras))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c65e0da3",
   "metadata": {},
   "source": [
    "### Dicionário\n",
    "\n",
    "Exercício 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cdea69d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1234-5678\n"
     ]
    }
   ],
   "source": [
    "contatos = {\"Ana\": \"1234-5678\", \"Bruno\": \"8765-4321\"}\n",
    "\n",
    "print(contatos[\"Ana\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "979dd017",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Ana': '1234-5678', 'Bruno': '8765-4321', 'Carlos': '1122-3344'}\n"
     ]
    }
   ],
   "source": [
    "contatos[\"Carlos\"] = \"1122-3344\"\n",
    "\n",
    "print(contatos)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6b8a7a61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Bruno': '8765-4321', 'Carlos': '1122-3344'}\n"
     ]
    }
   ],
   "source": [
    "del contatos[\"Ana\"]\n",
    "\n",
    "print(contatos)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01355f75",
   "metadata": {},
   "source": [
    "### Calculadora de medidas\n",
    "\n",
    "Exercício 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d72ec820",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A média de Carolina é 8.00\n",
      "Carolina foi aprovado.\n"
     ]
    }
   ],
   "source": [
    "# entrada do nome do aluno\n",
    "nome_aluno = input(\"Digite o nome do aluno: \")\n",
    "notas = []\n",
    "\n",
    "# entrada das notas\n",
    "nota1 = float(input(\"Digite a primeira nota: \"))\n",
    "notas.append(nota1)\n",
    "nota2 = float(input(\"Digite a segunda nota: \"))\n",
    "notas.append(nota2)\n",
    "nota3 = float(input(\"Digite a terceira nota: \"))\n",
    "notas.append(nota3)\n",
    "\n",
    "# média\n",
    "media = sum(notas) / len(notas)\n",
    "print(f\"A média de {nome_aluno} é {media:.2f}\")\n",
    "\n",
    "# aprovação\n",
    "if media >= 7.0:\n",
    "    print(f\"{nome_aluno} foi aprovado.\")\n",
    "else:\n",
    "    print(f\"{nome_aluno} foi reprovado.\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf803fb3",
   "metadata": {},
   "source": [
    "### Soma de números pares\n",
    "\n",
    "Atividades extras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f138c798",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Números inteiros: [5, 7, 6, 9, 10]\n",
      "A soma dos números pares é: 16\n"
     ]
    }
   ],
   "source": [
    "# Entrada dos números\n",
    "entrada = input(\"Insira uma lista de números separados por espaço: \")\n",
    "\n",
    "# Transformar a entrada em uma lista de strings com split()\n",
    "lista_string_numeros = entrada.split()\n",
    "\n",
    "# Converter cada valor da lista para inteiro usando um loop for\n",
    "numeros_int = []\n",
    "for num_str in lista_string_numeros:\n",
    "    numeros_int.append(int(num_str))\n",
    "\n",
    "# Verificação\n",
    "print(\"Números inteiros:\", numeros_int)\n",
    "\n",
    "# Passo 4: criar uma variável para armazenar a soma dos números pares\n",
    "soma_pares = 0\n",
    "\n",
    "# Passo 5: usar um loop for para percorrer os números e verificar se são pares\n",
    "for num in numeros_int:\n",
    "    if num % 2 == 0:  # verifica se o resto da divisão por 2 é 0 (par)\n",
    "        soma_pares += num\n",
    "\n",
    "# Exibir o resultado final\n",
    "print(\"A soma dos números pares é:\", soma_pares)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

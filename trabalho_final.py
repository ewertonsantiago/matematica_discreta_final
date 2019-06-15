#Trabalho Matemática Discreta
'''
1 – Qual a probabilidade do gênero ser feminino, possuir um animal de estimação e possuir veículo?

2 – Qual a probabilidade do gênero ser homem, residir no brasil e trabalhar no departamento de support?

3 – Qual a probabilidade do gênero ser mulher, trabalhar no departamento de marketing e não possuir animal de estimação?

4 – Qual a probabilidade do gênero ser homem, gostar de filmes de comedy e não possuir veículo?

5 – Qual a probabilidade do gênero ser mulher, não possuir animal de estimação e não possuir veículo?
'''

import csv
from fractions import Fraction

Respostas = {
    "Genero": {"Masculino": 0, "Feminino": 0},
    "Animal": {"Sim": 0, "Nao": 0},
    "Veiculo": {"Sim": 0, "Nao": 0},
    "Pais": {"Brasil": 0},
    "Departamento": {"Marketing": 0, "Suporte": 0},
    "Filmes": {"Comedia": 0}
}

with open('/home/ewerton/Downloads/MOCK_DATA.csv', 'r', encoding='utf-8', errors='ignore') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        for key, val in row.items():
            if key.lower() == 'gender':
                if val.lower() == 'male':
                    Respostas['Genero']['Masculino'] += 1
                elif val.lower() == 'female':
                    Respostas['Genero']['Feminino'] += 1
            elif key.lower() == 'has_pet':
                if val.lower() == 'true':
                    Respostas['Animal']['Sim'] += 1
                elif val.lower() == 'false':
                    Respostas['Animal']['Nao'] += 1
            elif key.lower() == 'has_car':
                if val.lower() == 'true':
                    Respostas['Veiculo']['Sim'] += 1
                elif val.lower() == 'false':
                    Respostas['Veiculo']['Nao'] += 1 
            elif key.lower() == 'country':
                if val.lower() == 'brazil':
                    Respostas['Pais']['Brasil'] += 1
            elif key.lower() == 'department':
                if val.lower() == 'marketing':
                    Respostas['Departamento']['Marketing'] += 1
                elif val.lower() == 'Support':
                    Respostas['Departamento']['Suporte'] += 1
            elif key.lower() == 'prefered_movie_genres':
                if val.lower() == 'comedy':
                    Respostas['Filmes']['Comedia'] += 1


def tal_que(predicado, espaco):
    """Os resultados no espaco amostral para os quais o predicado é verdadeiro. Se espaço e um conjunto ,
    retorna um subconjunto {resultado , ...}
    Se espaco e ProbDist , retorna um ProbDist{resultado , frequencia}"""
    if isinstance(espaco, ProbDist):
        return ProbDist({o: espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}


def P(evento, espaco):
    """A probabilidade de um evento , dado um espaco amostral de resultados
    equiprovaveis.
    evento: uma colecao de resultados , ou um predicado.
    espaco: um conjunto de resultados ou a distribuicao de probabilidade
    na forma de pares {resultado: frequencia}."""
    if callable(evento):
        evento = tal_que(evento, espaco)
    if isinstance(espaco, ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))


class ProbDist(dict):
    """Uma distribuicao de probablidade; um mapeamento {resultado:probabilidade}"""

    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome] / total
            assert self[outcome] >= 0


def joint(A, B, sep=''):
    """A probabilidade conjunta de duas distribuições de probabilidade
        independentes.
    Resultado é todas as entradas da forma {a+sep+b: P(a)*P(b)}"""
    return ProbDist({a + sep + b: A[a] * B[b]
                     for a in A
                     for b in B})


def sexo_m(r):
    return 'Masculino' in r

def sexo_f(r):
    return 'Feminino' in r



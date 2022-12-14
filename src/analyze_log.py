import csv
from collections import Counter
import os.path


def verify_file(path):
    if not path.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")


def post_text(dishes_maria,
 hamburger_counter,
 never_ordered,
 days_not_attended):
    with open('data/mkt_campaign.txt', 'w') as file:
        lines = [
            list(Counter(dishes_maria))[0] + '\n',
            str(hamburger_counter) + '\n',
            str(never_ordered) + '\n',
            str(days_not_attended) + '\n',
        ]
        file.writelines(lines)


def count_joao(row):
    days_not_attended = {'segunda-feira', 'terça-feira', 'sabado'}
    joao_dishes = {'hamburguer', 'pizza', 'coxinha', 'misto-quente'}
    if row[2] in days_not_attended:
        days_not_attended.remove(row[2])
    if row[1] in joao_dishes:
        joao_dishes.remove(row[1])
    return [joao_dishes, days_not_attended]


def analyze_log(path):
    verify_file(path)
    dishes_maria = []
    hamburger_counter = 0
    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in csv_reader:
            if row[0] == 'maria':
                dishes_maria.append(row[1])
            if row[0] == 'arnaldo' and row[1] == 'hamburguer':
                hamburger_counter += 1
            if row[0] == 'joao':
                joao = count_joao(row)
    post_text(dishes_maria, hamburger_counter, joao[0], joao[1])

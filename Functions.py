import random

def weight_builder(length, m1, q1, m2, q2):
    half = length / 2
    result = [0] * length  # builds an empty list of zeros
    for i in range(0, length):
        if i <= half:
            result[i] = m1 * (i / length) + q1
        else:
            result[i] = m2 * (i / length) + q2
    return result


def custom_pdf_number_generator(population, weigths):
    return random.choices(population, weigths)

def adjusted_number_generator(max_int, population, weight):
    # Genero un numero
    num1 = custom_pdf_number_generator(population, weight)
    # Genero un secondo numero
    num2 = custom_pdf_number_generator(population, weight)
    # Moltiplico i due numeri generati tra loro (chiamo questo numero "prod")
    prod = num1[0] * num2[0]  # le parentesi quadre servono perchè si tratta di liste unitarie
    # Calcolo il resto intero della divisione tra prod e il numero casuale massimo che voglio estrarre
    return prod % max_int

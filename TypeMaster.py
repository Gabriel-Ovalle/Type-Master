import random

def get_random_words(word_list, num_words=9):
    return random.sample(word_list, num_words)

def typing_game():
    palabras = ["Esternocleidomastoideo", "zapote", "trapking", "Electroencefalografista", "Contrarrevolucionario", "Desoxirribonucleótido", "ciclotrimetilenotrinitramina", "otorrinolaringología", "Pseudohermafroditismo"]
    palabras_seleccionadas = get_random_words(palabras)
    errores = 0
    total_palabras = len(palabras_seleccionadas)
    
    print("Typing Test: Type the given word correctly and press Enter")
    print("--------------------------------------------------------")
    
    for word in palabras_seleccionadas:
        user_input = input(f"Type this word: {word}\n> ")
        if user_input == word:
            print("Correct!")
        else:
            print("Incorrect!")
            errores += 1
    
    Precision = ((total_palabras - errores) / total_palabras) * 100
    print("\nTest Completado!")
    print(f"Total de errores: {errores}")
    print(f"Precision: {Precision:.2f}%")

if __name__ == "__main__":
    typing_game()
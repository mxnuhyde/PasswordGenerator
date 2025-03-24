import itertools

def generate_passwords(data, output_file):
    # Estrai le varie parti della data di nascita
    day = data['data_nascita'][:2]
    month = data['data_nascita'][3:5]
    year = data['data_nascita'][6:10]
    short_year = year[2:]  # Gli ultimi due numeri dell'anno
    full_date = day + month + year
    short_date = day + month + short_year
    date_combinations = [year, full_date, day, month, day + month, day + year, month + year, short_date]
    
    # Creazione di un elenco per contenere le combinazioni di parole chiave
    base_words = []
    
    # Aggiungi le combinazioni di base usando i dati forniti
    base_words.append(data['nome'])
    base_words.append(data['cognome'])
    base_words.extend(data['parole_aggiuntive'])  # Parole fornite dall'utente
    
    # Aggiungi varianti con lettere maiuscole, minuscole e con l'iniziale maiuscola
    base_words = list(set(base_words + [word.capitalize() for word in base_words] + 
                          [word.upper() for word in base_words] + [word.lower() for word in base_words]))
    
    # Simboli da combinare
    symbols = ['!', '@', '#', '$', '%']

    # Scrivi direttamente su file le password generate
    with open(output_file, 'w') as file:
        for word in base_words:
            for date_part in date_combinations:
                for symbol in symbols:
                    # Aggiungi le combinazioni parola + data + simbolo e altre configurazioni
                    file.write(f"{word}{date_part}{symbol}\n")
                    file.write(f"{word}{symbol}{date_part}\n")
                    file.write(f"{date_part}{word}{symbol}\n")
                    file.write(f"{date_part}{symbol}{word}\n")
                    file.write(f"{symbol}{word}{date_part}\n")
                    file.write(f"{symbol}{date_part}{word}\n")
                # Aggiungi combinazioni senza simbolo
                file.write(f"{word}{date_part}\n")
                file.write(f"{date_part}{word}\n")
            # Aggiungi combinazioni parola + simbolo senza la data
            for symbol in symbols:
                file.write(f"{word}{symbol}\n")
                file.write(f"{symbol}{word}\n")
            # Aggiungi solo la parola e la data
            file.write(f"{word}\n")
        for date_part in date_combinations:
            file.write(f"{date_part}\n")

    print(f"Password generate salvate in: {output_file}")

# Funzione per chiedere i dati all'utente
def get_user_data():
    print("Inserisci i dati della persona per generare le possibili password:")
    
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    data_nascita = input("Data di nascita (formato DD/MM/YYYY): ")
    
    parole_aggiuntive = []
    while True:
        parola = input("Inserisci una parola aggiuntiva (lascia vuoto per terminare): ")
        if parola == "":
            break
        parole_aggiuntive.append(parola)
    
    data = {
        'nome': nome,
        'cognome': cognome,
        'data_nascita': data_nascita,
        'parole_aggiuntive': parole_aggiuntive
    }
    
    return data

# Chiedi i dati all'utente
user_data = get_user_data()

# Genera il nome del file basato sul cognome
output_file = f"passwords_{user_data['cognome']}.txt"

# Genera e salva le password direttamente su file
generate_passwords(user_data, output_file)

# Password Generator

This Python script generates a variety of password combinations based on user-provided data, such as a person's name, surname, and birth date. The generated passwords are saved to a text file for easy retrieval and use.

## 📋 Features

- **User Input**: Requests user details including name, surname, and birth date (DD/MM/YYYY format).
- **Password Generation**: Generates a wide range of password combinations using the user's name, surname, birth date, and additional custom words.
- **Symbol Integration**: Incorporates common symbols such as `!`, `@`, `#`, `$`, and `%` into the password combinations.
- **Custom Word Input**: Allows the user to provide additional words to include in the password combinations.
- **Multiple Combinations**: Generates passwords in various formats, including:
  - Name + Date + Symbol
  - Date + Name + Symbol
  - Symbol + Name + Date
  - Name + Date (without symbols)
  - Name + Symbol (without date)
  - Date only (without name and symbol)

## 🧑‍💻 How It Works

1. The script asks the user to input their **name**, **surname**, and **birth date**.
2. The user can also add **custom words** that they want to include in the generated passwords.
3. The script then combines these inputs in various formats and saves the generated passwords to a `.txt` file.

## ⚙️ How to Use

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/mxnuhyde/PasswordGenerator.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install itertools
    ```

3. Run the script:
    ```bash
    python password_generator.py
    ```

4. Enter the required data when prompted:
    - **Name**: Your first name
    - **Surname**: Your last name
    - **Birth Date**: Your birth date in `DD/MM/YYYY` format
    - **Additional Words**: Any extra words you'd like to include (leave empty to finish)

5. The generated passwords will be saved in a file named `passwords_<surname>.txt`.

## 📂 Files

- `password_generator.py`: The main Python script that generates passwords.
- `passwords_<surname>.txt`: The output file containing the generated passwords.

## 🔒 Security

Ensure you keep your generated passwords secure. These passwords are based on personal data, so avoid sharing them publicly or using them in unsecured environments.

## 🛠️ License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

---

Happy password generating! 🔐

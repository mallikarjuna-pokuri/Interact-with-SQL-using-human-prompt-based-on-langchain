# SQLChat: Conversational SQL Interface

Welcome to SQLChat, your conversational interface to interact seamlessly with a SQL database using LangChain.

## Overview

SQLChat enables users to engage in natural language conversations with a SQL database. LangChain powers the underlying natural language processing, transforming user prompts into SQL queries for interacting with the database. This project aims to provide an intuitive and human-friendly way to query and retrieve information from a PostgreSQL database.

## Features

- **Conversational Interface**: Engage in natural language conversations with your SQL database.
- **LangChain Integration**: Utilizes LangChain for natural language processing and SQL query generation.
- **Seamless eSQL Connection**: Easily connect and interact with your SQL database through a chat-based interface.

## Getting Started

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/mallikarjuna-pokuri/Interact-with-SQL-using-human-prompt-based-on-langchain.git
    cd Interact-with-SQL-using-human-prompt-based-on-langchain
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure SQL Connection**:

    Update the PostgreSQL connection details in the configuration file.

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

5. **Access the Chat Interface**:

    Open your web browser and navigate to `http://http://localhost:8501/` to start chatting with your SQL database.

## Usage

1. Type your questions or prompts in natural language.
2. SQLChat will convert your prompts into SQL queries using LangChain.
3. The SQL queries are executed on the PostgreSQL database, and results are displayed in the chat interface.

## Contributing
Contributions are welcome! Follow these steps to contribute:


1. Fork the repository
2. Create a new branch (git checkout -b feature/improvement)
3. Make changes and commit (git commit -am 'Add feature')
4. Push to the branch (git push origin feature/improvement)
5. Create a pull request

## License
This project is licensed under the MIT License.

Feel free to reach out to mallikarjunapokuri595@gmail.com for any questions or concerns.

Happy coding! 🚀


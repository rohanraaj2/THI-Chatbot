
# Charlie Chatbot

A simple AI chatbot built using [ChatterBot](https://chatterbot.readthedocs.io/en/stable/index.html) to help new international students at Technische Hochschule Ingolstadt. This chatbot uses a basic rule-based training system by reading question-answer pairs from external files.

## 🧠 Project Idea

- Store training data (questions and answers) in external text files.
- Read the data dynamically from the `training/` directory.
- Train the chatbot using `ListTrainer` from ChatterBot.
- Example: One training file contains several related questions and one shared answer.

## 📁 Directory Structure

```
project-root/
│
├── charlie.py              # Main chatbot setup and training script
├── training/               # Directory with all training .txt files
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
├── Dockerfile              # Optional: for containerization
├── docker-compose.yml      # Optional: for service orchestration
└── README.md               # This file
```

## 🛠️ Tools Used

- Python 3
- ChatterBot: AI conversational engine
- Docker & Docker Compose (optional): To run and restart the chatbot easily

## 📄 Format of Training Files

Each `.txt` file in the `training/` directory should follow this format:

```
How are you?
Hello!
Good Day!
---
Hey there – how are you?
```

- **Top lines**: Multiple user inputs (questions)
- **Line with "---"**: Separator
- **Last line**: Common answer for all the above inputs

## ⚙️ How It Works

1. List all files in the `training` directory:
    ```python
    import os
    files = os.listdir('./training')
    ```
2. Read each file line by line:
    ```python
    with open(filename, 'r') as f:
        for line in f:
            # process line
    ```
3. Parse questions and answers:
    ```python
    questions = []
    mode = 'questions'
    for line in f:
        if line.strip() == '---':
            mode = 'answer'
        elif mode == 'questions':
            questions.append(line.strip())
        elif mode == 'answer':
            for question in questions:
                trainer.train(question, line.strip())
            questions = []
    ```

## 🚀 Quickstart

1. Clone or copy the repository.
2. Install dependencies:
    ```bash
    pip install chatterbot chatterbot_corpus
    ```
3. Add your training data:
    - Place `.txt` files inside the `training/` directory.
4. Run the chatbot:
    ```bash
    python charlie.py
    ```

## 🐳 Docker Commands (if using)

```bash
docker compose up -d         # Start the chatbot
docker compose restart       # Restart after making code or data changes
docker compose down          # Stop the chatbot
```

## 🧰 Debugging Tips

Check running containers:
```bash
docker ps -a
```
Find logs of a specific container:
```bash
docker logs <container-id>
```

Editor cheat sheet (for ne):
https://cheatography.com/pryl/cheat-sheets/ne-nice-editor/

## 📚 Resources

- [ChatterBot Docs](https://chatterbot.readthedocs.io/en/stable/)
- [Docker Compose](https://docs.docker.com/compose/)

## 👨‍💻 Developed for

Computer Science and Artificial Intelligence Introductory Project — Summer Semester 2025  
Technische Hochschule Ingolstadt  
Faculty of Computer Science

---

Let me know if you also want a `requirements.txt`, Dockerfile, or web interface HTML included!

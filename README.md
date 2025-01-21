# Restaurant assistant bot

this is a bot that helps users explore menu of the restaurant and take their orders

# getting started

clone repository

```bash
git clone https://github.com/Aurumdev952/restaurant-assistant-agent.git
cd restaurant-assistant-agent
```

install dependencies

```bash
pip install -r requirements.txt
```

create a posgreSQL database and add missing environment variables
```
OPENAI_API_KEY=
DATABASE_URI=
```

```bash
cp .env.example .env
```

apply migrations

```bash
alembic update head
```

seed data

```bash
python insert.py
```

run the bot

```bash
python main.py
```





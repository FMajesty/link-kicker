# Link Kicker
Do you have a problem with just forgetting to read the articles you've saved links to like me? 
This bot was created to solve this problem.

➡ [Start using a bot](https://t.me/link_kicker_bot)

## Installation and local launch
1. Clone this repo: `git clone https://github.com/FMajesty/link-kicker`
2. Create `.env` with `cp .env.example .env` and fill it out
3. Create `commands.yaml` with `cp commands.yaml.example commands.yaml` and change command descriptions if you want
4. Install [poetry](https://python-poetry.org/) on your machine (or just `pip install poetry` in env)
5. Run `poetry install` in the root folder for requirements installing
6. Run `pybabel compile -d locales -D link_kicker` in the root folder for compiling locales
7. Run `aerich upgrade` in the root folder for running migrations
8. Run `make run`

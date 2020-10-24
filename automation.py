import os
import math
import requests
import pandas as pd
pd.options.mode.chained_assignment = None


response = requests.get("https://leetcode.com/api/problems/all")
df_raw = pd.json_normalize(response.json()['stat_status_pairs'])

d = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
df_raw['difficulty'] = df_raw['difficulty.level'].map(d)

columns = ['stat.frontend_question_id', 'stat.question__title', 'stat.question__title_slug', 'difficulty', 'stat.total_submitted', 'stat.total_acs', 'paid_only']
df = df_raw[columns]

new_columns = ['question_id', 'question_title', 'question_title_slug', 'difficulty', 'answer_submitted', 'answer_accepted', 'paywall']
df.columns = new_columns

df.set_index('question_id', inplace=True)
df.sort_index(inplace=True)

df['url'] = df['question_title_slug'].map(lambda slug: f'https://leetcode.com/problems/{slug}/')


def get_folder_name(i, n=100):
    return f'{math.floor(i / n) * n:04d}-{math.ceil(i / n) * n:04d}'


def get_path(i, slug):
    return f'{get_folder_name(i)}/{i}-{slug}.py'


def create_file(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    open(filepath, 'a').close()


ids = [1, 2]
create_files = False

for i in ids:
    filepath = get_path(i, df['question_title_slug'][i])
    print(f"|{i}|[{df['question_title'][i]}]({df['url'][i]})|[Python]({filepath})|{df['difficulty'][i]}|")
    if create_files:
        create_file(filepath)

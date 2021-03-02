import os
import requests
import pandas as pd

pd.options.mode.chained_assignment = None

response = requests.get("https://leetcode.com/api/problems/all")
df_raw = pd.json_normalize(response.json()['stat_status_pairs'])

d = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
df_raw['difficulty'] = df_raw['difficulty.level'].map(d)

columns = ['stat.frontend_question_id', 'stat.question__title', 'stat.question__title_slug', 'difficulty',
           'stat.total_submitted', 'stat.total_acs', 'paid_only']
df = df_raw[columns]

new_columns = ['question_id', 'question_title', 'question_title_slug', 'difficulty', 'answer_submitted',
               'answer_accepted', 'paywall']
df.columns = new_columns

df.set_index('question_id', inplace=True)
df.sort_index(inplace=True)

df['url'] = df['question_title_slug'].map(lambda slug: f'https://leetcode.com/problems/{slug}/')


def create_file(df, i):
    filepath = f'solutions/{i}-{df["question_title_slug"][i]}.py'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    open(filepath, 'a').close()


def get_row(df, i):
    return f"|{i}|[{df['question_title'][i]}]({df['url'][i]})|[Python](solutions/{i}-{df['question_title_slug'][i]}.py)|{df['difficulty'][i]}|"


def get_commit_summary(df, i):
    return f"Add {i}-{df['question_title_slug'][i]}"


def update_readme(source, destination, rows, placeholder='$PLACEHOLDER$'):
    with open(source, 'rb') as f:
        content = f.read()
    rows = '\r\n'.join(rows)
    content = str(content, 'utf-8').replace(placeholder, rows)
    content = content.replace('\r\n', '\n')
    with open(destination, "w") as f:
        f.write(content)


if __name__ == "__main__":

    ids = [1, 2, 7, 8, 9, 13, 36, 179, 189, 279, 347, 509, 628, 872, 957, 1304, 1366, 1447, 1456, 14, 875, 478, 1528,
           1449, 709, 1342, 941, 944, 1195, 1448, 1116, 1394, 1309, 1115, 1114, 973, 405, 28, 1523, 1408, 1295, 11, 17,
           78, 659, 104, 121, 122, 136, 155, 202, 322, 4, 5, 3, 6, 10, 12, 16, 19, 18, 23, 27, 20, 25, 26, 29, 24, 39,
           45, 76, 35, 33, 34, 38, 41, 43, 42, 48, 53, 54, 64, 226, 66, 70, 227, 56, 55, 58, 57, 67, 169, 206, 237, 283,
           303, 338]

    create_files = True

    table = []
    for i in sorted(ids):
        table.append(get_row(df, i))
        if create_files:
            create_file(df, i)

    update_readme('source.md', 'README.md', table)

    print(get_row(df, ids[-1]))
    print(get_commit_summary(df, ids[-1]))
    pd.Series([get_commit_summary(df, ids[-1])]).to_clipboard(index=False, header=False)

import csv
import json
import uuid

with open('jovokepek.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar='"', delimiter=',')
    rows = list(reader)

print(rows[1])

questions = []

def answer(str):
    if str == 'IGEN':
        return True
    elif str == 'NEM':
        return False
    else:
        return None

candidates = ['d578d28c-dbac-4bae-9cc4-963b506e0101', '7a6f9a15-2e71-4bca-a45d-94680f9b4755', '94b53e83-7875-4c16-9ccf-4becae64f089', '1a93946b-27ba-4fd2-a05b-6474b276815c', 'df6eee27-f75d-430b-bc22-dc3cafa2bc90', '1ad707e9-a9c8-4e92-a244-00e156ad25a2']
answers = {c: [] for c in candidates}
for row in rows[1:]:
    qid = str(uuid.uuid4())
    questions.append({
        'id': qid,
        'title': row[1],
        "statement": row[1],
        "detail": row[2],
        "tags": [row[0]],
    })
    for i, candidate in enumerate(candidates):
        answers[candidate].append({"questionId": qid, "answer": answer(row[1+(i+1)*2]), 'comment': row[1+(i+1)*2+1]})


with open('data/instance/voksmonitor.hu/parkolasi-jovokepek/voksmonitor/questions.json', 'w') as json_file:
    json.dump(questions, json_file, indent=4)

with open('data/instance/voksmonitor.hu/parkolasi-jovokepek/voksmonitor/candidates-answers.json', 'w') as json_file:
    json.dump(answers, json_file, indent=4)


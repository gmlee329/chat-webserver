import urllib.request
import json

url = 'http://104.196.217.33/' # request url(can change)
con = '> '

def request(url):
    return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

questions = request(url)
questionlist = questions['questions']
def option(command):
    if command == '/h':
        print(con+"command [ help : '/h', quit : '/q', mannual : '/m' ]")
    elif command == '/q':
        exit()
    elif command == '/m':
        print(con+"enter the question in the list(enter '/q' to quit)")
        print(con+'questions :', questionlist)
    else:
        print(con+"command not exist(enter '/h' to help)")
        
def start():
    print(con+"enter the question in the list(enter '/h' to help)")
    print(con+'questions :', questionlist)
    run()

def run():
    while True:
        question = input(con).strip()
        if question.startswith('/'):
            option(question)
            continue
        question_number = ''
        for i, q in enumerate(questionlist):
            if question == q:
                question_number = str(i)
                break
        get_url = url + 'chat?question=' + question_number
        answer = request(get_url)
        print(con+answer['answer'])

start()

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import openai


openai.api_key_path = '../code.txt'

def index(request):
    prompt = request.POST.get('prompt') if request.method == 'POST' else ''
    activity = request.POST.get('activity') if request.method == 'POST' else 0
    print(activity)
    match activity:
        case 'fichier_a':
            f = open('form/context/activityA.txt', 'r')
            context = f.read()
        case 'fichier_b':
            f = open('form/context/activityB.txt', 'r')
            context = f.read()
        case 'fichier_c':
            f = open('form/context/activityC.txt', 'r')
            context = f.read()
        case _:
            context = 'write like an author of book'
    
    template = loader.get_template('form/index.html')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": context
            },
            {
                "role": "user", 
                "content": prompt
            },
        ],
    )
    response = completion.choices[0].message['content'] if request.method == 'POST' else ''
    context = { 'GPT_respons' : response,}
    return HttpResponse(template.render(context, request))

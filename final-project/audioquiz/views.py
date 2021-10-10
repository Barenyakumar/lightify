from django.shortcuts import render,redirect
from .models import QuesModel
from django.http import JsonResponse

# Create your views here.
def audioquiz(request):
    quiz=QuesModel.objects.all()
    if request.method == 'POST':
        print(request.POST)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in quiz:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'results.html', context)

    return render(request,'aqz.html',{'quiz':quiz})



def getquiz(request):
    quiz=QuesModel.objects.all()
    quiz=list(quiz.values())
    for item in quiz:
        del item['ans']
    return JsonResponse({"quiz":quiz})


def results(request):
    pass

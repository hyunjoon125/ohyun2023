from django.shortcuts import render, HttpResponse, redirect
from memo.models import Memo
from memo.forms import MemoForm


# Create your views here.
# sticky_memo/memo/views.py

def get_all_memo(request):
    memo_list = Memo.objects.all()
    context = {"memos": memo_list}

    return render(request, "memo_list.html", context)

def get_memo(request, id):
    memo = Memo.objects.get(id=id)
    context = {"memo": memo } 

    return render(request, "memo_detail.html", context)


def create_memo(request):
    if request.method == 'GET':
        form = MemoForm(request.POST)
        context= {'form': form}
        return render(request, 'memo_create.html', context)
    
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')

def update_memo(request, id):
    memo= Memo.objects.get(id=id)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
def delete_memo(request, id):
    memo= Memo.objects.get(id=id)
    if request.method == 'POST':
        memo.delete()
        return redirect('memo_list')

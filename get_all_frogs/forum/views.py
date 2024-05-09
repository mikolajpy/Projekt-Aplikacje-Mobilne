from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from get_all_frogs.models import Zabka, StoreComment


def store_list(request):
    if request.user.is_authenticated:
        stores = Zabka.objects.all()
        return render(request, 'store_list.html', {'stores': stores})
    else:
        return HttpResponseNotFound("hello") 
    

def store_detail(request, store_id):
    store = get_object_or_404(Zabka, id=store_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        comment = StoreComment.objects.create(store=store, user=request.user, comment=comment_text)
        comment.save()
        return redirect('store-detail', store_id=store_id)
    comments = StoreComment.objects.filter(store=store)
    return render(request, 'store_detail.html', {'store': store, 'comments': comments})

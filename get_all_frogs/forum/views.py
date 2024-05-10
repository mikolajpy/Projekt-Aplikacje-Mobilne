from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from get_all_frogs.models import Zabka, StoreComment
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib import messages

def store_list(request):
    if request.user.is_authenticated:
        stores = Zabka.objects.all()
        return render(request, 'store_list.html', {'stores': stores})
    else:
        return HttpResponseNotFound("hello") 
    
@login_required
def store_detail(request, store_id):
    if request.user.is_authenticated:
        store = get_object_or_404(Zabka, id=store_id)

        # Sprawdź, czy użytkownik już dodał komentarz
        existing_comment = StoreComment.objects.filter(store=store, user=request.user).exists()

        if request.method == 'POST':
            if existing_comment:
                messages.warning(request, 'Już dodałeś komentarz pod tym sklepem !')
                return redirect('store-detail', store_id=store_id)
            
            comment_text = request.POST.get('comment')
            rating = request.POST.get('rating')
            comment = StoreComment.objects.create(store=store, user=request.user, comment=comment_text, Ocena=rating)
            comment.save()
            return redirect('store-detail', store_id=store_id)

        comments = StoreComment.objects.filter(store=store)
        total_comments = comments.count()
        average_rating = comments.aggregate(Avg('Ocena'))['Ocena__avg']

        return render(request, 'store_detail.html', {'store': store, 'comments': comments, 'total_comments': total_comments, 'average_rating': average_rating})
    ### DO DEBUGOWANIA 
    else:
        return HttpResponseNotFound("hello") 
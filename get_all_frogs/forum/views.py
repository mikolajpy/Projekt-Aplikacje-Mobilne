from django.shortcuts import render, get_object_or_404, redirect
from get_all_frogs.models import Zabka, StoreComment
from django.db.models import Avg
from django.contrib import messages

def store_list(request):
    if request.user.is_authenticated:
        stores = Zabka.objects.all()
        return render(request, 'store_list.html', {'stores': stores})
    
def store_detail(request, store_id):
    if request.user.is_authenticated:
        store = get_object_or_404(Zabka, id=store_id)
        comments = StoreComment.objects.filter(store=store, parent__isnull=True)
        total_comments = comments.count()
        average_rating = comments.aggregate(Avg('Ocena'))['Ocena__avg']
        existing_comment = StoreComment.objects.filter(store=store, user=request.user).exists()

        if request.method == 'POST' and 'parent_id' not in request.POST:
            if existing_comment:
                messages.warning(request, 'Już dodałeś komentarz pod tym sklepem !')
                return redirect('store-detail', store_id=store_id)  
            comment_text = request.POST.get('comment')
            rating = request.POST.get('rating')
            comment = StoreComment(store=store, user=request.user, comment=comment_text, Ocena=rating)
            comment.save()
        elif request.method == 'POST':
            parent_id = request.POST.get('parent_id')
            parent_comment = get_object_or_404(StoreComment, id=parent_id, store=store)
            comment_text = request.POST.get('comment')
            comment = StoreComment(store=store, user=request.user, comment=comment_text, parent=parent_comment)
            comment.save()

        return render(request, 'store_detail.html', {'store': store, 'comments': comments, 'total_comments': total_comments, 'average_rating': average_rating})
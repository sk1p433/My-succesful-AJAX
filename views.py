def simple_ajax(request):
    form = UserCommentForm
    return render(request, 'store/simple_ajax.html', {"UserCommentForm": form})

def simple_ajax_test(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == "POST" and is_ajax:
        form = UserCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False}, status=400)
    else:
        form = UserCommentForm()

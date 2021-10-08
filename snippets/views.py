from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from snippets.models import Snippet

from snippets.forms import SnippetForm
# Create your views here.
def top(request):
	snippets = Snippet.objects.all()
	context = {"snippets": snippets}
	#return HttpResponse(b"Hello World")
	return render(request, "snippets/top.html", context)

@login_required
def snippets_new(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			snippet = form.save(commit=False)
			snippet.created_by = request.user
			snippet.save()
			return redirect(snippets_detail, snippet_id=snippet.pk)
	else:
		form = SnippetForm()
	return render(request, "snippets/snippet_new.html", {'form': form})

@login_required
def snippets_edit(request, snippet_id):
	snippet = get_object_or_404(Snippet, pk=snippet_id)
	if snippet.created_by.id != request.user.id:
		return HttpResponseForbidden("このスニペットの編集は許可されていません。")

	if request.method == "POST":
		form = SnippetForm(request.POST, instance=snippet)
		if form.is_valid():
			snippet.save()
			return redirect(snippets_detail, snippet_id=snippet.id)
	else:
		form = SnippetForm(instance=snippet)
	return render(request, "snippets/snippet_edit.html", {'form': form})

def snippets_detail(request, snippet_id):
	snippet = get_object_or_404(Snippet, pk=snippet_id)
	return render(request, "snippets/snippet_detail.html",{'snippet':snippet})
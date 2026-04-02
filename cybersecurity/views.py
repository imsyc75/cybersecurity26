from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_note(request, note_id):
    # flaw: Notes were accessed directly by ID without checking ownership.
    # Attackers can view other people's notes simply by modifying the ID in the URL.
    note = get_object_or_404(Note, pk=note_id)

    # fix: Check if the owner of the note is the user who made the current request.
    # note = get_object_or_404(Note, pk=note_id)
    # if note.user != request.user:
    #     return HttpResponseForbidden("<h1>403 Forbidden</h1><p>You do not have permission to view this note.</p>")

    return render(request, 'note_detail.html', {'note': note})

def home(request):
    user_notes = Note.objects.filter(user=request.user)
    return render(request, 'home.html', {'notes': user_notes})

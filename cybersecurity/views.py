from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from django.http import HttpResponseForbidden
from django.db import connection

@login_required
def view_note(request, note_id):
    # flaw1: Notes were accessed directly by ID without checking ownership.
    # Attackers can view other people's notes simply by modifying the ID in the URL.
    note = get_object_or_404(Note, pk=note_id)

    # fix1: Check if the owner of the note is the user who made the current request.
    # note = get_object_or_404(Note, pk=note_id)
    # if note.user != request.user:
    #     return HttpResponseForbidden("<h1>403 Forbidden</h1><p>You do not have permission to view this note.</p>")

    return render(request, 'note_detail.html', {'note': note})

def home(request):
    user_notes = Note.objects.filter(user=request.user)
    return render(request, 'home.html', {'notes': user_notes})


@login_required
def search_notes(request):
    query = request.GET.get('query', '')
    notes = []
    
    if query:
        # flaw2：Directly concatenating user input using f-string or string addition
        # This method does not escape user input, leading to SQL injection.
        sql = f"SELECT * FROM cybersecurity_note WHERE title = '{query}'"
        
        with connection.cursor() as cursor:
            cursor.execute(sql)
            columns = [col[0] for col in cursor.description]
            notes = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
        # fix2: Use parameterized queries to prevent SQL injection.
        # sql = "SELECT * FROM cybersecurity_note WHERE title = %s"
        # with connection.cursor() as cursor:
        #     cursor.execute(sql, [query])
        #     columns = [col[0] for col in cursor.description]
        #     notes = [dict(zip(columns, row)) for row in cursor.fetchall()]        
    return render(request, 'search.html', {'notes': notes, 'query': query})
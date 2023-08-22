from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util
import random
import markdown2

# items for the form, inherits from forms
class NewWikiForm(forms.Form):
    title = forms.CharField(label="TITLE", max_length=100,
                error_messages={
                    'required': 'Your wiki needs a title',
                    'max_length': 'The title is too long.',
                    })

    content = forms.CharField(label="CONTENT",
                min_length=100,
                widget=forms.Textarea(attrs={'rows': 20}),
                error_messages={
                    'required': 'Your wiki needs at least 100 characters.',
                    'min_length': 'The text is too short, wiki needs at least 100 characters.',
                    })

    # hidden input 'edit' to check if it is a new page, or a editing page
    is_edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

# Create your views here
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() #when you render the page, you send it a list of all the entries
    })

def get_entry(request, title):
    if util.get_entry(title) == None: #if page does not exist, render 404 template
        return render(request, "encyclopedia/404.html", {
            "entry": title
            })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown2.markdown(util.get_entry(title))
        })

def new_entry(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)

        if form.is_valid(): #if the form is valid
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            is_edit = form.cleaned_data["is_edit"]

            # check if another wiki with the same title exists
            if util.get_entry(title) == None or is_edit: #if it doesn't save the entry
                print(is_edit)
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", kwargs={"title": title})) #redirect to entry page
            else:   #  if there is already a wiki with same title, load the same page with the original form,
                    # and a field with existing_entry: True
                    # so that user gets error message
                return render(request, "encyclopedia/new_entry.html", {
                "form": form,
                "existing_entry": True,
                "entry_title": title #send entry title to inform user they can edit the original entry page
            })
        else:   # if not, load the same page with the original form,
                # so that user gets error message
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })
    else: #if not a POST request, it is a new form
        return render(request, "encyclopedia/new_entry.html", {
            "form": NewWikiForm()
        })

def save_wiki(form, request):
    ...

def random_entry(request):
    random_entry = random.choice(util.list_entries()) # select a random entry
    return HttpResponseRedirect(reverse("entry", kwargs={"title": random_entry})) #redirects to the random page
    #PS: Entry [Name of the function in urls.py], kwargs = name of the url I am using in urls.py for name=entry

def search(request):
    search_query = request.GET.get("q", "").lower() #gets the search parameter, apply lowercase for comparing
    entries_substring = [] # create a list to store entries with a substring of search_query

    #checks if there is a page title with search parameter
    if (util.get_entry(search_query) is not None):
        return HttpResponseRedirect(reverse("entry", kwargs={"title": search_query}))
    else:
        for entry in util.list_entries(): #for each entry in the list of entries
            if search_query in entry.lower(): #check if the search_query is a substring of query
                entries_substring.append(entry) # if so, appends to the list

    # check the size of the entries_substring to see if there are pages
    # that could have a match with what the user wants
    if len(entries_substring) == 0: # if no entries with substring were found, we return the 404 page
        return render(request, "encyclopedia/404.html", {
            "entry": search_query
            })
    else: # if substrings were found, return list
        return render(request, "encyclopedia/search.html", {
            "search_term": search_query,
            "entries": entries_substring
            })

def edit_entry(request, title):
    if util.get_entry(title) == None:  #test for error, if page does not exist, render 404 template
        return render(request, "encyclopedia/404.html", {
            "entry": title
            })
    else:
        content_edit = util.get_entry(title)
        form_edit = NewWikiForm(initial={"title": title,
                                        "content": content_edit,
                                        "is_edit": True })

        return render(request, "encyclopedia/new_entry.html", {
            "form": form_edit,
            "is_edit": True
        })

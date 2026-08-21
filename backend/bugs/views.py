import os

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from google import genai

from .forms import BugForm
from .models import Bug


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:

        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        },
    )


@login_required
def dashboard_view(request):

    bugs = Bug.objects.all()

    total_bugs = bugs.count()

    open_bugs = bugs.filter(
        status="OPEN"
    ).count()

    in_progress_bugs = bugs.filter(
        status="IN_PROGRESS"
    ).count()

    resolved_bugs = bugs.filter(
        status="RESOLVED"
    ).count()

    context = {
        "bugs": bugs,
        "total_bugs": total_bugs,
        "open_bugs": open_bugs,
        "in_progress_bugs": in_progress_bugs,
        "resolved_bugs": resolved_bugs,
    }

    return render(
        request,
        "dashboard.html",
        context,
    )


@login_required
def bug_create_view(request):

    if request.method == "POST":

        form = BugForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    else:

        form = BugForm()

    return render(
        request,
        "bug_form.html",
        {
            "form": form,
            "page_title": "Add Bug",
            "button_text": "Create Bug",
        },
    )


@login_required
def bug_edit_view(request, pk):

    bug = get_object_or_404(
        Bug,
        pk=pk
    )

    if request.method == "POST":

        form = BugForm(
            request.POST,
            instance=bug
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    else:

        form = BugForm(
            instance=bug
        )

    return render(
        request,
        "bug_form.html",
        {
            "form": form,
            "page_title": "Edit Bug",
            "button_text": "Save Changes",
            "bug": bug,
        },
    )


@login_required
def bug_delete_view(request, pk):

    bug = get_object_or_404(
        Bug,
        pk=pk
    )

    if request.method == "POST":

        bug.delete()

        return redirect("dashboard")

    return render(
        request,
        "confirm_delete.html",
        {
            "bug": bug
        },
    )


@login_required
@require_POST
def improve_description_view(request):

    description = request.POST.get(
        "description",
        ""
    ).strip()

    if not description:

        return JsonResponse(
            {
                "success": False,
                "error": "Please enter a bug description first.",
            },
            status=400,
        )

    api_key = os.environ.get(
        "GEMINI_API_KEY"
    )

    if not api_key:

        return JsonResponse(
            {
                "success": False,
                "error": "Gemini API key is not configured.",
            },
            status=500,
        )

    try:

        client = genai.Client(
            api_key=api_key
        )

        prompt = f"""
You are a software bug-reporting assistant.

Improve the following bug description so that it is:
- clear
- concise
- professional
- technically understandable

Do not invent information that is not present.

Return only the improved bug description.

Original description:
{description}
"""

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        improved_description = response.text.strip()

        return JsonResponse(
            {
                "success": True,
                "description": improved_description,
            }
        )

    except Exception as error:

        return JsonResponse(
            {
                "success": False,
                "error": str(error),
            },
            status=500,
        )
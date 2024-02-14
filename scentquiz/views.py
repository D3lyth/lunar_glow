from django.shortcuts import render
from .models import QuizQuestion, ScentOption

def process_quiz_responses(request, questions):
    """
    Process user responses to the quiz questions and determine the preferred scent profile.
    """
    scent_profiles = {'Fruity': 0, 'Oriental': 0, 'Fresh': 0, 'Floral': 0, 'Woody': 0}

    if request.method == 'POST':
        for question in questions:
            user_response_id = request.POST.get(f'question_{question.id}')
            user_response = ScentOption.objects.get(id=user_response_id)
            scent_profiles[user_response.scent_profile] += 1

        return max(scent_profiles, key=scent_profiles.get)

def get_quiz_questions():
    """
    Retrieve all quiz questions from the database.
    """
    return QuizQuestion.objects.all()

def determine_preferred_profile(request, questions):
    """
    Determine the preferred scent profile based on user responses.
    """
    preferred_profile = process_quiz_responses(request, questions)
    return preferred_profile

def render_quiz(request):
    """
    Render the quiz page with the list of questions.
    """
    questions = get_quiz_questions()
    return render(request, 'scentquiz/quiz.html', {'questions': questions})

def render_quiz_result(request, preferred_profile):
    """
    Render the quiz result page with the preferred scent profile.
    """
    return render(request, 'scentquiz/result.html', {'preferred_profile': preferred_profile})

def quiz(request):
    """
    View function for the quiz page.
    """
    return render_quiz(request)

def pending_user_stories_context(request):
    from apps.administracion.models import Grained, Note
    from apps.autenticacion.settings import PROJECT_US_APROVE



    try:
        user = request.user.user
        user_projects = user.get_projects()

        projects = []

        for project in user_projects:
            if project[0].has_perm(user, PROJECT_US_APROVE[0]):
                projects.append(project[0])

        user_stories = []
        graineds = Grained.objects.filter(sprint__project__in=projects, sprint__state='Ejecucion', state=3, user_story__state=1)
        for grain in graineds:
            if not grain.user_story in user_stories:
                x = grain.user_story
                x.grain = grain
                user_stories.append(x)

        pending_user_stories = []
        for us in user_stories:
            worked = 0
            for note in Note.objects.filter(grained__user_story=us, aproved=True):
                worked = worked + note.work_load

            if worked >= us.estimated_time and not(us in pending_user_stories):
                pending_user_stories.append(us)

        context = {
            'pending_user_stories': pending_user_stories
        }
        return context

    except AttributeError:
        return {}


def pending_notes_context(request):
    from apps.proyecto.models import Project
    from apps.administracion.models import Note
    from apps.autenticacion.models import User
    from apps.autenticacion.settings import PROJECT_US_APROVE



    try:
        user = request.user.user
        user_projects = user.get_projects()

        projects = []

        for project in user_projects:
            if project[0].has_perm(user, PROJECT_US_APROVE[0]):
                projects.append(project[0])


        pending_notes = list(
            Note.notes.filter(
                aproved=False,
                grained__user_story__project__in=projects,
                grained__user_story__state=1,
                grained__sprint__state='Ejecucion'
            )
        )
        context = {
            'pending_notes': pending_notes
        }
        return context

    except AttributeError:
        return {}

def assignments_context(request):
    try:
        user = request.user.user
        from apps.administracion.models import Grained
        from apps.proyecto.models import Team

        teams = Team.teams.filter(user=user)
        user_stories = []
        for team in teams:
            graineds = Grained.graineds.filter(developers=team, user_story__state__in=[0, 1], sprint__state='Ejecucion')
            for grained in graineds:
                user_story = grained.user_story

                if not(user_story in user_stories):
                    user_stories.append(user_story)

        user_stories.sort(key=lambda x: x.get_weight(), reverse=True)
        #user_stories.sort(key=lambda x: x.date_sprint, reverse=True)

        context = {
            'assignments': user_stories
        }

        return context

    except AttributeError:
        return {}



def notifications_count_context(request):
    pending_notes_length = len( pending_notes_context(request).get('pending_notes', []) )
    assignments_length = len( assignments_context(request).get('assignments', []) )
    pending_user_stories_length = len( pending_user_stories_context(request).get('pending_user_stories', []) )


    print(pending_user_stories_context(request))
    context = {
        'notifications_count': pending_notes_length + assignments_length + pending_user_stories_length
    }

    return context
        
def url_names_context(request):
    from scrunban.settings import base as base_settings
    return {'URL_NAMES': base_settings.URL_NAMES }

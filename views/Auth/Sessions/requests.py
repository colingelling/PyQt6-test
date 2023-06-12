def load_user_session():
    # get access to the other class first
    from core.Handlers.Sessions.UserSessions import UserSessions
    user_sessions = UserSessions()

    # open the session
    user_sessions.open_session()

    # store session value(s)
    current_session = user_sessions.current_session
    current_session.update({
        'id': user_sessions.settings.value('id')
    })

    # request these values within this window 'view' next to the id which is default
    user_sessions.request_session = [
        'firstname'
    ]

    # change the session
    user_sessions.change_session()

    for key, value in user_sessions.new_session.items():
        user_sessions.settings.setValue(key, value)
        user_sessions.settings.sync()
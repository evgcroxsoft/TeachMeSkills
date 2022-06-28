import app
import datetime
from flask import session

app.permanent_session_lifetime = datetime.timedelta(hours=1)

def session_check():
    session.permanent = True
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
        session.modified = True
    return f"{session['visits']}"
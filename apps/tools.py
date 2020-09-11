import datetime
from app import db
from .models import Commparam


def generate_id(param_name):
    dt = str(datetime.date.today()).replace('-', '')
    commparam = Commparam.query.filter_by(param_name=param_name).first()

    if commparam is None:
        commparam = Commparam(param_name=param_name)
        db.session.add(commparam)
        num = 1
    else:
        commparam.param_value += 1
        num = commparam.param_value
        db.session.add(commparam)

    id = '%s%08d' % (dt, num)

    return id

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import pyramid_sqlalchemy
import json
import models
import random


@view_config(
    route_name='hello',
    renderer='templates/home.jinja2'
)
def home(request):
    st = models.select_all(models.Structures)
    struc = []
    for i in range(len(st)):
        struc.append([st[i].data,st[i].id])
    return {"struc": struc}


@view_config(
    route_name='struc',
    renderer='templates/EditStruc.jinja2'
)
def struc(request):
    id = request.matchdict['id']
    data = models.select_needed(models.Structures,int(id))
    struc = data.data
    return {"id": id, "data" : struc}



@view_config(
    route_name='rec',
    renderer='templates/record_edit.jinja2'
)
def recEdit(request):
    id = request.matchdict['id']
    data = models.select_needed(models.Records,int(id))
    struc = data.data
    return {"id": id, "data" : struc}


@view_config(
    route_name='rec_edit',
)
def rEdit(request):
    data = dict(request.POST)
    prop = {}
    for k,val in data.items():
        if k != 'custId':
            prop[k] = val
    models.update(models.Records,data['custId'],prop,'data')
    return HTTPFound('/')


@view_config(
    route_name='see',
    renderer='templates/StrucInfo.jinja2'
)
def strucs(request):
    id = request.matchdict['id']
    data = models.select_needed(models.Structures,int(id))
    struc = data.data
    return {"data" : struc}


@view_config(
    route_name='records',
    renderer='templates/Records.jinja2'
)
def recs(request):
    id = request.matchdict['id']
    strucName = models.select_needed(models.Structures,int(id)).data['title']
    data = models.select_needed_records(models.Records,int(id))
    struc = []
    for i in range(len(data)):
        struc.append([data[i].data,data[i].id])
    return {"data": struc,"strId":id,"name": strucName}


@view_config(
    route_name='recInfo',
    renderer='templates/RecordInfo.jinja2'
)
def rec(request):
    id = request.matchdict['id']
    data = models.select_needed(models.Records,int(id))
    return {"data": data.data,"id" : id}


@view_config(
    route_name='delete',
)
def delete(request):
    id = request.matchdict['id']
    data = models.delete_elem(models.Structures,id)
    return HTTPFound('/')


@view_config(
    route_name='deleterec',
)
def delete(request):
    id = request.matchdict['id']
    models.delete_elem(models.Records,id)
    return HTTPFound('/')


@view_config(
    route_name='newstruc',
    renderer='templates/add_struc.jinja2'
)
def newstruc(request):
    return {"id": None}

@view_config(
    route_name='newrec',
    renderer='templates/add_record.jinja2'
)
def newrec(request):
    id = request.matchdict['id']
    data = models.select_needed(models.Structures, int(id))
    return {"id": id,'data': data.data}


@view_config(
    route_name='str_edit',
    renderer='templates/EditStruc.jinja2'
)
def edit(request):
    data = dict(request.POST)
    row = models.select_needed(models.Structures,data['custId'])
    to_update = row.data
    set_def = ''
    prop = {}
    for k,val in data.items():
        if k != 'custId' and 'type' not in k and 'descrinput' not in k and 'description' not in k:
            name = val
            dic = {}
        elif 'type' in k:
            dic['type'] = val
            if val == "string":
                set_def = "Default"
            elif val == "number":
                set_def = "minimum"
            elif val == "array":
                set_def = "default"
        elif 'descrinput' in k:
            if set_def == 'default':
                dic[set_def] = val.replace("'","").strip('][').split(', ')
            else:
                dic[set_def] = val
        elif 'description' in k:
            dic['description'] = val
            prop[name] = dic

    to_update['properties'] = prop
    models.update(models.Structures,data['custId'],to_update,'data')
    return HTTPFound('/')


@view_config(
    route_name='adds'
)
def add(request):
    data = dict(request.POST)
    set_def = ''
    prop = {}
    for k,val in data.items():
        if k != 'custId' and 'type' not in k and 'descrinput' not in k and 'description' not in k:
            name = val
            dic = {}
        elif 'type' in k:
            dic['type'] = val
            if val == "string":
                set_def = "Default"
            elif val == "number":
                set_def = "minimum"
            elif val == "array":
                set_def = "default"
        elif 'descrinput' in k:
            if set_def == 'default':
                dic[set_def] = val.replace("'","").strip('][').split(', ')
            else:
                dic[set_def] = val
        elif 'description' in k:
            dic['description'] = val
            prop[name] = dic

    structure = {'title': data['title'],
                 'type': 'object',
                 'properties': prop
                 }

    data = models.Structures(id=random.randint(5,3000),data=structure,created=2,created_by=3,updated=4,updated_by=5)
    # models.add_to_db('structures','(data,created,created_by,updated,updated_by)',(random.randint(5,3000),str(structure),2,3,4,5))
    models.add_to_db(data)
    return HTTPFound('/')


@view_config(
    route_name='addrec'
)
def addrec(request):
    data = dict(request.POST)
    dic = {}
    for k,val in data.items():
        if k != 'custId':
            dic[k] = val

    data = models.Records(id=random.randint(5,3000),structure_id=data['custId'],data=dic,created=2,created_by=3,updated=4,updated_by=5)
    models.add_to_db(data)
    return HTTPFound('/')


if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_static_view(name='static', path='static')
        config.include('pyramid_debugtoolbar')
        config.add_route('hello', '/')
        config.add_route('str_edit', '/str_edit')
        config.add_route('rec_edit', '/rec_edit')
        config.add_route('struc', '/struc/{id}')
        config.add_route('rec', '/rec/{id}')
        config.add_route('see', '/see/{id}')
        config.add_route('records', '/records/{id}')
        config.add_route('newstruc', '/add')
        config.add_route('newrec', '/addRec/{id}')
        config.add_route('adds', '/add_str')
        config.add_route('addrec', '/rec_add/{id}')
        config.add_route('delete', '/delete/{id}')
        config.add_route('deleterec', '/deleterec/{id}')
        config.add_route('recInfo', '/recInf/{id}')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
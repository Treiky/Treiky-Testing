# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.requerimiento.models import Requirement, Project
from apps.requerimiento.forms import reqForm, projForm, newUserForm, projectSearch

@login_required
def view_req(request):
    return render_to_response(
        'list_Requirements.html',
        RequestContext(
            request,
            {'requerimiento': Requirement.objects.filter(project__user=request.user).order_by('-date_created'),}
            ),
                )


@login_required
def write_req(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = reqForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.author = request.user
            new_req.save()
            return view_req(request)
    else:
        form = reqForm(initial=request.user)
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Publique su nuevo Requerimiento:',
        }))


@login_required
def write_project(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = projForm(request.POST)
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.save()
            return resultado_alta_proyecto(request)
    else:
        form = projForm()

    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Proyectos:',
        }))


def new_user(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.save()
            return resultado_alta_usuario(request)
    else:
        form = newUserForm()

    return render_to_response('registration/alta.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))

def resultado_alta_usuario(request, mensaje):
    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El alta se registro correctamente, recibira la clave por email '+mensaje,
        }))

def resultado_alta_proyecto(request):
    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


def logoutuser(request):
    logout(request)
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


@login_required
def update_project(request, project):
    layout = 'vertical'

    if request.method == 'POST':
        print 'prueba'
        form = projForm(request.POST)
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.save()
            return resultado_alta_proyecto(request)
    else:
        a = Project.objects.filter(name=project, user=request.user)
        form = projForm()
        for proj in a:
            form = projForm(initial={'name': proj.name, 'description': proj.description})

    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Modificacion de Projecto:',
        }))


@login_required
def searchProject(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = projectSearch(request.POST)
        proyecto = request.POST.get('project', '')
        if form.is_valid():
            request.method = ''
            return update_project(request, proyecto)
    else:
        form = projectSearch()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Administrador de Proyecto',
        }))

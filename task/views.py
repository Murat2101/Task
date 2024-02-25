from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Task  # Подставьте соответствующую модель задачи
import json

def task_list(request):
    tasks = Task.objects.all()  # Получаем все задачи из базы данных
    task_data = []  # Создаем список для данных задач

    for task in tasks:
        task_data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description
            # Добавьте другие поля задачи по вашему усмотрению
        })

    return JsonResponse(task_data, safe=False)  # Возвращаем список задач в формате JSON



def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description')
            # Добавьте другие поля задачи по вашему усмотрению
        )
        return JsonResponse({'id': task.id, 'message': 'Задача создана успешно'}, status=201)
    else:
        return HttpResponse('Метод Не разрешен', status=405)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу по ID

    task_data = {
        'id': task.id,
        'title': task.title,
        'description': task.description
        # Добавьте другие поля задачи по вашему усмотрению
    }

    return JsonResponse(task_data, safe=False)  # Возвращаем данные задачи в формате JSON



def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу по ID

    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        # Обновите другие поля задачи по вашему усмотрению
        task.save()
        return JsonResponse({'message': 'Задача успешно обновлена'})
    else:
        return HttpResponse('Метод Не разрешен', status=405)



def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу по ID

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Задача успешно удалена'})
    else:
        return HttpResponse('Метод Не разрешен', status=405)
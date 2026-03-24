from django.shortcuts import render
from django.http import JsonResponse
import json

def calculator(request):
    return render(request, 'calculator.html')

def calculate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expression = data.get('expression', '')
            
            # Basic validation
            if not expression:
                return JsonResponse({'error': 'No expression provided'}, status=400)
            
            # Evaluate the expression
            try:
                result = eval(expression)
                return JsonResponse({'result': result})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405) 
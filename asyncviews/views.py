import asyncio
from django.http import JsonResponse

async def contador_async(request):
    
    contador = []
    for num in range(1, 6):  
        await asyncio.sleep(1.5)  
        contador.append(num)
        print(f"Contador: {num}")
    
    return JsonResponse({"contador": contador})

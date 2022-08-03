from random import randint, uniform
from django.shortcuts import render
from django.http import HttpResponse
from numpy import double
from .models import guns, cases

def Trap(request):
    return render(request, 'html/trap.html')

def OpenCase(request):
    url = request.build_absolute_uri()
    lol = []
    case = ""
    for i in url[::-1]:
        if i == '/':
            break
        case = i + case

    print(case)
    print('------------------')    
    guns_in_case = guns.objects.all().filter(collection = case)
    print(guns_in_case)
    print(len(guns_in_case))
    all_guns_in_case_arr = []
    for i in guns_in_case:
        # print(i.gun_url)
        all_guns_in_case_arr.append(i)
    print('------------------')
    i = k = 0
    guns_amount = len(guns_in_case)
    # print(guns_amount)
    while i < guns_amount:
        while k < guns_amount - 1:
            if float(all_guns_in_case_arr[k].cost) > float(all_guns_in_case_arr[k+1].cost):
                buf = all_guns_in_case_arr[k]
                all_guns_in_case_arr[k] = all_guns_in_case_arr[k+1]
                all_guns_in_case_arr[k+1] = buf
            k += 1
        if buf == 0:
            i = guns_amount
        i += 1
        k = buf = 0
    print(all_guns_in_case_arr)
    print('------------------')
    ind = []
    
    for i in range(1,27):
        num = randint(0,guns_amount-1)
        ind.append(all_guns_in_case_arr[num])
    print(all_guns_in_case_arr)
    print(len(all_guns_in_case_arr))
    print('------------------')
    ind.append(all_guns_in_case_arr[GetGun(all_guns_in_case_arr)])
    print('------------------')
    for i in range(28,31):
        num = randint(0,guns_amount-1)
        ind.append(all_guns_in_case_arr[num])

    print(f"--------------------{ind[26].name}------------------------")

    return render(request, 'html/openCase.html', {'guns':ind,'all_guns':all_guns_in_case_arr})

def Cases(request):
    all_cases = cases.objects.all()
    return render(request, 'html/cases.html', {'cases': all_cases})

def Login(request):
    return render(request, 'html/login.html')

def Handler_404(request, exception):
    return render(request, 'html/404.html')

def GetGun(all_guns_in_case_arr):
    
    costs =[]
    intervals = []
    total_cost = 0
    max_random_num = 0
    guns_amount = len(all_guns_in_case_arr)
    
    for i in all_guns_in_case_arr:
        total_cost += float(i.cost)
    print("****************")
    for i in all_guns_in_case_arr:
        gun_cost = float(i.cost) 
        costs.append(gun_cost)
        interval = float(("%.2f" % (total_cost / gun_cost))) * 100
        print(interval)
        max_random_num += interval
        intervals.append(round(max_random_num))
    print("****************")
    print(intervals)
    print(max_random_num)
    random_num = randint(intervals[0], max_random_num)
    i = 0
    print("****************")
    while i < guns_amount:
        if random_num >= intervals[i]:
            i += 1
            continue
        else:
            i -= 1
            break
    if i == guns_amount:
        i -= 1
    # print("-------------")
    # print(max_random_num)
    # print(costs)
    # print(intervals)
    print(i)
    return i

from django.shortcuts import render
from minizinc import Instance, Model, Solver
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, "index.html")

def calculador(request):
    
    universidad = Model()
    universidad.add_string(
    """
    int: n; 
    int: m; 
    set of int: rango=1..n;
    set of int: rangoCiudades=1..m;
    array[rangoCiudades, 1..2] of 0..n: ciudades;

    array[rangoCiudades] of var 0..n*2: distancias;
    array[1..2] of var 0..n: ubicacion;

    constraint ubicacion[1] in ciudades[..,1] /\ ubicacion[2] in ciudades[..,2];

    constraint forall(i in rangoCiudades)(distancias[i] = abs(ciudades[i,1] - ubicacion[1]) + abs(ciudades[i,2] - ubicacion[2]));


    solve minimize max(distancias);

    """
    )

    chuffed = Solver.lookup("chuffed")
    instance = Instance(chuffed, universidad)

    instance["n"] = 10
    instance["m"] = 10
    instance["ciudades"] = [[0,1],[2,4],[3,8],[4,1],[6,3],[6,4],[6,5],[8,7],[9,3],[9,10]]


    result = instance.solve()
    return JsonResponse({"objective":result.solution.objective, "distancias":result.solution.distancias, "ubicacion":result.solution.ubicacion}, safe=False)



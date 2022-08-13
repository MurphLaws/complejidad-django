% Parametros
int: n; % Tamaño de la región.
int: m; % # de ciudades.
set of int: rango=1..n;
set of int: rangoCiudades=1..m;
array[rangoCiudades, 1..2] of 0..n: ciudades;

% Variables
array[rangoCiudades] of var 0..n*2: distancias;
array[1..2] of var 0..n: ubicacion;

% Restricciones
% La universidad debe estar ubicada en un municipio.
constraint ubicacion[1] in ciudades[..,1] /\ ubicacion[2] in ciudades[..,2];

% Definición de distancias
constraint forall(i in rangoCiudades) (
	distancias[i] = abs(ciudades[i,1] - ubicacion[1]) + abs(ciudades[i,2] - ubicacion[2]));

% Función objetivo
solve minimize max(distancias);

output["Ubicación de la universidad (E,N): \(ubicacion)\n"]++
["Distancia más larga: \(max(distancias))"];

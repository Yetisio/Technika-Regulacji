%wielomian w mianowniku transmitancji
Ms = [1 4 1 -6];

%tworzenie macierzy dla wykresu 3D
x = linspace(6, 10, 50);
y = linspace(0, 1/4, 50);
[X, Y] = meshgrid(x, y);
result = zeros(size(X));

% do tworzenia wykresu 3D dla PI
for i = 1:numel(X)
    kp = X(i);
    ki = Y(i);
    model = 'projekt3_sim.slx';
    [simOut] = sim(model);
    result(i) = simOut.Q(end);
    close_system(model, 0);
end


%do zrobienia wykresów 2D dla PI 
%do zrobienia wykresów 2D dla P
%tworzy wykres 3D
figure; 
surf(X, Y, result); 
xlabel('X');
zlim([0, 1000]);
ylabel('Y'); 
zlabel('Z'); 
title('3D Graph');



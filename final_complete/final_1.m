a = 0;
b = 1;
c = 0;
d = 1;

fun = @(x,y) ((x.*y+1).*(x.*y-x-y)+x^2+y^2) - ((x.*y).*(x-1).*(y-1));
gfun = @(x,y) g_final(x,y,a,b,c,d);
n = 6;
m = 10;
N = 10000;
[xx,yy, w] = poisson2D(fun, gfun, m,n, N, a, b, c, d);

x = zeros(n+1, 1);
y = zeros(m+1,1);
x(2:end-1) = xx;
y(2:end-1) = yy;
x(1) = a; x(end) = b;
y(1) = c; y(end) = d;
u = zeros(n+1, m+1);
u(2:end-1, 2:end-1) = w;
%define boundary values
for i = 1:n+1
    u(i, 1) = gfun(x(i), c);
    u(i, end) = gfun(x(i),d);
end
%define boundary values
for j = 1:m+1
    u(1, j) = gfun(a, y(j));
    u(end, j) = gfun(b, y(j));
end
%define points for plotting exact solutions
truesol = @(x,y) (x.*y.*(x-1).*(y-1))/2;
utrue = zeros(length(x), length(y));
for i = 1:length(x)
    for j = 1:length(y)
        utrue(i,j) = truesol( x(i), y(j));
    end
end

figure(1)
[X,Y] = meshgrid(x,y);
surfc(X', Y', u)
title('Approximated Solution')
saveas(gcf,'final_1_approx.png')

figure(2)
surfc(X', Y', utrue)
title('Exact Solution')
saveas(gcf,'final_1_exact.png')

figure(3)
surfc(X', Y', abs(u-utrue)/norm(utrue))
tit = ['Error: ' , num2str(max(max(abs(u-utrue)/norm(utrue))))];
title(tit)
saveas(gcf,'final_1_error.png')

disp(u)
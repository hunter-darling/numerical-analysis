function [x,w] = CNMethod_final(f, l, T, alpha, h, k)

m = l/h;
w = zeros(m,1);
%edited parameters of CNMethod to accept h and k rather than N and m
%h = l/m; 
%k = T/N;
N = T/k;
lambda = alpha^2*k/h^2;
w(m) = 0;
for i = 1:m
    x(i) = i*h;
end
%step 2 
for i = 1:m-1
    w(i) = f(i*h);
end 

l = zeros(m,1);
u = zeros(m,1);
%step 3
l(1) = 1+ lambda;
u(1) = -lambda/(2*l(1));


%step 4
for i = 2:m-2
    l(i) = 1 + lambda + lambda*u(i-1)/2;
    u(i) = -lambda / (2*l(i));
end

%step 5
l(m-1) = 1+lambda + lambda*u(m-2)/2;

z = zeros(m-2,1);
%steps 7-20 perform Gauss-Seidel iterations
%step 6
for j = 1:N
    %step 7
    t = j*k;
    z(1) = ( (1-lambda)*w(1) + lambda/2* w(2))/l(1);
    
    %step 8
    for i = 2:m-1
        z(i) = ( (1-lambda)*w(i) + lambda/2* (w(i+1)+w(i-1)+z(i-1)))/l(i);
    end
    
    %step 9
    w(m-1) = z(m-1);
    
    %step 10
    for i = m-2:-1:1
        w(i) = z(i) - u(i)*w(i+1);
    end
    
end
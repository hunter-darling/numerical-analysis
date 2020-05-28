function [x,y, w] = poisson2D(fun, g, m,n, N, a, b, c, d)

h = (b-a)/n;
k = (d-c)/m;

%step 2
x = zeros(n-1,1);
for i = 1:n-1
    x(i) = a+ i*h;
end

%step 3
y = zeros(m-1,1);
for j=1:m-1
    y(j) = c+j*k;
end

%step 4
w = zeros(n-1, m-1);
for i = 1:n-1
    for j = 1:m-1
        w(i,j) = 0;
    end
end

%step 5
lambda = h^2/k^2;
mu = 2*(1+lambda);
l = 1;

TOL = 10^-8;
%step 6
while l <= N
    
    %step 7
    z = (-h^2*fun(x(1), y(m-1)) + g(a, y(m-1)) + lambda*g(x(1), d) + lambda*w(1, m-2) + w(2,m-1) ) /mu;
    
    NORM = abs(z - w(1,m-1));
    w(1,m-1) = z;
    
    
    
    %step 8
    for i = 2:n-2
        z = (-h^2 * fun(x(i), y(m-1)) + lambda*g(x(i),d) + w(i-1,m-1) + w(i+1,m-1) + lambda*w(i,m-2)) /mu;
        if abs(w(i,m-1) - z) > NORM
            NORM = abs(w(i,m-1)-z);
        end
        w(i,m-1) = z;
    end
    %step 9
    z = ( -h^2*fun(x(n-1),y(m-1)) + g(b, y(m-1)) + lambda*g(x(n-1),d) + w(n-2,m-1) + lambda*w(n-1, m-2)) / mu;
    if abs( w(n-1,m-1)-z) > NORM
        NORM = abs( w(n-1,m-1) - z);
    end
    w(n-1,m-1) = z;
    
    %step 10
    for j = m-2:-1:2
        %step 11
        z = ( -h^2*fun(x(1),y(j)) + g(a,y(j)) + lambda*w(1,j+1) + lambda*w(1,j-1) + w(2,j))/mu;
        if abs( w(1,j) - z) >NORM
            NORM = abs( w(1,j) - z);
        end
        w(1,j) = z;
        
        %step 12
        for i = 2:n-2
            z = ( -h^2*fun(x(i),y(j)) + w(i-1,j) + lambda*w(i,j+1) + w(i+1,j) + lambda*w(i,j-1))/mu;
            if abs( w(i,j) - z) >NORM
                NORM = abs( w(i,j) - z);
            end
            w(i,j) = z;
        end
        
        %step 13
        z = (-h^2 * fun( x(n-1),y(j)) + g(b, y(j)) + w(n-2, j) + lambda*w(n-1,j+1) + lambda*w(n-1,j-1))/mu;
        if abs( w(n-1,j) -z) > NORM
            NORM =abs( w(n-1,j) -z);
        end
        w(n-1,j) = z;
    end
    
    
    %step 14
    z = (-h^2*fun(x(1),y(1)) + g(a,y(1)) + lambda*g(x(1), c) + lambda*w(1,2) + w(2,1))/mu;
    if abs( w(1,1)-z) > NORM
        NORM = abs( w(1,1)-z);
    end
    w(1,1) = z;
    
    %step 15
    for i = 2:n-2
        z = ( -h^2*fun(x(i),y(1)) + lambda*g(x(i), c) + w(i-1,1) + lambda*w(i,2) +w(i+1,1))/mu;
        if abs(w(i,1)-z) > NORM
            NORM = abs(w(i,1)-z);
        end
        w(i,1) = z;
    end
    
    
    %step 16
    z = (-h^2 * fun(x(n-1),y(1)) + g(b,y(1)) + lambda*g(x(n-1), c) + w(n-2,1) + lambda*w(n-1,2))/mu;
    if abs(w(n-1,1)-z) > NORM
        NORM = abs(w(n-1,1) - z);
    end
    w(n-1,1) = z;
    
    
    %step 17
    if NORM <= TOL
        break
    else
        l = l+1;
    end
end
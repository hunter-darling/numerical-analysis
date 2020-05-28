alpha = 1;
l = 2;
T = 2;
h=0.1;
k=0.1;
% this process was modified to hold some variables static
% and iterate over others to control for changes to different
% variable sample step sizes
while h > 0.001 
    while k > 0.001
        fun = @(x) sin(pi*x*(x-(1/2)));
        [xx, w] = CNMethod_final(fun, l, T, alpha, h, k);

        x = zeros(length(xx)+1, 1);
        x(1) = 0;
        x(2:end) = xx;

        u = zeros(length(xx)+1, 1);
        u(1) = 0;
        u(2:end) = w;

        % compare values of x, u, and w at each iteration of h & k
        fprintf('\nh = %.4f k = %.4f\n', h, k)
        fprintf('\nx = %.4f u = %.4f w = %.4f \n', x, u, w)

        % plots the path of convergence after h & k are decreased
        plot(x, u, 'k-', 'linewidth', 2)
        hold on
        saveas(gcf,'final_2_hkcomp.png')
    % iterate h and k
        k = k/10;
    end
h = h/10;
end
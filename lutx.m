function [L,U,p] = lutx(A)
%LU Triangular factorization
% [L,U,p] = lutx(A) produces a unit lower triangular
% matrix L, an upper triangular matrix U, and a
% permutation vector p, so that L*U = A(p,:).
[n,n] = size(A);
p = (1:n)';
for k = 1:n-1
    disp('k:')
    disp(k)
    % Find largest element below diagonal in k-th column
    [r,m] = max(abs(A(k:n,k)));
    %disp([r,m])
    m = m+k-1;
    disp('m:')
    disp(m)
    %disp('A[m,k]')
    %disp(A(m,k))
    % Skip elimination if column is zero
    if (A(m,k) ~= 0)
        % Swap pivot row
        if (m ~= k)
            A([k m],:) = A([m k],:);
            p([k m]) = p([m k]);
            %disp(A)
            %disp(p)
        end
        % Compute multipliers
        i = k+1:n;
        disp('inside 1 loop:')
        %disp(A(i,k))
        %disp(A(k,k))
        A(i,k) = A(i,k)/A(k,k);
        disp(A)
        % Update the remainder of the matrix
        j = k+1:n;
        disp(A(i,j))
        disp(A(i,k))
        disp(A(k,j))
        A(i,j) = A(i,j) - A(i,k)*A(k,j);
        
    end
end
% Separate result
L = tril(A,-1) + eye(n,n);
U = triu(A);
end

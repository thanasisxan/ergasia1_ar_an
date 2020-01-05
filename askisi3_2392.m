clear all
A = [[2, 1, 5]
     [4, 4, -4]
     [1, 3, 1]];

%disp(A(2:3,1))

[L, U, P] = lutx(A);

%disp(L)
%disp(P)
%disp(U)
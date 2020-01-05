/*
 * File: lutx.c
 *
 * MATLAB Coder version            : 4.0
 * C/C++ source code generated on  : 18-Dec-2019 22:25:01
 */

/* Include Files */
#include <math.h>
#include <string.h>
#include "rt_nonfinite.h"
#include "lutx.h"

/* Function Definitions */

/*
 * LU Triangular factorization
 *  [L,U,p] = lutx(A) produces a unit lower triangular
 *  matrix L, an upper triangular matrix U, and a
 *  permutation vector p, so that L*U = A(p,:).
 * Arguments    : double A[9]
 *                double L[9]
 *                double U[9]
 *                double p[3]
 * Return Type  : void
 */
void lutx(double A[9], double L[9], double U[9], double p[3])
{
  int i;
  int k;
  int m;
  int j_size_idx_1;
  double y_data[3];
  int istart;
  signed char I[9];
  boolean_T exitg1;
  double ex;
  int b_m[2];
  int iv0[2];
  signed char i_data[2];
  signed char tmp_data[2];
  double b_A[6];
  double A_data[2];
  signed char b_p[2];
  signed char j_data[2];
  double b_tmp_data[4];
  double b_A_data[2];
  for (i = 0; i < 3; i++) {
    p[i] = 1.0 + (double)i;
  }

  for (k = 0; k < 2; k++) {
    /*  Find largest element below diagonal in k-th column */
    for (m = -1; m + 2 <= 3 - k; m++) {
      y_data[m + 1] = fabs(A[((k + m) + 3 * k) + 1]);
    }

    if (3 - k <= 2) {
      if ((y_data[0] < y_data[1]) || (rtIsNaN(y_data[0]) && (!rtIsNaN(y_data[1]))))
      {
        istart = 2;
      } else {
        istart = 1;
      }
    } else {
      if (!rtIsNaN(y_data[0])) {
        istart = 1;
      } else {
        istart = 0;
        m = 2;
        exitg1 = false;
        while ((!exitg1) && (m <= 3)) {
          if (!rtIsNaN(y_data[m - 1])) {
            istart = m;
            exitg1 = true;
          } else {
            m++;
          }
        }
      }

      if (istart == 0) {
        istart = 1;
      } else {
        ex = y_data[istart - 1];
        for (m = istart; m < 3; m++) {
          if (ex < y_data[m]) {
            ex = y_data[m];
            istart = m + 1;
          }
        }
      }
    }

    m = istart + k;

    /*  Skip elimination if column is zero */
    if (A[(m + 3 * k) - 1] != 0.0) {
      /*  Swap pivot row */
      if (m != 1 + k) {
        b_m[0] = m;
        b_m[1] = 1 + k;
        iv0[0] = 1 + k;
        iv0[1] = m;
        for (i = 0; i < 3; i++) {
          for (istart = 0; istart < 2; istart++) {
            b_A[istart + (i << 1)] = A[(b_m[istart] + 3 * i) - 1];
          }
        }

        for (i = 0; i < 3; i++) {
          for (istart = 0; istart < 2; istart++) {
            A[(iv0[istart] + 3 * i) - 1] = b_A[istart + (i << 1)];
          }
        }

        b_m[0] = m - 1;
        b_m[1] = k;
        iv0[0] = k;
        iv0[1] = m - 1;
        for (i = 0; i < 2; i++) {
          b_p[i] = (signed char)p[b_m[i]];
        }

        for (i = 0; i < 2; i++) {
          p[iv0[i]] = b_p[i];
        }
      }

      /*  Compute multipliers */
      m = 2 - k;
      istart = 1 - k;
      for (i = 0; i <= istart; i++) {
        i_data[i] = (signed char)((k + i) + 2);
      }

      for (i = 0; i < m; i++) {
        tmp_data[i] = (signed char)(i_data[i] - 1);
      }

      for (i = 0; i < m; i++) {
        A_data[i] = A[(i_data[i] + 3 * k) - 1] / A[k + 3 * k];
      }

      for (i = 0; i < m; i++) {
        A[tmp_data[i] + 3 * k] = A_data[i];
      }

      /*  Update the remainder of the matrix */
      j_size_idx_1 = 2 - k;
      istart = 1 - k;
      for (i = 0; i <= istart; i++) {
        j_data[i] = (signed char)((k + i) + 2);
      }

      for (i = 0; i < j_size_idx_1; i++) {
        for (istart = 0; istart < m; istart++) {
          b_tmp_data[istart + m * i] = A[(i_data[istart] + 3 * (j_data[i] - 1))
            - 1];
        }
      }

      for (i = 0; i < m; i++) {
        A_data[i] = A[(i_data[i] + 3 * k) - 1];
      }

      for (i = 0; i < j_size_idx_1; i++) {
        b_A_data[i] = A[k + 3 * (j_data[i] - 1)];
      }

      for (i = 0; i < m; i++) {
        for (istart = 0; istart < j_size_idx_1; istart++) {
          A[(i_data[i] + 3 * (j_data[istart] - 1)) - 1] = b_tmp_data[i + m *
            istart] - A_data[i] * b_A_data[istart];
        }
      }
    }
  }

  /*  Separate result */
  memcpy(&L[0], &A[0], 9U * sizeof(double));
  m = 1;
  for (j_size_idx_1 = 0; j_size_idx_1 < 3; j_size_idx_1++) {
    for (i = 1; i <= m; i++) {
      L[(i + 3 * j_size_idx_1) - 1] = 0.0;
    }

    if (m < 3) {
      m++;
    }
  }

  for (i = 0; i < 9; i++) {
    I[i] = 0;
  }

  for (k = 0; k < 3; k++) {
    I[k + 3 * k] = 1;
  }

  for (i = 0; i < 9; i++) {
    U[i] = A[i];
    L[i] += (double)I[i];
  }

  istart = 2;
  for (j_size_idx_1 = 0; j_size_idx_1 < 2; j_size_idx_1++) {
    for (i = istart; i < 4; i++) {
      U[(i + 3 * j_size_idx_1) - 1] = 0.0;
    }

    istart++;
  }
}

/*
 * File trailer for lutx.c
 *
 * [EOF]
 */

/*
 * File: _coder_lutx_api.h
 *
 * MATLAB Coder version            : 4.0
 * C/C++ source code generated on  : 18-Dec-2019 22:25:01
 */

#ifndef _CODER_LUTX_API_H
#define _CODER_LUTX_API_H

/* Include Files */
#include "tmwtypes.h"
#include "mex.h"
#include "emlrt.h"
#include <stddef.h>
#include <stdlib.h>
#include "_coder_lutx_api.h"

/* Variable Declarations */
extern emlrtCTX emlrtRootTLSGlobal;
extern emlrtContext emlrtContextGlobal;

/* Function Declarations */
extern void lutx(real_T A[9], real_T L[9], real_T U[9], real_T p[3]);
extern void lutx_api(const mxArray * const prhs[1], int32_T nlhs, const mxArray *
                     plhs[3]);
extern void lutx_atexit(void);
extern void lutx_initialize(void);
extern void lutx_terminate(void);
extern void lutx_xil_terminate(void);

#endif

/*
 * File trailer for _coder_lutx_api.h
 *
 * [EOF]
 */

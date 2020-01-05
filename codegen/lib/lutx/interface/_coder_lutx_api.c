/*
 * File: _coder_lutx_api.c
 *
 * MATLAB Coder version            : 4.0
 * C/C++ source code generated on  : 18-Dec-2019 22:25:01
 */

/* Include Files */
#include "tmwtypes.h"
#include "_coder_lutx_api.h"
#include "_coder_lutx_mex.h"

/* Variable Definitions */
emlrtCTX emlrtRootTLSGlobal = NULL;
emlrtContext emlrtContextGlobal = { true,/* bFirstTime */
  false,                               /* bInitialized */
  131466U,                             /* fVersionInfo */
  NULL,                                /* fErrorFunction */
  "lutx",                              /* fFunctionName */
  NULL,                                /* fRTCallStack */
  false,                               /* bDebugMode */
  { 2045744189U, 2170104910U, 2743257031U, 4284093946U },/* fSigWrd */
  NULL                                 /* fSigMem */
};

/* Function Declarations */
static real_T (*b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId))[9];
static const mxArray *b_emlrt_marshallOut(const real_T u[3]);
static real_T (*c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src,
  const emlrtMsgIdentifier *msgId))[9];
static real_T (*emlrt_marshallIn(const emlrtStack *sp, const mxArray *A, const
  char_T *identifier))[9];
static const mxArray *emlrt_marshallOut(const real_T u[9]);

/* Function Definitions */

/*
 * Arguments    : const emlrtStack *sp
 *                const mxArray *u
 *                const emlrtMsgIdentifier *parentId
 * Return Type  : real_T (*)[9]
 */
static real_T (*b_emlrt_marshallIn(const emlrtStack *sp, const mxArray *u, const
  emlrtMsgIdentifier *parentId))[9]
{
  real_T (*y)[9];
  y = c_emlrt_marshallIn(sp, emlrtAlias(u), parentId);
  emlrtDestroyArray(&u);
  return y;
}
/*
 * Arguments    : const real_T u[3]
 * Return Type  : const mxArray *
 */
  static const mxArray *b_emlrt_marshallOut(const real_T u[3])
{
  const mxArray *y;
  const mxArray *m1;
  static const int32_T iv2[1] = { 0 };

  static const int32_T iv3[1] = { 3 };

  y = NULL;
  m1 = emlrtCreateNumericArray(1, iv2, mxDOUBLE_CLASS, mxREAL);
  emlrtMxSetData((mxArray *)m1, (void *)&u[0]);
  emlrtSetDimensions((mxArray *)m1, iv3, 1);
  emlrtAssign(&y, m1);
  return y;
}

/*
 * Arguments    : const emlrtStack *sp
 *                const mxArray *src
 *                const emlrtMsgIdentifier *msgId
 * Return Type  : real_T (*)[9]
 */
static real_T (*c_emlrt_marshallIn(const emlrtStack *sp, const mxArray *src,
  const emlrtMsgIdentifier *msgId))[9]
{
  real_T (*ret)[9];
  static const int32_T dims[2] = { 3, 3 };

  emlrtCheckBuiltInR2012b(sp, msgId, src, "double", false, 2U, dims);
  ret = (real_T (*)[9])emlrtMxGetData(src);
  emlrtDestroyArray(&src);
  return ret;
}
/*
 * Arguments    : const emlrtStack *sp
 *                const mxArray *A
 *                const char_T *identifier
 * Return Type  : real_T (*)[9]
 */
  static real_T (*emlrt_marshallIn(const emlrtStack *sp, const mxArray *A, const
  char_T *identifier))[9]
{
  real_T (*y)[9];
  emlrtMsgIdentifier thisId;
  thisId.fIdentifier = (const char *)identifier;
  thisId.fParent = NULL;
  thisId.bParentIsCell = false;
  y = b_emlrt_marshallIn(sp, emlrtAlias(A), &thisId);
  emlrtDestroyArray(&A);
  return y;
}

/*
 * Arguments    : const real_T u[9]
 * Return Type  : const mxArray *
 */
static const mxArray *emlrt_marshallOut(const real_T u[9])
{
  const mxArray *y;
  const mxArray *m0;
  static const int32_T iv0[2] = { 0, 0 };

  static const int32_T iv1[2] = { 3, 3 };

  y = NULL;
  m0 = emlrtCreateNumericArray(2, iv0, mxDOUBLE_CLASS, mxREAL);
  emlrtMxSetData((mxArray *)m0, (void *)&u[0]);
  emlrtSetDimensions((mxArray *)m0, iv1, 2);
  emlrtAssign(&y, m0);
  return y;
}

/*
 * Arguments    : const mxArray * const prhs[1]
 *                int32_T nlhs
 *                const mxArray *plhs[3]
 * Return Type  : void
 */
void lutx_api(const mxArray * const prhs[1], int32_T nlhs, const mxArray *plhs[3])
{
  real_T (*L)[9];
  real_T (*U)[9];
  real_T (*p)[3];
  const mxArray *prhs_copy_idx_0;
  real_T (*A)[9];
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  st.tls = emlrtRootTLSGlobal;
  L = (real_T (*)[9])mxMalloc(sizeof(real_T [9]));
  U = (real_T (*)[9])mxMalloc(sizeof(real_T [9]));
  p = (real_T (*)[3])mxMalloc(sizeof(real_T [3]));
  prhs_copy_idx_0 = emlrtProtectR2012b(prhs[0], 0, false, -1);

  /* Marshall function inputs */
  A = emlrt_marshallIn(&st, emlrtAlias(prhs_copy_idx_0), "A");

  /* Invoke the target function */
  lutx(*A, *L, *U, *p);

  /* Marshall function outputs */
  plhs[0] = emlrt_marshallOut(*L);
  if (nlhs > 1) {
    plhs[1] = emlrt_marshallOut(*U);
  }

  if (nlhs > 2) {
    plhs[2] = b_emlrt_marshallOut(*p);
  }
}

/*
 * Arguments    : void
 * Return Type  : void
 */
void lutx_atexit(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  mexFunctionCreateRootTLS();
  st.tls = emlrtRootTLSGlobal;
  emlrtEnterRtStackR2012b(&st);
  emlrtLeaveRtStackR2012b(&st);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
  lutx_xil_terminate();
}

/*
 * Arguments    : void
 * Return Type  : void
 */
void lutx_initialize(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  mexFunctionCreateRootTLS();
  st.tls = emlrtRootTLSGlobal;
  emlrtClearAllocCountR2012b(&st, false, 0U, 0);
  emlrtEnterRtStackR2012b(&st);
  emlrtFirstTimeR2012b(emlrtRootTLSGlobal);
}

/*
 * Arguments    : void
 * Return Type  : void
 */
void lutx_terminate(void)
{
  emlrtStack st = { NULL,              /* site */
    NULL,                              /* tls */
    NULL                               /* prev */
  };

  st.tls = emlrtRootTLSGlobal;
  emlrtLeaveRtStackR2012b(&st);
  emlrtDestroyRootTLS(&emlrtRootTLSGlobal);
}

/*
 * File trailer for _coder_lutx_api.c
 *
 * [EOF]
 */

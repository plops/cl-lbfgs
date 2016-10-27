[
{ "tag": "typedef", "ns": 0, "name": "lbfgsfloatval_t", "location": "/usr/local/include/lbfgs.h:54:16", "type": { "tag": ":double", "bit-size": 64, "bit-alignment": 64 } },
{ "tag": "enum", "ns": 0, "name": "", "id": 1, "location": "/usr/local/include/lbfgs.h:74:1", "fields": [{ "tag": "field", "name": "LBFGS_SUCCESS", "value": 0 }, { "tag": "field", "name": "LBFGS_CONVERGENCE", "value": 0 }, { "tag": "field", "name": "LBFGS_STOP", "value": 1 }, { "tag": "field", "name": "LBFGS_ALREADY_MINIMIZED", "value": 2 }, { "tag": "field", "name": "LBFGSERR_UNKNOWNERROR", "value": 4294966272 }, { "tag": "field", "name": "LBFGSERR_LOGICERROR", "value": 4294966273 }, { "tag": "field", "name": "LBFGSERR_OUTOFMEMORY", "value": 4294966274 }, { "tag": "field", "name": "LBFGSERR_CANCELED", "value": 4294966275 }, { "tag": "field", "name": "LBFGSERR_INVALID_N", "value": 4294966276 }, { "tag": "field", "name": "LBFGSERR_INVALID_N_SSE", "value": 4294966277 }, { "tag": "field", "name": "LBFGSERR_INVALID_X_SSE", "value": 4294966278 }, { "tag": "field", "name": "LBFGSERR_INVALID_EPSILON", "value": 4294966279 }, { "tag": "field", "name": "LBFGSERR_INVALID_TESTPERIOD", "value": 4294966280 }, { "tag": "field", "name": "LBFGSERR_INVALID_DELTA", "value": 4294966281 }, { "tag": "field", "name": "LBFGSERR_INVALID_LINESEARCH", "value": 4294966282 }, { "tag": "field", "name": "LBFGSERR_INVALID_MINSTEP", "value": 4294966283 }, { "tag": "field", "name": "LBFGSERR_INVALID_MAXSTEP", "value": 4294966284 }, { "tag": "field", "name": "LBFGSERR_INVALID_FTOL", "value": 4294966285 }, { "tag": "field", "name": "LBFGSERR_INVALID_WOLFE", "value": 4294966286 }, { "tag": "field", "name": "LBFGSERR_INVALID_GTOL", "value": 4294966287 }, { "tag": "field", "name": "LBFGSERR_INVALID_XTOL", "value": 4294966288 }, { "tag": "field", "name": "LBFGSERR_INVALID_MAXLINESEARCH", "value": 4294966289 }, { "tag": "field", "name": "LBFGSERR_INVALID_ORTHANTWISE", "value": 4294966290 }, { "tag": "field", "name": "LBFGSERR_INVALID_ORTHANTWISE_START", "value": 4294966291 }, { "tag": "field", "name": "LBFGSERR_INVALID_ORTHANTWISE_END", "value": 4294966292 }, { "tag": "field", "name": "LBFGSERR_OUTOFINTERVAL", "value": 4294966293 }, { "tag": "field", "name": "LBFGSERR_INCORRECT_TMINMAX", "value": 4294966294 }, { "tag": "field", "name": "LBFGSERR_ROUNDING_ERROR", "value": 4294966295 }, { "tag": "field", "name": "LBFGSERR_MINIMUMSTEP", "value": 4294966296 }, { "tag": "field", "name": "LBFGSERR_MAXIMUMSTEP", "value": 4294966297 }, { "tag": "field", "name": "LBFGSERR_MAXIMUMLINESEARCH", "value": 4294966298 }, { "tag": "field", "name": "LBFGSERR_MAXIMUMITERATION", "value": 4294966299 }, { "tag": "field", "name": "LBFGSERR_WIDTHTOOSMALL", "value": 4294966300 }, { "tag": "field", "name": "LBFGSERR_INVALIDPARAMETERS", "value": 4294966301 }, { "tag": "field", "name": "LBFGSERR_INCREASEGRADIENT", "value": 4294966302 }] },
{ "tag": "enum", "ns": 0, "name": "", "id": 2, "location": "/usr/local/include/lbfgs.h:152:1", "fields": [{ "tag": "field", "name": "LBFGS_LINESEARCH_DEFAULT", "value": 0 }, { "tag": "field", "name": "LBFGS_LINESEARCH_MORETHUENTE", "value": 0 }, { "tag": "field", "name": "LBFGS_LINESEARCH_BACKTRACKING_ARMIJO", "value": 1 }, { "tag": "field", "name": "LBFGS_LINESEARCH_BACKTRACKING", "value": 2 }, { "tag": "field", "name": "LBFGS_LINESEARCH_BACKTRACKING_WOLFE", "value": 2 }, { "tag": "field", "name": "LBFGS_LINESEARCH_BACKTRACKING_STRONG_WOLFE", "value": 3 }] },
{ "tag": "typedef", "ns": 0, "name": "lbfgs_parameter_t", "location": "/usr/local/include/lbfgs.h:358:3", "type": { "tag": "struct", "ns": 1229741907, "name": "", "id": 3, "location": "/usr/local/include/lbfgs.h:198:9", "bit-size": 896, "bit-alignment": 64, "fields": [{ "tag": "field", "name": "m", "bit-offset": 0, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "epsilon", "bit-offset": 64, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "past", "bit-offset": 128, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "delta", "bit-offset": 192, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "max_iterations", "bit-offset": 256, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "linesearch", "bit-offset": 288, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "max_linesearch", "bit-offset": 320, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "min_step", "bit-offset": 384, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "max_step", "bit-offset": 448, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "ftol", "bit-offset": 512, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "wolfe", "bit-offset": 576, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "gtol", "bit-offset": 640, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "xtol", "bit-offset": 704, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "orthantwise_c", "bit-offset": 768, "bit-size": 64, "bit-alignment": 64, "type": { "tag": "lbfgsfloatval_t" } }, { "tag": "field", "name": "orthantwise_start", "bit-offset": 832, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "orthantwise_end", "bit-offset": 864, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }] } },
{ "tag": "typedef", "ns": 0, "name": "lbfgs_evaluate_t", "location": "/usr/local/include/lbfgs.h:378:27", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "lbfgs_progress_t", "location": "/usr/local/include/lbfgs.h:406:15", "type": { "tag": ":function-pointer" } },
{ "tag": "function", "name": "lbfgs", "ns": 0, "location": "/usr/local/include/lbfgs.h:477:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "n", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "parameter", "name": "x", "type": { "tag": ":pointer", "type": { "tag": "lbfgsfloatval_t" } } }, { "tag": "parameter", "name": "ptr_fx", "type": { "tag": ":pointer", "type": { "tag": "lbfgsfloatval_t" } } }, { "tag": "parameter", "name": "proc_evaluate", "type": { "tag": "lbfgs_evaluate_t" } }, { "tag": "parameter", "name": "proc_progress", "type": { "tag": "lbfgs_progress_t" } }, { "tag": "parameter", "name": "instance", "type": { "tag": ":pointer", "type": { "tag": ":void" } } }, { "tag": "parameter", "name": "param", "type": { "tag": ":pointer", "type": { "tag": "lbfgs_parameter_t" } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "lbfgs_parameter_init", "ns": 0, "location": "/usr/local/include/lbfgs.h:495:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "param", "type": { "tag": ":pointer", "type": { "tag": "lbfgs_parameter_t" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "lbfgs_malloc", "ns": 0, "location": "/usr/local/include/lbfgs.h:508:18", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "n", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":pointer", "type": { "tag": "lbfgsfloatval_t" } } },
{ "tag": "function", "name": "lbfgs_free", "ns": 0, "location": "/usr/local/include/lbfgs.h:516:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "x", "type": { "tag": ":pointer", "type": { "tag": "lbfgsfloatval_t" } } }], "return-type": { "tag": ":void" } },
{ "tag": "const", "name": "LBFGS_IEEE_FLOAT", "ns": 0, "location": "/usr/local/include/lbfgs.h:47:9", "type": { "tag": ":long", "bit-size": 64, "bit-alignment": 64 }, "value": 1 },
{ "tag": "const", "name": "__LBFGS_H__", "ns": 0, "location": "/usr/local/include/lbfgs.h:30:9", "type": { "tag": ":long", "bit-size": 64, "bit-alignment": 64 } },
{ "tag": "const", "name": "LBFGS_FLOAT", "ns": 0, "location": "/usr/local/include/lbfgs.h:40:9", "type": { "tag": ":long", "bit-size": 64, "bit-alignment": 64 }, "value": 64 }
]
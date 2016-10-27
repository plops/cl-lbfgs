

(eval-when (:compile-toplevel)
  (ql:quickload :cl-autowrap))

(defpackage :f
  (:use :cl :autowrap))

(in-package :f)

#+nil
(delete-file "lbfgs.x86_64-pc-linux-gnu.spec")

(c-include "lbfgs.h"
	   :spec-path (merge-pathnames "stage/cl-lbfgs/"
				       (user-homedir-pathname))
	   :exclude-arch ("arm-pc-linux-gnu"
			  "i386-unknown-freebsd"
			  "i386-unknown-openbsd"
			  "i686-apple-darwin9"
			  "i686-pc-linux-gnu"
			  "i686-pc-windows-msvc"
			  "x86_64-apple-darwin9"
                                        ;"x86_64-pc-linux-gnu"
			  "x86_64-pc-windows-msvc"
			  "x86_64-unknown-freebsd"
			  "x86_64-unknown-openbsd")
	   :exclude-sources ("/usr/*")
	   :include-definitions ("lbfgs")
	   ;:sysincludes '("/usr/local/include")
	   :trace-c2ffi t )

;; Sample code from 
;; http://www.chokkan.org/software/liblbfgs/

(defcallback evaluate lbfgsfloatval-t
    ((instance :pointer)
     (x (:pointer lbfgsfloatval-t))
     (g (:pointer lbfgsfloatval-t))
     (n :int)
     (step lbfgsfloatval-t))
  (let ((fx 0d0))
    (declare (type double-float fx))
    (dotimes (i n)
      (let ((t1 (- 1d0 (cffi:mem-aref x lbfgsfloatval-t i)))
	    (t2 (* 10d0
		   (- (cffi:mem-aref x lbfgsfloatval-t (+ i 1))
		      (expt (cffi:mem-aref x lbfgsfloatval-t i) 2)))))
	(setf (cffi:mem-aref g lbfgsfloatval-t (+ i 1)) (* 20d0 t2)
	      (cffi:mem-aref g lbfgsfloatval-t i)
	      (* -2d0 (+ (* (cffi:mem-aref x lbfgsfloatval-t i)
			    (cffi:mem-aref g lbfgsfloatval-t (+ 1 i)))
			 t1))
	      fx (+ fx (expt t1 2) (expt t2 2)))))
    fx))

(defcallback progress :int
    ((instance :pointer)
     (x (:pointer lbfgsfloatval-t))
     (g (:pointer lbfgsfloatval-t))
     (fx lbfgsfloatval-t)
     (xnorm lbfgsfloatval-t)
     (gnorm lbfgsfloatval-t)
     (step lbfgsfloatval-t)
     (n :int)
     (k :int)
     (ls :int))
  (format t "iteration ~a" k))

